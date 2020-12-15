import bpy

# bpy.ops.export_scene.obj(filepath='/Users/jthuy/Desktop/BConv/test12.obj')

# datapath = "/Users/jthuy/Desktop/BConv/engenier_network.gpkg"

# with open(datapath, 'rb') as file:
#   data = file.read(10)
  
# print(data)

# import bpy

# bpy.ops.curve.primitive_bezier_curve_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
# bpy.ops.object.editmode_toggle()
# bpy.ops.curve.select_all(action='SELECT')
# bpy.ops.curve.handle_type_set(type='VECTOR')
# bpy.ops.curve.de_select_first()

# bpy.context.scene.objects['Plane'].data.vertices[0].co[2] = 2

# del all objects from scene
#for i in bpy.data.objects:
#    i.select_set(1)
#    bpy.ops.object.delete()

# del all objects from scene
for i in bpy.context.scene.objects:
    i.select_set(1)
    bpy.ops.object.delete()


# bpy.context.scene.objects['Plane'].data.vertices[0].co[2] = 2
# bpy.data.objects['Plane'].data.vertices[0].co[2] = 2