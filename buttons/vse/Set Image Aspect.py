import bpy

selected = bpy.context.selected_sequences

def correct_aspect(sequence):
    #adds a transform strip to the sequence and scales the aspect ratio to square pixels
    if sequence.type not in ['IMAGE', 'MOVIE']:
        return

    scene = bpy.context.scene
    render = scene.render
    image_x = sequence.elements[0].orig_width
    image_y = sequence.elements[0].orig_height
    if sequence.use_crop:
        #cropping on the clip is enabled, account for that when calculating the aspect ratio
        image_x = image_x - sequence.crop.min_x - sequence.crop.max_x
        image_y = image_y - sequence.crop.max_y - sequence.crop.min_y

    scene_aspect = (render.pixel_aspect_x * render.resolution_x) / (render.pixel_aspect_y * render.resolution_y)
    sequence_aspect = image_x / image_y

    if round(sequence_aspect, 2) == round(scene_aspect, 2):
        return

    #check for existing transform already applied to strip
    scale_sequence = None
    for seq in scene.sequence_editor.sequences:
        if seq.type == 'TRANSFORM':
            if seq.input_1 == sequence:
                scale_sequence = seq
                break

    if scale_sequence is None:
        scale_sequence = scene.sequence_editor.sequences.new_effect(name='Transform', type='TRANSFORM', channel=sequence.channel+1, seq1=sequence, frame_start=sequence.frame_final_start)

    if sequence_aspect > scene_aspect:
        #clip is wider than the scene
        scalex = 1
        scaley = scene_aspect / sequence_aspect
    else:
        #scene is wider than the clip
        scalex = sequence_aspect / scene_aspect
        scaley = 1
    scale_sequence.scale_start_x = scalex
    scale_sequence.scale_start_y = scaley
    
for sequence in selected:
    correct_aspect(sequence)
