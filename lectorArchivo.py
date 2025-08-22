import string

def lectorArchivo(nombreArchivo):
    
    with open(nombreArchivo, "r", encoding="latin1") as archivo:
        lineas = archivo.readlines()
        dict = {}
        i = 0

        for linea in lineas:

           if(not linea.startswith("FECHA") and not linea.startswith("----")):         
                
                partes = linea.split()
                
                if partes:
                    fecha = partes[0]

                    # la linea esta completa
                    if(len(partes) == 4):
                        valormax = partes[1]
                        valormin = partes[2]
                        nombre = " ".join(partes[3:])

                    # falta valormax
                    elif(len(partes) == 3):
                        try:
                            float(partes[1])
                            valormax = partes[1]
                        except ValueError:
                            valormax = None
                        try:
                            float(partes[2])
                            valormin = partes[2]
                        except ValueError:
                            valormin = None
                    else:
                        valormax = None
                        valormin = None
                        nombre = " ".join(partes[3:])
                        
                    dict["fecha"] = fecha
                    dict["max"] = valormax
                    dict["min"] = valormin
                    dict["nombre"] = nombre
                    
                    print(dict)

    return 1#dict(enumerate(set(lineas)))