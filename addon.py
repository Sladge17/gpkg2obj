import bpy
import sys
sys.path.append('/Users/jthuy/.local/lib/python3.7/site-packages')

#import fiona
import geopandas

# parsing in geopandas
file = geopandas.read_file('/Users/jthuy/Desktop/BConv/engenier_network.gpkg')
file.head(10)


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
#for i in bpy.context.scene.objects:
#    i.select_set(1)
#    bpy.ops.object.delete()
#bpy.ops.object.select_all()
#bpy.ops.object.delete()



# plane vertex move
#bpy.ops.mesh.primitive_plane_add()
#bpy.data.objects[0].data.vertices[0].co[2] = 2
#bpy.context.scene.objects[0].data.vertices[0].co[2] = 2


# bezier point move
#bpy.ops.curve.primitive_bezier_curve_add()
#bpy.data.objects[0].data.splines.active.bezier_points[0].co[2] = 2
#bpy.context.object.data.splines.active.bezier_points[0].co[2] = 2