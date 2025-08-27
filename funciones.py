
#Un reporte por estación meteorológica de la temperatura máxima y mínima registradas en el período del último año.
def maxminPorAño(datos, anio):
    
    for estacion in datos :
        max = -1000
        min = 1000
                
        for temperaturaMaxima in datos[estacion]["tmax"]:
            
            if temperaturaMaxima != None:
                if max < temperaturaMaxima:
                        max = temperaturaMaxima
                    
        for temperaturaMinima in datos[estacion]["tmin"]:
            
            if temperaturaMinima != None:
                if min > temperaturaMinima:
                    min = temperaturaMinima
                        
        print(str(estacion)+" temperatura maxima: " + str(max))
        print(str(estacion)+" temperatura minima: " + str(min))

    return 1

#La estación meteorológica que registre la mayor amplitud térmica en el mismo día, indicando el día del año que ocurrió
def estacionMayorAmplitud(datos):  
    amplitudVieja = -1000.0
    estacionMayor, fechaMayor = None, None
    
    for estacion, valores in datos.items():
        fechas = valores["fecha"]
        tmaxs = valores["tmax"]
        tmins = valores["tmin"]
    
        for fecha, tmax, tmin in zip(fechas, tmaxs, tmins):
            if tmax is not None and tmin is not None:
                amplitud = abs(tmax - tmin)

                if amplitudVieja < amplitud:
                    amplitudVieja = amplitud
                    estacionMayor = estacion
                    fechaMayor = fecha
    
    print("Estacion con mayor amplitud: " + str(estacionMayor) + "\nen la fecha de:" + str(fechaMayor))
    
    return 1

#La estación meteorológica que registre la menor amplitud térmica en el mismo día, indicando el día del año que ocurrió
def estacionMenorAmplitud(datos):
    amplitudVieja = float("inf")
    estacionMenor, fechaMenor = None, None
    
    for estacion, valores in datos.items():
        fechas = valores["fecha"]
        tmaxs = valores["tmax"]
        tmins = valores["tmin"]
    
        for fecha, tmax, tmin in zip(fechas, tmaxs, tmins):
            if tmax is not None and tmin is not None:
                amplitud = abs(tmax - tmin)

                if amplitudVieja > amplitud:
                    amplitudVieja = amplitud
                    estacionMenor = estacion
                    fechaMenor = fecha
    
    print("Estacion con menor amplitud: " + str(estacionMenor) + "\nen la fecha de:" + str(fechaMenor))
    
    return 1

#La máxima diferencia de temperatura entre minima y máxima temperatura entre dos estaciones meteorológicas en un mismo día, indicando las temperaturas y las estaciones que las registraron.
def maximaDiferenciaEstaciones():
    return 1

#La mínima diferencia de temperatura entre minima y máxima temperatura entre dos estaciones meteorológicas en un mismo día, indicando las temperaturas y las estaciones que las registraron.
def minimaDiferenciaEstaciones():
    return 1