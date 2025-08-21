import string

def lectorArchivo(nombreArchivo):
    
    with open(nombreArchivo, "r", encoding="latin1") as archivo:
        lineas = archivo.readlines()
        i = 0
        listaParseada = []

        for linea in lineas:
           if(not linea.startswith("FECHA") and not linea.startswith("----")):         
              linea = linea.strip()

              linea = linea.replace(" ", "-")

              listaParseada.append(linea.strip())
              
              i = i+1

        #print(listaParseada)
    
        


    return dict(enumerate(set(lineas)))