import string

def leerArchivo(nombreArchivo):
    datos = {}
    
    with open(nombreArchivo, "r", encoding="latin1") as archivo:
        
        for linea in archivo:
            linea = linea.strip()
            
            #entrar omitiendo las primeras lineas
            if(not linea or linea.startswith("FECHA") or linea.startswith("----")):
                 continue
           
            #asignar fecha
            fecha = linea[0:8]
            valorMax, valorMin = None, None

            #intentar ingresar el valor de maximo
            try:
             valorMax = float(linea[10:14].strip())

            except(ValueError, IndexError):
                valorMax = None

            #intentar ingresar el valor de minimo
            try:
                valorMin = float(linea[16:20].strip())

            except(ValueError, IndexError):
                valorMin = None

            #asignar nombre
            nombre = " ".join(linea[21:].split())
            
            #si no hay datos inicializar el diccionario igual
            if nombre not in datos:
                datos[nombre] = {"tmax": [], "tmin": [], "fecha":[]}
            
            #meter datos dentro del diccionario
            datos[nombre]["tmax"].append(valorMax)
            datos[nombre]["tmin"].append(valorMin)
            datos[nombre]["fecha"].append(fecha)
                
    return datos

def escribirArchivo(resultados):
    
    with open("resultados.txt", "w", encoding="latin1") as archivo:
        
       
       
       
       
       archivo.write(str(resultados)+"\n")
        
    return 1