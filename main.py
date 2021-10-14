# Import a library of functions called 'pygame'
import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

#call main routine
largo= int(input('introduce el largo de la pantalla:'))
ancho= int(input('introduce el ancho de la pantalla:'))
size = (largo, ancho) # Define size of windows, en este caso hay que ponerlo entr () al añadir una variable int
colorfond_r = int(input('¿Qué nivel de rojo deseas?'))
colorfond_g = int(input('¿Qué nivel de verde deseas?'))
colorfond_b = int(input('¿Qué nivel de azul deseas?'))
bg_color = (colorfond_r, colorfond_g, colorfond_b)   #crear una variable con los tres tonos de color
titulo = input('Dime el nombre del titulo:') #declaramos la variable titulo para que nos pida por pantalla el nombre del juego
main2(size= size, titulo= titulo, colorfond= bg_color) #si ponemos = quiere decir que no importa el orden en el que introducimos
