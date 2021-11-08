"""
***Problema 2***
De la base data_schools sacar obtener el error estándar con Bootstrap de las variables de la base. Recordemos que tienen que simular N Muestras Boostrap con tamaño n. Luego, el otro ejercicio es que lo hagan con n-1.
"""

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

# Importamos la base data_schools
data = pd.read_excel('./data_schools.xlsx')

# Veamos los primeros datos de la tabla
print("Los primeros datos de la tabla:")
print(data.head())

# Veamos la correlación de la base
cor = spearmanr(data.LSAT, data.GPA)[0]
print("La correlación de la muestra es", cor)

def generaMuestra(tamanioBoot, tamanioMuestra):
    """Genera muestra de tamaño n de correlaciones de la muestra data"""
    muestra = list()
    for i in range(tamanioBoot):
        muestra_i = data.sample(n=tamanioMuestra, replace=True)
        muestra.append(spearmanr(muestra_i.LSAT, muestra_i.GPA)[0])
    return muestra

# Generamos la muestra de tamaño 3200
muestra = generaMuestra(3200, 15)

# Ahora veamos el error estándar de la muestra con Bootstrap
err_bootstrap = np.std(muestra)
print("El error estándar usando Bootstrap es:", err_bootstrap)

"""
    *Ahora pasemos con la segunda parte del ejercicio.*
"""

def generaJack(tamanioBoot, tamanioMuestra):
    """Genera muestra de tamaño n-1 de correlaciones de la muestra data"""
    muestra = list()
    for i in range(tamanioBoot):
        muestra_i = data.sample(n=tamanioMuestra, replace=True)
        remuestreo_i = muestra_i.sample(n=(tamanioMuestra-1), replace=True)
        muestra.append(spearmanr(remuestreo_i.LSAT, remuestreo_i.GPA)[0])
    return muestra

# Generamos muestra de tamaño 3200
muestra2 = generaJack(3200, 15)

# Ahora veamos el error estándar de esta muestra
err2_bootstrap = np.std(muestra2)
print("El error estándar con n-1 es:", err2_bootstrap)

# Ahora generemos ambas muestras del tamaño de la muestra original
muestra3 = generaMuestra(3200, len(data))
muestra4 = generaJack(3200, len(data))

err1 = np.std(muestra3)
err2 = np.std(muestra4)

print("Con", len(data), "usando bootstrap tenemos:", err1)
print("Con", len(data), "usando bootstrap n-1 tenemos:", err2)
