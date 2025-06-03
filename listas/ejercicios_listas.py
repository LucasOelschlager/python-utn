asignaturas: list = []
asignatura = []



'''
EJERCICIO 1

Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

while True:
        asignaturas.append(input('INGRESE LA ASIGNATURA: \n'))
        while True:
                option = input('Quiere agregar otra asignatura? (s/n)')
                if option.lower() == 'n' or option.lower() == 's':
                        break
                else:
                        print('Opcion invalida')
                        continue
        if option.lower() == 'n':
                break

print(asignaturas)
'''

'''
EJERCICIO 2
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo
estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.


while True:
        asignatura.append(input('Ingrese la asignatura: \n'))
        while True:
                option = input('¿Quiere ingresar otra asignatura? (S/N)')
                if option.lower() == 'n' or option.lower() == 's':
                        break
                else:
                        print('La opcion ingresada no es válida')
                        continue
        if option.lower() == 'n':
                break

asignaturas.append(asignatura)
for asignatura in asignaturas: 
        print(f'Yo estudio ',", ".join(asignatura))
'''



'''
EJERCICIO 3L
Escribir un programa que almacene las asignaturas de un curso (por ejemplo:
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota
que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En
<asignatura> has sacado <nota> donde <asignatura> es cada una de las asignaturas de
la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.


while True: 
        materia = input('Ingrese la asignatura \n')
        nota = float(input(f'Ingrese la nota de {materia} \n'))
        asignaturas.append({"Materia": materia, "Nota": nota})
        while True:
                option = input('¿Quiere ingresar otra asignatura? (S/N)')
                if option.lower() == 'n' or option.lower() == 's':
                        break
                else:
                        continue
        if option.lower() == 'n':
                print('Cargando notas... \n')
                break

for asignatura in asignaturas:
        print(f'Materia: {asignatura['Materia']}, Nota: {asignatura['Nota']}')              
'''

'''
EJERCICIO 4
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por
pantalla en orden inverso separados por comas.
numeros: list =[]
for num  in range (1, 11):
    numeros.append(num)
numeros.reverse()
print(", ".join(str(n) for n in numeros))
'''


'''
EJERCICIO 5
Escribir un programa que almacene las asignaturas de un curso (por ejemplo:
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota
que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el
programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

repetir = []
while True:
        materia_nombre = input('INGRESE UNA ASIGNATURA: ')
        while True:
                try:
                        nota = float(input(f'Ingrese la nota de {materia_nombre} '))
                        if nota < 0 or nota > 10:
                                print('Ingrese una nota valida (0-10)')
                                continue
                        elif nota < 6: 
                                repetir.append((materia_nombre, nota))
                                break
                        else:
                                asignatura.append((materia_nombre, nota))
                                break
                except ValueError:
                        print('Ingrese un número válido')
        option = input('Desea añadir otra asignatura? (S/N) ')
        if(option.lower() == 'n'):
                break
        else: 
                continue

print('Materias aprobadas ')
for materia in asignatura:
        print(f'Materia: {materia_nombre}\n Nota: {nota}')
print('Materias desaprobadas')
for materia_desaprobada in repetir:
        print(f'Materia: {materia_nombre}\n Nota: {nota}')


'''


'''
EJERCICIO 6
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras
que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
abecedario: list = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]



for letra in abecedario:
    if (abecedario.index(letra) + 1) % 3 == 0:
       abecedario.remove(letra)
print(abecedario)


'''

'''
EJERCICIO 7
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80,
65, 8, y muestre por pantalla el menor y el mayor de los precios.

precios =[50, 75, 46, 22, 80, 65, 8]
aux: int = precios[0]
for precio in precios:
        if precio < aux:
                aux = precio
        else:
                continue
print(f'El precio  mas bajo es {aux}' )
for precio in precios:
        if precio > aux:
                aux = precio
        else: 
                continue
print(f'El precio mas alto es {aux}')

OTRA FORMA MAS FACIL

print('El precio mas bajo es: ', min(precios))
print('El precio mas alto es: ', max(precios))

'''







    
    
  
    




                



          













