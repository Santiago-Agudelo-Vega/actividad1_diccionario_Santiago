# Creación de un diccionario vacío
mi_diccionario = {}
import os
sw = True

def fnt_agregar(diccionario, id_persona, nombre, edad, ciudad):
    if id_persona == '' or nombre == '' or edad == '' or ciudad == '':
        enter = input('Debe diligenciar toda la información solicitada <ENTER>')
    else:
        diccionario[id_persona] = {'nombre': nombre, 'edad': edad, 'ciudad': ciudad}
        enter = input(f'\nLa persona {nombre} ha sido registrada con éxito <ENTER>')

def fnt_selector(op):
    if op == '1':
        os.system('cls')
        nombre = input('Nombre:  ')
        edad = input('Edad:  ')
        ciudad = input('Ciudad:  ')
        id = input('Id: ')
        fnt_agregar(mi_diccionario, id, nombre, edad, ciudad)
        
while sw == True:
    os.system('cls')
    opcion = input('1. Registrar\n2. Mostrar\n3. Salir\n- >  ')
    if opcion == '1':
        fnt_selector(opcion)
    elif opcion == '2':
        os.system('cls')
        print('\nCantidad de registros: ',len(mi_diccionario),'\n')
        for clave, valor in mi_diccionario.items():
            print(f"{clave}: {valor}")
        enter = input('\n\nPresione ENTER para continuar...')
    elif opcion == '3':
        sw = False