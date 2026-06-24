from __future__ import annotations

from dataclasses import dataclass
from unicodedata import normalize


@dataclass
class Vaso:
    tipo: str
    cantidad: int
    onzas: int

    def hay_disponibles(self) -> bool:
        return self.cantidad > 0

    def retirar(self) -> None:
        if not self.hay_disponibles():
            raise ValueError("No hay vasos")
        self.cantidad -= 1


@dataclass
class Cafetera:
    onzas_cafe: int

    def tiene_cafe(self, onzas: int) -> bool:
        return self.onzas_cafe >= onzas

    def servir(self, onzas: int) -> None:
        if not self.tiene_cafe(onzas):
            raise ValueError("No hay cafe")
        self.onzas_cafe -= onzas


@dataclass
class Azucarero:
    cucharadas: int

    def tiene_azucar(self, cucharadas: int) -> bool:
        return self.cucharadas >= cucharadas

    def servir(self, cucharadas: int) -> None:
        if cucharadas < 0:
            raise ValueError("La cantidad de azucar no puede ser negativa")
        if not self.tiene_azucar(cucharadas):
            raise ValueError("No hay azucar")
        self.cucharadas -= cucharadas


class MaquinaCafe:
    MENSAJE_OK = "Cafe servido"
    MENSAJE_SIN_VASOS = "No hay vasos"
    MENSAJE_SIN_CAFE = "No hay cafe"
    MENSAJE_SIN_AZUCAR = "No hay azucar"

    def __init__(self, cafetera: Cafetera, azucarero: Azucarero, vasos: list[Vaso]):
        self.cafetera = cafetera
        self.azucarero = azucarero
        self._vasos = {_normalizar(vaso.tipo): vaso for vaso in vasos}

    def seleccionar_vaso(self, tipo: str) -> Vaso:
        try:
            return self._vasos[_normalizar(tipo)]
        except KeyError as exc:
            raise ValueError(f"Tipo de vaso no soportado: {tipo}") from exc

    def servir_cafe(self, tipo_vaso: str, cucharadas_azucar: int) -> str:
        if cucharadas_azucar < 0:
            raise ValueError("La cantidad de azucar no puede ser negativa")

        vaso = self.seleccionar_vaso(tipo_vaso)

        if not vaso.hay_disponibles():
            return self.MENSAJE_SIN_VASOS
        if not self.cafetera.tiene_cafe(vaso.onzas):
            return self.MENSAJE_SIN_CAFE
        if not self.azucarero.tiene_azucar(cucharadas_azucar):
            return self.MENSAJE_SIN_AZUCAR

        vaso.retirar()
        self.cafetera.servir(vaso.onzas)
        self.azucarero.servir(cucharadas_azucar)
        return self.MENSAJE_OK


def _normalizar(valor: str) -> str:
    sin_acentos = normalize("NFKD", valor).encode("ascii", "ignore").decode("ascii")
    return sin_acentos.strip().lower()
