import string

def lectorArchivo(nombreArchivo):
    datos = {}
    
    with open(nombreArchivo, "r", encoding="latin1") as archivo:
        

        for linea in archivo:
            linea = linea.strip()
            if(not linea or linea.startswith("FECHA") or linea.startswith("----")):
                 continue
           
            partes = linea.split()
            fecha = partes[0]
            valorMax, valorMin = None, None

            try:
             valorMax = float(partes[1])

            except(ValueError, IndexError):
                valorMax = None

            try:
                valorMin = float(partes[1])

            except(ValueError, IndexError):
                valorMin = None

            if(valorMax is not None and valorMin is not None):
                nombre = " ".join(partes[3:])
            elif(valorMax is not None):
                nombre = " ".join(partes[2:])
            else:
                nombre = " ".join(partes[1:])
            
            
            if nombre not in datos:
                datos[nombre] = {"tmax": [], "tmin": [], "fecha":[]}
            
            datos[nombre]["tmax"].append(valorMax)
            datos[nombre]["tmin"].append(valorMin)
            datos[nombre]["fecha"].append(fecha)
                
    return datos