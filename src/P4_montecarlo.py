import numpy as np
from scipy import stats

def simular_mes_operaciones():
    tiempo_total_mes = 30 * 6 * 60  # 30 días * 6 horas * 60 minutos
    tiempo_acumulado = 0
    pacientes_operados = 0

    while tiempo_acumulado < tiempo_total_mes:
        # Tiempo de espera pre-operatorio (distribución normal)
        tiempo_espera = max(0, np.random.normal(16, 4))
        
        # Tiempo de cirugía (distribución exponencial)
        tiempo_cirugia = np.random.exponential(56)
        
        # Tiempo post-operatorio (distribución uniforme)
        tiempo_post = np.random.uniform(15, 25)
        
        # Tiempo total para este paciente
        tiempo_total_paciente = tiempo_espera + tiempo_cirugia + tiempo_post
        
        # Si hay tiempo suficiente para este paciente
        if tiempo_acumulado + tiempo_total_paciente <= tiempo_total_mes:
            tiempo_acumulado += tiempo_total_paciente
            pacientes_operados += 1
        else:
            break

    return pacientes_operados

# Ejecutar la simulación varias veces para obtener un promedio
num_simulaciones = 10000
resultados = [simular_mes_operaciones() for _ in range(num_simulaciones)]

promedio_pacientes = np.mean(resultados)
desviacion_estandar = np.std(resultados)

print(f"Promedio de pacientes operados en un mes: {promedio_pacientes:.2f}")
print(f"Desviación estándar: {desviacion_estandar:.2f}")

# Intervalo de confianza del 95%
intervalo_confianza = stats.norm.interval(0.95, loc=promedio_pacientes, scale=desviacion_estandar / np.sqrt(num_simulaciones))

print(f"Intervalo de confianza del 95%: {intervalo_confianza}")
