import pyvista as pv
import numpy as np

# Crear una geometría simple del detector de agua Cherenkov
detector = pv.Sphere(radius=10)

# Generar puntos aleatorios que representen partículas interactuando con el detector
num_points = 1000
theta = np.random.uniform(0, np.pi, num_points)
phi = np.random.uniform(0, 2 * np.pi, num_points)
r = np.random.uniform(0, 10, num_points)
x = r * np.sin(theta) * np.cos(phi)
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

# Crear el plotter y agregar la geometría del detector y los puntos de interacción
p = pv.Plotter()
p.add_mesh(detector, color='blue', opacity=0.5)
p.add_points(np.column_stack([x, y, z]), color='yellow', point_size=5)
p.show()
