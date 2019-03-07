#hasattr(bpy.context.scene.sequence_editor, 'active_strip') and bpy.context.scene.sequence_editor.active_strip.type == 'SCENE'
import bpy


scene = bpy.context.scene
sequencer = scene.sequence_editor
strip = sequencer.active_strip

strip_scene = strip.scene
workspaces = [workspace for workspace in bpy.data.workspaces.keys() if 'compositing' in workspace.lower()]
if len(workspaces) >= 1:
    workspace = bpy.data.workspaces[workspaces[0]]
    bpy.context.window.workspace = workspace
    bpy.context.window.scene = strip_scene
