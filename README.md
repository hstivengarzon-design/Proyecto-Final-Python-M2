# Proyecto Final - Python

## Descripción

Este proyecto consiste en un programa desarrollado en Python que reúne dos ejercicios prácticos mediante un menú principal.

El programa permite:

* Validar la longitud de una palabra.
* Determinar el cuadrante de un punto según sus coordenadas.
* Registrar las palabras ingresadas durante la sesión.
* Validar los datos ingresados por el usuario.

El proyecto fue realizado como parte del proceso de aprendizaje de los fundamentos de Python.

---

## Menú principal

Al ejecutar el programa se muestra el siguiente menú:

```text
==================================================
       PROYECTO FINAL - PYTHON
==================================================
1. Validar longitud de una palabra
2. Determinar cuadrante
3. Salir
```

El usuario puede seleccionar una de las tres opciones.

---

## 1. Validar longitud de una palabra

Esta opción solicita al usuario una palabra que tenga entre **4 y 8 letras**.

El programa utiliza la función `len()` para conocer la cantidad de caracteres ingresados.

### Funcionamiento

* Si la palabra tiene menos de 4 letras, muestra un mensaje de error.
* Si tiene más de 8 letras, muestra un mensaje de error.
* Si tiene entre 4 y 8 letras, la palabra es aceptada.
* El usuario puede volver a intentarlo hasta ingresar una palabra válida.

Además, se utiliza una **lista** para almacenar todas las palabras que el usuario haya intentado ingresar durante la sesión.

```python
palabras_intentadas = []
```

Cada intento se agrega utilizando:

```python
palabras_intentadas.append(palabra)
```

Al finalizar correctamente el reto, se muestra el registro de palabras ingresadas.

---

## 2. Determinar cuadrante

Esta opción permite ingresar las coordenadas **X** y **Y** de un punto.

El programa determina en qué cuadrante se encuentra el punto dependiendo de si las coordenadas son positivas o negativas.

### Cuadrantes

| Coordenada X | Coordenada Y | Resultado     |
| ------------ | ------------ | ------------- |
| Positiva     | Positiva     | Cuadrante I   |
| Negativa     | Positiva     | Cuadrante II  |
| Negativa     | Negativa     | Cuadrante III |
| Positiva     | Negativa     | Cuadrante IV  |

El programa no permite utilizar `0` como coordenada.

### Tupla de cuadrantes

Los nombres de los cuadrantes se almacenan en una **tupla**:

```python
cuadrantes = (
    "Cuadrante I",
    "Cuadrante II",
    "Cuadrante III",
    "Cuadrante IV"
)
```

Se utiliza una tupla porque estos nombres no necesitan modificarse durante la ejecución del programa.

Para mostrar el cuadrante correspondiente se utilizan los índices de la tupla:

```python
cuadrantes[0]
cuadrantes[1]
cuadrantes[2]
cuadrantes[3]
```

---

## Validación de datos

El programa cuenta con diferentes validaciones para evitar errores durante su ejecución.

### Coordenadas diferentes de cero

El programa verifica que ninguna de las coordenadas sea `0`.

Si el usuario ingresa `0`, se muestra un mensaje de error y se solicitan nuevamente los datos.

### Números enteros

Para las coordenadas se utiliza `int()`.

Si el usuario ingresa un valor que no puede convertirse en un número entero, se utiliza `try` y `except ValueError` para controlar el error.

### Uso de `continue`

El programa utiliza `continue` para regresar al comienzo del ciclo cuando se encuentra un dato incorrecto y permitir que el usuario vuelva a intentarlo.

### Uso de `break`

Se utiliza `break` cuando el usuario selecciona la opción **3. Salir**, permitiendo finalizar el ciclo principal y terminar el programa.

---

## Colecciones utilizadas

En este proyecto se utilizan dos tipos de colecciones de Python.

### Lista

La lista `palabras_intentadas` almacena todas las palabras ingresadas por el usuario durante la sesión.

```python
palabras_intentadas = []
```

Las listas permiten agregar nuevos elementos mientras el programa está funcionando.

### Tupla

La tupla `cuadrantes` almacena los nombres de los cuatro cuadrantes.

```python
cuadrantes = (
    "Cuadrante I",
    "Cuadrante II",
    "Cuadrante III",
    "Cuadrante IV"
)
```

A diferencia de una lista, una tupla se utiliza para mantener estos datos sin modificarlos durante la ejecución.

---

## Estructuras de programación utilizadas

Durante el desarrollo del proyecto se aplicaron diferentes conceptos básicos de Python:

* Variables.
* Listas.
* Tuplas.
* Condicionales `if`, `elif` y `else`.
* Ciclos `while`.
* `input()` para recibir información del usuario.
* `int()` para convertir datos a números enteros.
* `len()` para conocer la longitud de una palabra.
* `try` y `except` para controlar errores.
* `continue` para repetir una parte del ciclo.
* `break` para finalizar el programa.
* Operadores de comparación.
* Operadores lógicos.

---

## Tecnologías utilizadas

* **Lenguaje:** Python
* **Editor:** Visual Studio Code
* **Control de versiones:** Git
* **Repositorio:** GitHub

---

## Estructura del proyecto

```text
Proyecto Final Python/
│
├── HAROLD_GARZON_proyectoM2.py
└── README.md
```

---

## Cómo ejecutar el programa

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir una terminal.
4. Ejecutar el siguiente comando:

```bash
python HAROLD_GARZON_proyectoM2.py
```

5. Seleccionar una opción del menú.
6. Seguir las instrucciones que aparecen en pantalla.

---

## Objetivo del proyecto

El objetivo de este proyecto es aplicar los conocimientos aprendidos sobre los fundamentos de Python mediante ejercicios prácticos.

Se busca utilizar diferentes estructuras de programación para crear un programa interactivo capaz de recibir información, validarla, procesarla y mostrar un resultado al usuario.

---

## Autor

**Harold Garzon**

Proyecto realizado como parte del proceso de aprendizaje de Python.
