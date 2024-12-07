import bpy

# This is to make printed data show up in blender console. Otherwise it doesn't unless you launch blender from terminal.
def print(data):
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                override = {'window': window, 'screen': screen, 'area': area}
                bpy.ops.console.scrollback_append(override, text=str(data), type="OUTPUT")       

context = bpy.context
obj = context.object
action =  context.object.animation_data.action


filepath = "~/camera_locs"


import bpy

context = bpy.context
obj = context.object
action =  context.object.animation_data.action
#print("fcurve_dic = {")
filepath_orig = "Users/varun/cam_locs/"
for fcurve in action.fcurves:
    filepath = filepath_orig + fcurve.data_path + str(fcurve.array_index)
    with open(filepath, 'w+',  encoding='utf-8') as f:
        print("'%s[%d]' : [" % (fcurve.data_path, fcurve.array_index))
        i = 0
        for kfp in fcurve.keyframe_points:
            #print("\t{", end="")
            for prop in ["co"]:
                co = getattr(kfp, prop)
                vals = "{'x':%.4f, 'y':%.4f}\n"  %  co[:]
            f.write(vals)
            if i >= 50 and i < 52:
                print("\t[%s]" % ", ".join(vals))
            i += 1
        print("\t]")
#print("}")

# Below is Irrelevant: Another method
"""
def write_some_data(context, filepath):
    print("running write_some_data...")
    camera = context.active_object
    mw = camera.matrix_world
    scene = context.scene
    frame = scene.frame_start

    f = open(filepath, 'w', encoding='utf-8')
    while frame <= scene.frame_end:
        scene.frame_set(frame)
        x, y, z = mw.to_translation()
        rx, ry, rz = mw.to_euler('XYZ')
        f.write("%d" % frame)
        f.write(", ")
        f.write("%5.3f, %5.3f, %5.3f" % (x, y, z))
        f.write(", ")
        f.write("%5.3f, %5.3f, %5.3f" % (rx, ry, rz))
        f.write("\n")
        frame += 1
    f.close()

#     return {'FINISHED'}
"""

#write_some_data(context, filepath)