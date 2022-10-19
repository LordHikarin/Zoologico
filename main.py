from animales import *
select=0
while(True):
    select=input("Selecciona una opcion: \n 1: Agregar, 2: Buscar, 3: Eliminar, 4: Mostrar todo, 5: Cerrar Programa \n")
    if select == "1":
        add(input("Escribe el nombre: "),
            input("Escribe la especie: "),
            input("Escribe el tipo de alimento: "),
            int(input("Escribe el tiempo necesario que debe estar afuera (Minutos): ")),
            int(input("Escribe el tiempo entre cada comida (Minutos): ")))
    elif select == "2":
        read(input("Buscar: "))
    elif select == "3":
        delete(input("Eliminar: "))
    elif select == "4":
        show()
    elif select == "5":
        print("Buenas Noches!")
        break
    else:
        break