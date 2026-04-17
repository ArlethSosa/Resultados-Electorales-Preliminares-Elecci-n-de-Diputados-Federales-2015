# Aldo Martínez Hernández y Arleth Magali Sosa García (INA)
# Descripción: Proyecto Final de Analítica de Datos, que lee una base de datos y regresa datos estadisticos, reportes y gráficas.

import csv
import matplotlib.pyplot as plot


def calcular_votos_anulados():
    '''La función calcula el total de votos anulados'''
    archivo = open("diputados.csv")
    entrada = csv.reader(archivo)
    diputados = list(entrada)[6:]
    anulados = []
    for renglon in diputados:
        if renglon[28] != " " and renglon[28] != "Sin dato" and renglon[28] != "Ilegible":
            anulados.append(int(renglon[28]))
            
    total_anulados = sum(anulados)
    
    return total_anulados

def calcular_votos_pais():
    '''La función calcula el total de votos del país'''
    archivo = open("diputados.csv")
    entrada = csv.reader(archivo)
    diputados = list(entrada)[6:]
    votos = []
    for renglon in diputados:
        if renglon[29] != " ":
            votos.append(int(renglon[29]))
            
    total_votos = sum(votos)
    
    return total_votos
        
        
def calcular_porcentaje_participacion_pais():
    '''La función calcula el porcentaje de participación electoral de todo el país'''
    archivo = open("diputados.csv")
    entrada = csv.reader(archivo)
    diputados = list(entrada)[6:]
    lista_nominal = []
    lista_votos = []
    for renglon in diputados:
        if renglon[29] != " ":
            lista_votos.append(int(renglon[29]))
            
        if renglon[30] != " ":
            lista_nominal.append(int(renglon[30]))
    
    porcentaje_participacion_pais = (sum(lista_votos)/sum(lista_nominal))*100
    
    return porcentaje_participacion_pais
            
            
def calcular_porcentaje_participacion(estado):
    '''La función calcula el porcentaje de participación electoral de un estado en específico'''
    archivo = open("diputados.csv")
    entrada = csv.reader(archivo)
    diputados = list(entrada)[6:]
    votos_estado = []
    lista_nominal = []
    for renglon in diputados:
        if renglon[1] == estado and renglon[29] != " ":
            votos_estado.append(int(renglon[29]))
            
        if renglon[1] == estado and renglon[30] != " ":
            lista_nominal.append(int(renglon[30]))
               
    if sum(lista_nominal) == 0:
        return 0
    
      
    porcentaje_participacion_ciudadana = (sum(votos_estado)/sum(lista_nominal))*100
    
    return porcentaje_participacion_ciudadana

def asignar_nombre_partido(partido):
    '''La función calcula el total de votos del partido que se ingrese'''
    votos_partidos = calcular_votos_partido()
    nombres_partido = ["PAN", "PRI", "PRD", "PVEM", "PT", "Mov.Ciudadano", "Nueva Alianza", "Morena", "Partido Humanista", "Encuentro Social"]
    for nombre in nombres_partido:
        if partido == nombre:
            indice = nombres_partido.index(nombre)
            
    votos = 0       
    for dato in votos_partidos:
        if indice == votos_partidos.index(dato):
            votos += dato
                                    
    return votos
        
    
          
def calcular_votos_partido():
    '''La función calcula el total de votos de todos los partidos'''
    archivo = open("diputados.csv")
    entrada = csv.reader(archivo)
    diputados = list(entrada)[6:]
    PAN = 0
    PRI = 0
    PRD = 0
    PVEM = 0
    PT = 0
    Movimiento_Ciudadano = 0
    Nueva_Alianza = 0
    Morena = 0
    Partido_Humanista = 0
    Encuentro_Social = 0
    for renglon in diputados:
        if renglon[13] != " " and renglon[13] != "Ilegible" and renglon[13] != "Sin dato":
            PAN += int(renglon[13])
                
        if renglon[14] != " " and renglon[14] != "Ilegible" and renglon[14] != "Sin dato":
            PRI += int(renglon[14])
                
        
        if renglon[15] != " " and renglon[15] != "Ilegible" and renglon[15] != "Sin dato":
            PRD += int(renglon[15])
    
        
        if renglon[16] != " " and renglon[16] != "Ilegible" and renglon[16] != "Sin dato":
            PVEM += int(renglon[16])
    
        
        if renglon[17] != " " and renglon[17] != "Ilegible" and renglon[17] != "Sin dato":
            PT += int(renglon[17])
    
        
        if renglon[18] != " " and renglon[18] != "Ilegible" and renglon[18] != "Sin dato":
            Movimiento_Ciudadano += int(renglon[18])
    
        
        if renglon[19] != " " and renglon[19] != "Ilegible" and renglon[19] != "Sin dato":
            Nueva_Alianza += int(renglon[19])
    
        
        if renglon[20] != " " and renglon[20] != "Ilegible" and renglon[20] != "Sin dato":
            Morena += int(renglon[20])
                
        
        if renglon[21] != " " and renglon[21] != "Ilegible" and renglon[21] != "Sin dato":
            Partido_Humanista += int(renglon[21])
                
        
        if renglon[22] != " " and renglon[22] != "Ilegible" and renglon[22] != "Sin dato":
            Encuentro_Social += int(renglon[22])
                
    votos_partidos = [PAN, PRI, PRD, PVEM, PT, Movimiento_Ciudadano, Nueva_Alianza, Morena, Partido_Humanista, Encuentro_Social]
    
    return votos_partidos 
        

def calcular_votos_estado(estado):
    '''La función calcula el total de votos de un estado en específico'''
    archivo = open("diputados.csv")
    entrada = csv.reader(archivo)
    diputados = list(entrada)[6:]
    votos_estados = []
    for renglon in diputados:
        if renglon[1] == estado and renglon[29] != " ":
            votos_estados.append(int(renglon[29]))
            
    
    suma_votos = sum(votos_estados)
            
    return suma_votos


def calcular_votos_partido_estado(partido, estado):
    '''La función calcula el total de votos de un partido en un estado en específico'''
    partido = int(partido)
    archivo = open("diputados.csv")
    entrada = csv.reader(archivo)
    diputados = list(entrada)[6:]
    votos_partido = []
    for renglon in diputados:
        if partido == 0:
            if renglon[1] == estado and renglon[13] != " " and renglon[13] != "Ilegible" and renglon[13] != "Sin dato":
                votos_partido.append(int(renglon[13]))
                
        elif partido == 1:
            if renglon[1] == estado and renglon[14] != " " and renglon[14] != "Ilegible" and renglon[14] != "Sin dato":
                votos_partido.append(int(renglon[14]))
        elif partido == 2:
            if renglon[1] == estado and renglon[15] != " " and renglon[15] != "Ilegible" and renglon[15] != "Sin dato":
                votos_partido.append(int(renglon[15]))
    
        elif partido == 3:
            if renglon[1] == estado and renglon[16] != " " and renglon[16] != "Ilegible" and renglon[16] != "Sin dato":
                votos_partido.append(int(renglon[16]))
    
        elif partido == 4:
            if renglon[1] == estado and renglon[17] != " " and renglon[17] != "Ilegible" and renglon[17] != "Sin dato":
                votos_partido.append(int(renglon[17]))
    
        elif partido == 5:
            if renglon[1] == estado and renglon[18] != " " and renglon[18] != "Ilegible" and renglon[18] != "Sin dato":
                votos_partido.append(int(renglon[18]))
    
        elif partido == 6:
            if renglon[1] == estado and renglon[19] != " " and renglon[19] != "Ilegible" and renglon[19] != "Sin dato":
                votos_partido.append(int(renglon[19]))
    
        elif partido == 7:
            if renglon[1] == estado and renglon[20] != " " and renglon[20] != "Ilegible" and renglon[20] != "Sin dato":
                votos_partido.append(int(renglon[20]))
                
        elif partido == 8:
            if renglon[1] == estado and renglon[21] != " " and renglon[21] != "Ilegible" and renglon[21] != "Sin dato":
                votos_partido.append(int(renglon[21]))
                
        elif partido == 9:
            if renglon[1] == estado and renglon[22] != " " and renglon[22] != "Ilegible" and renglon[22] != "Sin dato":
                votos_partido.append(int(renglon[22]))
        
    suma_votos = sum(votos_partido)
      
    return suma_votos


def graficar_graficas_default(opcion):
    '''La función realiza la gráfica dependiendo de la opción que se ingrese'''
    archivo = open("diputados.csv")
    entrada = csv.reader(archivo)
    diputados = list(entrada)[6:]           
    nombres_partido = ["PAN", "PRI", "PRD", "PVEM", "PT", "Mov.Ciudadano", "Nueva Alianza", "Morena", "Partido Humanista", "Encuentro Social"]
    partidos = calcular_votos_partido()
    if opcion == 0:
        estados = []
        for renglon in diputados:
            estados.append(renglon[1])
        
        nombres_estados = list(set(estados))
        suma_votos_estados = []
        for indice in nombres_estados:
            suma_votos_estados.append(calcular_votos_estado(indice))
    
        grafica_barras_votos = plot.bar(nombres_estados, suma_votos_estados)
        plot.title("Total de Votos por Estado")
        plot.ylabel("Votos")
        plot.xticks(rotation=90)
        plot.grid()
        plot.show()
        
    elif opcion == 1:
        grafica_barras = plot.bar(nombres_partido, partidos)
        plot.title("Total de votos en el país por partido")
        plot.ylabel("Votos")
        plot.xticks(rotation=90)
        plot.grid()
        grafica_barras[1].set_color("darkgreen")
        grafica_barras[2].set_color("y")
        grafica_barras[3].set_color("lightgreen")
        grafica_barras[4].set_color("r")
        grafica_barras[5].set_color("orange")
        grafica_barras[6].set_color("c")
        grafica_barras[7].set_color("brown")
        grafica_barras[8].set_color("m")
        grafica_barras[9].set_color("violet")
        plot.show()
          
    elif opcion == 2:
        lista_porcentaje = []
        for partido in partidos:
            porcentaje = (partido/sum(partidos))*100
            lista_porcentaje.append(porcentaje)
        
        angulos = -180*lista_porcentaje[0]
        plot.pie(lista_porcentaje, autopct = "%.1f%%", labels = nombres_partido, startangle = angulos)
        plot.title("Porcentaje de votos por partido")
        plot.show()
           
    elif opcion == 3:
        lista_nominal = []
        lista_votos = []
        for renglon in diputados:
            if renglon[29] != " ":
                lista_votos.append(int(renglon[29]))
            
            if renglon[30] != " ":
                lista_nominal.append(int(renglon[30]))
            
        votos_esperados = sum(lista_nominal)
        votos_reales = sum(lista_votos)
        ejex = [votos_esperados, votos_reales]
        nombres_ejex = ["Votos esperados", "Votos reales"]
        grafica_participacion = plot.bar(nombres_ejex, ejex)
        plot.title("Participación Ciudadana")
        plot.ylabel("Votos")
        plot.grid()
        grafica_participacion[0].set_color("r")
        grafica_participacion[1].set_color("g")
        plot.show()
           
    elif opcion == 4:
        lista_nominal = []
        lista_votos = []
        lista_porcentajes = []
        for renglon in diputados:
            if renglon[29] != " ":
                lista_votos.append(int(renglon[29]))
            
            if renglon[30] != " ":
                lista_nominal.append(int(renglon[30]))
        
        lista_porcentajes.append(((sum(lista_nominal) - sum(lista_votos))/sum(lista_nominal))*100)
        lista_porcentajes.append((sum(lista_nominal)/sum(lista_nominal))*100)
        etiquetas = ["Votos Reales", "Votos esperados"]
        angulos = -180*lista_porcentajes[0]
        plot.pie(lista_porcentajes, autopct = "%.1f%%", labels = etiquetas, startangle = angulos)
        plot.title("Porcentaje de participación ciudadana")
        plot.show()
    
    
def main():
    print('''Bienvenido a la base de datos del conteo electoral de votos para el cargo de diputado.
Elecciones realizadas en junio del 2015 - Toma de posesión:  1 diciembre del 2015 - 2018\n''')
    
    respuesta = input('''¿Que desea saber?
Eliga una de las siguientes opciones de la base de datos:\n
Estadisticas = 1
Reportes = 2
Gráficas = 3
Salir = 0\n
[ATENCIÓN, DEBE INGRESAR UN NÚMERO DE LOS MENCIONADOS ANTERIORMENTE SIN CARACTÉRES ESPECIALES O FLOTANTES]\n''')
    
    while respuesta.isdecimal() != True or int(respuesta) >= 4 or int(respuesta) < 0:
        print("Error, debe ingresar un número entero sin caracteres especiales\n")
        respuesta = input('''¿Que desea saber?
Eliga una de las siguientes opciones de la base de datos:\n
Estadisticas = 1
Reportes = 2
Gráficas = 3
Salir = 0\n
[ATENCIÓN, DEBE INGRESAR UN NÚMERO DE LOS MENCIONADOS ANTERIORMENTE SIN CARACTÉRES ESPECIALES O FLOTANTES]\n''')
    respuesta = int(respuesta)          
    while respuesta != 0:
        if respuesta == 1:
            print("Has elegido Estadisticas\n")
            print("El partido con mayor número de votos en el pais; es el PRI con", max(calcular_votos_partido()), "votos")
            print("El partido con menor número de votos en el pais; es el Partido Humanista con", min(calcular_votos_partido()), "votos")
            print("El porcentaje de participación ciudadana de todo el país es: %.4f"% (calcular_porcentaje_participacion_pais()),"%\n")
            opcion = input('''¿Quiere saber el porcentaje de la participación ciudadana de algún estado en específico?\n
Si = 1
No = 2\n''')
            if opcion.isdecimal() == True:
                opcion = int(opcion)
                if opcion < 3 and opcion > 0:
                    if opcion == 1:
                        estado = input("Ingresa el estado en mayúscula del cuál quieres saber el porcentaje de participación ej.[AGUASCALIENTES](NO OLVIDES LOS ACENTOS): ")
                        print()
                        porcentaje_participacion = calcular_porcentaje_participacion(estado)
                        if porcentaje_participacion == 0:
                            print("\nError, revisa la escritura del estado solicitado, debe ser en MAYÚSCULAS y con ACENTOS\n")
                            respuesta = 4
                                
                        else:
                            print("El porcentaje de participación ciudadana en", estado, "es: %.4f" % porcentaje_participacion,"%")
                            print("Si desea visualizar una gráfica de la participación ciudadana para comparar, ingrese al apartado de Gráficas en el menú principal\n")
                            respuesta = 4
                
                    elif opcion == 2:
                        respuesta = 4
                        
                else:
                    print("Error, debes ingresar un número de los listados anteriormente sin caracteres especiales o flotantes\n")
                    respuesta = 4                           
                                
            else:
                print("Error, debes ingresar un número de los listados anteriormente sin caracteres especiales o flotantes\n")
                respuesta = 4


        elif respuesta == 2:
            print("Has elegido Reportes\n")
            print("El total de votos del país es: ", calcular_votos_pais())
            print("El total de votos anulados en el país es: ", calcular_votos_anulados(),"\n")
            print("El total de votos del partido PAN es: ", asignar_nombre_partido("PAN"))
            print("El total de votos del partido PRI es: ", asignar_nombre_partido("PRI"))
            print("El total de votos del partido PRD es: ", asignar_nombre_partido("PRD"))
            print("El total de votos del partido PVEM es: ", asignar_nombre_partido("PVEM"))
            print("El total de votos del partido PT es: ", asignar_nombre_partido("PT"))
            print("El total de votos del partido Mov.Ciudadano es: ", asignar_nombre_partido("Mov.Ciudadano"))
            print("El total de votos del partido Nueva Alianza es: ", asignar_nombre_partido("Nueva Alianza"))
            print("El total de votos del partido Morena es: ", asignar_nombre_partido("Morena"))
            print("El total de votos del partido Partido Humanista es: ", asignar_nombre_partido("Partido Humanista"))
            print("El total de votos del partido Encuentro Social es: ", asignar_nombre_partido("Encuentro Social"),"\n")
            opcion = input("¿Quiere saber el total de votos de algún estado en específico?\n Si = 1\n No = 2\n")
            if opcion.isdecimal() == True:
                opcion = int(opcion)
                if opcion < 3 and opcion > 0:
                    if opcion == 1:
                        estado = input("Ingresa el estado en mayúscula del cuál quieres saber el total de votos ej.[AGUASCALIENTES](NO OLVIDES LOS ACENTOS): ")
                        total_votos = calcular_votos_estado(estado)
                        if total_votos == 0:
                            print("\nError, revisa la escritura del estado solicitado, debe ser en MAYÚSCULAS y con ACENTOS\n")
                            
                        else:
                            print("El total de votos de", estado, "es: ",total_votos)
                            print()
                            
                    elif opcion == 2:
                        respuesta = 4
                    
                else:
                    print("Error, debes ingresar un número de los listados anteriormente sin caracteres especiales o flotantes\n")
                    respuesta = 4
            else:
                print("Error, debes ingresar un número de los listados anteriormente sin caracteres especiales o flotantes\n")
                repsuesta = 4
                
            opcion = input("\n¿Quiere saber el total de votos en un estado; de algún partido en específico?\n Si = 1\n No = 2\n")
            if opcion.isdecimal() == True:
                opcion = int(opcion)
                if opcion < 3 and opcion > 0:
                    if opcion == 1:
                        estado = input("Ingresa el estado en mayúsculas a evaluar el total de votos del partido, ej.[AGUASCALIENTES](NO OLVIDES LOS ACENTOS): ")
                        print("\n¿De que partido quieres saber el total de votos?")
                        partido = input('''Ingresa el número de acuerdo al partido del que quieres saber el número de votos:\n
PAN = 0
PRI = 1
PRD = 2
PVEM = 3
PT = 4
Movimiento Ciudadano = 5
Nueva Alianza = 6
Morena = 7
Partido Humanista = 8
Encuentro Social = 9\n''')
                        if partido.isdecimal() == True:
                            if int(partido) == 0:
                                nombre_partido = "PAN"
                            elif int(partido) == 1:
                                nombre_partido = "PRI"
        
                            elif int(partido) == 2:
                                nombre_partido = "PRD"
           
                            elif int(partido) == 3:
                                nombre_partido = "PVEM"
    
                            elif int(partido) == 4:
                                nombre_partido = "PT"
    
                            elif int(partido) == 5:
                                nombre_partido = "Movimiento Ciudadano"
        
                            elif int(partido) == 6:
                                nombre_partido = "Nueva Alianza"
    
                            elif int(partido) == 7:
                                nombre_partido = "Morena"
                
                            elif int(partido) == 8:
                                nombre_partido = "Partido Humanista"
                
                            elif int(partido) == 9:
                                nombre_partido = "Encuentro Social"
            
                            votos_partido = calcular_votos_partido_estado(partido,estado)
                            if votos_partido == 0:
                                print("\nError, debes ingresar un número entero adjudicado a los partidos anteriores\n")
                                respuesta = 4
                            
            
                            else:
                                print()
                                print("El total de votos del partido:", nombre_partido,":", "en el estado de", estado, "es:", votos_partido,"\n")
                                respuesta = 4
    
                        else:
                            print()
                            print("Error, debes ingresar un número entero señalado a la par de cada partido\n")
                            respuesta = 4
                            
                    elif opcion == 2:
                        respuesta = 4
                        
                else:
                    print("Error, debes ingresar un número de los listados anteriormente sin caracteres especiales o flotantes\n")
                    respuesta = 4
                    
            else:
                print("Error, debes ingresar un número de los listados anteriormente sin caracteres especiales o flotantes\n")
                respuesta = 4
                                    
            
        elif respuesta == 3:
            print("Has elegido Gráficas\n")
            opcion = input('''¿Que gráfica desea ver?
Total de votos por estado (Barras) = 0
Total de votos por partido (Barras) = 1
Porcentaje de votos por partido (Pastel) = 2
Participación ciudadana del país (Barras) = 3
Porcentaje de Participación ciudadana del país (Pastel) = 4\n''')
            if opcion.isdecimal() == True:
                opcion = int(opcion)
                if opcion < 5 and opcion > -1:
                    if opcion == 0:
                        print("Se está calculando su resultado, el proceso puede tardar de 30 a 45 segundos. Disculpe las molestias, por favor espere.\nPara una mejor visualización de las gráficas: expanda la figura de gráficas a pantalla completa.\n Para salir al menú principal cierre la ventana de graficas.")
                        graficar_graficas_default(opcion)
                        respuesta = 4
                        
                    elif opcion == 1:
                        print("Para una mejor visualización de las gráficas: expanda la figura de gráficas a pantalla completa.\n Para salir al menú principal cierre la ventana de graficas.")
                        graficar_graficas_default(opcion)
                        respuesta = 4
                    
                    elif opcion == 2:
                        print("Para una mejor visualización de las gráficas: expanda la figura de gráficas a pantalla completa.\n Para salir al menú principal cierre la ventana de graficas.")
                        graficar_graficas_default(opcion)
                        respuesta = 4
                    
                    elif opcion == 3:
                        print("Para una mejor visualización de las gráficas: expanda la figura de gráficas a pantalla completa.\n Para salir al menú principal cierre la ventana de graficas.")
                        graficar_graficas_default(opcion)
                        respuesta = 4
                     
                    elif opcion == 4:
                        print("Para una mejor visualización de las gráficas: expanda la figura de gráficas a pantalla completa.\n Para salir al menú principal cierre la ventana de graficas.")
                        graficar_graficas_default(opcion)
                        respuesta = 4
                        
                else:
                    print("Error, debe ingresar un número de los listados anteriormente sin caracteres especiales o flotantes")
                    respuesta = 4
                    
            else:
                print("Error, debe ingresar un número de los listados anteriormente sin caracteres especiales o flotantes")
                respuesta = 4
                          
                                      
        elif respuesta == 4:
            respuesta = input('''\nHa vuelto al menú principal, ¿Que desea saber?
Estadisticas = 1
Reportes = 2
Gráficas = 3
Salir = 0\n''')
            if respuesta.isdecimal() == True:
                respuesta = int(respuesta)
                if respuesta < 5 and respuesta > -1:
                    respuesta = int(respuesta)
                    
                else:
                    print("Error, debes ingresar un número de los listados anteriormente sin caracteres especiales o flotantes\n")
                    respuesta = 4
                        
            else:
                print("Error, debes ingresar un número de los listados anteriormente sin caracteres especiales o flotantes\n")
                respuesta = 4
                
                 
        else:
            print("Error, debes ingresar un número de los listados anteriormente sin caracteres especiales o flotantes\n")
            respuesta = 4
                
    
        
        
        
    print("\nGracias por haber ingresado a la base de datos del conteo electoral. Que tenga un buen día :)")
        
#######################################################################################################################    
          
        
main()