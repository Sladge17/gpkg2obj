import bpy
import sys # to work geopandas
sys.path.append('/Users/jthuy/.local/lib/python3.7/site-packages')
import geopandas


path = "/Users/jthuy/Desktop/BConv/"
file = "engenier_network.gpkg"


# parsing in geopandas



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

def main():
	clear_scene()
#	parsing_file()
	create_mesh()
#	export_mesh2obj()

def clear_scene():
	bpy.ops.object.select_all(action='SELECT')
	bpy.ops.object.delete()	

def parsing_file():
	data = geopandas.read_file(path + file)
	print(data.head(1))
	
def create_mesh():
	create_pipeline()
	
def create_pipeline():
	create_pipe()
	
def create_pipe():
	bpy.ops.curve.primitive_bezier_curve_add()
	set_vertpos(bpy.context.selected_objects[0].data.splines[0].bezier_points[0], (0, 0, 0))
	set_vertpos(bpy.context.selected_objects[0].data.splines[0].bezier_points[1], (0, 0, 2))
	
def set_vertpos(vertex, pos):
	vertex.co[0] = pos[0]
	vertex.co[1] = pos[1]
	vertex.co[2] = pos[2]
	
	

def export_mesh2obj(name="test.obj"):
	if (len(bpy.data.objects)):
		bpy.ops.export_scene.obj(filepath=(path+name), use_selection=True, use_materials=False)


if __name__ == "__main__":
	main()