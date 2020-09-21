#len(bpy.context.selected_sequences) > 0
import bpy
import os
delete = False

scene = bpy.context.scene
sequencer = scene.sequence_editor

for strip in bpy.context.selected_sequences:
    if strip.type in ['IMAGE', 'MOVIE']:
        clip = None
        if strip.type == 'MOVIE':
            filepath = strip.filepath
        elif strip.type == 'IMAGE':
            filepath = os.path.join(strip.directory, strip.elements[0].filename)
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

            strip_scene.use_nodes = True
            nodes = strip_scene.node_tree.nodes
            for node in nodes:
                nodes.remove(node)
            node_input = nodes.new(type="CompositorNodeMovieClip")
            node_input.location = (-100, 400)
            node_input.clip = clip
            node_output = nodes.new(type="CompositorNodeComposite")
            node_output.location = (400, 400)
            links = strip_scene.node_tree.links
            links.new(node_input.outputs['Image'], node_output.inputs['Image'])

            strip_start = strip.frame_start
            strip_channel = strip.channel
            strip_final_start = strip.frame_final_start
            strip_final_end = strip.frame_final_end
            if delete:
                try:
                    sequencer.sequences.remove(strip)
                except:
                    strip_channel = strip_channel + 1
            else:
                strip_channel = strip_channel + 1
            scene_strip = sequencer.sequences.new_scene(name=strip_scene.name, scene=strip_scene, channel=strip_channel, frame_start=strip_start)
            scene_strip.frame_final_start = strip_final_start
            scene_strip.frame_final_end = strip_final_end
            scene_strip.channel = strip_channel
            scene_strip.frame_start = strip_start
            sequencer.active_strip = scene_strip
