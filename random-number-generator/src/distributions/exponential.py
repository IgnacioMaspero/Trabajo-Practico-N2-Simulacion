import numpy as np

def generar_exponencial(_lambda, tamano):
    return np.random.exponential(1 / _lambda, tamano)