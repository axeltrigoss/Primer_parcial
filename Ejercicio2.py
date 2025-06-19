from super_heroes_data import super_heroes

# A. Listado ordenado de forma ascendente por nombre
personajes_ordenados = super_heroes.copy()
personajes_ordenados.sort(key=lambda x: x['superhero'])

print("1. Personajes ordenados por nombre:")
for p in personajes_ordenados:
    print(p['superhero'])

# B. Posición de The Thing y Rocket Raccoon
nombres = [p['superhero'] for p in super_heroes]
if 'The Thing' in nombres:
    print("2. The Thing está en la posición:", nombres.index('The Thing'))
if 'Rocket Raccoon' in nombres:
    print("Rocket Raccoon está en la posición:", nombres.index('Rocket Raccoon'))

# C. Listando todos los villanos
villanos = []
for p in super_heroes:
    if p['alignment'] == 'bad':
        villanos.append(p)
print("3. Villanos:")
for v in villanos:
    print(v['superhero'])

# D. Poniendo villanos en cola (lista) y mostrar los de antes de 1980
cola_villanos = []
for v in villanos:
    cola_villanos.append(v)

print("4. Villanos que aparecieron antes de 1980:")
while cola_villanos:
    villano = cola_villanos.pop(0)
    if villano['year'] and villano['year'] < 1980:
        print(villano['superhero'], "-", villano['year'])

# E. Superhéroes que empiezan con Bl, G, My o W
print("5. Superhéroes que empiezan con Bl, G, My o W:")
for p in super_heroes:
    nombre = p['superhero']
    if nombre.startswith("Bl") or nombre.startswith("G") or nombre.startswith("My") or nombre.startswith("W"):
        print(nombre)

# F. Ordenando por nombre real
personajes_con_nombre_real = []
for p in super_heroes:
    if p['real_name']:
        personajes_con_nombre_real.append(p)

personajes_con_nombre_real.sort(key=lambda x: x['real_name'])

print("6. Personajes ordenados por nombre real:")
for p in personajes_con_nombre_real:
    print(p['real_name'], "-", p['superhero'])

# G. Ordenando por fecha de aparición
personajes_con_fecha = []
for p in super_heroes:
    if p['year']:
        personajes_con_fecha.append(p)

personajes_con_fecha.sort(key=lambda x: x['year'])

print("7. Superhéroes ordenados por fecha de aparición:")
for p in personajes_con_fecha:
    print(p['year'], "-", p['superhero'])

# H. Modificando nombre real de Ant-Man
for p in super_heroes:
    if p['superhero'] == 'Ant-Man':
        p['real_name'] = 'Scott Lang'
        print("8. Nombre real de Ant-Man actualizado a Scott Lang.")

# I. Mostrando personajes con 'time-traveling' o 'suit' en su biografía
print("9. Personajes con 'time-traveling' o 'suit' en la biografía:")
for p in super_heroes:
    if 'bio' in p:
        bio = p['bio'].lower()
        if 'time-traveling' in bio or 'suit' in bio:
            print(p['superhero'])

# J. Eliminando a Electro y Baron Zemo y mostrar si estaban
nuevos_personajes = []
eliminados = []

for p in super_heroes:
    if p['superhero'] == 'Electro' or p['superhero'] == 'Baron Zemo':
        eliminados.append(p)
    else:
        nuevos_personajes.append(p)

print("10. Electro y Baron Zemo eliminados:")
for e in eliminados:
    print(e['superhero'], "-", e['real_name'] if e['real_name'] else "Sin nombre real")
