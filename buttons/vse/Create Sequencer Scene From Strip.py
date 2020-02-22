#len(bpy.context.selected_sequences) > 0
import bpy
import os
delete = True

scene = bpy.context.scene
sequencer = scene.sequence_editor

for strip in bpy.context.selected_sequences:
    if strip.type in ['IMAGE', 'MOVIE']:
        clip = None
        if strip.type == 'MOVIE':
            filepath = strip.filepath
        elif strip.type == 'IMAGE':
            filepath = os.path.join(strip.directory+strip.elements[0].filename)
        for check_clip in bpy.data.movieclips:
            if check_clip.filepath == filepath:
                clip = check_clip
                break
        if clip is None:
            if strip.type == 'MOVIE':
                clip = bpy.data.movieclips.load(filepath)
            elif strip.type == 'IMAGE':
                clip = bpy.data.movieclips.load(filepath)

        if clip:
            bpy.ops.scene.new(type='EMPTY')
            strip_scene = bpy.context.scene
            strip_scene.name = strip.name
            bpy.context.window.scene = scene
            strip_scene.frame_end = strip.frame_duration
            strip_scene.render.resolution_x = clip.size[0]
            strip_scene.render.resolution_y = clip.size[1]

            strip_scene.sequence_editor_create()
            if strip.type == 'MOVIE':
                strip_scene.sequence_editor.sequences.new_movie(name=strip.name, filepath=filepath, channel=1, frame_start=1)
            else:
                filenames = []
                for element in strip.elements:
                    filenames.append(element.filename)
                new_strip = strip_scene.sequence_editor.sequences.new_image(name=strip.name, filepath=filepath, channel=1, frame_start=1)
                if len(filenames) > 1:
                    for filename in filenames[1:]:
                        new_strip.elements.append(filename)
                else:
                    new_strip.frame_final_duration = strip.frame_final_duration

            strip_start = strip.frame_start
            strip_channel = strip.channel
            strip_final_start = strip.frame_final_start
            strip_final_end = strip.frame_final_end
            scene_strip = sequencer.sequences.new_scene(name=strip_scene.name, scene=strip_scene, channel=strip_channel, frame_start=strip_start)
            scene_strip.scene_input = 'SEQUENCER'
            scene_strip.frame_final_start = strip_final_start
            scene_strip.frame_final_end = strip_final_end
            input_1s = []
            input_2s = []
            if delete:
                for test_strip in sequencer.sequences:
                    if hasattr(test_strip, 'input_1'):
                        if test_strip.input_1 == strip:
                            input_1s.append(test_strip)
                    if hasattr(test_strip, 'input_2'):
                        if test_strip.input_2 == strip:
                            input_2s.append(test_strip)
                for test_strip in input_2s:
                    test_strip.input_2 = scene_strip
                for test_strip in input_1s:
                    test_strip.input_1 = scene_strip
                try:
                    sequencer.sequences.remove(strip)
                except:
                    strip_channel = strip_channel + 1
            else:
                strip_channel = strip_channel + 1
            scene_strip.channel = strip_channel
            scene_strip.frame_start = strip_start
            sequencer.active_strip = scene_strip
