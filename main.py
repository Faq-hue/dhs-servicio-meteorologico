import administradorArchivo, funciones

datos = administradorArchivo.leerArchivo("registro_temperatura365d_smn.txt")
menu = 1

while(menu == 1):

    print("Menu")
    print("1. Reporte por estación meteorológica de la temperatura máxima y mínima registradas en el período del último año.")
    print("2. La estación meteorológica que registre la mayor amplitud térmica en el mismo día, indicando el día del año que ocurrió")
    print("3. La estación meteorológica que registre la menor amplitud térmica en el mismo día, indicando el día del año que ocurrió")
    print("4. La máxima diferencia de temperatura entre minima y máxima temperatura entre dos estaciones meteorológicas en un mismo día, indicando las temperaturas y las estaciones que las registraron.")
    print("5. La mínima diferencia de temperatura entre minima y máxima temperatura entre dos estaciones meteorológicas en un mismo día, indicando las temperaturas y las estaciones que las registraron.")
    print("_. Salir")
    opcion = input()

    match opcion:
        case "1":
            anio = input("Ingrese el año ")
            administradorArchivo.escribirArchivo(funciones.maxminPorAño(datos,anio))

        case "2":
            administradorArchivo.escribirArchivo(funciones.estacionMayorAmplitud(datos))

        case "3":
            administradorArchivo.escribirArchivo(funciones.estacionMenorAmplitud(datos))

        case "4":
            administradorArchivo.escribirArchivo(funciones.maximaDiferenciaEstaciones(datos))

        case "5":
            administradorArchivo.escribirArchivo(funciones.minimaDiferenciaEstaciones(datos))

        case _:
            print("Saliendo del programa")
            menu = 0
