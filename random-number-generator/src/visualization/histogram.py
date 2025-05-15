def dibujar_histograma(datos, cant_intervalos):
    import matplotlib.pyplot as plt

    # Create histogram
    plt.figure(figsize=(10, 6))
    plt.hist(datos, bins=cant_intervalos, edgecolor='black', alpha=0.7)

    # Set titles and labels
    plt.title('Histograma de frecuencia')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')

    # Set x and y limits
    plt.xlim(min(datos), max(datos))
    plt.ylim(0, max(plt.hist(datos, bins=cant_intervalos)[0]) + 1)

    # Show grid
    plt.grid(axis='y', alpha=0.75)

    # Show the plot
    plt.show()