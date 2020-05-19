# -*- coding: utf-8 -*-
"""
Created on Mon May 11 16:37:56 2020

@author: Nikki Frazer
CTA200H
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


plt.rcParams['ytick.minor.visible'] = True
plt.rcParams['xtick.minor.visible'] = True


#Question 1
"""
Create a function that takes (x, y) positions, and returns a two-dimensional 
symmetric Gaussian function. Describe the parameters that are needed for the 
Gaussian function beyond the x and y positions. Describe how you would make 
this a fully generic two dimensional Gaussian function.
"""
def two_d_Gauss(x, y, mu, sigma):
    """
    Given a position of (x,y), return a 2D symmetric Gaussian function
    
    example of x and y:
    x = np.linspace(-1,1,10)
    y = np.linspace(-1,1,10)
    """
    #values
    
    #create coordinates
    X,Y = np.meshgrid(x, y) 
    #Gaussian equation
    z = np.exp(-((X-mu)**2+(Y-mu)**2)/2.0*sigma**2)
    
    return z

#Question 2
#plot an imagemap of a 2D gaussian function
z = two_d_Gauss(np.linspace(-1,1,50), np.linspace(-1,1,100), 0, 0.5)


plt.figure()
plt.imshow(z, cmap="viridis", origin='lower', aspect='equal', extent=(-1, 1, -1, 1))
plt.title('Question 2')
plt.savefig("CTA200.Question 2.pdf")
plt.show()
plt.clf()

#Question 3
#create random noise and add it to the data to be plotted
noise = np.random.normal(0, 0.2, size=(100, 50))
noisy_z = z + noise 


#Question 4
#create an inset axis
fig = plt.figure()
plt.imshow(z, cmap="viridis", origin='lower', aspect='equal', extent=(-1, 1, -1, 1))
plt.title('Question 4')
ax = fig.add_axes([0.21,0.525,1/3,1/3])
ax.imshow(noisy_z, cmap="jet", origin='lower', aspect='equal', extent=(-1, 1, -1, 1))
ax.tick_params(axis='y', which='both', labelleft=False, labelright=True, labeltop=False)
plt.savefig("CTA200.Question4.pdf")
plt.show()


#Questions 5
#create a white arrow 
fig = plt.figure()
plt.imshow(z, cmap="viridis", origin='lower', aspect='equal', extent=(-1, 1, -1, 1))
plt.title('Question 5')
ax = fig.add_axes([0.21,0.525,1/3,1/3])
ax.imshow(noisy_z, cmap="jet", origin='lower', aspect='equal', extent=(-1, 1, -1, 1))
ax.tick_params(axis='y', which='both', labelleft=False, labelright=True, labeltop=False)
ax.arrow(0,0,1,-1, width= 0.20, clip_on=False, color='w', head_length=0.4, head_width=0.6,zorder=10)
plt.savefig("CTA200.Question5.pdf")
plt.show()


#Question 6
#plot three sets of random numbers marked by letters on both axes 
#set one
points_1_x = np.random.uniform(-0.9, 0.9, 5)
points_1_y = np.random.uniform(-0.9, 0.9, 5)
#set two 
points_2_x = np.random.uniform(-0.9, 0.9, 5)
points_2_y = np.random.uniform(-0.9, 0.9, 5)
#set three
points_3_x = np.random.uniform(-0.9, 0.9, 5)
points_3_y = np.random.uniform(-0.9, 0.9, 5)


#plot
fig = plt.figure()
ax0 = fig.add_axes([0,0,1,1])
ax0.imshow(z, cmap="viridis", origin='lower', aspect='equal', extent=(-1, 1, -1, 1))
ax0.scatter(points_1_x, points_1_y, marker="$a$",color='red')
ax0.scatter(points_3_x, points_3_y, marker='$c$', color='black')
ax0.set_title('Question 6')
ax = fig.add_axes([0.12,0.65,1/3,1/3])
ax.imshow(noisy_z, cmap="jet", origin='lower', aspect='equal', extent=(-1, 1, -1, 1))
ax.arrow(0,0,1.5,-1.5, width= 0.20, clip_on=False, color='w', head_length=0.4, head_width=0.6,zorder=10)
ax.tick_params(axis='y', which='both', labelleft=False, labelright=True, labeltop=False)
ax.scatter(points_2_x, points_2_y, marker='$b$',color='blue')
ax.scatter(points_3_x, points_3_y, marker='$c$', color='black')
plt.savefig("CTA200.Question6.pdf")
plt.show()



#Question 7
#plot with horizontal colourbar
fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
#main plot
c = ax1.imshow(z, cmap="viridis", origin='lower', aspect='equal', extent=(-1, 1, -1, 1))
ax1.set_title('Question 7')
ax1.scatter(points_1_x, points_1_y, marker="$a$",color='red')
ax1.scatter(points_3_x, points_3_y, marker='$c$', color='black')
#inset axis plot
ax2 = fig.add_axes([0.19,0.64,1/3,1/3])
ax2.imshow(noisy_z, cmap="jet", origin='lower', aspect='equal', extent=(-1, 1, -1, 1))
ax2.arrow(0,0,1,-1, width= 0.20, clip_on=False, color='w', head_length=0.4, head_width=0.6,zorder=10)
ax2.tick_params(axis='y', which='both', labelleft=False, labelright=True, labeltop=False)
ax2.scatter(points_2_x, points_2_y, marker='$b$',color='blue')
ax2.scatter(points_3_x, points_3_y, marker='$c$', color='black')
divider = make_axes_locatable(ax1)
cax = divider.append_axes('bottom', size = '5%', pad =0.5)
plt.colorbar(c, cax=cax, orientation='horizontal')
#Question 8
plt.savefig("CTA200.Question7.pdf", bbox_inches='tight')
plt.show()

























