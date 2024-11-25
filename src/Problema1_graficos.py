import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import lognorm
from matplotlib.ticker import FuncFormatter

# Función para formatear los números
def human_format(num, pos):
    magnitud = 0
    while abs(num) >= 1000:
        magnitud += 1
        num /= 1000
    return '%i%s' % (num, ['', 'k', 'M', 'G', 'T', 'P'][magnitud])

formatter = FuncFormatter(human_format)

# Configuración de estilo general
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'Times New Roman',  # Cambiar la fuente
    'axes.edgecolor': 'black',        # Color de los bordes
    'grid.color': 'gray',             # Color de las líneas de la cuadrícula
    'grid.alpha': 0.3                 # Transparencia de la cuadrícula
})

def load_data(url):
    return pd.read_csv(url)

def plot_histogram(data, filename):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(data, bins=30, alpha=0.7, color='#4c72b0', edgecolor='black')
    ax.set_title("Distribución de Precios de Venta", fontsize=20)
    ax.set_xlabel("Precio de Venta (USD)", fontsize=19)
    ax.set_ylabel("Frecuencia", fontsize=19)
    plt.xticks(fontsize=17)
    plt.yticks(fontsize=17)
    ax.xaxis.set_major_formatter(formatter)

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

def plot_box_violin(data, filename):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=data, color='#92c5de', ax=ax, linewidth=1, width=0.30, orient='h')
    sns.violinplot(x=data, color='#f4a582', alpha=0.5, ax=ax, linewidth=1.5)
    ax.set_title("Análisis de la Distribución de Precios", fontsize=20)
    ax.set_xlabel("Precio de Venta (USD)", fontsize=19)
    ax.xaxis.set_major_formatter(formatter)
    plt.xticks(fontsize=17)

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

def plot_histogram_with_lognormal_fit(data, filename):
    shape, loc, scale = lognorm.fit(data, floc=0)
    x = np.linspace(min(data), max(data), 1000)
    pdf = lognorm.pdf(x, shape, loc=loc, scale=scale)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(data, bins=30, density=True, alpha=0.7, color='#4c72b0', edgecolor='black', label="Histograma")
    ax.plot(x, pdf, color='#e84a5f', linewidth=2, label="Log-Normal Ajustada")
    ax.set_title("Ajuste de Distribución Log-Normal", fontsize=20)
    ax.set_xlabel("Precio de Venta (USD)", fontsize=19)
    ax.set_ylabel("Densidad", fontsize=19)
    ax.xaxis.set_major_formatter(formatter)
    plt.xticks(fontsize=17)
    plt.yticks(fontsize=17)
    ax.legend(fontsize=16)

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()


def main():
    url = 'data/ames-housing.csv'
    data = load_data(url)
    sale_price = data['SalePrice']

    plot_histogram(sale_price, "histograma_saleprice.png")
    plot_box_violin(sale_price, "boxplot_violin_saleprice.png")
    plot_histogram_with_lognormal_fit(sale_price, "densidad_ajustada.png")

if __name__ == "__main__":
    main()
