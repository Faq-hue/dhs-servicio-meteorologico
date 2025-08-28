# dhs-servicio-meteorologico
Dessarrollo de Herramientas de Software — Trabajo Práctico
Maximiliano A. Eschoyez
Fecha de Entrega: Lunes 1 de Septiembre de 2025

## Resumen
El objetivo de este Trabajo Práctico es implementar lo visto en clases sobre el uso de colecciones en Python3.
El programa a desarrollar para esta etapa tiene como objetivo tomar un archivo de texto con las temperaturas máximas y mínimas del país y realizar diferentes análisis sobre los datos.

## Consigna
Dado un archivo de entrada con temperaturas máximas y mínimas de los últimos 365 días para diferentes estaciones meteorológicas del Servicio Meteorológico Nacional (SMN) se debe construir un programa en Python3 que gestione esos datos. El programa debe leer los datos del archivo y colocarlos en un diccionario cuyas claves son los nombres de las estaciones meteorológicas. El valor asociado a cada clave debe ser otro diccionario con claves tmax y tmin que mapean con una lista de temperaturas. Durante la lectura, si no se encuentra registrada una temperatura, se la almacenará con el valor None.
Por ejemplo, para acceder a la temperatura mínima de tres días atrás usar datos["CORDOBA OBSERVATORIO"]["tmin"][-3]
El programa deberá reportar en un archivo de texto lo siguiente:
- Un reporte por estación meteorológica de la temperatura máxima y mínima registradas en el período del último año.
- La estación meteorológica que registre la mayor amplitud térmica en el mismo día, indicando el día del año que ocurrió
- La estación meteorológica que registre la menor amplitud térmica en el mismo día, indicando el día del año que ocurrió
- La máxima diferencia de temperatura entre minima y máxima temperatura entre dos estaciones meteorológicas en un mismo día, indicando las temperaturas y las estaciones que las registraron.
- La mínima diferencia de temperatura entre minima y máxima temperatura entre dos estaciones meteorológicas en un mismo día, indicando las temperaturas y las estaciones que las registraron.
