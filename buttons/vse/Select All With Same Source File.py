#hasattr(bpy.context.scene.sequence_editor, 'active_strip')
import bpy

def get_source(strip):
    if strip.type == 'MOVIE':
        source = strip.filepath
    elif strip.type == 'SOUND':
        source = strip.sound.filepath
    elif strip.type == 'SCENE':
        source = strip.scene.name
    elif strip.type == 'MOVIECLIP':
        #??
        source = None
    elif strip.type == 'IMAGE':
        source = strip.elements[0].filename
    else:
        source = None
    return source

sequencer = bpy.context.scene.sequence_editor
if len(sequencer.meta_stack) > 0:
    sequences = sequencer.meta_stack[-1].sequences
else:
    sequences = sequencer.sequences
active = sequencer.active_strip
source = get_source(active)
if source:
    for sequence in sequences:
        if get_source(sequence) == source:
            sequence.select = True
        else:
            sequence.select = False