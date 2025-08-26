import administradorArchivo, funciones

datos = administradorArchivo.leerArchivo("registro_temperatura365d_smn.txt")
#print(datos["AZUL AERO"]["tmin"])

funciones.maxminPorAño(datos)