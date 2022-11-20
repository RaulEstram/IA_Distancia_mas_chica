from libs.lugares import CatalogoLugares
from libs.algoritmo_genetico import Algorithm

# menu

index_lugares_recorrer = []
lugares_recorrer = []

print("Lugares Disponibles: ")
for index in range(len(CatalogoLugares.lugares)):
    print(f"{index}.- {CatalogoLugares.lugares[index]}")

inicio = int(input("Digite donde quiere iniciar: "))

while True:

    opcion = input("Digite la opccion que quiere recorrer (Digite 'e' para salir o 't' para terminar la eleccion): ")
    if opcion == "e":
        break
    if opcion == "t":
        index_lugares_recorrer = list(set(index_lugares_recorrer))
        for index in index_lugares_recorrer:
            lugares_recorrer.append(CatalogoLugares.lugares[index])
        ag = Algorithm(lugares_recorrer, 1000, CatalogoLugares.lugares[inicio])
        ag.run()
        print()
        print("Mejor Ruta")
        print(ag.rutas[0])
        break
    try:
        index_lugares_recorrer.append(int(opcion))
    except ValueError:
        pass
