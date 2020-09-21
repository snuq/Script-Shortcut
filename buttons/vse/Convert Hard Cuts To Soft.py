import bpy

def convert_hard_to_soft(strip):
    hard_left = strip.animation_offset_start
    hard_right = strip.animation_offset_end
    channel = strip.channel
    strip.animation_offset_start = 0
    strip.animation_offset_end = 0
    strip.frame_offset_start += hard_left
    strip.frame_offset_end += hard_right
    strip.frame_start -= hard_left
    strip.channel = channel
    
for strip in bpy.context.selected_sequences:
    convert_hard_to_soft(strip)
