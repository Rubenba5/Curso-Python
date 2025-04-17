#Texto
Texto = input("Añade un texto:")
Texto_Minusculas = Texto.lower()

#Letras
Letras = []
Letras.append(input("Dime la primera letra:").lower())
Letras.append(input("Dime la segunda letra:").lower())
Letras.append(input("Dime la tercera letra:").lower())
Cantidad_palabras1 = Texto_Minusculas.count(Letras[0])
Cantidad_palabras2 = Texto_Minusculas.count(Letras[1])
Cantidad_palabras3 = Texto_Minusculas.count(Letras[2])
Letras_Total = (Cantidad_palabras1+Cantidad_palabras2+Cantidad_palabras3)

#Contar palabras
Palabras = Texto.split()
Contar = len(Palabras)

#Primera y ultima letra
Primera_Letra = Texto[0]
Ultima_Letra = Texto[-1]

#Palabras en orden inverso
Palabras.reverse()
Texto_Inveritido = " ".join(Palabras)


#Aparicion de la palabra python
Python = bool("python" in Texto_Minusculas)
Expresar = ""

if (Python == True):
    Expresar = "aparece"

else:
    Expresar = "no aparece"

#Final
print(" ")
print("Este texto contiene:")
print(f"-Aparecen {Contar} palabra en este texto.")
print(f"-Las letras {Letras[0]}, {Letras[1]}, {Letras[2]} añadidas aparecen {Letras_Total} veces.")
print(f"-La primera letra y la ultima son: {Primera_Letra} y {Ultima_Letra}.")
print(f"-El texto al reves sería asi: {Texto_Inveritido}.")
print(f'-La palabra "python" {Expresar} en el texto.')

