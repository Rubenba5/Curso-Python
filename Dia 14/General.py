# Librerias / Bibliotecas.
import cv2
import face_recognition as fr
from pathlib import Path


# Ruta de Archivos.
ruta = Path(Path.home(), "Proyectos", "Recursos_14")


# Cargar Imagenes.
foto_control = fr.load_image_file(Path(ruta, "FotoA.png")) # Foto A.
foto_prueba = fr.load_image_file(Path(ruta, "FotoB.png")) # Foto B.


# Localizar la cara de foto control.
lugar_cara_control = fr.face_locations(foto_control)[0]
cara_codificada_control = fr.face_encodings(foto_control)[0]


# Mostrar rectangulo del lugar de la cara de foto control.
cv2.rectangle(foto_control, # Foto donde se monstrara el rectangulo.
              (lugar_cara_control[3], lugar_cara_control[0]), # Valores de X e Y del vertice superior izquierdo.
              (lugar_cara_control[1], lugar_cara_control[2]), # Valores de X e Y del vertice inferior derecho.
              (0, 255, 0), # Color del rectangulo (RGB).
              2) # Grosor del borde del rectrangulo.


# Localizar la cara de foto prueba
lugar_cara_prueba = fr.face_locations(foto_prueba)[0] # Indice 0.
cara_codificada_prueba = fr.face_encodings(foto_prueba)[0] # Indice 0.


# Mostrar rectangulo del lugar de la cara de foto prueba.
cv2.rectangle(foto_prueba, # Foto donde se monstrara el rectangulo.
              (lugar_cara_prueba[3], lugar_cara_prueba[0]), # Valores de X e Y del vertice superior izquierdo.
              (lugar_cara_prueba[1], lugar_cara_prueba[2]), # Valores de X e Y del vertice inferior derecho.
              (0, 255, 0), # Color del rectangulo (RGB).
              2) # Grosor del borde del rectrangulo.


# Pasar imagenes de sistema BGR a RGB.
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)


# Realizar comparación entre las caras de foto control y foto prueba.
# Si la distancia entre las caras es menor a 0,6 hay coincidencia. Esta tolerancia es modificable.
resultado = fr.compare_faces([cara_codificada_control], cara_codificada_prueba) # Compara una lista de fotos codificadas con otra foto codificada.

if resultado[0]:
    resultado = "Si son iguales"

elif not resultado[0]:
    resultado = "No son iguales"


# Medida de la distancia entre las caras de las fotos.
distancia = fr.face_distance([cara_codificada_control], cara_codificada_prueba) # Compara una lista de una foto codificada con otra foto codificada.


# Mostrar resultados en las fotos
cv2.putText(foto_control, # Donde se va a mostrar
            f"{resultado} | {distancia.round(2)}", # Texto
            (125, 50), # Localización
            cv2.FONT_HERSHEY_COMPLEX, # Tipo de letra
            1, # Escala de letra
            (255,255,255), # Color (RGB)
            2) # Grosor de letra


# Mostrar imagenes en pantalla.
cv2.imshow("Foto Control", foto_control) # Nombre a monstar, Foto a monstrar.
cv2.imshow("Foto Prueba", foto_prueba) # Nombre a monstar, Foto a monstrar.


# Mantener el programa ejecutandose.
cv2.waitKey(0) # Cerrar el Programa, pulsando la telca "0".


