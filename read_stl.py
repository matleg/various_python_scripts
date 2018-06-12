from __future__ import print_function
import numpy
from stl import mesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d


# Create a new plot
fig = plt.figure()

axes = fig.add_subplot(111, projection='3d')


# Using an existing stl file:
your_mesh = mesh.Mesh.from_file('pont.stl')
print(your_mesh)
print('v0',your_mesh.v0,your_mesh.v0.shape) # all the first vertices of each tri
#print(your_mesh.v1,your_mesh.v1.shape)
#print(your_mesh.v2,your_mesh.v2.shape)
#print(your_mesh.points,your_mesh.points.shape) # 20x9
all_stl_v = [your_mesh.v0,your_mesh.v1,your_mesh.v2] # list de 3 tableaux
print('all_stl_v',all_stl_v, type(all_stl_v), len(all_stl_v))


all_stl_vertices_concatenated = numpy.concatenate(all_stl_v) # 1 tableau de 60
#print(all_stl_vertices_concatenated, all_stl_vertices_concatenated.shape)  #60x3


num_v0_vertices = len(your_mesh.v0)
print(numpy.arange(1, 3 * num_v0_vertices + 1, 3, dtype=numpy.int32))
print(numpy.arange(2, 3 * num_v0_vertices + 1, 3, dtype=numpy.int32))


all_ids = numpy.concatenate([
                numpy.arange(1, 3 * num_v0_vertices + 1, 3, dtype=numpy.int32),
                numpy.arange(2, 3 * num_v0_vertices + 1, 3, dtype=numpy.int32),
                numpy.arange(3, 3 * num_v0_vertices + 1, 3, dtype=numpy.int32)])

##print(all_ids, all_ids.shape)
##[ 1  4  7 10 13 16 19 22 25 28 31 34 37 40 43 46 49 52 55 58  2  5  8 11
## 14 17 20 23 26 29 32 35 38 41 44 47 50 53 56 59  3  6  9 12 15 18 21 24
## 27 30 33 36 39 42 45 48 51 54 57 60] (60L,)




print(your_mesh.values)


print(dir(your_mesh))
print(type(your_mesh))

dists = [1,2,3,4,5]
erf_disps = [6,7,8,9,10]

print((dists, erf_disps), type((dists, erf_disps)))
(dists, erf_disps) = zip(*[(x[0], x[1]) for x in zip(dists,erf_disps)])
print((dists, erf_disps), type((dists, erf_disps)))




##axes.add_collection3d(art3d.Poly3DCollection(your_mesh.vectors))
##
### Auto scale to the mesh size
##scale = your_mesh.points.flatten(-1)
##axes.auto_scale_xyz(scale, scale, scale)
##plt.show()

