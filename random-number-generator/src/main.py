import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest, uniform, expon, norm, chi2
from distributions.uniform import generar_uniforme
from distributions.exponential import generar_exponencial
from distributions.normal import generar_normal
import tkinter as tk
from tkinter import ttk, messagebox

def generar_y_analizar():
    try:
        # Obtener valores de la interfaz
        tamano_de_muestra = int(sample_size_entry.get())
        if not (1 <= tamano_de_muestra <= 1000000):
            raise ValueError("La muestra DEBE ser un valor entre 1 y 1.000.000.")

        distribucion = distribution_combobox.get()
        intervalos = int(intervals_combobox.get())

        # Validaciones según la distribución seleccionada
        if distribucion == "Uniforme":
            a = float(param1_entry.get())
            b = float(param2_entry.get())
            if a >= b:
                raise ValueError("En la distribución uniforme, el valor A debe ser menor que el valor B.")
            numeros_aleatorios = generar_uniforme(tamano_de_muestra, a, b)
            dist = uniform(loc=a, scale=b-a)
        elif distribucion == "Exponencial":
            _lambda = float(param1_entry.get())
            if _lambda <= 0:
                raise ValueError("En la distribución exponencial, lambda debe ser mayor a 0.")
            numeros_aleatorios = generar_exponencial(_lambda, tamano_de_muestra)
            dist = expon(scale=1/_lambda)
        elif distribucion == "Normal":
            media = float(param1_entry.get())
            desviacion = float(param2_entry.get())
            if desviacion <= 0:
                raise ValueError("En la distribución normal, la media y la desviación estándar deben ser mayores a 0.")
            numeros_aleatorios = generar_normal(tamano_de_muestra, media, desviacion)
            dist = norm(loc=media, scale=desviacion)
        else:
            raise ValueError("Distribución invalida!!")

        # Realizar la prueba de bondad de ajuste
        prueba_bondad_de_ajuste(numeros_aleatorios, dist, distribucion, intervalos)

        # Graficar el histograma
        plot_histogram(numeros_aleatorios, intervalos)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def plot_histogram(datos, intervalos):
    counts, bin_edges, _ = plt.hist(datos, bins=intervalos, edgecolor='black')
    plt.title('Histograma de frecuencias')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.grid(axis='y', alpha=0.75)
    plt.xlim(min(datos), max(datos))
    # Mostrar los límites de los intervalos en el eje x
    plt.xticks(bin_edges, [f"{edge:.2f}" for edge in bin_edges], rotation=45)
    plt.tight_layout()
    plt.show()

def prueba_bondad_de_ajuste(datos, distribucion, nombre_distribucion, intervalos):
    if len(datos) >= 30:
        # Prueba de Chi-cuadrado
        observed, bin_edges = np.histogram(datos, bins=intervalos)
        expected = len(datos) * np.diff(distribucion.cdf(bin_edges)) # Marca de Clase
        chi2_stat = np.sum((expected - observed) ** 2 / expected)
        p_valor = chi2.sf(chi2_stat, df=intervalos - 1)  #probabilidad de obtener un valor mayor que chi2_stat
        resultado = f"\nPrueba de CHI-Cuadrado para distribucion {nombre_distribucion}:\n"
        resultado += f"Estadistico de prueba: {chi2_stat}\nP-valor: {p_valor}\n"
        if p_valor > 0.05:
            resultado += "Los datos siguen la distribucion elegida (no es posible rechazar la H0)."
        else:
            resultado += "Los datos NO siguen la distribucion elegida (se rechazaza la H0)."
    else:
        # Prueba de Kolmogorov-Smirnov
        ks_stat, p_valor = kstest(datos, distribucion.cdf)
        resultado = f"\nPrueba de Kolmogorov-Smirnoff para distribucion {nombre_distribucion}:\n"
        resultado += f"Estadistico de prueba: {ks_stat}\nP-valor: {p_valor}\n"
        if p_valor > 0.05:
            resultado += "Los datos siguen la distribucion elegida (no es posible rechazar la H0)."
        else:
            resultado += "Los datos NO siguen la distribucion elegida (se rechazaza la H0)."
    
    print(resultado)
    messagebox.showinfo("Resultados de la prueba de bondad de ajuste", resultado)

def on_distribution_change(event):
    distribucion = distribution_combobox.get()
    if distribucion == "Exponencial":
        param1_label.config(text="Lambda:")
        param2_label.grid_remove()
        param2_entry.grid_remove()
    elif distribucion == "Uniforme":
        param1_label.config(text="A:")
        param2_label.config(text="B:")
        param2_label.grid()
        param2_entry.grid()
    elif distribucion == "Normal":
        param1_label.config(text="Media:")
        param2_label.config(text="Desv. estándar:")
        param2_label.grid()
        param2_entry.grid()

# Crear la interfaz gráfica
root = tk.Tk()
root.geometry("800x600")
root.title("Generador de numeros aleatorios")

# Tamaño de muestra
tk.Label(root, text="Tamaño de la muestra (1-1.000.000):").grid(row=0, column=0, sticky="w")
sample_size_entry = tk.Entry(root)
sample_size_entry.grid(row=0, column=1)

# Selección de distribución
tk.Label(root, text="Distribución:").grid(row=1, column=0, sticky="w")
distribution_combobox = ttk.Combobox(root, values=["Uniforme", "Exponencial", "Normal"])
distribution_combobox.grid(row=1, column=1)

# Parámetros de la distribución
param1_label = tk.Label(root, text="Parametro 1:")
param1_label.grid(row=2, column=0, sticky="w")
param1_entry = tk.Entry(root)
param1_entry.grid(row=2, column=1)

param2_label = tk.Label(root, text="Parametro 2 (si aplica):")
param2_label.grid(row=3, column=0, sticky="w")
param2_entry = tk.Entry(root)
param2_entry.grid(row=3, column=1)

# Número de intervalos
tk.Label(root, text="Intervalos (10, 15, 20, 25):").grid(row=4, column=0, sticky="w")
intervals_combobox = ttk.Combobox(root, values=[10, 15, 20, 25])
intervals_combobox.grid(row=4, column=1)
intervals_combobox.set(10)

# Botón para generar
generate_button = tk.Button(root, text="Generar y analizar", command=generar_y_analizar)
generate_button.grid(row=5, column=0, columnspan=2)

distribution_combobox.bind("<<ComboboxSelected>>", on_distribution_change)

root.mainloop()