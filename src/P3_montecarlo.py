import numpy as np

# Parámetros de las distribuciones
mean_window_1 = 150
std_dev_window_1 = 4  # sqrt(16)

mean_window_2 = 163
std_dev_window_2 = 3.74  # sqrt(14)

lambda_window_3 = 180  # Para la distribución exponencial

# Número de corridas
num_simulations = 100000

# Simulación de Monte Carlo
count_over_500 = 0

for _ in range(num_simulations):
    # Autos atendidos en cada ventanilla
    autos_window_1 = np.random.normal(mean_window_1, std_dev_window_1)
    autos_window_2 = np.random.normal(mean_window_2, std_dev_window_2)
    autos_window_3 = np.random.exponential(lambda_window_3)

    # Total de autos atendidos
    total_autos = autos_window_1 + autos_window_2 + autos_window_3

    # Contar si se atendieron más de 500 autos
    if total_autos > 500:
        count_over_500 += 1

# Calcular la probabilidad
probability_over_500 = count_over_500 / num_simulations
print(f"La probabilidad de que el peaje atienda más de 500 autos diarios es: {probability_over_500:.4f}")

# desviacion estandar de la probabilidad
std_dev = np.sqrt(probability_over_500 * (1 - probability_over_500) / num_simulations)

print(f"Desviación estándar de la probabilidad: {std_dev:.6f}")