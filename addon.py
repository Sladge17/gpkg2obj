import bpy
import sys # to work geopandas
sys.path.append('/Users/jthuy/.local/lib/python3.7/site-packages')
import pandas as pd
import geopandas as gpd

path = "/Users/jthuy/Desktop/BConv/"
file = "engenier_network.gpkg"

pipe_diameter = 0.2
pepe_resolution = 2 # equally 8 edges
box_size = (1, 1, 1)


def main():
	clear_scene()
	parsing_file()
#	create_mesh()
#	export_meshes()


def clear_scene():
	bpy.ops.object.select_all(action='SELECT')
	bpy.ops.object.delete()	


def parsing_file():
	data = gpd.read_file(path + file)
	print(data.head(1))
	

def create_mesh():
#	create_pipeline()
	create_box((0, 0, 0))
	
def create_pipeline():
	create_pipe()
	extrude_pipe((2, 0, 2))
	add_pipe()
	set_pipelinesetting(bpy.context.selected_objects[0])
	
def create_pipe():
	bpy.ops.curve.primitive_bezier_curve_add()
	set_vertpos(bpy.context.selected_objects[0].data.splines[0].bezier_points[0], (0, 0, 0))
	set_vertpos(bpy.context.selected_objects[0].data.splines[0].bezier_points[1], (0, 0, 2))
	
def extrude_pipe(pos):
	bpy.ops.object.editmode_toggle()
	bpy.context.edit_object.data.splines[0].bezier_points[0].select_control_point = 0
	bpy.context.edit_object.data.splines[0].bezier_points[0].select_left_handle = 0
	bpy.context.edit_object.data.splines[0].bezier_points[0].select_right_handle = 0
	bpy.ops.curve.extrude_move()
	set_vertpos(bpy.context.edit_object.data.splines[0].bezier_points[2], (pos[0], pos[1], pos[2]))
	bpy.context.edit_object.data.splines[0].bezier_points[2].select_control_point = 0
	bpy.context.edit_object.data.splines[0].bezier_points[2].select_left_handle = 0
	bpy.context.edit_object.data.splines[0].bezier_points[2].select_right_handle = 0
	bpy.context.edit_object.data.splines[0].bezier_points[1].select_control_point = 1
	# 'value' need fix, angle betveen vertexes respondsiable (1.4 = 90 deg) !!!
	bpy.ops.transform.transform(mode='CURVE_SHRINKFATTEN', value=(1.4, 0, 0, 0))
	bpy.ops.object.editmode_toggle()
	
def add_pipe():
	bpy.ops.object.editmode_toggle()
	bpy.ops.curve.primitive_bezier_curve_add()
	set_vertpos(bpy.context.edit_object.data.splines[1].bezier_points[0], (1, 0, 0))
	set_vertpos(bpy.context.edit_object.data.splines[1].bezier_points[1], (1, 0, 2))
	bpy.ops.object.editmode_toggle()
	
def set_pipelinesetting(pipeline):
	pipeline.data.bevel_depth = pipe_diameter
	pipeline.data.bevel_resolution = pepe_resolution
	bpy.ops.object.editmode_toggle()
	bpy.ops.curve.select_all(action='SELECT')
	bpy.ops.curve.handle_type_set(type='VECTOR')
	bpy.ops.object.editmode_toggle()
	
def create_box(pos):
	bpy.ops.mesh.primitive_cube_add()
	set_vertpos(bpy.context.scene.objects[0].data.vertices[0], (pos[0] - box_size[0] / 2, pos[1] - box_size[1] / 2, pos[2] - box_size[2] / 2))
	set_vertpos(bpy.context.scene.objects[0].data.vertices[1], (pos[0] - box_size[0] / 2, pos[1] - box_size[1] / 2, pos[2] + box_size[2] / 2))
	set_vertpos(bpy.context.scene.objects[0].data.vertices[2], (pos[0] - box_size[0] / 2, pos[1] + box_size[1] / 2, pos[2] - box_size[2] / 2))
	set_vertpos(bpy.context.scene.objects[0].data.vertices[3], (pos[0] - box_size[0] / 2, pos[1] + box_size[1] / 2, pos[2] + box_size[2] / 2))
	set_vertpos(bpy.context.scene.objects[0].data.vertices[4], (pos[0] + box_size[0] / 2, pos[1] - box_size[1] / 2, pos[2] - box_size[2] / 2))
	set_vertpos(bpy.context.scene.objects[0].data.vertices[5], (pos[0] + box_size[0] / 2, pos[1] - box_size[1] / 2, pos[2] + box_size[2] / 2))
	set_vertpos(bpy.context.scene.objects[0].data.vertices[6], (pos[0] + box_size[0] / 2, pos[1] + box_size[1] / 2, pos[2] - box_size[2] / 2))
	set_vertpos(bpy.context.scene.objects[0].data.vertices[7], (pos[0] + box_size[0] / 2, pos[1] + box_size[1] / 2, pos[2] + box_size[2] / 2))

def set_vertpos(vertex, pos):
	vertex.co[0] = pos[0]
	vertex.co[1] = pos[1]
	vertex.co[2] = pos[2]


def export_meshes():
	for mesh in bpy.data.objects:
		mesh.select_set(1)
		export_mesh2obj()
		mesh.select_set(0)

def export_mesh2obj(index=[1]):
	suffix = ""
	if index[0] < 10:
		suffix = "00"
	elif index[0] < 100:
		suffix = "0"
	name = f"object_{suffix}{index[0]}.obj"
	bpy.ops.export_scene.obj(filepath=(path+name), use_selection=True, use_materials=False)
	index[0] += 1


if __name__ == "__main__":
	main()