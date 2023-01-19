edades = [20, 41, 6, 18, 23]

# Recorriendo los elementos
for edad in edades:
    print(edad)

# Recorriendo los índices
for i in range(len(edades)):
    print(edades[i])

# Con while y los índices
indice = 0

while indice < len(edades):
    print(edades[indice])
    indice += 1



números = []

números.append(10)
números.append(5)
números.append(3)

print(números)
# Mostrará [10, 5, 3]


# Unimos la lista anterior con una nueva
números = números + [10, 5, 3]

print(números)
# Mostrará [10, 5, 3]

palabras = ['hola', 'hello', 'ola']

palabras.pop(1)

print(palabras)
# Mostrará ['hola', 'ola']


palabras.remove('hello')

print(palabras)
# Mostrará ['hola', 'hello', 'ola']

