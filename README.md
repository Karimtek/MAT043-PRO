<!-- @format -->
# Proyecto MAT043:  Probabilidad y Estadística

#### Profesor que dicta el curso: Dr. Ronny Vallejos


| Integrante         | Rol         | mail                                     |
| ------------------ | ----------- | ---------------------------------------- |
| Karime Jarufe      | 202330020-9 | [kjarufe](mailto:kjarufe@usm.cl)         |
| Francisco González | 202330029-2 | [fgonzalezmi](mailto:fgonzalezmi@usm.cl) |

---

Este repositorio contiene el desarrollo completo del proyecto de análisis y simulación en estadística aplicada. El proyecto utiliza herramientas y técnicas avanzadas de probabilidad y estadística computacional para resolver una serie de problemas prácticos, aplicando simulación Monte Carlo y otros métodos estadísticos. La programación en **Python** se utiliza para implementar los modelos, realizar simulaciones y generar los resultados de los problemas planteados.

El repositorio incluye el código fuente para resolver los problemas, los gráficos generados a partir de los datos y el documento final en formato LaTeX que describe el análisis, los resultados obtenidos y las conclusiones.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```markdown
Proyecto
│
├── src/
│    ├── Problema1_graficos.py
│    ├── Problema1_valores.py
│    ├── Problema2.py
│    ├── Problema3.py
│    ├── Problema4.py
│    ├── data/ (# contiene "ames-housing.csv" )
│    ├── images/ (# imágenes de los gráficos del proyecto)
│    └── test/ (# carpeta para pruebas unitarias)
│
├── docs/
│    ├── proyecto.tex
│    └── proyecto.pdf
│
└── readme.md
```

### Descripción de las carpetas y archivos

1. **`src/`**: Esta carpeta contiene el código fuente de los problemas planteados en el proyecto.

   - **`Problema1_graficos.py`**: Código relacionado con el análisis de precios de casas, incluyendo la visualización y el ajuste de una distribución log-normal a los datos de precios.
   - **`Problema1_valores.py`**: Código relacionado con el cálculo de probabilidad y esperanza relacionado con la problematica.
   - **`Problema2.py`**: Código para la simulación de Monte Carlo que estima la cantidad de asientos extra disponibles en vuelos, utilizando la distribución de Poisson para modelar los no-shows de los pasajeros.
   - **`Problema3.py`**: Código para simular la probabilidad de que un peaje logre atender más de 500 autos en un día, utilizando distribuciones normales y exponenciales.
   - **`Problema4.py`**: Código para la simulación de la capacidad de una sala de operaciones, modelando tiempos de espera y cirugía con distribuciones normales y exponenciales.
   - **`data/`**: carpeta en la que se almacena *ames-housing.csv*, archivo que contiene los datos estudiado en el problema 1.
   - **`image/`**: Carpeta que contiene las imágenes generadas, como los gráficos de los histogramas y las distribuciones ajustadas, que se utilizan para visualizar los resultados de los análisis.
   - **`test/`**: Carpeta reservada para pruebas unitarias.

2. **`docs/`**: Esta carpeta contiene los documentos de presentación del proyecto.

   - **`proyecto.tex`**: El archivo fuente de LaTeX que contiene el documento completo del proyecto, donde se describen los métodos utilizados, los resultados y las conclusiones. Este archivo incluye tanto los cálculos teóricos como los resultados obtenidos computacionalmente.
   - **`proyecto.pdf`**: El archivo PDF resultante, generado a partir de `proyecto.tex`, que incluye todos los detalles del análisis, gráficos y conclusiones.

3. **`README.md`**: Este archivo. Contiene información general sobre el repositorio.

## Propósito del Proyecto

El objetivo de este proyecto es aplicar métodos de probabilidad y estadística para resolver problemas prácticos que se encuentran en diversas áreas, como la economía, la ingeniería y la gestión de recursos. A través del uso de simulaciones y modelos estadísticos, se busca proporcionar soluciones a problemas complejos y estimar resultados bajo condiciones de incertidumbre.

En particular, los codigos en este repositorio abordan los siguientes problemas de nuestro proyecto:

- **Análisis de precios de casas en Ames, Iowa**, ajustando un modelo log-normal a los datos.
- **Estimación de asientos extra disponibles en vuelos**, utilizando simulaciones basadas en la distribución de Poisson.
- **Simulación de probabilidad de atención en un peaje**, con modelos de distribución normal y exponencial.
- **Simulación de la capacidad de una sala de operaciones**, utilizando distribuciones normales, exponenciales y uniformes.

El proyecto también muestra cómo los métodos computacionales, como la simulación Monte Carlo, pueden ser utilizados para obtener soluciones precisas.

## Instrucciones para Ejecutar el Proyecto

1. **Requisitos previos**:

   - Instalar Python 3.6 o superior.
   - Instalar las siguientes bibliotecas:
     ```bash
     pip install numpy pandas matplotlib seaborn scipy
     ```

2. **Ejecución**:

   - Para ejecutar los scripts de cada problema, simplemente corra el archivo correspondiente en la carpeta `src/`. Por ejemplo:
     ```bash
     python src/problema1.py
     ```
