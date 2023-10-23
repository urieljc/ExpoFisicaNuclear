import pyvista as pv
import numpy as np

# Crear una malla para representar el detector de agua (esto es un ejemplo simplificado)
detector_mesh = pv.Cylinder(radius=5, height=10)

# Crear un plotter de PyVista
plotter = pv.Plotter()

# Agregar el detector de agua a la visualización
plotter.add_mesh(detector_mesh, color='blue', opacity=0.5)

# Configurar la visualización
plotter.set_background('white')
plotter.show_grid()

# Configurar la cámara
plotter.view_isometric()

# Mostrar la visualización interactiva
plotter.show()
