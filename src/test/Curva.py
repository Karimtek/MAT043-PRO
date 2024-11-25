import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Cargar los datos
url = "ames-housing.csv"
ames_data = pd.read_csv(url)

# Configurar el estilo de los gráficos
sns.set(style="whitegrid")

# Crear un histograma y una curva de densidad
plt.figure(figsize=(12, 8))
sns.histplot(ames_data['SalePrice'], bins=30, kde=False, color='lightblue', stat='density', label='Histograma')

# Ajustar una distribución normal
mu, std = stats.norm.fit(ames_data['SalePrice'])  # Ajustar la distribución normal
xmin, xmax = plt.xlim()  # Limites del eje x
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mu, std)  # Calcular la densidad de probabilidad
plt.plot(x, p, 'k', linewidth=2, label='Ajuste Normal')

# Ajustar una distribución log-normal
shape, loc, scale = stats.lognorm.fit(ames_data['SalePrice'], floc=0)  # Ajustar la distribución log-normal
p_lognorm = stats.lognorm.pdf(x, shape, loc, scale)
plt.plot(x, p_lognorm, 'r-', linewidth=2, label='Ajuste Log-normal')

# Guardar la figura
plt.savefig('CurvaDensidad.png', dpi=300)

# Personalizar el gráfico
plt.title('Histograma de SalePrice con Ajustes de Densidad')
plt.xlabel('Precio de Venta (SalePrice)')
plt.ylabel('Densidad')
plt.legend()
plt.show()

# Realizar una prueba de bondad de ajuste
# Prueba Kolmogorov-Smirnov para la distribución normal
ks_stat_norm, ks_p_value_norm = stats.kstest(ames_data['SalePrice'], 'norm', args=(mu, std))

# Prueba Kolmogorov-Smirnov para la distribución log-normal
ks_stat_lognorm, ks_p_value_lognorm = stats.kstest(ames_data['SalePrice'], 'lognorm', args=(shape, loc, scale))

# Imprimir resultados
print(f"Prueba Kolmogorov-Smirnov para Normal: Estadística KS = {ks_stat_norm:.4f}, p-valor = {ks_p_value_norm:.4f}")
print(f"Prueba Kolmogorov-Smirnov para Log-normal: Estadística KS = {ks_stat_lognorm:.4f}, p-valor = {ks_p_value_lognorm:.4f}")
