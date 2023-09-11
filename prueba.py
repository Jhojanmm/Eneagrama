import matplotlib.pyplot as plt

# Coordenadas de los puntos en el eneagrama
puntos = {
    '1': (0, 1),
    '2': (0.866, 0.5),
    '3': (0.866, -0.5),
    '4': (0, -1),
    '5': (-0.866, -0.5),
    '6': (-0.866, 0.5),
    '7': (0.5, 0.866),
    '8': (0.5, -0.866),
    '9': (-0.5, -0.866),
}

# Conexiones entre puntos en el eneagrama
conexiones = [('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', '1'), ('1', '7'), ('3', '8'), ('5', '9')]

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(8, 8))

# Dibujar las líneas de conexión
for inicio, fin in conexiones:
    xi, yi = puntos[inicio]
    xf, yf = puntos[fin]
    ax.plot([xi, xf], [yi, yf], 'b-')

# Dibujar los puntos
for eneatipo, (x, y) in puntos.items():
    ax.plot(x, y, 'ro', markersize=10)
    ax.annotate(eneatipo, (x, y), fontsize=12, ha='center', va='center')

# Configurar límites y aspecto
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_axis_off()

# Título
ax.set_title('Eneagrama')

# Mostrar la figura
plt.show()
