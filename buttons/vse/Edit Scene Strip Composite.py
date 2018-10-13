#hasattr(bpy.context.scene.sequence_editor, 'active_strip') and bpy.context.scene.sequence_editor.active_strip.type == 'SCENE'
import bpy

scene = bpy.context.scene
sequencer = scene.sequence_editor
strip = sequencer.active_strip

stripScene = strip.scene
screens = [screen for screen in bpy.data.screens.keys() if 'compositing' in screen.lower()]
if len(screens) >= 1:
    screen = bpy.data.screens[screens[0]]
    bpy.context.window.screen = screen
    screen.scene = stripScene
