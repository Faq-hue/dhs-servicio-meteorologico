import administradorArchivo, funciones

datos = administradorArchivo.leerArchivo("registro_temperatura365d_smn.txt")
#print(datos["AZUL AERO"]["fecha"])

#funciones.maxminPorAño(datos)
funciones.estacionMayorAmplitud(datos)
funciones.estacionMenorAmplitud(datos)

