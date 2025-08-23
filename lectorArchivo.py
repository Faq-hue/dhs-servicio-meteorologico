import string

def lectorArchivo(nombreArchivo):
    
    with open(nombreArchivo, "r", encoding="latin1") as archivo:
        lineas = archivo.readlines()
        datos = {}

        for linea in lineas:

           if(not linea.startswith("FECHA") and not linea.startswith("----") and not linea.startswith(" ")):         
                
                partes = linea.split()
                
                if (partes):
                    fecha = partes[0]

                    valormax, valormin, nombre = None, None, None
                    
                    if(type(partes[1]) == float or type(partes[2]) == float):
                        valormax = partes[1]
                        valormin = partes[2]
                        nombre = " ".join(partes[3:])

                    # al string le falta todo
                    if(type(partes[1] == string)):
                        valormax = None
                        valormin = None
                        nombre = " ".join(partes[1:])
                    
                    else:

                        # al string le falta max o min
                        try:
                            
                            valormax = float(partes[1])
                        except :
                            valormax = None

                        try:      
                            valormin = float(partes[2])
                        except :
                            valormin = None
                        
                        nombre = " ".join(partes[2:])


                    # el string esta completo
                    #if(len(partes) >= 4):
                     #   try:
                      #      valormax = float(partes[1])
                       # except ValueError:
                        #    valormax = None

                        #try:
                         #   valormin = float(partes[2])
                        #except ValueError:
                         #   valormin = None
                        
                        #nombre = " ".join(partes[3:])
                    
                    
                    #temperaturas = {"tmax": valormax, "tmin":valormin, "fecha": fecha}
                    if nombre not in datos:
                        datos[nombre] = {"tmax": [], "tmin": [], "fecha":[]}
                    
                    datos[nombre]["tmax"].append(valormax)
                    datos[nombre]["tmin"].append(valormin)
                    datos[nombre]["fecha"].append(fecha)
                
    return datos