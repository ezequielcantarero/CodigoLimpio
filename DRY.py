"""3. DRY - No Repetir Código
Ejemplo Básico: Evitar código duplicado

❌ Mal Código (Código repetido en funciones similares):"""
def area_rectangulo(base, altura):
    return base * altura

def area_cuadrado(lado):
    return lado * lado

"""✅ Buen Código (Función reutilizable):"""
def calcular_area(forma, *args):
    if forma == "rectangulo":
        return args[0] * args[1]
    elif forma == "cuadrado":
        return args[0] ** 2


"""Ejemplo Intermedio: Uso de Clases para evitar duplicación

🎯 Refactorización de funciones repetitivas en una clase genérica.
❌ Mal Código (Múltiples funciones que repiten lógica de validación):"""
def validar_email(email):
    if "@" not in email:
        raise ValueError("Email inválido")
    return True

def validar_usuario(usuario):
    if len(usuario) < 3:
        raise ValueError("Usuario muy corto")
    return True

"""✅ Buen Código (Uso de una clase para reutilizar lógica de validación):"""
class Validador:
    @staticmethod
    def validar_email(email):
        if "@" not in email:
            raise ValueError("Email inválido")
        return True

    @staticmethod
    def validar_usuario(usuario):
        if len(usuario) < 3:
            raise ValueError("Usuario muy corto")
        return True


"""Ejemplo Complejo: DRY con Patrones de Diseño

🎯 Evitar código duplicado usando el patrón Factory para la creación de objetos.
❌ Mal Código (Múltiples clases que crean objetos de manera manual y repetitiva):"""
class PDF:
    def generar(self):
        return "Generando PDF"

class Excel:
    def generar(self):
        return "Generando Excel"

class Reporte:
    def generar_reporte(self, tipo):
        if tipo == "PDF":
            return PDF().generar()
        elif tipo == "Excel":
            return Excel().generar()

"""✅ Buen Código (Uso del patrón Factory para evitar repeticiones innecesarias):"""
class ReporteFactory:
    @staticmethod
    def crear_reporte(tipo):
        reportes = {
            "PDF": PDF,
            "Excel": Excel
        }
        return reportes[tipo]().generar()


"""
NOTA 1
Qué es staticmethod y cómo se usa?

En Python, @staticmethod es un decorador que define un método estático dentro de una clase.

📌 Características clave de @staticmethod:
✅ No requiere self ni cls como primer argumento.
✅ Se puede llamar sin necesidad de instanciar la clase.
✅ Útil para métodos auxiliares que no dependen de atributos de instancia o clase.


Ejemplo 1: Uso Básico

✅ Método sin staticmethod (Requiere instanciar la clase)"""
class Matematica:
    def sumar(a, b):  # ⚠ Falta self
        return a + b

print(Matematica.sumar(2, 3))  # ❌ Error: faltan argumentos

"""✅ Con staticmethod (Se puede llamar sin crear instancia)"""
class Matematica:
    @staticmethod
    def sumar(a, b):
        return a + b

print(Matematica.sumar(2, 3))  # ✅ Output: 5


"""Ejemplo 2: Métodos Auxiliares dentro de una Clase

✅ Método estático como función de utilidad"""
class Utilidades:
    @staticmethod
    def es_par(numero):
        return numero % 2 == 0

print(Utilidades.es_par(10))  # ✅ Output: True
print(Utilidades.es_par(7))   # ✅ Output: False

"""Ejemplo 3: Comparación con Métodos de Instancia y Clase
Tipo de Método	                Requiere Instancia	Requiere Clase	Accede a self	Accede a cls
Método de Instancia	            ✅ Sí	            ❌ No	    ✅ Sí	        ❌ No
Método de Clase (@classmethod)	❌ No	            ✅ Sí	    ❌ No	        ✅ Sí
Método Estático (@staticmethod)	❌ No	            ❌ No	    ❌ No	        ❌ No

🔹 Ejemplo con los tres tipos:"""
class Ejemplo:
    def metodo_instancia(self):
        return "Método de instancia"

    @classmethod
    def metodo_clase(cls):
        return "Método de clase"

    @staticmethod
    def metodo_estatico():
        return "Método estático"

obj = Ejemplo()
print(obj.metodo_instancia())  # ✅ Se llama desde una instancia
print(Ejemplo.metodo_clase())  # ✅ Se llama desde la clase
print(Ejemplo.metodo_estatico())  # ✅ Se llama sin instanciar

"""Ejemplo 3: Comparación entre Métodos Normales, classmethod y staticmethod"""
class Ejemplo:
    atributo_clase = "Soy un atributo de clase"

    def metodo_normal(self):
        return f"Accediendo a: {self.atributo_clase}"

    @classmethod
    def metodo_de_clase(cls):
        return f"Accediendo a través de la clase: {cls.atributo_clase}"

    @staticmethod
    def metodo_estatico():
        return "No necesito acceso a la instancia ni a la clase"

# Instanciamos la clase
e = Ejemplo()

# Métodos normales requieren una instancia
print(e.metodo_normal())   # ✅ Accediendo a: Soy un atributo de clase

# Métodos de clase pueden ser llamados desde la clase o instancia
print(Ejemplo.metodo_de_clase())  # ✅ Accediendo a través de la clase: Soy un atributo de clase

# Métodos estáticos pueden llamarse desde la clase directamente
print(Ejemplo.metodo_estatico())  # ✅ No necesito acceso a la instancia ni a la clase

"""
Método normal (self): Usa atributos de la instancia.
Método de clase (cls): Usa atributos de la clase.
Método estático: No usa ni self ni cls, solo realiza una operación independiente."""


"""Ejemplo 4: Uso en Validaciones

✅ Casos de uso: Un staticmethod es útil cuando queremos una función que no dependa de la instancia."""
class Validador:
    @staticmethod
    def es_numero_entero(valor):
        return isinstance(valor, int)

# No necesitamos instanciar la clase
print(Validador.es_numero_entero(5))  # ✅ Output: True
print(Validador.es_numero_entero("Hola"))  # ✅ Output: False


"""Ejemplo 5: Uso en Formateo de Fechas

✅ Un staticmethod en una clase de utilidad que formatea fechas."""
from datetime import datetime

class FormatoFecha:
    @staticmethod
    def obtener_fecha_actual():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(FormatoFecha.obtener_fecha_actual())  # ✅ Output: "2025-02-28 10:30:45"

"""Ejemplo 6: Uso en Conversión de Unidades

✅ Cuando una clase ofrece funciones matemáticas generales."""
class Conversor:
    @staticmethod
    def celsius_a_fahrenheit(celsius):
        return (celsius * 9/5) + 32

print(Conversor.celsius_a_fahrenheit(25))  # ✅ Output: 77.0

"""¿Cuándo usar staticmethod?

✅ Cuando el método no necesita acceder a self (atributos de instancia) ni a cls (atributos de clase).
✅ Cuando queremos organizar funciones relacionadas dentro de una clase, sin forzar la creación de instancias.
✅ Para crear utilidades y funciones auxiliares dentro de una clase.

Resumen
Tipo de Método	Necesita self	Necesita cls	Puede llamarse sin instanciar
Método Normal	✅ Sí	❌ No	❌ No
Método de Clase (@classmethod)	❌ No	✅ Sí	✅ Sí
Método Estático (@staticmethod)	❌ No	❌ No	✅ Sí

📌 Conclusión: Usa staticmethod cuando una función está relacionada con la clase, pero no necesita acceso a la instancia ni a la clase."""




"""
NOTA 2

Tipos de Métodos en Python (Resumen)

En Python, existen tres tipos de métodos en una clase:

    Método de Instancia (Normal)
    Método de Clase (@classmethod)
    Método Estático (@staticmethod)

Tipo de Método	Requiere self	Requiere cls	Se puede llamar sin instanciar
Método de Instancia	✅ Sí	❌ No	❌ No
Método de Clase (@classmethod)	❌ No	✅ Sí	✅ Sí
Método Estático (@staticmethod)	❌ No	❌ No	✅ Sí

1️⃣ Método de Instancia (Normal)

✅ Se usa para trabajar con atributos y métodos de la instancia.
✅ Tiene acceso a self.
"""
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre  # Atributo de instancia

    def saludar(self):  # Método normal
        return f"Hola, soy {self.nombre}"

p = Persona("Juan")
print(p.saludar())  # ✅ Output: "Hola, soy Juan"

"""🔹 Caso de uso: Cuando el método necesita acceder o modificar atributos de una instancia específica.

2️⃣ Método de Clase (@classmethod)

✅ Se usa cuando queremos trabajar con atributos o métodos de la clase, no de la instancia.
✅ Usa cls en lugar de self.
✅ Se puede llamar sin instanciar la clase.
"""
class Persona:
    cantidad_personas = 0  # Atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre
        Persona.cantidad_personas += 1

    @classmethod
    def obtener_total(cls):  # Método de clase
        return f"Total de personas: {cls.cantidad_personas}"

print(Persona.obtener_total())  # ✅ Output: "Total de personas: 0"

p1 = Persona("Ana")
p2 = Persona("Luis")

print(Persona.obtener_total())  # ✅ Output: "Total de personas: 2"

"""🔹 Caso de uso: Cuando queremos trabajar con atributos compartidos por todas las instancias.

3️⃣ Método Estático (@staticmethod)

✅ No usa self ni cls, por lo que no accede a atributos de instancia ni de clase.
✅ Se usa cuando el método es relevante para la clase pero no necesita acceder a datos de la instancia o la clase.
✅ Se puede llamar sin instanciar la clase.
"""
class Calculadora:
    @staticmethod
    def sumar(a, b):  # No necesita self ni cls
        return a + b

print(Calculadora.sumar(3, 5))  # ✅ Output: 8

"""    🔹 Caso de uso: Métodos que realizan operaciones independientes de la clase.

📌 Resumen Final

🔹 Método Normal: Usa self, trabaja con la instancia.
🔹 Método de Clase (@classmethod): Usa cls, trabaja con atributos de la clase.
🔹 Método Estático (@staticmethod): No usa self ni cls, es independiente."""