#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class threedvis:
    """
    A library for easy 3D visualizations using Matplotlib.
    """

    @staticmethod
    def scatter3d(x, y, z, color='b', size=20, title="3D Scatter Plot",
                  xlabel="X-axis", ylabel="Y-axis", zlabel="Z-axis"):
        """
        Creates a 3D scatter plot.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, c=color, s=size)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)
        plt.show()

    @staticmethod
    def line3d(x, y, z, color='r', linewidth=2, title="3D Line Plot",
               xlabel="X-axis", ylabel="Y-axis", zlabel="Z-axis"):
        """
        Creates a 3D line plot.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y, z, color=color, linewidth=linewidth)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)
        plt.show()

    @staticmethod
    def surface3d(func, xlim=(-5, 5), ylim=(-5, 5), title="3D Surface Plot",
                  xlabel="X-axis", ylabel="Y-axis", zlabel="Z-axis"):
        """
        Creates a 3D surface plot based on a function.
        """
        x = np.linspace(xlim[0], xlim[1], 50)
        y = np.linspace(ylim[0], ylim[1], 50)
        X, Y = np.meshgrid(x, y)
        Z = func(X, Y)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)
        plt.show()

    @staticmethod
    def wireframe3d(func, xlim=(-5, 5), ylim=(-5, 5), title="3D Wireframe Plot",
                    xlabel="X-axis", ylabel="Y-axis", zlabel="Z-axis"):
        """
        Creates a 3D wireframe plot based on a function.
        """
        x = np.linspace(xlim[0], xlim[1], 50)
        y = np.linspace(ylim[0], ylim[1], 50)
        X, Y = np.meshgrid(x, y)
        Z = func(X, Y)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_wireframe(X, Y, Z, color='black')
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)
        plt.show()

    @staticmethod
    def bar3d(x, y, z, dx, dy, dz, title="3D Bar Plot",
              xlabel="X-axis", ylabel="Y-axis", zlabel="Z-axis"):
        """
        Creates a 3D bar plot.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.bar3d(x, y, z, dx, dy, dz)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)
        plt.show()

