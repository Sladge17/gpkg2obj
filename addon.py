import bpy
import sys # to work geopandas
sys.path.append('/Users/jthuy/.local/lib/python3.7/site-packages')
#import pandas as pd
import geopandas as gpd
import numpy as np

path = "/Users/jthuy/Desktop/BConv/"
file = "engenier_network.gpkg"

pipe_diameter = 0.2
pepe_resolution = 2 # equally 8 edges
box_size = (1, 1, 1)


def main():
#	clear_scene()

    data = gpd.read_file(path + file)
    df = data[['ID', 'SECT_TYPE', 'SECT_WIDTH', 'SECT_HEIGH', 'H1', 'geometry']]
    for string in range(len(df)):
        id = int(df['ID'][string])
        vertex = len(df['geometry'][string][0].xy[0])

        for vertex in range(len(df['geometry'][string][0].xy[0]) - 1):
            crd_x1 = round(df['geometry'][string][0].xy[0][vertex], 3)
            crd_y1 = round(df['geometry'][string][0].xy[1][vertex], 3)
            crd_x2 = round(df['geometry'][string][0].xy[0][vertex + 1], 3)
            crd_y2 = round(df['geometry'][string][0].xy[1][vertex + 1], 3)
            crd_z = -round(df['H1'][string].item(), 3)
#            df['H1'][string] = int(df['H1'][string])
#            print(type(df['H1'][string]))
            create_pipe(crd_x1, crd_y1, crd_x2, crd_y2, crd_z)
            break
        break
    
#	parsing_file() NEED DEL
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
	
def create_pipe(crd_x1, crd_y1, crd_x2, crd_y2, crd_z):
#	print(type(crd_z), crd_z)
	bpy.ops.curve.primitive_bezier_curve_add()
	set_vertpos(bpy.context.selected_objects[0].data.splines[0].bezier_points[0], (crd_x1, crd_y1, crd_z))
	set_vertpos(bpy.context.selected_objects[0].data.splines[0].bezier_points[1], (crd_x2, crd_y2, crd_z))
	set_pipelinesetting(bpy.context.selected_objects[0]) # TMP LINE
	
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