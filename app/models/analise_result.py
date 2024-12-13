from enum import Enum
from dataclasses import dataclass

class PadraoGeracao(Enum):
    FIXO = "fixo"
    ESPELHO = "espelho"
    ESPELHO_K = "espelho_k"
    INCREMENTAL = "incremental"
    ALEATORIO = "aleatorio"
    INDEFINIDO = "indefinido"

@dataclass
class AnaliseResult:
    padrao: PadraoGeracao
    vulneravel: bool
    descricao: str

    @property
    def to_dict(self):
        return {
            'padrao': self.padrao.value,
            'vulneravel': self.vulneravel,
            'descricao': self.descricao
        }



