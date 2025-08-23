import administradorArchivo, funciones

datos = administradorArchivo.leerArchivo("registro_temperatura365d_smn.txt")

funciones.maxminPorAño(datos)