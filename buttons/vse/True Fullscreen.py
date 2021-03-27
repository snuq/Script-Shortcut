#bpy.context.space_data.view_type == 'PREVIEW'

import bpy


class TrueFullscreen(bpy.types.Operator):
    """True fullscreen preview"""
    bl_label = "True Fullscreen"
    bl_idname = "sequencer.true_fullscreen"

    runs = 0
    original_area = None
    original_region = None
    total_areas = 0

    def execute(self, context):
        self.invoke(context, None)
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        self.original_area = context.area
        if len(context.screen.areas) > 1:
            bpy.ops.wm.window_fullscreen_toggle()
        self.runs = 0
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        if self.runs == 0:
            override = context.copy()
            if len(context.screen.areas) > 1:
                bpy.ops.screen.screen_full_area(override, use_hide_panels=True)  #This has to be delayed because if it is run in the invoke function, it crashes blender...
            else:
                return self.end(context)
        elif self.runs == 1:
            override = context.copy()
            area = context.screen.areas[0]
            override['area'] = area
            override['space_data'] = area.spaces.active
            self.original_region = None
            for region in area.regions:
                if region.type == 'PREVIEW':
                    self.original_region = region
                    break
            if self.original_region:
                override['region'] = self.original_region
                bpy.ops.sequencer.view_all_preview(override)  #This has to be delayed because if it is run right after the screen_full_area, it crashes blender...
        self.runs = self.runs + 1
        if event.type in {'RIGHTMOUSE', 'ESC'}:
            return self.end(context)
        return {'PASS_THROUGH'}
    
    def end(self, context):
        override = context.copy()
        area = self.original_area
        override['area'] = area
        override['space_data'] = area.spaces.active
        if self.original_region:
            override['region'] = self.original_region
        bpy.ops.screen.screen_full_area(override, use_hide_panels=True)
        bpy.ops.wm.window_fullscreen_toggle()
        return {'FINISHED'}


bpy.utils.register_class(TrueFullscreen)
bpy.ops.sequencer.true_fullscreen()
