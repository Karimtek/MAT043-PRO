import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import lognorm

# Cargar datos
url = 'data/ames-housing.csv'
data = pd.read_csv(url)
sale_price = data['SalePrice']

# Histograma
plt.hist(sale_price, bins=30, alpha=0.7, color='blue')
plt.title("Histograma de SalePrice")
plt.xlabel("Precio de Venta")
plt.ylabel("Frecuencia")
plt.savefig("histograma_saleprice.png")
plt.show()

# Boxplot y Violin plot
plt.figure(figsize=(12, 6))
sns.boxplot(x=sale_price, color='lightblue')
sns.violinplot(x=sale_price, color='pink', alpha=0.5)
plt.title("Boxplot y Violin Plot de SalePrice")
plt.savefig("boxplot_violin_saleprice.png")
plt.show()

# Ajuste de distribución log-normal
shape, loc, scale = lognorm.fit(sale_price, floc=0)
x = np.linspace(min(sale_price), max(sale_price), 1000)
pdf = lognorm.pdf(x, shape, loc=loc, scale=scale)

# Graficar histograma y densidad ajustada
plt.hist(sale_price, bins=30, density=True, alpha=0.7, color='blue', label="Histograma")
plt.plot(x, pdf, color='red', label="Log-Normal Ajustada")
plt.title("Histograma con Densidad Ajustada")
plt.xlabel("Precio de Venta")
plt.ylabel("Densidad")
plt.legend()
plt.savefig("densidad_ajustada.png")
plt.show()
