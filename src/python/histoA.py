import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df = pd.read_csv('ames-housing.csv')

# Crear una figura con 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 6))

# Histograma
sns.histplot(data=df, x='SalePrice', kde=False, ax=ax1)
ax1.set_title('Histograma de SalePrice')
ax1.set_xlabel('Precio de Venta')
ax1.set_ylabel('Frecuencia')

# Boxplot
sns.boxplot(y=df['SalePrice'], ax=ax2)
ax2.set_title('Boxplot de SalePrice')
ax2.set_ylabel('Precio de Venta')

# Violin plot
sns.violinplot(y=df['SalePrice'], ax=ax3)
ax3.set_title('Violin Plot de SalePrice')
ax3.set_ylabel('Precio de Venta')

plt.tight_layout()

# Guardar cada plot como PNG
fig.savefig('histograma_saleprice.png', dpi=300)  # Guardar la figura completa

# Guardar subplots individuales si es necesario
ax1.figure.savefig('histograma_saleprice.png', dpi=300)
ax2.figure.savefig('boxplot_saleprice.png', dpi=300)
ax3.figure.savefig('violin_plot_saleprice.png', dpi=300)

# Ajustar el diseño y mostrar la figura
plt.show()
