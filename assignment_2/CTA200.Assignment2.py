# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:24:59 2020

@author: Nikki Frazer
Student Number: 1003111116
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#Question 1
#create the basic plot
def divergent(x:int, y:int, iteration_count:int):
    """Given the data point x y where c_pair= x + iy
    is in the complex plane. x and y values are from -2 to 2 exclusive.
    Return a list of ones and zeros corresponding to whether a z
    value diverges or converges at that point c."""
    
    z = complex(0,0)
    c_pair = complex(x,y)
    c_values = []
    
    for iteration in range(iteration_count):
        z = (z * z) + (c_pair)
        #split z into real and imaginary parts
        #if the real part of z goes over 2, the point will diverge
        zR = z.real
        #at each iteration check if the point is diverging 
        if zR > 2:
            c_values.append(0)
            break
    else:
        c_values.append(1)
        #if zR reaches 2, break out of loop since it will diverge
    return c_values

print("For point (1, 1) in the complex plane, it is divergent if 0, convergent if 1:", divergent(1, 1, 50))


def mandel_plot(threshold, density):
    """
    Given a threshold, return a plot for a mandelbrot set,
    calling upon the function divergent to supply the 
    values of when an iteration of z diverges or converges.
    
    """
    x_axis = np.linspace(-2, 2, density)
    y_axis = np.linspace(-2, 2, density)
    x_length = len(x_axis)
    y_length = len(y_axis)
    
    X, Y = np.meshgrid(x_axis, y_axis)
    c= []
    
    for i in range(x_length):
        for k in range(y_length):
            x = X[i,k]
            y = Y[i,k]
            c = c + divergent(x, y, threshold)
    
    c = np.array(c)
    
    plt.scatter(np.reshape(X, -1), np.reshape(Y, -1), c=np.reshape(c,-1))
    plt.title("Basic Mandelbrot Plot")
    plt.xlabel("real axis")
    plt.ylabel("imaginary axis")
    plt.show()

   
mandel_plot(50, 250)


#Colourbar Plot: count the number of iterations it takes for each point C to diver or converge (github)

def how_many_iterations(x:int, y:int, iteration_count:int):
    """Count how many iterations it takes to establish that 
    a certain point c: x + iy is not part of the Mandelbrot set
    """
    
    z = complex(0, 0)
    c_pair = complex(x,y)
    c_values = []
    
    for iteration in range(iteration_count):
        z = (z * z) + (c_pair)
        #split z into real and imaginary parts
        #if the real part of z goes over 2, the point will diverge
        zR = z.real
        #at each iteration check if the point is diverging 
        if zR > 2:
            c_values.append(iteration)
            break
    else:
        c_values.append(0)
        #if zR reaches 2, break out of loop since it will diverge
    return c_values

def mandelbrot_scale(threshold, density):
    """
    Given a threshold, return a plot for a mandelbrot set,
    calling upon the function divergent to supply the 
    values of when an iteration of z diverges or converges.
    
    """
    x_axis = np.linspace(-2, 2, density)
    y_axis = np.linspace(-2, 2, density)
    x_length = len(x_axis)
    y_length = len(y_axis)
    
    X, Y = np.meshgrid(x_axis, y_axis)
    c= []
    
    for i in range(x_length):
        for k in range(y_length):
            x = X[i,k]
            y = Y[i,k]
            c = c + how_many_iterations(x, y, threshold)
    
    c = np.array(c)
    
    plt.scatter(np.reshape(X, -1), np.reshape(Y, -1), c=np.reshape(c,-1), cmap="Spectral")
    plt.colorbar(label="Colour")
    plt.title("Colourscale Mandelbrot")
    plt.xlabel("real axis")
    plt.ylabel("imaginary axis")
    plt.show()
   
mandelbrot_scale(50, 250)


#Question 2
#population 
N = 1000 
#timeline of 200 days
t = np.linspace(0, 200, 200)
#inital numbers N = I + S + R
#inital number of infected individuals
infected_0 = 1
#initial number of susceptible individuals
sus_0 = 999
#initial value of recovered individuals
recovered_0 = 0
y_naught = sus_0, infected_0, recovered_0
beta = 1
gamma = 0.10
# The SIR model differential equations
def SIR(t, y):
    S = y[0]
    I = y[1]
    R = y[2]
    dS_dt = -(beta * S * I) / 1000
    dI_dt = ((beta * S * I) / (1000)) - (gamma * I)
    dR_dt = gamma * I
    return dS_dt, dI_dt, dR_dt


#integrate the functions using scipy
sol = solve_ivp(SIR, [0,200], y_naught, t_eval=t)
#parameter set one 
#plot
plt.plot(sol.t,sol.y[0], color="slateblue")
plt.plot(sol.t,sol.y[1], color="red")
plt.plot(sol.t,sol.y[2], color="mediumseagreen")
plt.title(r'SIR Population Model 1: $\beta$: 1 $\gamma$: 0.10')
plt.xlabel('Time (days)')
plt.ylabel('Population')
plt.legend(["Susceptible","Infected","Recovered"])
plt.figure()


#parameter set two
beta = 0.2
gamma = 0.10
# The SIR model differential equations
def SIR(t, y):
    S = y[0]
    I = y[1]
    R = y[2]
    dS_dt = -(beta * S * I) / 1000
    dI_dt = ((beta * S * I) / (1000)) - (gamma * I)
    dR_dt = gamma * I
    return dS_dt, dI_dt, dR_dt


#integrate the functions using scipy
sol = solve_ivp(SIR, [0,200], y_naught, t_eval=t)

#plot
plt.plot(sol.t,sol.y[0], color="slateblue")
plt.plot(sol.t,sol.y[1], color="red")
plt.plot(sol.t,sol.y[2], color="mediumseagreen")
plt.title(r'SIR Population Model 2: $\beta$: 0.2 $\gamma$: 0.10')
plt.xlabel('Time (days)')
plt.ylabel('Population')
plt.legend(["Susceptible","Infected","Recovered"])
plt.figure()


#parameter set three
beta = 1
gamma = 0.50
# The SIR model differential equations
def SIR(t, y):
    S = y[0]
    I = y[1]
    R = y[2]
    dS_dt = -(beta * S * I) / 1000
    dI_dt = ((beta * S * I) / (1000)) - (gamma * I)
    dR_dt = gamma * I
    return dS_dt, dI_dt, dR_dt


#integrate the functions using scipy
sol = solve_ivp(SIR, [0,200], y_naught, t_eval=t)

#plot
plt.plot(sol.t,sol.y[0], color="slateblue")
plt.plot(sol.t,sol.y[1], color="red")
plt.plot(sol.t,sol.y[2], color="mediumseagreen")
plt.title(r'SIR Population Model 3: $\beta$: 0.1 $\gamma$: 0.50')
plt.xlabel('Time (days)')
plt.ylabel('Population')
plt.legend(["Susceptible","Infected","Recovered"])
plt.figure()
#parameter set four 
beta = 5
gamma = 0.10
# The SIR model differential equations
def SIR(t, y):
    S = y[0]
    I = y[1]
    R = y[2]
    dS_dt = -(beta * S * I) / 1000
    dI_dt = ((beta * S * I) / (1000)) - (gamma * I)
    dR_dt = gamma * I
    return dS_dt, dI_dt, dR_dt


#integrate the functions using scipy
sol = solve_ivp(SIR, [0,200], y_naught, t_eval=t)

#plot
plt.plot(sol.t,sol.y[0], color="slateblue")
plt.plot(sol.t,sol.y[1], color="red")
plt.plot(sol.t,sol.y[2], color="mediumseagreen")
plt.title(r'SIR Population Model 4: $\beta$: 5 $\gamma$: 0.10')
plt.xlabel('Time (days)')
plt.ylabel('Population')
plt.legend(["Susceptible","Infected","Recovered"])
plt.figure()