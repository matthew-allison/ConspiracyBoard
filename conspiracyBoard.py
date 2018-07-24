import bpy
from math import radians

corkBoardMesh = bpy.ops.mesh.primitive_plane_add(radius=10, location=(0, 0, 3.5), rotation=(radians(90), 0, 0))
