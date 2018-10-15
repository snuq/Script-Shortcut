#bpy.context.active_object.mode == 'EDIT'

import bpy


bpy.ops.object.editmode_toggle()
bpy.ops.object.shape_key_remove()
bpy.ops.object.editmode_toggle()
