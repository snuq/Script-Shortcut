#len(bpy.context.selected_objects) > 1 and bpy.context.object
#More than two objects must be selected for this to work, an active object must be selected as well.
#Many objects may be selected, they will all be applied to the selection.
#This script will get the bounding areas of the non-active selected objects, and select all vertices within the active object that are in those ranges.

import bpy


bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action = 'DESELECT')
bpy.ops.object.mode_set(mode="OBJECT")
active = bpy.context.object
active_mat = active.matrix_world
active_vertices = active.data.vertices
selectors = []
for selector in bpy.context.selected_objects:
    if selector != active:
        mat = selector.matrix_world
        verts = selector.data.vertices
        x_neg = (mat * sorted(verts, key=lambda i: i.co.x)[0].co)[0]
        x_pos = (mat * sorted(verts, key=lambda i: i.co.x)[-1].co)[0]
        y_neg = (mat * sorted(verts, key=lambda i: i.co.y)[0].co)[1]
        y_pos = (mat * sorted(verts, key=lambda i: i.co.y)[-1].co)[1]
        z_neg = (mat * sorted(verts, key=lambda i: i.co.z)[0].co)[2]
        z_pos = (mat * sorted(verts, key=lambda i: i.co.z)[-1].co)[2]
        selectors.append([x_neg, x_pos, y_neg, y_pos, z_neg, z_pos])

for vert in active_vertices:
    select = False
    x, y, z = (active_mat * vert.co)
    for selector in selectors:
        x_neg, x_pos, y_neg, y_pos, z_neg, z_pos = selector
        if x >= x_neg and x <= x_pos and y >= y_neg and y <= y_pos and z >= z_neg and z <= z_pos:
            select = True
    vert.select = select
bpy.ops.object.mode_set(mode="EDIT")
