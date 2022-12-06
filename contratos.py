from abc import ABC, abstractmethod
from datetime import datetime
from Curso_Udemy.aula75.Prova_Python.colaborador import Colaborador
from itertools import count


class Contrato(ABC):
    def __init__(self, dia: int, mes: int, ano: int, colaborador: Colaborador, ativo: bool = False) -> None:
        self._ativo = ativo
        self._colaborador = colaborador
        self._dataEncerramento = None
        self._dataInicio = datetime(dia, mes, ano)
        self._id = count()

    @property
    def id(self):
        return self._id

    @property
    def dataInicio(self) -> datetime:
        return self._dataInicio

    @dataInicio.setter
    def dataInicio(self, dataInicio: str) -> None:
        self._dataInicio = datetime.strptime(dataInicio, "%Y-%m-%d")

    @property
    def dataEncerramento(self) -> datetime:
        return self._dataEncerramento

    @dataEncerramento.setter
    def dataEncerramento(self, dataEncerramento: str) -> None:
        self._dataEncerramento = datetime.strptime(dataEncerramento, "%Y-%m-%d")

    @property
    def colaborador(self) -> Colaborador:
        return self._colaborador

    @colaborador.setter
    def colaborador(self, colaborador: Colaborador) -> None:
        self._colaborador = colaborador

    @property
    def ativo(self) -> bool:
        return self._ativo

    @ativo.setter
    def ativo(self, status: bool) -> None:
        self._ativo = status

    def EncerrarContrato(self):
        hoje = datetime.today().day
        dif = abs((hoje - self.dataInicio.day))
        if dif > 0:
            self.ativo = False

    @abstractmethod
    def calcVencimento(self) -> float:
        pass


class ContratoAssalariado(Contrato):
    def __init__(self, dia: int, mes: int, ano: int, colaborador: Colaborador
                 , salarioMensal: float, percInsalubridade: float = 0,
                 percPericulosidade: float = 0) -> None:
        super().__init__(dia, mes, ano, colaborador)
        self._salarioMensal = salarioMensal
        self._percInsalubridade = percInsalubridade
        self._percPericulosidade = percPericulosidade

    @property
    def salarioMensal(self) -> float:
        return self._salarioMensal

    @salarioMensal.setter
    def salarioMensal(self, salario) -> None:
        self._salarioMensal = salario

    @property
    def percInsalubridade(self) -> float:
        return self._percInsalubridade

    @percInsalubridade.setter
    def percInsalubridade(self, perc) -> None:
        self._percInsalubridade = perc

    @property
    def perPericulosidade(self) -> float:
        return self._percPericulosidade

    @perPericulosidade.setter
    def perPericulosidade(self, perc) -> None:
        self._percPericulosidade = perc

    def calcVencimento(self) -> float:
        venc = (self.salarioMensal * (2 / 100))
        if 25 <= venc <= 125:
            return venc


class ContratoComissionado(Contrato):
    def __init__(self, dia: int, mes: int, ano: int, colaborador: Colaborador,
                 perComissao: float, ajudaCusto: float) -> None:
        super().__init__(dia, mes, ano, colaborador)
        self._perComissao = perComissao
        self._ajudaCusto = ajudaCusto

    @property
    def perComissao(self) -> float:
        return self._perComissao

    @perComissao.setter
    def perComissao(self, perc) -> None:
        self._perComissao = perc

    @property
    def ajudaCusto(self) -> float:
        return self._ajudaCusto

    @ajudaCusto.setter
    def ajudaCusto(self, ajuda) -> None:
        self._ajudaCusto = ajuda

    def calcVencimento(self, vlFaturam) -> float:
        salario = (vlFaturam * (self.perComissao / 100))
        venc = ((self.ajudaCusto * (0.5 / 100)) + (salario * (1 / 100)))
        if venc >= 25:
            return venc


class ContratoHorista(Contrato):
    def __init__(self, dia: int, mes: int, ano: int, colaborador: Colaborador,
                 horaMes: int, valorHora: float) -> None:
        super().__init__(dia, mes, ano, colaborador)
        self._horaMes = horaMes
        self._valorHora = valorHora

    @property
    def horaMes(self) -> int:
        return self._horaMes

    @horaMes.setter
    def horaMes(self, horaMes) -> None:
        self._horaMes = horaMes

    @property
    def valorHora(self) -> float:
        return self._valorHora

    @valorHora.setter
    def valorHora(self, valorHora) -> None:
        self._valorHora = valorHora

    def calcVencimento(self) -> float:
        salario = self.horaMes * self.valorHora
        if salario <= 5000:
            venc = (salario * (2 / 100))
            return venc
        else:
            venc = (salario * (2.5 / 100))
            return venc
