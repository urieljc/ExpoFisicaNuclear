import pyvista as pv
import numpy as np

# Crear un rayo cósmico
origin = [0, 0, 0]
direction = [1, 1, 1]  # Dirección del rayo cósmico
length = 10  # Longitud del rayo cósmico
num_branches = 5  # Número de ramificaciones

# Generar puntos para el rayo cósmico y sus ramificaciones
points = [origin]
for i in range(num_branches):
    branch_direction = np.random.normal(0, 1, 3)  # Dirección de la ramificación
    branch = origin + length * branch_direction
    points.append(branch)

# Crear la estructura de datos PolyData con PyVista
lines = np.column_stack([list(range(len(points)-1)), list(range(1, len(points)))])
cloud = pv.PolyData()
cloud.points = points
cloud.lines = lines

# Crear la trama de PyVista
p = pv.Plotter()
p.add_lines(cloud, width=5, color='blue')
p.show()
