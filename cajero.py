suma = 0
retiros = []
depositos = []

menu_volver = True

num_cuenta = int(input("Ingrese su numero de cuenta"))
contraseña = int(input("Ingrese una contraseña de numeros"))
datos_cuenta = (num_cuenta, contraseña)

while menu_volver:
    menu = int(input(
        "Que desea hacer? \n(1) ver saldo" \
        "\n(2) retirar dinero "
        "\n(3) depositar dinero " \
        "\n(4) ver el historial de movimientos" \
        "\n(5) Ver datos de la cuenta  " \
        "\n(6) salir del programa\n"))

    opciones = {"datos de la cuenta" : datos_cuenta,
                "saldo" : suma ,
                "retiro" : retiros,
                "deposito" : depositos
    }

    if menu == 1: 
        print(opciones["saldo"])

    elif menu == 2: 
        monto_mayor = True
        while monto_mayor:
            retirar_dinero = int(input("Ingrese cuanto dinero desea retirar\n"))            

            if retirar_dinero > suma :
                print("ese monto supera al saldo de la cuenta, intentelo de nuevo\n")
            else:
                suma = suma - retirar_dinero
                print("---"*30)
                print("Retiro Exitoso :)")
                print("---"*30)
                monto_mayor = False
                retiros.append(retirar_dinero)
                

    elif menu == 3:
        
        depositar = int(input("Ingrese cuanto dinero desea depositar: \n"))
        suma =  depositar + suma
        opciones["saldo"] = {suma}
        print("Deposito exitoso :)")
        depositos.append(depositar)
    elif menu == 4:
        print("---"*40)
        for i in retiros:
            print("---"*20)
            print(f"se retiró: ", i)
        print("---"*40)
        for n in depositos:
            print("---"*20)
            print("se depositó: ", n)
            print("---"*20)
    elif menu == 5:
        opciones ("")
    elif menu == 6:
        menu_volver = False





    


