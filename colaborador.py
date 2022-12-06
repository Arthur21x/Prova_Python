from datetime import datetime


class Colaborador:
    def __init__(self, matricula: str, cpf: str, nome: str, dia: int, mes: int, ano: int,
                 situacao: bool = None) -> None:
        self._matricula = matricula
        self._cpf = cpf
        self._nome = nome
        self._dataNascimento = datetime(ano, mes, dia)
        self._situacao = situacao

    @property
    def matricula(self) -> str:
        return self._matricula

    @matricula.setter
    def matricula(self, matricula: str) -> None:
        self._matricula = matricula

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, cpf: str) -> None:
        if self.valida_cpf(cpf):
            self._cpf = cpf
        else:
            raise ValueError("Digite um CPF válido, por favor...")

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def dataNascimento(self):
        return self._dataNascimento

    @dataNascimento.setter
    def dataNascimento(self, dataNascimento: str) -> None:
        if (datetime.today().year - self.dataNascimento.year) >= 18:
            self._dataNascimento = datetime.strptime(dataNascimento, "%d/%m/%Y")
        else:
            raise ValueError("Você precisa ser maior de 18 anos para se tornar um colaborador")

    @property
    def situacao(self) -> bool:
        return self._situacao

    @situacao.setter
    def situacao(self, situacao) -> None:
        self._situacao = situacao

    @staticmethod
    def valida_cpf(cpf: str) -> bool:
        if len(cpf) == 11 and isinstance(cpf, str) and cpf.isnumeric():
            nove_digitos = cpf[:9]
            contador_regressivo_1 = 10

            resultado_digito_1 = 0
            for digito in nove_digitos:
                resultado_digito_1 += int(digito) * contador_regressivo_1
                contador_regressivo_1 -= 1
            digito_1 = (resultado_digito_1 * 10) % 11
            digito_1 = digito_1 if digito_1 <= 9 else 0

            dez_digitos = nove_digitos + str(digito_1)
            contador_regressivo_2 = 11

            resultado_digito_2 = 0
            for digito in dez_digitos:
                resultado_digito_2 += int(digito) * contador_regressivo_2
                contador_regressivo_2 -= 1
            digito_2 = (resultado_digito_2 * 10) % 11
            digito_2 = digito_2 if digito_2 <= 9 else 0

            cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

            if cpf == cpf_gerado_pelo_calculo:
                return True
            return False
        return False

    def ativar(self) -> None:
        self._situacao = True

    def desativar(self) -> None:
        self._situacao = False



