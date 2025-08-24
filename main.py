import administradorArchivo, funciones

datos = administradorArchivo.leerArchivo("registro_temperatura365d_smn.txt")

#print(datos["AZUL AERO"]["tmax"][0])

funciones.maxminPorAño(datos)