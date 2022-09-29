from stdiomask import getpass
import hashlib
import os

clear = lambda: os.system('cls')
import math
from datetime import datetime
aceleracion = 0 # Definimos la aceleracion inicial
pi = math.pi # Importamos pi de la libreria Math
latitud1 = 0
longitud1 = 0
def Distancia(lat1, log1, lat2, log2):
    # Radio de la tierra en kilometros
    radio = 6371
    # Convertimos las cordenadas en radianes
    lat = (lat2 - lat1) * (math.pi / 180)
    log = (log2 - log1) * (math.pi / 180)
    # Punto 1
    a = (math.sin(lat / 2) * math.sin(lat / 2)) + (math.cos(lat1 * (math.pi / 180)) * (math.cos(lat2 * (math.pi / 180)))) * (math.sin(log / 2) * math.sin(log / 2))
    # Punto 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Distancia total
    d = radio*c
    return d
def main():
    clear()
    print("Menu principal")
    print("---------")
    print()
    print("1 - Registrarse")
    print("2 - Ingresar")
    print()
    while True:
        print()
        userChoice = input("Selecciona una opcion: ")
        if userChoice in ['1', '2']:
            break
    if userChoice == '1':
        Registrarse()
    else:
        Ingresar()

def Registrarse():
    clear()
    print("Registrar")
    print("--------")
    print()
    while True:
        userName = input("Ingresa tu nombre: ").title()
        if userName != '':
            break
    userName = sanitizeName(userName)
    if userAlreadyExist(userName): 
        displayUserAlreadyExistMessage()
    else:
        while True:
            userPassword = getpass("Ingresa tu contraseña:  ")
            if userPassword != '':
                break
        while True:
            confirmPassword = getpass("Confirma tu contraseña: ")
            if confirmPassword == userPassword:
                break
            else:
                print("Contraseñas no coinciden")
                print()
        if userAlreadyExist(userName, userPassword):
            while True:
                print()
                error = input("Tu ya estas regristrado.\n\nPresiona (T) Para intentarlo denuevo:\nPresiona (L) Para Ingresar: ").lower()
                if error == 't':
                    Registrarse()
                    break
                elif error == 'l':
                    Ingresar()
                    break
        addUserInfo([userName, hash_password(userPassword)])

        print()
        print("Registrado!")

def Ingresar():
    clear()
    print("Ingresar")
    print("-----")
    print()
    usersInfo = {}
    with open('userInfo.txt', 'r') as file:
        for line in file:
            line = line.split()
            usersInfo.update({line[0]: line[1]})

    while True:
        userName = input("Ingresa tu nombre: ").title()
        userName = sanitizeName(userName)
        if userName not in usersInfo:
            print("Tu no estas registrado")
            print()
        else:
            break
    while True:
        userPassword = getpass("Ingresa tu contraseña: ")
        if not check_password_hash(userPassword, usersInfo[userName]):
            print("Contraseña incoorrecta")
            print()
        else:
            break
    print()
    print("Has ingresado!")
    print("Bienvenido", userName)
    print() 
    clear()
    opc = input 
    print(datetime.now().strftime("Dia %d del %m del %Y %H:%M:%S"))
    opcion = ""
    encendido = False
    # Se le preguta si quiere comenzar una carrera
    carrera = input("Presione 1 para comenzar una carrera\nPresione 2 para salir\n")
    # Si escoje 1, se le da a escojer una opcion
    if carrera == "1":
                # Se genera un bucle para que el usuario pueda escojer alguna de las opciones hasta que desee salir
                while opcion != "8":
                    print("1. - Ingresar ubicación GPS Inicial, LATITUD")
                    print("2. - Ingresar ubicación GPS Inicial, LONGITUD")
                    print("3. - Encender el vehículo.")
                    print("4. - Acelerar vehículo")
                    print("5. - Descelerar vehículo")
                    print("6. - Apagar Vehículo")
                    print("7. - Girar Vehículo.")
                    print("8. - Finalizar carrera")
                    opcion = input()
                    # Si escoje 1, se le pide que ingrese la latitud
                    if opcion == "1":
                        latitud1 = float(input("Ingrese la latitud:\n"))
                        print("Latitud ingresada correctamente\n")
                    # Si escoje 2, se le pide que ingrese la longitud
                    elif opcion == "2":
                        longitud1 = float(input("Ingrese la longitud:\n"))
                        print("Longitud ingresada correctamente\n")
                    # Si escoje 3, se le informa que el vehiculo se encendio
                    elif opcion == "3":
                        print("Encendiendo vehículo...\n")
                        encendido = True
                    # Si escoje 4 y el auto esta encendido ( true ), se le informa que el vehiculo se acelero
                    elif opcion == "4" and encendido:
                        aceleracion += 10
                        print("Usted está viajando a", aceleracion, "Km/h\n")
                    # Si escoje 5 y el auto esta encendido ( true ), se le informa que el vehiculo se desacelero
                    elif opcion == "5" and encendido:
                        if aceleracion < 10:
                            print("Usted está detenido\n")
                        elif aceleracion >= 10:
                            if aceleracion == 10:
                                aceleracion = 0
                                print("Usted está detenido\n")
                            elif aceleracion > 10:
                                aceleracion -= 10
                                print("Usted está viajando a", aceleracion, "Km/h\n")
                    # Si escoje 6 y el auto esta encendido ( true ), se le informa que el vehiculo se apago
                    elif opcion == "6" and encendido:
                        print("Apagando vehículo...\n")
                        encendido = False
                    # Si escoje 7 y el auto esta encendido ( true ), se le informa que el vehiculo giro
                    elif opcion == "7" and encendido:
                        print("Girando vehículo...\n")
                    # Si escoje 8, se le informa que la carrera finalizo y tendra que ingresar la latitud y longitud del destino y le dira cuanto es el total a pagar
                    elif opcion == "8":
                        print("Finalizando carrera...\n")
                        latitud2 = float(input("Ingrese la latitud de destino:\n"))
                        longitud2 = float(input("Ingrese la longitud de destino:\n"))
                        distancia = Distancia(latitud1, longitud1, latitud2, longitud2)
                        print("Distancia recorrida:", round(distancia, 2), "Km")
                        print("Total a pagar por el viaje: $", round(distancia*(220*1.8))) # Como no nos indica investigue y segun meganoticias uber en 2018 cobraba 220 pesos por km recorrido, no encontre informacion actualizada pero por el precio de la gasolina en 2018 que estaba a 737 vs hoy que esta a 1310 multiplicare por 1.8 aprox ese valor
                    else:
                        print("Puede que el motor este apagado o no haya ingresado una opción válida\n")
    elif carrera == "2": # Si escoje 2, se le informa que se saldra del programa
                print("Saliendo del programa...")   
            
            

def addUserInfo(userInfo: list):
    with open('userInfo.txt', 'a') as file:
        for info in userInfo:
            file.write(info)
            file.write(' ')
        file.write('\n')

def userAlreadyExist(userName, userPassword=None):
    if userPassword == None:
        with open('userInfo.txt', 'r') as file:
            for line in file:
                line = line.split()
                if line[0] == userName:
                    return True
        return False
    else:
        userPassword = hash_password(userPassword)
        usersInfo = {}
        with open('userInfo.txt', 'r') as file:
            for line in file:
                line = line.split()
                if line[0] == userName and line[1] == userPassword:
                    usersInfo.update({line[0]: line[1]})
        if usersInfo == {}:
            return False
        return usersInfo[userName] == userPassword

def displayUserAlreadyExistMessage():
    while True:
        print()
        error = input("Tu ya estas registrado.\n\nPresiona (T) para intentarlo denuevo :\nPresiona (L) Para ingresar: ").lower()
        if error == 't':
            Registrarse()
            break
        elif error == 'l':
            Ingresar()
            break

def sanitizeName(userName):
    userName = userName.split()
    userName = '-'.join(userName)
    return userName

def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_password_hash(password, hash):
    return hash_password(password) == hash

main()
    # Se genera un bucle para que el usuario pueda escojer alguna de las opciones hasta que desee salir
