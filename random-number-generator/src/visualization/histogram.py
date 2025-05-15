def dibujar_histograma(datos, cant_intervalos):
    import matplotlib.pyplot as plt
    import numpy as np

    # Calcular los bins y el histograma
    counts, bin_edges, _ = plt.hist(datos, bins=cant_intervalos, edgecolor='black', alpha=0.7)

    # Set titles and labels
    plt.title('Histograma de frecuencia')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')

    # Set x and y limits
    plt.xlim(min(datos), max(datos))
    plt.ylim(0, max(counts) + 1)

    # Mostrar los límites de los intervalos en el eje x
    plt.xticks(bin_edges, [f"{edge:.2f}" for edge in bin_edges], rotation=45)

    # Show grid
    plt.grid(axis='y', alpha=0.75)

    # Show the plot
    plt.tight_layout()
    plt.show()