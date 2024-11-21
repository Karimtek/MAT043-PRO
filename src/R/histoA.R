# Cargar las librerías necesarias
library(ggplot2)
library(readr)

# Leer el archivo CSV
datos <- read_csv("ames-housing.csv", show_col_types = FALSE)

# 1. Histograma
histograma <- ggplot(datos, aes(x = SalePrice)) +
  geom_histogram(binwidth = 10000, fill = "skyblue", color = "black") +
  labs(title = "Histograma de SalePrice",
       x = "Precio de Venta",
       y = "Frecuencia") +
  theme_minimal()

# 2. Boxplot
boxplot <- ggplot(datos, aes(y = SalePrice)) +
  geom_boxplot(fill = "lightgreen") +
  labs(title = "Boxplot de SalePrice",
       y = "Precio de Venta") +
  theme_minimal()

# 3. Violin plot
violin_plot <- ggplot(datos, aes(x = "", y = SalePrice)) +
  geom_violin(fill = "lightpink") +
  labs(title = "Violin Plot de SalePrice",
       x = "",
       y = "Precio de Venta") +
  theme_minimal()

# Mostrar los gráficos
print(histograma)
print(boxplot)
print(violin_plot)

# Opcional: Guardar los gráficos como archivos PNG
ggsave("histograma_saleprice.png", histograma, width = 8, height = 6)
ggsave("boxplot_saleprice.png", boxplot, width = 8, height = 6)
ggsave("violinplot_saleprice.png", violin_plot, width = 8, height = 6)
