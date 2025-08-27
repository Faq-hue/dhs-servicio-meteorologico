
#Un reporte por estación meteorológica de la temperatura máxima y mínima registradas en el período del último año.
def maxminPorAño(datos, anio):
    resultados = {}

    for estacion, registros in datos.items():
        #filtramos por año
        if "fechas" in registros:
            tmaxFiltrado = [
                t for t, f in zip(registros["tmax"], registros["fechas"])
                if f.year == anio and t is not None
            ]
            tminFiltrado = [
                t for t, f in zip(registros["tmin"], registros["fechas"])
                if f.year == anio and t is not None
            ]
        else:
            #si no hay fechas, usamos todo
            tmaxFiltrado = [t for t in registros["tmax"] if t is not None]
            tminFiltrado = [t for t in registros["tmin"] if t is not None]

        if tmaxFiltrado and tminFiltrado:
            tmaxReg = max(tmaxFiltrado)
            tminReg = min(tminFiltrado)

            resultados[estacion] = {
                "tmax": tmaxReg,
                "tmin": tminReg
            }

            print(f"{estacion}: tmax={tmaxReg}, tmin={tminReg}")
        else:
            print(f"{estacion}: sin datos válidos en {anio}")

    return resultados


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
def maximaDiferenciaEstaciones(datos):
    # Tomamos las fechas de la primera estación como referencia
    primeraEstacion = next(iter(datos))
    fechas = datos[primeraEstacion]["fecha"]

    mayorDiferencia = float("-inf")
    mayorFecha = None
    estacionTmax = None
    estacionTmin = None
    valorTmax = None
    valorTmin = None

    for i, fechaActual in enumerate(fechas):
        tmaxDelDia = float("-inf")
        estacionMax = ""
        tminDelDia = float("inf")
        estacionMin = ""

        # Recorremos todas las estaciones
        for estacion, registros in datos.items():
            # ⚠️ Chequeamos que el índice exista en ambas listas
            if i < len(registros["tmax"]) and i < len(registros["tmin"]):
                tmaxi = registros["tmax"][i]
                tmini = registros["tmin"][i]

                if tmaxi is not None and tmaxi > tmaxDelDia:
                    tmaxDelDia = tmaxi
                    estacionMax = estacion

                if tmini is not None and tmini < tminDelDia:
                    tminDelDia = tmini
                    estacionMin = estacion

        # Solo calculamos si encontramos valores válidos
        if estacionMax and estacionMin:
            diferencia = tmaxDelDia - tminDelDia

            if diferencia > mayorDiferencia:
                mayorDiferencia = diferencia
                mayorFecha = fechaActual
                estacionTmax = estacionMax
                estacionTmin = estacionMin
                valorTmax = tmaxDelDia
                valorTmin = tminDelDia

    print("Fecha:", mayorFecha)
    print("Mayor diferencia:", mayorDiferencia, "°C")
    print(f"Tmax: {valorTmax} °C ({estacionTmax})")
    print(f"Tmin: {valorTmin} °C ({estacionTmin})")

    return 1


#La mínima diferencia de temperatura entre minima y máxima temperatura entre dos estaciones meteorológicas en un mismo día, indicando las temperaturas y las estaciones que las registraron.
def minimaDiferenciaEstaciones(datos):
    
    # Tomamos las fechas de la primera estación como referencia
    primeraEstacion = next(iter(datos))
    fechas = datos[primeraEstacion]["fecha"]

    menorDiferencia = float("inf")
    menorFecha = None
    estacionTmax = None
    estacionTmin = None
    valorTmax = None
    valorTmin = None

    for i, fechaActual in enumerate(fechas):
        tmaxDelDia = float("-inf")
        estacionMax = ""
        tminDelDia = float("inf")
        estacionMin = ""

        # Recorremos todas las estaciones
        for estacion, registros in datos.items():
            # ⚠️ Chequeamos que el índice exista en ambas listas
            if i < len(registros["tmax"]) and i < len(registros["tmin"]):
                tmaxi = registros["tmax"][i]
                tmini = registros["tmin"][i]

                if tmaxi is not None and tmaxi > tmaxDelDia:
                    tmaxDelDia = tmaxi
                    estacionMax = estacion

                if tmini is not None and tmini < tminDelDia:
                    tminDelDia = tmini
                    estacionMin = estacion

        # Solo calculamos si encontramos valores válidos
        if estacionMax and estacionMin:
            diferencia = tmaxDelDia - tminDelDia

            if diferencia < menorDiferencia:
                menorDiferencia = diferencia
                menorFecha = fechaActual
                estacionTmax = estacionMax
                estacionTmin = estacionMin
                valorTmax = tmaxDelDia
                valorTmin = tminDelDia

    print("Fecha:", menorFecha)
    print("Mayor diferencia:", menorDiferencia, "°C")
    print(f"Tmax: {valorTmax} °C ({estacionTmax})")
    print(f"Tmin: {valorTmin} °C ({estacionTmin})")

    return 1