import bpy


sequencer = bpy.context.scene.sequence_editor
if len(sequencer.meta_stack) > 0:
    sequences = sequencer.meta_stack[-1].sequences
else:
    sequences = sequencer.sequences
for sequence in sequences:
    if sequence.type == 'SCENE':
        sequence.mute = not sequence.mute
