#Actividades  
#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.  
edad = int(input("¡Hola! Por favor, dime tu edad: "))
           
if edad > 18 :
    print("¡Perfecto! Ya eres mayor de edad.")   
#----------------------------------------------------------------------------------------------------------------------------------
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”.

nota = float(input("¿Qué nota te sacaste en el examen? "))

if nota >= 6 :
        print("¡Felicidades! Estás Aprobado.")
else:
    print("Ánimo, esta vez estás Desaprobado, ¡pero la próxima te irá mejor!")
#---------------------------------------------------------------------------------------------------------------------------------- 
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar.  
numero = int(input("Por favor, ingresa un número par: "))

if numero  % 2 == 0:
    print("¡Genial! Ha ingresado un número par.")
else:
    print("Ups, ese no es par. Por favor, intenta de nuevo con un número par.")
#---------------------------------------------------------------------------------------------------------------------------------- 
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece:  
#• Niño/a: menor de 12 años.  
#• Adolescente: mayor o igual que 12 años y menor que 18 años.  
#• Adulto/a joven: mayor o igual que 18 años y menor que 30 años.  
#• Adulto/a: mayor o igual que 30 años.  
edad = int(input("Dime tu edad y te diré tu categoría: "))

if edad < 0:
    print("Por favor, ingrese un número positivo")
elif edad < 12:
    print("Eres un Niño/a. ¡A disfrutar el juego!")
elif edad < 18:
    print("Estás en la etapa de Adolescente.")
elif edad < 30:
    print("Eres un Adulto/a joven. ¡Mucho potencial!")
else:
    print("Eres un Adulto/a. ¡Toda una vida de experiencias!")
#---------------------------------------------------------------------------------------------------------------------------------- 
#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
#Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos 
#que tiene un iterable tal como una lista o un string.  
contraseña = input("Crea una contraseña (debe tener entre 8 y 14 caracteres): ")

if 8 <= len(contraseña) <= 14:
    print("¡Excelente! Ha ingresado una contraseña correcta.")
else:
    print("¡Atención! Por favor, ingresa una contraseña que tenga entre 8 y 14 caracteres.")
#---------------------------------------------------------------------------------------------------------------------------------- 
#6) Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en 
#kilovatios (kWh) e indique la categoría del consumo según el siguiente criterio: 
#• Menor que 150 kWh: “Consumo bajo”. 
#• Entre 150 y 300 kWh (inclusive): “Consumo medio”. 
#• Mayor que 300 kWh: “Consumo alto”. 
#Además, si el consumo supera los 500 kWh, mostrar un mensaje adicional que diga: 
#“Considere medidas de ahorro energético”. 
#El programa debe imprimir por pantalla la categoría correspondiente. 
consumo = float(input("Ingrese su consumo mensual de energía eléctrica en kWh: "))

if consumo < 150:
    categoria = "Consumo bajo"
elif consumo >= 150 and consumo <= 300:
    categoria = "Consumo medio"
else:
    categoria = "Consumo alto"
print(f"Categoría: {categoria}")

if consumo > 500:
    print("Considere medidas de ahorro energético")
#---------------------------------------------------------------------------------------------------------------------------------- 
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla.  
texto = input(" ¡Hola! Ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"

if texto[-1] in vocales:
    texto += "!"
    print(texto)
else:
    print(texto)
#---------------------------------------------------------------------------------------------------------------------------------- 
#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee:  
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.  
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.  
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.  
#El programa debe transformar el nombre ingresado de acuerdo con la opción seleccionada por 
#el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas. 
print("¡Hola! Qué gusto saludarte. ✨")
nombre = input("Por favor, dime tu nombre para comenzar: ")
print(f"\n¡Mucho gusto, {nombre}! Ahora, elige cómo quieres que lo transforme:")
print("1 ➔ Todo en MAYÚSCULAS")
print("2 ➔ Todo en minúsculas")
print("3 ➔ Formato de Título (Muy elegante)")

opcion = input("\n¿Qué opción prefieres? (1, 2 o 3): ")

if opcion == "1":
    resultado = nombre.upper()
    mensaje = "¡Listo! Aquí tienes tu nombre con mucha fuerza:"
elif opcion == "2":
    resultado = nombre.lower()
    mensaje = "Perfecto, aquí lo tienes en una versión más sencilla:"
elif opcion == "3":
    resultado = nombre.title()
    mensaje = "¡Excelente elección! Se ve muy bien así:"
else:
    resultado = None
    mensaje = "Vaya, parece que esa opción no está en mi lista. ¡Inténtalo de nuevo! ❤️"

if resultado:
    print(f"\n{mensaje}")
    print(f"✨ {resultado} ✨")
else:
    print(f"\n{mensaje}")
#---------------------------------------------------------------------------------------------------------------------------------- 
#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla:  
#• Menor que 3: "Muy leve" (imperceptible).  
#• Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).  
#• Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños).  
#• Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles).  
#• Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).  
#• Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 
print("Hola. 🌍 Soy tu asistente de información sísmica.")
print("Espero que te encuentres bien. Por favor, dime la magnitud que deseas consultar.")

try:

    magnitud = float(input("\nIngresa la magnitud en la escala de Richter: "))

    if magnitud < 3:
        categoria = "Muy leve (imperceptible para la mayoría)"
    elif 3 <= magnitud < 4:
        categoria = "Leve (se siente un ligero movimiento)"
    elif 4 <= magnitud < 5:
        categoria = "Moderado (se siente claramente, pero rara vez causa daños)"
    elif 5 <= magnitud < 6:
        categoria = "Fuerte (podría causar daños en construcciones frágiles)"
    elif 6 <= magnitud < 7:
        categoria = "Muy Fuerte (¡Cuidado! Puede causar daños importantes)"
    else:
        categoria = "Extremo (alerta de daños graves a gran escala)"

    print("\n--- Resultado del Análisis ---")
    print(f"Magnitud: {magnitud}")
    print(f"Clasificación: {categoria}")
    print("------------------------------")
    print("¡Recuerda siempre mantener la calma y seguir los protocolos de seguridad! 🙏")

except ValueError:
    print("\nOops, parece que no ingresaste un número válido. Por favor, intenta de nuevo usando puntos para los decimales (ejemplo: 5.5).")
#---------------------------------------------------------------------------------------------------------------------------------- 
#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año :
print("¡Hola! 🌍 Vamos a descubrir en qué estación del año te encuentras.")

hemisferio = input("¿En qué hemisferio estás? (N para Norte / S para Sur): ").upper()

mes = int(input("¿En qué número de mes estamos? (1-12): "))
dia = int(input("¿Qué día del mes es hoy?: "))

# Creamos un valor numérico para la fecha (Mes * 100 + Día). Ejemplo: 21 de diciembre = 1221
fecha = mes * 100 + dia

if (fecha >= 1221) or (fecha <= 320):
    periodo = 1  # 21 dic al 20 mar
elif (fecha >= 321) and (fecha <= 620):
    periodo = 2  # 21 mar al 20 jun
elif (fecha >= 621) and (fecha <= 920):
    periodo = 3  # 21 jun al 20 sep
else:
    periodo = 4  # 21 sep al 20 dic
    
estacion = ""

if hemisferio == "N":
    if periodo == 1: estacion = "Invierno"
    elif periodo == 2: estacion = "Primavera"
    elif periodo == 3: estacion = "Verano"
    else: estacion = "Otoño"
elif hemisferio == "S":
    if periodo == 1: estacion = "Verano"
    elif periodo == 2: estacion = "Otoño"
    elif periodo == 3: estacion = "Invierno"
    else: estacion = "Primavera"
else:
    estacion = "desconocida (por favor, verifica si escribiste N o S)"

if estacion != "desconocida":
    print(f"\n✨ Según tus datos, ¡te encuentras en **{estacion}**! Que disfrutes mucho de este clima. 🌤️")
else:
    print(f"\nUps, parece que hubo un error: {estacion}.")