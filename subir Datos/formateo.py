import pyperclip
import re
import time

# Función para formatear el texto
def formatear_texto(texto):
    # Eliminar espacios en blanco múltiples y reemplazarlos por un espacio
    texto_formateado = re.sub(r'\s+', ' ', texto)
    return texto_formateado

# Función para copiar el texto formateado al portapapeles
def copiar_al_portapapeles(texto):
    pyperclip.copy(texto)

# Variable para almacenar el contenido del portapapeles
contenido_anterior = ""

while True:
    # Obtener el contenido actual del portapapeles
    contenido_actual = pyperclip.paste()

    # Verificar si el contenido ha cambiado desde la última vez
    if contenido_actual != contenido_anterior:
        # Formatear el contenido
        contenido_formateado = formatear_texto(contenido_actual)

        # Copiar el contenido formateado de nuevo al portapapeles
        copiar_al_portapapeles(contenido_formateado)

        print("Texto formateado y copiado al portapapeles:")
        print(contenido_formateado)

        # Actualizar el contenido anterior
        contenido_anterior = contenido_actual

    # Esperar un corto período antes de verificar nuevamente
    time.sleep(1)
