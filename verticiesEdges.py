import bpy
import bmesh
       

# The 2d array of points to generate and connect
verts = [[ 1.10319034e+00,  0.00000000e+00],
       [ 1.26810220e+00,  7.32139148e-01],
       [ 3.72237910e-01,  6.44734972e-01],
       [ 5.96399037e-17,  9.73993543e-01],
       [-1.06300704e+00,  1.84118219e+00],
       [-4.74673446e-01,  2.74052842e-01],
       [-9.73993543e-01,  1.19279807e-16],
       [-1.84118219e+00, -1.06300704e+00],
       [-2.74052842e-01, -4.74673446e-01],
       [-9.06804577e-17, -4.93641420e-01],
       [ 1.10623236e+00, -1.91605065e+00],
       [ 9.05699733e-01, -5.22905984e-01],
       [ 1.10319034e+00,  0.00000000e+00]]

       
mesh = bpy.data.meshes.new("mesh")  # add a new mesh
obj = bpy.data.objects.new("MyObject", mesh)  # add a new object using the mesh

scene = bpy.context.scene
scene.collection.objects.link(obj)  # put the object into the scene (link)
bpy.context.view_layer.objects.active = obj  # set as the active object in the scene
obj.select_set(state=True)  # select object

mesh = bpy.context.object.data
bm = bmesh.new()
last = None
end = None
beginning = None
for v in range(0, len(verts)):
    new = bm.verts.new((verts[v][0], verts[v][1], 0))  # add a new vert
    if v == len(verts) - 1:
        end = new
    if v == 0:
        beginning = new
    if last != None:
        bm.edges.new([last, new])
        last = new
    else:
        last = new
bm.edges.new([beginning, end])
    

# make the bmesh the object's mesh
bm.to_mesh(mesh)  
bm.free()  # always do this when finished