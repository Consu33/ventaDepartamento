import random as ra
import numpy as np
depto=np.empty([10,4], dtype="object")
lista_compradores = []
encabezado = ["A","B","C","D"]
ganancias_totales = 0



## INICIO FUNCIONES

# INICIO DEF comprar
def comprar():
    global ganancias_totales
    while True:
        try:
            print("depto ---- \n", depto)
            encabezado = ["A","B","C","D"]

            # capturo los datos
            print("Ingrese piso del departamento (1/10): ")
            piso = int(input())
            print("Ingrese tipo de departamento (A,B,C,D):")
            tipoDepartamento = str(input()).upper()           

            # identifico coordenadas para la matriz
            indiceColumna = piso - 1
            indiceEncabezado = encabezado.index(tipoDepartamento)

            # consulto disponibilidad en matriz
            if(depto[indiceColumna][indiceEncabezado] == 'X'):
                print("El departamento esta vendido. Reintente")
                continue

            elif(depto[indiceColumna][indiceEncabezado] == ' '):

                #TODO antes de comprar el depto debo capturar el rut del comprado
                print("Favor de ingresar nombre y apellido para registro ")
                nombre = str(input())
                print("Favor de ingresar rut para registro")
                rut = int(input())
                     
                #TODO asociar tipo depto a valor
                print("-----------------------------------------------------------")   
                print("Valores tipo departamento, Inmobiliaria Murito")
                print("Departamento A : $3.800 UF")
                print("Departamento B : $3.000 UF")
                print("Departamento C : $2.800 UF")
                print("Departamento D : $3.500 UF")

                if(tipoDepartamento == 'A'):
                    valorDepto = int(3800)
                if(tipoDepartamento == 'B'):
                    valorDepto = int(3000)
                if(tipoDepartamento == 'C'):
                    valorDepto = int(2800)
                if(tipoDepartamento == 'D'):
                    valorDepto = int(3500)

                ganancias_totales += valorDepto      

                depto[indiceColumna][indiceEncabezado] = 'X'
                print("-----------------------------------------------------------")
                print("FELICITACIONES!!! Departamento disponible.")

                #TODO Agregar datos de el cliente (RUT) y departamento

                datos_comprador = {
                    "nombre": nombre,
                    "rut": rut,
                    "piso" : piso,
                    "depto": tipoDepartamento,
                }
                
                lista_compradores.append(datos_comprador)

            print(f" Su departamento es piso: ' {piso} 'depto: ' {tipoDepartamento}'")
            print(f" Registrado a nombre de: ', {nombre} 'rut:' {rut}'")
            print(f" Monto total a pagar: ', {valorDepto}")
            print("depto ---- \n", depto)
            break
            

        except:
            print("Pucha te equivocaste!!! vuelve a intentarlo")   
            
# Inicio mostrar compradores
def mostrar_compradores():
    if len(lista_compradores) > 0:
        print("Lista de compradores:")
        for comprador in lista_compradores:
            print(comprador)
    else:
        print("No hay compradores registrados.")

# Inicio reasignar compra
def reasignar_compra():
    if len(lista_compradores) > 0:
        print("Ingrese el rut del comprador cuya compra desea reasignar:")
        rut = int(input())
        comprador_encontrado = None

        for comprador in lista_compradores:
            if comprador["rut"] == rut:
                comprador_encontrado = comprador
                break

        if comprador_encontrado:
            print(f"Comprador encontrado: {comprador_encontrado['nombre']}")
            print("Ingrese el nuevo piso del departamento (1/10):")
            nuevo_piso = int(input())
            print("Ingrese el nuevo tipo de departamento (A, B, C, D):")
            nuevo_tipo = str(input()).upper()

            
            indiceColumna = nuevo_piso - 1
            indiceEncabezado = encabezado.index(nuevo_tipo) 

            if depto[indiceColumna][indiceEncabezado] == 'X':
                print("El departamento seleccionado ya está vendido.")
            else:
                depto[indiceColumna][indiceEncabezado] = 'X'
                depto[indiceColumna][encabezado.index(comprador_encontrado["TipoDepto"])] = ' '
                comprador_encontrado["TipoDepto"] = nuevo_tipo
                print("Reasignación de compra exitosa.")
        else:
            print("No se encontró un comprador con el Rut ingresado.")
    else:
        print("No hay compradores registrados.")
## FIN FUNCIONES


#Recorremos cada fila de la matriz (son 10 filas) // OCUPE SU EJEMPLO PROFE de asignacion de asientos :)
for encabezado in range(10):
    #Una vez posicionado en la fila. Recorremos las columnas (son 4 columnas)
    for indiceColumna in range(4):
        #Ahora llenamos cada departamento con números
        #Aleatorios 0 ó 1. Donde X significa no disponible y
        #0 un asiento disponible.
        # depto[encabezado][indiceColumna] = ra.randint(0,1)
        depto[encabezado][indiceColumna] = ra.choice(["X", " "])



print("Bienvenidos a Inmobiliaria Murito")

while True:
    print(" Que desea hacer? ")
    print ("1. Comprar departamento")
    print ("2. Mostrar departamento")
    print ("3. Ver listado de compradores")
    print ("4. Buscar compradores")
    print ("5. Reasignar compra")
    print ("6. Mostrar ganancias totales")
    print ("7. Salir")
    opcion = int(input())

    # si opcion no es mayor que cero y menor que ocho - vuelve a ingresar opcion
    if not(opcion > 0 and opcion < 8):
        print("Opcion no valida, intente de nuevo")
        continue
    
    if opcion == 1 :
        print("Elegiste la opción 1, que departamento deseas comprar")
        comprar()    

    if opcion == 2 :
        print("Elegiste la opción 2, mostrando departamentos")
        print("departamentos no disponibles, informados con una X \n", depto)

    if opcion == 3 :
        print("Elegiste la opción 3, listado de compradores")
        print("Lista de compradores:")
        for comprador in lista_compradores:
            print(comprador)  

    if opcion == 4 :
        print("Elegiste la opción 4, buscando compradores")
        mostrar_compradores()

    if opcion == 5 :
        print("Elegiste la opción 5, reasignando compra")
        reasignar_compra()

    if opcion == 6 :
        print("Elegiste la opción 6, ganancias totales")
        print(f"Las ganancias totales son:,'{ganancias_totales}")
        ganancias_totales()

    if opcion == 7 :
        print("Elegiste la opción 7, salir.......... hasta luego!")
        break
