# ============================================================
# Actividad Formativa 3
# Implementación y evaluación de filtros digitales
# Autor: Jesús Carrizales Guerra
# ============================================================

# Importación de librerías
#NumPy permite crear y manipular señales digitales.
#Matplotlib genera las gráficas.
#SciPy Signal proporciona funciones para diseñar y aplicar filtros digitales.
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ============================================================
# Creación de la señal de prueba

# Frecuencia de muestreo (Hz)
fs = 1000
# Tiempo de 0 a 1 segundo
t = np.linspace(0, 1, fs, endpoint=False)
# Señal compuesta por dos frecuencias
senal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)
# ============================================================
# Agregar ruido blanco
ruido = 0.3 * np.random.randn(len(t))
senal_ruido = senal + ruido
# ============================================================
# Gráfica de la señal con ruido
plt.figure(figsize=(10,5))
plt.plot(t, senal, label='Señal original')
plt.plot(t, senal_ruido, label='Señal con ruido', alpha=0.7)
plt.title('Señal original y señal con ruido')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()

plt.show()
# ============================================================
# Filtro Pasa Bajos (Butterworth)
# ============================================================

# Frecuencia de corte (Hz)
fc = 10

# Diseño del filtro Butterworth de orden 4
b, a = signal.butter(4, fc/(fs/2), btype='low')
# Aplicar el filtro
senal_pasabajos = signal.filtfilt(b, a, senal_ruido)
# ============================================================
# Gráfica del filtro pasa bajos
# ============================================================
plt.figure(figsize=(10,5))

plt.plot(t, senal_ruido, label='Señal con ruido', alpha=0.6)
plt.plot(t, senal_pasabajos, label='Señal filtrada', linewidth=2)

plt.title('Filtro Pasa Bajos Butterworth')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()

plt.show()

# ============================================================
# Filtro Pasa Altos (Butterworth)
# ============================================================
# Frecuencia de corte
fc_alto = 15

# Diseño del filtro pasa altos
b_alto, a_alto = signal.butter(4, fc_alto/(fs/2), btype='high')

# Aplicación del filtro
senal_pasaaltos = signal.filtfilt(b_alto, a_alto, senal_ruido)
# ============================================================
# Gráfica del filtro pasa altos
# ============================================================
plt.figure(figsize=(10,5))

plt.plot(t, senal_ruido, label='Señal con ruido', alpha=0.6)
plt.plot(t, senal_pasaaltos, label='Señal filtrada')

plt.title('Filtro Pasa Altos Butterworth')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

plt.legend()
plt.grid()
plt.show()

# ============================================================
# Filtro Pasa Bandas (Butterworth)
# ============================================================

# Frecuencias límite
baja = 10
alta = 25

# Diseño del filtro pasa bandas
b_banda, a_banda = signal.butter(
    4,
    [baja/(fs/2), alta/(fs/2)],
    btype='band'
)

# Aplicación del filtro
senal_pasbanda = signal.filtfilt(
    b_banda,
    a_banda,
    senal_ruido
)

# ============================================================
# Gráfica del filtro pasa bandas
# ============================================================

plt.figure(figsize=(10,5))

plt.plot(t, senal_ruido, label='Señal con ruido', alpha=0.6)
plt.plot(t, senal_pasbanda, label='Señal filtrada')

plt.title('Filtro Pasa Bandas Butterworth')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

plt.legend()
plt.grid()

plt.show()

# ============================================================
# Respuesta en frecuencia del filtro pasa bajos
# ============================================================

w, h = signal.freqz(b, a, worN=8000)

plt.figure(figsize=(10,5))

plt.plot(
    (w/np.pi)*(fs/2),
    abs(h)
)

plt.title('Respuesta en frecuencia del filtro pasa bajos')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Ganancia')

plt.grid()

plt.show()