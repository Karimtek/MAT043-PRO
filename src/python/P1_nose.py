import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import lognorm
from matplotlib.ticker import FuncFormatter

# Función para formatear números a escalas humanas
def human_format(num, pos):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000
    return '%i%s' % (num, ['', 'k', 'M', 'G', 'T', 'P'][magnitude])

formatter = FuncFormatter(human_format)

# Configuración de estilo general
plt.style.use('seaborn-whitegrid')  # Cambiar el estilo
plt.rcParams.update({
    'font.family': 'Times New Roman',  # Cambiar la fuente
    'font.size': 12,                  # Tamaño base de fuente
    'axes.titlesize': 14,             # Tamaño del título de los ejes
    'axes.labelsize': 12,             # Tamaño de las etiquetas de los ejes
    'legend.fontsize': 12,            # Tamaño de las leyendas
    'axes.edgecolor': 'black',        # Color de los bordes
    'grid.color': 'gray',             # Color de las líneas de la cuadrícula
    'grid.alpha': 0.3                 # Transparencia de la cuadrícula
})

# Cargar datos
url = 'ames-housing.csv'
data = pd.read_csv(url)
sale_price = data['SalePrice']

# Gráfico 1: Histograma
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(sale_price, bins=30, alpha=0.7, color='#4c72b0', edgecolor='black')
ax.set_title("Distribución de Precios de Venta", fontsize=16)
ax.set_xlabel("Precio de Venta (USD)", fontsize=14)
ax.set_ylabel("Frecuencia", fontsize=14)
ax.xaxis.set_major_formatter(formatter)

# Guardar y mostrar
plt.tight_layout()
plt.savefig("P1/histograma_saleprice_formal.png")
plt.show()

# Gráfico 2: Boxplot y Violin Plot
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(x=sale_price, color='#92c5de', ax=ax, linewidth=1.5)
sns.violinplot(x=sale_price, color='#f4a582', alpha=0.5, ax=ax, linewidth=1.5)
ax.set_title("Análisis de la Distribución de Precios", fontsize=16)
ax.set_xlabel("Precio de Venta (USD)", fontsize=14)
ax.xaxis.set_major_formatter(formatter)

# Guardar y mostrar
plt.tight_layout()
plt.savefig("P1/boxplot_violin_saleprice_formal.png")
plt.show()

# Gráfico 3: Histograma con Densidad Log-Normal Ajustada
shape, loc, scale = lognorm.fit(sale_price, floc=0)
x = np.linspace(min(sale_price), max(sale_price), 1000)
pdf = lognorm.pdf(x, shape, loc=loc, scale=scale)

fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(sale_price, bins=30, density=True, alpha=0.7, color='#4c72b0', edgecolor='black', label="Histograma")
ax.plot(x, pdf, color='#e84a5f', linewidth=2, label="Log-Normal Ajustada")
ax.set_title("Ajuste de Distribución Log-Normal", fontsize=16)
ax.set_xlabel("Precio de Venta (USD)", fontsize=14)
ax.set_ylabel("Densidad", fontsize=14)
ax.xaxis.set_major_formatter(formatter)
ax.legend()

# Guardar y mostrar
plt.tight_layout()
plt.savefig("P1/densidad_ajustada_formal.png")
plt.show()
