#hasattr(bpy.context.scene.sequence_editor, 'active_strip') and (bpy.context.scene.sequence_editor.active_strip.type == 'MOVIE' or bpy.context.scene.sequence_editor.active_strip.type == 'IMAGE')
import bpy

scene = bpy.context.scene
sequencer = scene.sequence_editor
strip = sequencer.active_strip

bpy.ops.scene.new(type='EMPTY')
stripScene = bpy.context.scene
stripScene.name = strip.name
bpy.context.screen.scene = scene

stripScene.use_nodes = True
nodes = stripScene.node_tree.nodes
for node in nodes:
    nodes.remove(node)
nodeInput = nodes.new(type="CompositorNodeMovieClip")
nodeInput.location = ((-100, 400))
if strip.type == 'MOVIE':
    clip = bpy.data.movieclips.load(strip.filepath)
elif strip.type == 'IMAGE':
    clip = bpy.data.movieclips.load(strip.directory+strip.elements[0].filename)

nodeInput.clip = clip
stripScene.frame_start = strip.frame_offset_start + 1
stripScene.frame_end = strip.frame_offset_start + strip.frame_final_duration
stripScene.render.resolution_x = clip.size[0]
stripScene.render.resolution_y = clip.size[1]

nodeOutput = nodes.new(type="CompositorNodeComposite")
nodeOutput.location = ((400, 400))
links = stripScene.node_tree.links
links.new(nodeInput.outputs['Image'], nodeOutput.inputs['Image'])

stripChannel = strip.channel
stripStart = strip.frame_final_start
sceneStrip = sequencer.sequences.new_scene(name = stripScene.name, scene = stripScene, channel = stripChannel, frame_start = stripStart)
sequencer.active_strip = sceneStrip
sceneStrip.frame_start = stripStart