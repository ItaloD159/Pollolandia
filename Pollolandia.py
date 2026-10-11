from datetime import datetime
#Clases de persona
class Persona:
    def __init__(self, nombre, dni=""):
        self.nombre = nombre
        self.dni = dni

class Empleado(Persona):
    def __init__(self, nombre, codigo, dni=""):
        super().__init__(nombre, dni)
        self.codigo = codigo

class Cliente(Persona):
    def __init__(self, nombre, dni="", ruc="", razon_social="", num_celular=""):
        super().__init__(nombre, dni)
        self.ruc = ruc
        self.razon_social = razon_social
        self.num_celular = num_celular

#Clases de entrega
class Entrega:
    def __init__(self, tipo):
        self.tipo = tipo

class Salon(Entrega):
    def __init__(self, num_mesa):
        super().__init__("Consumo en salón")
        self.num_mesa = num_mesa

class Delivery(Entrega):
    def __init__(self, direccion, celular, costo_envio = 5.00):
        super().__init__("Delivery")
        self.direccion = direccion
        self.celular = celular
        self.costo_envio = costo_envio

#Clases de pedido y pago
class Pedido:
    def __init__(self, id_pedido, monto_total, entrega):
        self.id_pedido = id_pedido
        self.monto_total = monto_total
        self.entrega = entrega

class Metodo_Pago:
    def __init__(self, monto, estado):
        self.monto = monto
        self.estado = estado

#Clase almacén
class almacen:
    def __init__(self):
        self.gaseosas = {
        "inka_500ml": 20,
        "coca_500ml": 20,
        "inka_2lts": 15,
        "coca_2lts": 15,
        }
        self.pollos = 100.00
        self.papas = 100.00
        self.ensaladas = 100.00
        self.arroz_chaufa = 20.00

    def verificar_stock(self, cant_pollos, cant_papas, cant_ensaladas,cant_arroz_chaufa, cant_gaseosas):
        if self.pollos < cant_pollos:
            return False
        if self.papas < cant_papas:
            return False
        if self.ensaladas < cant_ensaladas:
            return False
        if self.arroz_chaufa < cant_arroz_chaufa:
            return False
        for gaseosa, cantidad in cant_gaseosas.items():
            if self.gaseosas.get(gaseosa, 0) < cantidad:
                return False
        return True


    def descontar_stock(self, cant_pollos, cant_papas, cant_ensaladas,cant_arroz_chaufa, cant_gaseosas):
        self.pollos -= cant_pollos
        self.papas -= cant_papas
        self.ensaladas -= cant_ensaladas
        self.arroz_chaufa -= cant_arroz_chaufa

        #Creamos una lista de gaseosas para poder descontarlas del stock
        for gaseosa, cantidad in cant_gaseosas.items():
            if gaseosa in self.gaseosas:
                self.gaseosas[gaseosa] -= cantidad

#-------------------------------------------------------------------------------
#Creamos el inicio de sesión del cajero
class Sistema_Caja:
    def __init__(self):
        #Registramos al cajero
        self.cajero = Empleado("Bonifacio", "1234")
        #Generamos ID de pedidos
        self.id_pedido = 1
        self.almacen = almacen()
        #Agregamos variables temporales actuales para llevar un control de lo que se va vendiendo
        self.cant_pollos_actual = 0
        self.cant_papas_actual = 0
        self.cant_ensaladas_actual = 0
        self.cant_arroz_chaufa_actual = 0
        self.cant_gaseosas_actual = {}

    def iniciar_sesion(self):
        print("------------SISTEMA DE CAJA POLLOLANDIA------------")

        while True:
            codigo_ingresado = input("\nIngrese su código de cajero: ").strip()

            #Verificamos el código del cajero
            if codigo_ingresado == self.cajero.codigo:
                print(f"\n¡Bienvenido Cajero {self.cajero.nombre}!")
                print("Caja aperturada con éxito.")
                return True
            else:
                print("\nCódigo incorrecto. Intente de nuevo.")

    def menu(self):
        self.monto_total = 0.0
        #Si tomamos otro pedido, reiniciamos las variables actuales
        self.cant_pollos_actual = 0
        self.cant_papas_actual = 0
        self.cant_ensaladas_actual = 0
        self.cant_arroz_chaufa_actual = 0
        self.cant_gaseosas_actual = {}

        while True:
            print("\n-----------------------STOCK-----------------------")
            print(
                f"\nPollos: {self.almacen.pollos:.2f}, Papas: {self.almacen.papas:.2f}, \nEnsaladas: {self.almacen.ensaladas:.2f}, Arroz Chaufa: {self.almacen.arroz_chaufa:.2f} \nGaseosas: \nInka Cola 500ml: {self.almacen.gaseosas.get('inka_500ml', 0)}, Coca Cola 500ml: {self.almacen.gaseosas.get('coca_500ml', 0)}, \nInka Cola 2lts: {self.almacen.gaseosas.get('inka_2lts', 0)}, Coca Cola 2lts: {self.almacen.gaseosas.get('coca_2lts', 0)}"
            )
            print("\n-----------------------MENÚ-----------------------")
            print("1. 1/4 pollo (pierna) + papas + ensalada - S/18.00")
            print("2. 1/4 pollo (pecho) + papas + ensalada -- S/20.00")
            print("3. 1/2 pollo + papas + ensalada ---------- S/35.00")
            print("4. 1 pollo entero + papas + ensalada ----- S/65.00")
            print("5. 1 pollo entero + papas + arroz chaufa - S/75.00")
            print("6. Gaseosa Inka Cola 500ml --------------- S/4.50")
            print("7. Gaseosa Coca Cola 500ml --------------- S/4.50")
            print("8. Gaseosa Inka Cola 2lts ---------------- S/13.00")
            print("9. Gaseosa Coca Cola 2lts ---------------- S/13.00")
            print("10. Finalizar pedido")
            print("11. Salir")

            opcion = input("\nSeleccione la opción: ").strip()

            #Le colocamos los precios
            precio = 0

            if opcion == "1":
                if self.almacen.verificar_stock(
                    self.cant_pollos_actual + 0.25,
                    self.cant_papas_actual + 0.25,
                    self.cant_ensaladas_actual + 0.25,
                    self.cant_arroz_chaufa_actual,
                    self.cant_gaseosas_actual
                ):
                    precio = 18.00
                    self.cant_pollos_actual += 0.25
                    self.cant_papas_actual += 0.25
                    self.cant_ensaladas_actual += 0.25
                else:
                    print("No hay suficiente stock.")

            elif opcion == "2":
                if self.almacen.verificar_stock(
                    self.cant_pollos_actual + 0.25,
                    self.cant_papas_actual + 0.25,
                    self.cant_ensaladas_actual + 0.25,
                    self.cant_arroz_chaufa_actual,
                    self.cant_gaseosas_actual
                ):
                    precio = 20.00
                    self.cant_pollos_actual += 0.25
                    self.cant_papas_actual += 0.25
                    self.cant_ensaladas_actual += 0.25
                else:
                    print("No hay suficiente stock.")

            elif opcion == "3":
                if self.almacen.verificar_stock(
                    self.cant_pollos_actual + 0.50,
                    self.cant_papas_actual + 0.50,
                    self.cant_ensaladas_actual + 0.50,
                    self.cant_arroz_chaufa_actual,
                    self.cant_gaseosas_actual
                ):
                    precio = 35.00
                    self.cant_pollos_actual += 0.50
                    self.cant_papas_actual += 0.50
                    self.cant_ensaladas_actual += 0.50
                else:
                    print("No hay suficiente stock.")

            elif opcion == "4":
                if self.almacen.verificar_stock(
                    self.cant_pollos_actual + 1.00,
                    self.cant_papas_actual + 1.00,
                    self.cant_ensaladas_actual + 1.00,
                    self.cant_arroz_chaufa_actual,
                    self.cant_gaseosas_actual
                ):
                    precio = 65.00
                    self.cant_pollos_actual += 1.00
                    self.cant_papas_actual += 1.00
                    self.cant_ensaladas_actual += 1.00
                else:
                    print("No hay suficiente stock.")

            elif opcion == "5":
                if self.almacen.verificar_stock(
                    self.cant_pollos_actual + 1.00,
                    self.cant_papas_actual + 1.00,
                    self.cant_ensaladas_actual,
                    self.cant_arroz_chaufa_actual + 1.00,
                    self.cant_gaseosas_actual
                ):
                    precio = 75.00
                    self.cant_pollos_actual += 1.00
                    self.cant_papas_actual += 1.00
                    self.cant_arroz_chaufa_actual += 1.00
                else:
                    print("No hay suficiente stock.")
                    
            elif opcion == "6":
                gaseosas_pedido = self.cant_gaseosas_actual.copy()
                gaseosas_pedido["inka_500ml"] = gaseosas_pedido.get("inka_500ml", 0) + 1

                if self.almacen.verificar_stock(
                    self.cant_pollos_actual,
                    self.cant_papas_actual,
                    self.cant_ensaladas_actual,
                    self.cant_arroz_chaufa_actual,
                    gaseosas_pedido
                ):
                    precio = 4.50
                    self.cant_gaseosas_actual = gaseosas_pedido
                else:
                    print("No hay suficiente stock (Inka Cola 500ml).")

            elif opcion == "7":
                gaseosas_pedido = self.cant_gaseosas_actual.copy()
                gaseosas_pedido["coca_500ml"] = gaseosas_pedido.get("coca_500ml", 0) + 1

                if self.almacen.verificar_stock(
                    self.cant_pollos_actual,
                    self.cant_papas_actual,
                    self.cant_ensaladas_actual,
                    self.cant_arroz_chaufa_actual,
                    gaseosas_pedido
                ):
                    precio = 4.50
                    self.cant_gaseosas_actual = gaseosas_pedido
                else:
                    print("No hay suficiente stock (Coca Cola 500ml).")
            elif opcion == "8":
                gaseosas_pedido = self.cant_gaseosas_actual.copy()
                gaseosas_pedido["inka_2lts"] = gaseosas_pedido.get("inka_2lts", 0) + 1

                if self.almacen.verificar_stock(
                    self.cant_pollos_actual,
                    self.cant_papas_actual,
                    self.cant_ensaladas_actual,
                    self.cant_arroz_chaufa_actual,
                    gaseosas_pedido
                ):
                    precio = 13.00
                    self.cant_gaseosas_actual = gaseosas_pedido
                else:
                    print("No hay suficiente stock (Inka Cola 2L).")

            elif opcion == "9":
                gaseosas_pedido = self.cant_gaseosas_actual.copy()
                gaseosas_pedido["coca_2lts"] = gaseosas_pedido.get("coca_2lts", 0) + 1

                if self.almacen.verificar_stock(
                    self.cant_pollos_actual,
                    self.cant_papas_actual,
                    self.cant_ensaladas_actual,
                    self.cant_arroz_chaufa_actual,
                    gaseosas_pedido
                ):
                    precio = 13.00
                    self.cant_gaseosas_actual = gaseosas_pedido
                else:
                    print("No hay suficiente stock (Coca Cola 2L).")
                
            elif opcion == "10":
                if self.monto_total == 0:
                    print("No seleccionaste ninguna opción. Vuelve a intentarlo")
                else:
                    print(f"\nEl total a pagar es: S/{self.monto_total:.2f}")
                    return True
            elif opcion == "11":
                print("Se cierra la orden")
                return False
            else:
                print("Opción inválida.")

            #Sumamos los precios
            if precio > 0:
                self.monto_total += precio
                print(f"+ Subtotal actual: S/ {self.monto_total:.2f}")

    def comprobante(self):
        #Creamos las variables para el comprobante
        monto_comida = self.monto_total
        costo_envio = 0.0

        #Tipo de entrega
        while True:
            print("\n-----------TIPO DE ENTREGA----------")
            print("1. Salón")
            print("2. Delivery (+ S/5.00)")
        
            opcion = input("\nSeleccione la opción: ").strip()
        
            #Si es en salón
            if opcion == "1":
                num_mesa = input("Ingrese el número de mesa: ").strip()
                entrega_actual = Salon(num_mesa) #Creamos el objeto salon y lo igualamos a la variable
                monto_a_cobrar = monto_comida  # No hay costo adicional para consumo en salón
                break
            #Si es delivery
            elif opcion == "2":
                direccion = input("Ingrese la dirección: ").strip()
                num_celular = input("Ingrese el número de celular: ").strip()
                entrega_actual = Delivery(direccion, num_celular)
                costo_envio = entrega_actual.costo_envio
                monto_a_cobrar = (
                    monto_comida + costo_envio
                )
                print("+ Se agregaron S/ 5.00 por el costo del delivery")
                break
            else:
                print("Opción inválida.")

        #Emitimos un comprobante de venta
        while True:
            print("\n¿Desea boleta o factura?")
            print("1. Boleta")
            print("2. Factura")

            opcion = input("\nSeleccione la opción: ").strip()

            #Boleta
            if opcion == "1":
                print("\n----------DATOS DEL CLIENTE----------")
                nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
                dni_cliente = input("Ingrese el número de DNI del cliente: ").strip()
                cliente_actual = Cliente(nombre_cliente, dni=dni_cliente)
                break
            #Factura
            elif opcion == "2":
                print("\n----------DATOS DEL CLIENTE----------")
                nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
                ruc_cliente = input("Ingrese el número de RUC del cliente: ").strip()
                cliente_actual = Cliente(nombre_cliente, ruc=ruc_cliente)
                break

            else:
                print("\nOpción inválida.")

        #Creamos el pedido
        pedido_actual = Pedido(self.id_pedido, monto_a_cobrar, entrega_actual)

        if cliente_actual.dni:
            print(f"Pedido N°{pedido_actual.id_pedido} registrado a nombre de {cliente_actual.nombre} con DNI {cliente_actual.dni}.")
        elif cliente_actual.ruc:
            print(f"Pedido N°{pedido_actual.id_pedido} registrado a nombre de {cliente_actual.nombre} con RUC {cliente_actual.ruc}.")
        else:
            print(f"Pedido N°{pedido_actual.id_pedido} registrado a nombre de {cliente_actual.nombre}.")

        #Registramos el pago del pedido
        print("\n-------------------PAGO-------------------")
        print(f"Modalidad: {pedido_actual.entrega.tipo}")
        print(f"El monto total a cobrar es: S/.{self.monto_total:.2f}")

        while True:
            try:
                monto_cobrado = float(input("Ingrese el monto cobrado al cliente: S/."))
                
                if monto_cobrado>=self.monto_total:
                    vuelto = monto_cobrado - self.monto_total
                    print(f"El vuelto a entregar es de: S/.{vuelto:.2f}")

                    pago_actual = Metodo_Pago(monto_cobrado, "Completado")

                    #Creamos la impresión del comprobante
                    print("\n-----------COMPROBANTE DE PAGO------------")
                    print(f"Pedido N°{pedido_actual.id_pedido}")
                    print("Fecha de emisión:", datetime.now().strftime("%d/%m/%Y"))
                    print(f"Cliente: {cliente_actual.nombre}")
                    print(f"Tipo de entrega: {pedido_actual.entrega.tipo}")

                    # Si es en salón, muestra la mesa; si es delivery, muestra la dirección
                    if isinstance(pedido_actual.entrega, Salon):
                        print(f" N° de Mesa   : {pedido_actual.entrega.num_mesa}")
                    elif isinstance(pedido_actual.entrega, Delivery):
                        print(f" Dirección    : {pedido_actual.entrega.direccion}")
                        print(f" Celular      : {pedido_actual.entrega.celular}")

                    print("-" * 42)
                    print(f" Cliente      : {cliente_actual.nombre}")
                    if cliente_actual.dni:
                        print(f" DNI          : {cliente_actual.dni}")
                    elif cliente_actual.ruc:
                        print(f" RUC          : {cliente_actual.ruc}")

                    print("-" * 42)

                    
                    igv_comida = monto_comida - (monto_comida / 1.18)
                    print(f" IGV (18%)    : S/. {igv_comida:.2f}")

                    # Si es delivery, podemos mostrar el costo de envío desglosado opcionalmente
                    if costo_envio > 0:
                        print(
                            f" Subtotal Comida: S/. {monto_comida - igv_comida:.2f}"
                        )  # Opcional
                        print(f" Costo Delivery : S/. {costo_envio:.2f}")

                    print(f" Monto Total    : S/. {monto_a_cobrar:.2f}")
                    print(f" Efectivo       : S/. {monto_cobrado:.2f}")
                    print(f" Vuelto         : S/. {vuelto:.2f}")
                    print("=" * 42)
                    print("         ¡GRACIAS POR SU PREFERENCIA!")
                    print("=" * 42 + "\n")

                    #Descontamos el stock de lo que hemos vendido
                    self.almacen.descontar_stock(
                        self.cant_pollos_actual,
                        self.cant_papas_actual,
                        self.cant_ensaladas_actual,
                        self.cant_arroz_chaufa_actual,
                        self.cant_gaseosas_actual
                    )

                    self.id_pedido += 1     #Aumentamos el ID si se llegó a cobrar con éxito
                    break
                
                else:
                    print("El monto ingresado es menor al total a pagar. Intente de nuevo.")
            except ValueError:
                print("Ingrese un monto válido")  

#-------------------------------------------------------------------------------

#Ejecución en consola
caja = Sistema_Caja()
if caja.iniciar_sesion():
    while True:
        if caja.menu():
            caja.comprobante()

        #Otro pedido?
        while True:
            respuesta = input("\n¿Desea registrar otro pedido? (S/N): ").strip().lower()
            #Volvemos al menú
            if respuesta == 's':
                break
            
            elif respuesta == 'n':
                print("\nCaja cerrada.")
                exit()
            else:
                print("Opción inválida.")

    
