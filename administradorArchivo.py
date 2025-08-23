import string

def leerArchivo(nombreArchivo):
    datos = {}
    
    with open(nombreArchivo, "r", encoding="latin1") as archivo:
        

        for linea in archivo:
            linea = linea.strip()
            #entrar omitiendo las primeras lineas
            if(not linea or linea.startswith("FECHA") or linea.startswith("----")):
                 continue
           
            partes = linea.split()
            fecha = partes[0]
            valorMax, valorMin = None, None

            #intentar ingresar los valores de maximo y minimo
            try:
             valorMax = float(partes[1])

            except(ValueError, IndexError):
                valorMax = None

            try:
                valorMin = float(partes[1])

            except(ValueError, IndexError):
                valorMin = None

            #caso: no hay minimo ni maximo
            if(valorMax is not None and valorMin is not None):
                nombre = " ".join(partes[3:])
            #caso: no hay maximo
            elif(valorMax is not None):
                nombre = " ".join(partes[2:])
            #caso: no hay minimo
            else:
                nombre = " ".join(partes[1:])
            
            
            #si no hay datos inicializar el diccionario igual
            if nombre not in datos:
                datos[nombre] = {"tmax": [], "tmin": [], "fecha":[]}
            
            #meter datos dentro del diccionario
            datos[nombre]["tmax"].append(valorMax)
            datos[nombre]["tmin"].append(valorMin)
            datos[nombre]["fecha"].append(fecha)
                
    return datos

def escribirArchivo():
    return 1