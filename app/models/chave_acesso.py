from dataclasses import dataclass
from typing import Optional
from app.utils.validators import validate_chave_acesso

@dataclass
class ChaveAcesso:
    chave_completa: str
    cuf: str = None
    aamm: str = None
    cnpj: str = None
    mod: str = None
    serie: str = None
    nnf: str = None
    tp_emis: str = None
    cnf: str = None
    cdv: str = None

    def __post_init__(self):
        validate_chave_acesso(self.chave_completa)
        self._parse_chave()

    def _parse_chave(self):
        """Parse a chave de acesso em seus componentes."""
        self.cuf = self.chave_completa[:2]
        self.aamm = self.chave_completa[2:6]
        self.cnpj = self.chave_completa[6:20]
        self.mod = self.chave_completa[20:22]
        self.serie = self.chave_completa[22:25]
        self.nnf = self.chave_completa[25:34]
        self.tp_emis = self.chave_completa[34:35]
        self.cnf = self.chave_completa[35:43]
        self.cdv = self.chave_completa[43:]
