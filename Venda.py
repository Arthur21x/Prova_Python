from Prova_Python.contratos import ContratoComissionado
from itertools import count


class vendasComissionadas:
    def __init__(self, mes: int, ano: int, valor: float, contrComissionado: ContratoComissionado):
        self._id = count
        self._mes = mes
        self._ano = ano
        self._valor = valor
        self._contrComissionado = contrComissionado

    @property
    def id(self):
        return self._id

    @property
    def mes(self) -> int:
        return self._mes

    @mes.setter
    def mes(self, mes) -> None:
        self._mes = mes

    @property
    def ano(self) -> int:
        return self._ano

    @ano.setter
    def ano(self, ano) -> None:
        self._ano = ano

    @property
    def valor(self) -> float:
        return self._valor

    @valor.setter
    def valor(self, valor) -> None:
        self._valor = valor

    @property
    def contrComissionado(self) -> ContratoComissionado:
        return self._contrComissionado

    @contrComissionado.setter
    def contrComissionado(self, contrato) -> None:
        self._contrComissionado = contrato
