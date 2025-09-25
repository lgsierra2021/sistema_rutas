# 🚍Sistema Inteligente de Rutas en Transporte Masivo  

Este proyecto implementa un **sistema inteligente basado en conocimiento**, que permite calcular la mejor ruta entre dos estaciones en un sistema de transporte masivo local.  
El conocimiento se representa con **reglas lógicas** y se utiliza el algoritmo de **Dijkstra** para la búsqueda de la ruta más corta.  

---

## Objetivo
Desarrollar un sistema que, a partir de una base de conocimiento escrita en reglas lógicas, encuentre la mejor ruta desde un punto de origen **A** hasta un destino **B**, aplicando estrategias de **búsqueda heurística**.

---

## Representación del Conocimiento
El conocimiento se guarda como una lista de conexiones entre estaciones:  

(A, B, 5)
(A, C, 2)
(B, D, 4)
(C, D, 7)
(C, E, 3)
(D, F, 1)
(E, F, 5)

Cada tupla representa:
(Estación Origen, Estación Destino, Costo del trayecto)

---

## Tecnologías utilizadas
- **Lenguaje**: Python 3  
- **Algoritmo**: Dijkstra (búsqueda del camino más corto)  
- **Control de versiones**: Git + GitHub  
- **Documentación**: PDF + video  

---

## Ejecutar el archivo principal:

python ruta.py

---

## Ejemplo de salida

Mejor ruta de A a F: A -> B -> D -> F Costo total: 10

---

## Enlace del video 
https://drive.google.com/drive/folders/1vwTU3B1yt0r9DnMyRJsD2a4J2HAPPS-4?usp=sharing 

## Autor 

**Luis Gabriel Sierra Alarcon**



