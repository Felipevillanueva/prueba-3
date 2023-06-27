datos_personales = []
pelicula = []
cartelera =[]
boleta = []

lista_pelicula = [
    ["Super Mario Bros 3D", "12:50", 00, 2500],
    ["Spiderman Lejos de Casa", "12:50", 00, 2500],
    ["El Rey León", "12:50", 00, 2500],
    ]

colum1 = 15
fila1 = 10 
asientos = [["0"for _ in range (colum1)]for _ in range(fila1)]


def registrae_datos():
    nombre = input("ingrese su nombre")
    edad = int(input("ingrese su edad"))
    correo = input("ingrese su correo")
    descuento = int (input("estudia en el duoc? si/no?"))
    if descuento == 1:
        print("tiene descuento por estudiar en el duoc")
    else:
        print("no tiene descuento")
    datos_personales(nombre,edad,correo)


def mostra_cartelera ():
    print("cartelera disponible")
    for i, pelicula in enumerate(cartelera):
        print(i + 1, "_", 
        pelicula[0], "_ hora:",
        pelicula[1], "_ asientos_disponible:",
        pelicula[2], "- precio:", 
        pelicula[3])

def matris():
    print("cual asientos quieren?")
    print(" ", end ="")
    for i in range (1, colum1 + 1):
        print(i, end=" ")
    print()
    for i in range (fila1):
        print (chr(65 + i), end=" ")
    for j in range(colum1):
        print(asientos[i][j],end="")
        print()

def reservar_asientos():
    mostra_cartelera()
    pelicula_index = int(input(
    "seleccione una pelicula: "))-1
    if pelicula_index < 0 or pelicula_index >= len(cartelera):
        print("seleccione una pelicula")
        return

    asientos_disponibles = cartelera[pelicula_index][2]
    if asientos_disponibles== 0:
        print("no quedan asientos disponibles para esta pelicula")
        return


    
def mostrar_boletas ():
    print("__________boletas_generada")
    enumerate(boleta)
    nombre = boleta[0]
    correo = boleta[1]
    asientos_reservados = boleta[2]
    pelicula = boleta[3]
    asientos_seleccionados = boleta[4],
    mostrar_boletas(nombre,correo,pelicula,asientos_reservados,asientos_seleccionados)
    print("--------------------------------")     

 
      