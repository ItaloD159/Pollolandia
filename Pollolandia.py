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

#-------------------------------------------------------------------------------
#Creamos el inicio de sesión del cajero
class Sistema_Caja:
    def __init__(self):
        #Registramos al cajero
        self.cajero = Empleado("Bonifacio", "1234")
        #Generamos ID de pedidos
        self.id_pedido = 1

    def iniciar_sesion(self):
        print("----------SISTEMA DE CAJA POLLOLANDIA----------")

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

        while True:
            print("\n----------MENÚ----------")
            print("1. 1/4 pollo (pierna) + papas + ensalada - S/18.00")
            print("2. 1/4 pollo (pecho) + papas + ensalada -- S/20.00")
            print("3. 1/2 pollo + papas + ensalada ---------- S/35.00")
            print("4. 1 pollo entero + papas + ensalada ----- S/65.00")
            print("5. 1 pollo entero + papas + arroz chauda - S/75.00")
            print("6. Gaseosa Inka Cola o Coca Cola 500mlts - S/4.00")
            print("7. Gaseosa Inka Cola o Coca Cola 2lts ---- S/8.00")
            print("8. Gaseosa Inka Cola o Coca Cola 3lts ---- S/13.00")
            print("9. Finalizar pedido")
            print("10. Salir")

            opcion = input("\nSeleccione la opción: ").strip()

            #Le colocamos los precios
            precio = 0

            if opcion == "1": precio = 18.00
            elif opcion == "2": precio = 20.00
            elif opcion == "3": precio = 35.00
            elif opcion == "4": precio = 65.00
            elif opcion == "5": precio = 75.00
            elif opcion == "6": precio = 4.00
            elif opcion == "7": precio = 8.00
            elif opcion == "8": precio = 13.00
            elif opcion == "9":
                if self.monto_total == 0:
                    print("No seleccionaste ninguna opción. Vuelve a intentarlo")
                else:
                    print(f"\nEl total a pagar es: S/{self.monto_total:.2f}")
                    return True
            elif opcion == "10":
                print("Se cierra la orden")
                return False
            else:
                print("Opción inválida.")

            #Sumamos los precios
            if precio > 0:
                self.monto_total += precio
                print(f"+ Subtotal actual: S/ {self.monto_total:.2f}")

    def comprobante(self):
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
                break
            #Si es delivery
            elif opcion == "2":
                direccion = input("Ingrese la dirección: ").strip()
                num_celular = input("Ingrese el número de celular: ").strip()
                entrega_actual = Delivery(direccion, num_celular)
                self.monto_total += entrega_actual.costo_envio
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
        pedido_actual = Pedido(self.id_pedido, self.monto_total, entrega_actual)
        self.id_pedido += 1

        if cliente_actual.dni:
            print(f"Pedido N°{pedido_actual.id_pedido} registrado a nombre de {cliente_actual.nombre} con DNI {cliente_actual.dni}.")
        elif cliente_actual.ruc:
            print(f"Pedido N°{pedido_actual.id_pedido} registrado a nombre de {cliente_actual.nombre} con RUC {cliente_actual.ruc}.")
        else:
            print(f"Pedido N°{pedido_actual.id_pedido} registrado a nombre de {cliente_actual.nombre}.")

        #Registramos el pago del pedido
        print("\n----------PAGO----------")
        print(f"Modalidad: {pedido_actual.entrega.tipo}")
        print(f"El monto total a cobrar es: S/.{self.monto_total:.2f}")

        while True:
            try:
                monto_cobrado = float(input("Ingrese el monto cobrado al cliente: S/."))
                
                if monto_cobrado>=self.monto_total:
                    vuelto = monto_cobrado - self.monto_total
                    print(f"El vuelto a entregar es de: S/.{vuelto:.2f}")

                    pago_actual = Metodo_Pago(monto_cobrado, "Completado")
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

    
