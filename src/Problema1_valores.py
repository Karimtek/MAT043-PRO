import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import lognorm

# Cargar el archivo CSV
data = pd.read_csv('data/ames-housing.csv')

# Extraer la columna SalePrice
sale_price = data['SalePrice']

# Ajuste de la distribución log-normal a los datos
# Ajustar la distribución log-normal usando el método de máxima verosimilitud
shape, loc, scale = lognorm.fit(sale_price, floc=0)  # Ajuste sin desplazamiento en el valor mínimo

# Parámetros estimados: media logarítmica y desviación estándar logarítmica
mu = np.log(scale)  # media logarítmica
sigma = shape  # desviación estándar logarítmica

print(f'Parámetro estimado para la media logarítmica (μ): {mu:.2f}')
print(f'Parámetro estimado para la desviación estándar logarítmica (σ): {sigma:.2f}')

# Generar valores para la distribución ajustada
x = np.linspace(min(sale_price), max(sale_price), 1000)
pdf = lognorm.pdf(x, sigma, loc, scale)

# Cálculo de la probabilidad de que el precio de una casa exceda los 200,000 USD
# Usamos la función de distribución acumulada (CDF) de la log-normal para calcular P(X > 200,000)
probability_over_200k = 1 - lognorm.cdf(200000, sigma, loc, scale)
print(f'Probabilidad de que el precio exceda los 200,000 USD: {probability_over_200k:.4f}')

# Cálculo del valor esperado (E[X])
expected_value = np.exp(mu + (sigma**2) / 2)
print(f'Valor esperado del precio de las casas: {expected_value:,.2f} USD')
