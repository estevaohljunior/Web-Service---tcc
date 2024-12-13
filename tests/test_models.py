# tests/test_models.py
import pytest
from app.models.chave_acesso import ChaveAcesso

def test_chave_acesso_valida():
    chave = "25170921138765000243650010000237261123456784"
    chave_acesso = ChaveAcesso(chave)
    assert chave_acesso.cnf == "12345678"
    assert chave_acesso.nnf == "000023726"

def test_chave_acesso_invalida():
    with pytest.raises(ValueError):
        ChaveAcesso("chave_invalida")

