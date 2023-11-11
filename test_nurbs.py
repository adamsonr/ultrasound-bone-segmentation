# -*- coding: utf-8 -*-
"""
Demonstrates difference in behaviour of approximate_surface() with
uniform and random data
"""

import numpy as np 
from geomdl import fitting
import open3d as o3d

Nx, Ny = 100, 100
# Set up a surface on a uniform grid
X, Y = np.mgrid[-1:1:100j, -1:1:100j]
x_uniform, y_uniform = np.vstack([X.ravel(), Y.ravel()])
z_uniform = x_uniform**2 + y_uniform**2
points_uniform = np.array([x_uniform,y_uniform,z_uniform]).T 
surf_uniform = fitting.approximate_surface(points_uniform, size_u=100, size_v=100, degree_u=3, degree_v=3)
evalpts_uniform = np.array(surf_uniform.evalpts)

#%%
# Set up a surface on a random grid
X, Y = np.mgrid[-1:1:100j, -1:1:100j]
x_random, y_random = np.random.uniform(-1,1,Nx*Ny), np.random.uniform(-1,1,Nx*Ny) 
z_random = x_random**2 + y_random**2
points_random = np.array([x_random,y_random,z_random]).T 
surf_random = fitting.approximate_surface(points_random, size_u=100, size_v=100, degree_u=3, degree_v=3)
evalpts_random = np.array(surf_random.evalpts)

#%%
# Plot evaluated points approximated to uniform grid
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(evalpts_uniform)
pcd.paint_uniform_color([1, 0.706, 0])
o3d.visualization.draw_geometries([pcd])
#%%
# Plot evaluated points approximated to random grid
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(evalpts_random)
pcd.paint_uniform_color([1, 0.706, 0])
o3d.visualization.draw_geometries([pcd])
#%%


