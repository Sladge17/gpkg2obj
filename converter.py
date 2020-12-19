import bpy
import os
import geopandas as gpd
import numpy as np


path = os.path.join(os.getcwd(), r"Desktop/BConv")
file = "engenier_network.gpkg"

pepe_resolution = 2 # equally 8 edges
box_size = (1, 1, 1)


def main():
	clear_scene()
	data = gpd.read_file(os.path.join(path, file))

#	df = data[['ID', 'SECT_TYPE', 'SECT_WIDTH', 'SECT_HEIGH', 'H1', 'geometry']]
#	for string in range(len(df)):
#		id = int(df['ID'][string])
#		vertex = len(df['geometry'][string][0].xy[0])	
#		for vertex in range(len(df['geometry'][string][0].xy[0]) - 1):
#			crd_x1 = round(df['geometry'][string][0].xy[0][vertex], 3)
#			crd_y1 = round(df['geometry'][string][0].xy[1][vertex], 3)
#			crd_x2 = round(df['geometry'][string][0].xy[0][vertex + 1], 3)
#			crd_y2 = round(df['geometry'][string][0].xy[1][vertex + 1], 3)
#			crd_z = -round(df['H1'][string].item(), 3)
#			# df['H1'][string] = int(df['H1'][string]) #
#			# print(type(df['H1'][string])) #
#			create_pipe(crd_x1, crd_y1, crd_x2, crd_y2, crd_z)
#			break
#		break

	## FOR TEST
	df = data[['ID', 'SECT_TYPE', 'SECT_WIDTH', 'SECT_HEIGH', 'X1', 'Y1', 'Z1', 'X2', 'Y2', 'Z2']]
	for string in range(len(df)):
		id = str(int(df['ID'][string].item()))
		x1 = round(df['X1'][string].item(), 3)
		y1 = round(df['Y1'][string].item(), 3)
		z1 = -round(df['Z1'][string].item(), 3)
		x2 = round(df['X2'][string].item(), 3)
		y2 = round(df['Y2'][string].item(), 3)
		z2 = -round(df['Z2'][string].item(), 3)
		d = round(df['SECT_HEIGH'][string].item() / 1000, 3) # d / 1000 <--- FOR TEST
		create_mesh(string, id, x1, y1, z1, x2, y2, z2, d)
	## FOR TEST

	if not os.path.isdir(os.path.join(path, "result")):
		os.mkdir(os.path.join(path, "result"))
	export_meshes()


def clear_scene():
	bpy.ops.object.select_all(action='SELECT')
	bpy.ops.object.delete()	

def create_mesh(string, id, x1, y1, z1, x2, y2, z2, d):
	if not string:
		create_pipeline(id, x1, y1, z1, x2, y2, z2, d)
		bpy.ops.object.select_all(action='DESELECT')
		return	
	for object in bpy.data.objects:
		if object.name == id:
			object.select_set(1)
			add_pipe(x1, y1, z1, x2, y2, z2, d)
			break
	else:
		create_pipeline(id, x1, y1, z1, x2, y2, z2, d)
	bpy.ops.object.select_all(action='DESELECT')	
	
def create_pipeline(id, x1, y1, z1, x2, y2, z2, d):
	bpy.ops.curve.primitive_bezier_curve_add()
	bpy.context.selected_objects[0].name = id
	set_vertpos(bpy.context.selected_objects[0].data.splines[0].bezier_points[0], (x1, y1, z1))
	set_vertpos(bpy.context.selected_objects[0].data.splines[0].bezier_points[1], (x2, y2, z2))
	bpy.context.selected_objects[0].data.bevel_depth = d
	
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
	
def add_pipe(x1, y1, z1, x2, y2, z2, d):
	bpy.ops.object.editmode_toggle()
	bpy.ops.curve.primitive_bezier_curve_add()
	set_vertpos(bpy.context.edit_object.data.splines[1].bezier_points[0], (x1, y1, z1))
	set_vertpos(bpy.context.edit_object.data.splines[1].bezier_points[1], (x2, y2, z2))
	bpy.context.selected_objects[0].data.bevel_depth = d
	bpy.ops.object.editmode_toggle()
	
def set_pipelinesetting(pipeline):
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
		set_pipelinesetting(bpy.context.selected_objects[0])
		export_mesh2obj()
		mesh.select_set(0)

def export_mesh2obj():
	name = bpy.context.selected_objects[0].name
	bpy.ops.export_scene.obj(filepath=os.path.join(path, "result", name),
							use_selection=True,
							use_materials=False)


if __name__ == "__main__":
	main()