import pytest
from app.models.chave_acesso import ChaveAcesso
from app.services.analisador_service import AnalisadorService
from app.models.analise_result import PadraoGeracao

def test_analise_padrao_fixo():
    chaves = [
        ChaveAcesso("25170921138765000243650010000237261123456784"),
        ChaveAcesso("25170921138765000243650010000237271123456784")
    ]
    resultado = AnalisadorService.analisar_padrao(chaves)
    assert resultado.padrao == PadraoGeracao.FIXO
