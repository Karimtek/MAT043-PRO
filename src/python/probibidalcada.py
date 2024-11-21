import pandas as pd
from scipy import stats
import numpy as np

# Cargar los datos
url = "ames-housing.csv"
ames_data = pd.read_csv(url)



# Ajustar una distribución log-normal
shape, loc, scale = stats.lognorm.fit(ames_data['SalePrice'], floc=0)

# En el condado de Ames, ¿Cu´al es la probabilidad de que una casa cueste m´as de 200,000 US dollars?
price_threshold = 200000
probability_more_than_200k = 1 - stats.lognorm.cdf(price_threshold, shape, loc, scale)

# Imprimir la probabilidad
print(f"La probabilidad de que una casa cueste más de 200,000 dólares es: {probability_more_than_200k:.4f}")

# ¿Cuál es el valor esperado del precio de las casas a la venta en Ames de acuerdo al modelo ajustado?
expected_value = scale * np.exp((shape ** 2) / 2)

# Imprimir el valor esperado
print(f"El valor esperado del precio de las casas a la venta en Ames es: ${expected_value:.2f}")