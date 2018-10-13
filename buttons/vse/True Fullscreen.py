#bpy.context.space_data.view_type == 'PREVIEW'

import bpy

class SEQUENCE_MT_true_fullscreen(bpy.types.Operator):
    """True fullscreen preview"""
    bl_label = "True Fullscreen"
    bl_idname = "sequencer.true_fullscreen"

    runs = 0
    original_area = None

    def execute(self, context):
        self.invoke(context, None)
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        self.original_area = context.area
        bpy.ops.wm.window_fullscreen_toggle()
        self.runs = 0
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if self.runs == 0:
            override = context.copy()
            bpy.ops.screen.screen_full_area(override, use_hide_panels=True) #This has to be delayed because if it is run in the invoke function, it crashes blender...
        if self.runs == 1:
            bpy.ops.sequencer.view_all_preview() #This has to be delayed because if it is run right after the screen_full_area, it crashes blender...
        self.runs = self.runs + 1
        if event.type in {'RIGHTMOUSE', 'ESC'}:
            bpy.ops.wm.window_fullscreen_toggle()
            bpy.ops.screen.header()
            bpy.ops.screen.back_to_previous()
            override = context.copy()
            area = self.original_area
            override['area'] = area
            override['space_data'] = area.spaces.active
            for region in area.regions:
                if region.type == 'PREVIEW':
                    break
            override['region'] = region
            bpy.ops.sequencer.view_all_preview(override)
            return {'FINISHED'}
        return {'PASS_THROUGH'}

bpy.utils.register_class(SEQUENCE_MT_true_fullscreen)
bpy.ops.sequencer.true_fullscreen()

