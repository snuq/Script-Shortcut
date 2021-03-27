import bpy

for sequence in bpy.context.sequences:
    if sequence.frame_final_start <= bpy.context.scene.frame_current < sequence.frame_final_end:
        sequence.select = True
    else:
        sequence.select = False
