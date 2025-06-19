from super_heroes_data import heroes

# Usamos los primeros 15 personajes
nombres = [héroe['name'] for héroe in heroes[:15]]

# Función recursiva para buscar "Captain America"
def buscar_capitan(lista, indice=0):
    if indice >= len(lista):
        return False
    elif lista[indice] == "Captain America":
        return True
    else:
        return buscar_capitan(lista, indice + 1)

# Función recursiva para listar los héroes
def listar_heroes(lista, indice=0):
    if indice >= len(lista):
        return
    else:
        print(lista[indice])
        listar_heroes(lista, indice + 1)

# Ejecutar y mostrar resultados
esta = buscar_capitan(nombres)
print("¿Está Captain America en la lista?", esta)
print("\nListado de los héroes:")
listar_heroes(nombres)
