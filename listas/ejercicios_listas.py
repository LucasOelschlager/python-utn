asignaturas: list = []
asignatura = []






'''
EJERCICIO 1

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
'''

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
                




