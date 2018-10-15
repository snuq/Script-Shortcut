#hasattr(bpy.context.scene.sequence_editor, 'active_strip') and (bpy.context.scene.sequence_editor.active_strip.type == 'MOVIE' or bpy.context.scene.sequence_editor.active_strip.type == 'IMAGE')
import bpy


scene = bpy.context.scene
sequencer = scene.sequence_editor
strip = sequencer.active_strip

bpy.ops.scene.new(type='EMPTY')
strip_scene = bpy.context.scene
strip_scene.name = strip.name
bpy.context.screen.scene = scene

strip_scene.use_nodes = True
nodes = strip_scene.node_tree.nodes
for node in nodes:
    nodes.remove(node)
node_input = nodes.new(type="CompositorNodeMovieClip")
node_input.location = (-100, 400)
clip = None
if strip.type == 'MOVIE':
    clip = bpy.data.movieclips.load(strip.filepath)
elif strip.type == 'IMAGE':
    clip = bpy.data.movieclips.load(strip.directory+strip.elements[0].filename)

if clip:
    node_input.clip = clip
    strip_scene.frame_start = strip.frame_offset_start + 1
    strip_scene.frame_end = strip.frame_offset_start + strip.frame_final_duration
    strip_scene.render.resolution_x = clip.size[0]
    strip_scene.render.resolution_y = clip.size[1]

    node_output = nodes.new(type="CompositorNodeComposite")
    node_output.location = (400, 400)
    links = strip_scene.node_tree.links
    links.new(node_input.outputs['Image'], node_output.inputs['Image'])

    strip_channel = strip.channel
    strip_start = strip.frame_final_start
    scene_strip = sequencer.sequences.new_scene(name=strip_scene.name, scene=strip_scene, channel=strip_channel, frame_start=strip_start)
    sequencer.active_strip = scene_strip
    scene_strip.frame_start = strip_start
