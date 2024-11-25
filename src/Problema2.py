import numpy as np
import pandas as pd

num_simulations = 10000

# Capacidades de los aviones
capacities = {
    'Tipo 1': 150,
    'Tipo 2': 300,
    'Tipo 3': 400
}

# Número de vuelos por tipo de avión en un mes
flights = {
    'Tipo 1': 250,
    'Tipo 2': 145,
    'Tipo 3': 87
}

# Esperanza de no presentación (no show) como función de la capacidad
def no_show_lambda(capacity):
    return 0.07 * capacity


total_extra_seats = 0

for _ in range(num_simulations):
    for airplane_type, capacity in capacities.items():
        expected_no_show = no_show_lambda(capacity)
        # Generar el número de no shows según la distribución de Poisson
        no_shows = np.random.poisson(expected_no_show, flights[airplane_type])
        total_extra_seats += np.sum(no_shows)

average_extra_seats = total_extra_seats / num_simulations
print(f'Cantidad total promedio de asientos extra que pueden ser vendidos: {average_extra_seats:.2f}')