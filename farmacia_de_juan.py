inventario = {}
total_ventas = 0


def registrar_medicamento():
    nombre = input("Ingresa el nombre del medicamento que deseas: ").capitalize()

    if nombre in inventario:
        print("El medicamento ya está registrado.\n")
        return

    cantidad = int(input("Cantidad disponible: "))
    precio = float(input("Precio del medicamento: "))

    inventario[nombre] = {
        "cantidad": cantidad,
        "precio": precio
    }

    print("Su Medicamento se ha registrado correctamente.\n")


def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.\n")
        return

    print("\nInventario actual")
    print("-" * 30)

    for nombre, datos in inventario.items():
        print(f"{nombre}: {datos['cantidad']} unidades | Precio: ${datos['precio']}")

    print()


def vender_medicamento():
    global total_ventas

    nombre = input("Por favor ingrese el nombre del medicamento a vender: ").capitalize()

    if nombre not in inventario:
        print("Este medicamento no existe.\n")
        return

    cantidad = int(input("Cantidad a vender: "))

    if cantidad > inventario[nombre]["cantidad"]:
        print("No hay suficiente stock disponible.\n")
        return

    inventario[nombre]["cantidad"] -= cantidad
    venta = cantidad * inventario[nombre]["precio"]
    total_ventas += venta

    print(f"Venta realizada. Total de la venta: ${venta}\n")


def mostrar_total_ventas():
    print(f"Total de ventas del día: ${total_ventas}\n")


def mostrar_menu():
    print("Farmacia-de-Juan")
    print("1. Registrar medicamento")
    print("2. Consultar inventario")
    print("3. Vender medicamento")
    print("4. Mostrar total de ventas")
    print("5. Salir")


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_medicamento()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        vender_medicamento()
    elif opcion == "4":
        mostrar_total_ventas()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print(" Esta Opción no es válida.  por favcor Intente de nuevo.\n")
