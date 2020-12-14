import bpy

bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.export_scene.obj(filepath='/Users/jthuy/Desktop/BConv/test12.obj')
bpy.ops.wm.quit_blender()