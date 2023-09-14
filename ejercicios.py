from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False


class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.__elementos = []
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @propert
    def id(self):
        return self.__id

    def contiene(self, elemento):
        for e in self.__elementos:
            if e == elemento:
                return True
        return False

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.__elementos.append(elemento)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        for elemento in self.__elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        for elemento in otro_conjunto.__elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nombre_resultado = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        elementos_interseccion = [elemento for elemento in conjunto1.__elementos if conjunto2.contiene(elemento)]
        nuevo_conjunto = cls(nombre_resultado)
        nuevo_conjunto.__elementos = elementos_interseccion
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ", ".join([elemento.nombre for elemento in self.__elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"


