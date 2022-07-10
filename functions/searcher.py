#!/bin/python3.7
import os

def init_program(busqueda):
    busqueda = busqueda.replace(' ','+')
    busquedas = busqueda.split(',')
    for a in busquedas:
        os.system('xdg-open "https://duckduckgo.com/?t=ffab&q='+a+'&ia=web"')
        os.system('xdg-open "https://www.google.com/search?client=firefox-b-d&q='+a+'"')

nombre = input("Busqueda >> ")
init_program(nombre)