"""Principales Reglas de PEP 8

    Formato y Espaciado
        Usa 4 espacios por nivel de indentación (no tabulaciones).
        Mantén líneas de código con máximo 79 caracteres.
        Usa líneas en blanco entre clases y funciones.

    Nombres de Variables y Funciones
        Funciones y variables: snake_case → mi_funcion(), variable_ejemplo.
        Clases: CamelCase → MiClaseEjemplo.
        Constantes: MAYUSCULAS → VALOR_PI = 3.1416.
        Evita usar nombres de variables como l, O, I (pueden confundirse con números).

    Importaciones
        Cada importación en una línea
        Usa imports agrupados en este orden:
            Librerías estándar de Python
            Librerías externas (Django, NumPy, etc.)
            Módulos propios
            
    Espaciado dentro del código
        Usa un solo espacio alrededor de operadores:       
        Evita espacios extra dentro de paréntesis y corchetes

    Comentarios y Docstrings
        Usa # para comentarios cortos:        
        Usa docstrings (""" """) en funciones y clases  """

#Ejemplo Básico: Corrección de estilo

#❌ Mal Código (No sigue PEP 8): Formato

def suma (a,b):return a+b

#✅ Buen Código (Sigue PEP 8):

def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b

#Ejemplo Intermedio: Formateo adecuado

#❌ Mal Código (Mala estructura, mal espaciado, imports desordenados):

import os,sys
def multiplicar(a,b): return a*b
print(multiplicar(3,5))

#✅ Buen Código (Bien estructurado):

import os  
import sys  

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

if __name__ == "__main__":
    print(multiplicar(3, 5))

#Ejemplo Complejo: Organización de un proyecto

#🎯 Cómo organizar módulos correctamente siguiendo PEP 8.

#mi_proyecto/
#│── main.py
#│── calculadora.py
#│── tests/
#│   ├── test_calculadora.py

#✅ Ejemplo de calculadora.py con PEP 8 aplicado:

class Calculadora:
    """Calculadora básica con operaciones matemáticas."""
    
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b