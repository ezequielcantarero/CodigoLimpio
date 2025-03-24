"""Principios SOLID

Los principios SOLID son un conjunto de reglas para el diseño de software orientado a objetos, promoviendo código flexible y fácil de mantener.
1. Single Responsibility Principle (SRP) - Responsabilidad Única

Cada clase o función debe tener una sola responsabilidad.

❌ Mal Ejemplo (Múltiples responsabilidades):"""
class Reporte:
    def generar_pdf(self):
        pass  # Genera el PDF del reporte
    
    def guardar_en_db(self):
        pass  # Guarda el reporte en la base de datos

"""✅ Buen Ejemplo (Separa responsabilidades en clases distintas):"""
class Reporte:
    def generar_contenido(self):
        pass  # Genera el contenido del reporte

class ReportePDF:
    def generar_pdf(self, reporte):
        pass  # Convierte el reporte a PDF

class ReporteDB:
    def guardar_en_db(self, reporte):
        pass  # Guarda el reporte en la base de datos

"""2. Open/Closed Principle (OCP) - Abierto/Cerrado

Las clases deben estar abiertas para extensión, pero cerradas para modificación.

❌ Mal Ejemplo (Modifica código existente para agregar nueva funcionalidad):"""
class Calculadora:
    def operar(self, a, b, operacion):
        if operacion == "suma":
            return a + b
        elif operacion == "resta":
            return a - b

"""✅ Buen Ejemplo (Usa polimorfismo para extender funcionalidades sin modificar código existente):"""
from abc import ABC, abstractmethod

class Operacion(ABC):
    @abstractmethod
    def calcular(self, a, b):
        pass

class Suma(Operacion):
    def calcular(self, a, b):
        return a + b

class Resta(Operacion):
    def calcular(self, a, b):
        return a - b


"""
NOTA 1
Uso Básico de abstractmethod

Para usar abstractmethod, seguimos estos pasos:

    Importar ABC y abstractmethod desde abc.
    Crear una clase base abstracta, heredando de ABC.
    Definir métodos abstractos con @abstractmethod (sin implementación).
    Las subclases deben implementar esos métodos o Python lanzará un error.

Ejemplo 1: Uso Básico

❌ Sin abstractmethod (No obliga a implementar el método en la subclase)
"""
class Animal:
    def hacer_sonido(self):
        pass  # No obliga a implementarlo

class Perro(Animal):
    pass  # No define hacer_sonido() y no da error

p = Perro()
print(p.hacer_sonido())  # No genera error, pero es incorrecto

"""✅ Con abstractmethod (Obliga a implementar el método en la subclase)"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass  # Método obligatorio en subclases

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau Guau"

p = Perro()
print(p.hacer_sonido())  # ✅ Output: "Guau Guau"


"""Ejemplo 2: Implementando una Jerarquía de Figuras

✅ Clase abstracta para definir un método obligatorio calcular_area()
"""
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

# Crear instancias y calcular área
c = Circulo(5)
r = Rectangulo(4, 6)

print(c.calcular_area())  # ✅ Output: 78.54
print(r.calcular_area())  # ✅ Output: 24

"""
Ejemplo 3: Métodos Abstractos con Implementación

🔹 A veces, queremos que un método abstracto tenga una implementación base que las subclases puedan reutilizar."""
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca):
        self.marca = marca

    @abstractmethod
    def describir(self):
        print(f"Este vehículo es un {self.marca}")  # Implementación base

class Auto(Vehiculo):
    def describir(self):
        super().describir()  # Usa la implementación base
        print("Es un auto con 4 ruedas.")

coche = Auto("Toyota")
coche.describir()

"""✅ Output:

Este vehículo es un Toyota  
Es un auto con 4 ruedas.

    🔹 Ventaja: Podemos proporcionar una implementación base que las subclases pueden extender."""


"""Ejemplo 4: Clases Abstractas con Propiedades

Podemos definir propiedades abstractas con @property para que las subclases deban implementarlas."""
from abc import ABC, abstractmethod

class Persona(ABC):
    @property
    @abstractmethod
    def profesion(self):
        pass

class Doctor(Persona):
    @property
    def profesion(self):
        return "Médico"

d = Doctor()
print(d.profesion)  # ✅ Output: "Médico"

"""Conclusión
✅ abstractmethod garantiza que las subclases implementen métodos esenciales.
✅ Ayuda a mantener un diseño estructurado y evita errores por métodos olvidados.
✅ Puede combinarse con @property y super() para más flexibilidad."""


"""
Ejemplo Complejo: Dependency Inversion Principle (DIP)

🎯 Evitar dependencia directa en implementaciones específicas.
❌ Mal Código (La clase depende de una implementación específica, no de una abstracción):"""
class MySQLDatabase:
    def conectar(self):
        return "Conectado a MySQL"

class Usuario:
    def __init__(self):
        self.db = MySQLDatabase()

"""✅ Buen Código (Uso de interfaces para desacoplar dependencias):"""
class Database:
    def conectar(self):
        pass

class MySQLDatabase(Database):
    def conectar(self):
        return "Conectado a MySQL"

class Usuario:
    def __init__(self, db: Database):
        self.db = db
