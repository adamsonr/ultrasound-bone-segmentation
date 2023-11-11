# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.interpolate import RectBivariateSpline


# Load volume from disk.  Run save_vol.py to generate the npz file with
# the volume data
vol=np.load("vol.npz")['vol']
vol=vol[300:,:,:]

#%%
# Make point cloud of bone contour
points=np.argmax(vol, axis=0).T
points=points.astype('float64')
# Mask out the regions where there is no bone segment (mostly around the edge
# of the surface)
mask = (points>60)

# Set up normalized axis arrays
Nx, Ny, Nz = vol.shape
x=np.linspace(-1,1,Nx)
y=np.linspace(-1,1,Ny)
z=np.linspace(-1,1,Nz)
Y,Z = np.meshgrid(y,z)

# Fit surface to a bivariate spline
# the s parameter controls smoothing where larger s is smoother
# bbox is supposed to provide control over the data region that is fit.  s=9e7 produces a decent amount of smoothing
# but it produces an error if anything other than the full data extent is 
# specified

order = 3
# Do the spline fit
rbs = RectBivariateSpline(y,z,points.T, bbox=[-1,1,-1,1], kx=order, ky=order, s=9e7)
# Get smoothed surface location estimates
xfit=rbs.ev(Y,Z)

#%%
from scipy.ndimage import binary_erosion
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

# Mask out point outside of botn surface
points[np.logical_not(mask)] = np.nan
ax1.plot_surface(Y, Z, points)
ax1.set_title("Raw data")

# Spline fit produces artefact around the edges so we need to erode
# the mask inward to avoid displaying them
mask2=binary_erosion(mask, iterations=10)
xfit[np.logical_not(mask2)] = np.nan 
ax2.plot_surface(Y, Z, xfit)
ax2.set_title("Spline fit")

#%%

