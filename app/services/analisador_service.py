from typing import List
from app.models.chave_acesso import ChaveAcesso
from app.models.analise_result import PadraoGeracao, AnaliseResult

class AnalisadorService:
    @staticmethod
    def analisar_padrao(chaves: List[ChaveAcesso]) -> AnaliseResult:
        if not chaves:
            raise ValueError("Lista de chaves não pode estar vazia")

        if AnalisadorService._is_fixo(chaves):
            return AnaliseResult(
                PadraoGeracao.FIXO,
                True,
                "CNF fixo - Alta vulnerabilidade"
            )
        
        if AnalisadorService._is_espelho(chaves):
            return AnaliseResult(
                PadraoGeracao.ESPELHO,
                True,
                "CNF espelha o número da nota - Alta vulnerabilidade"
            )

        # Implementar outras verificações
        return AnaliseResult(
            PadraoGeracao.INDEFINIDO,
            True,
            "Padrão não identificado"
        )

    @staticmethod
    def _is_fixo(chaves: List[ChaveAcesso]) -> bool:
        primeiro_cnf = chaves[0].cnf
        return all(chave.cnf == primeiro_cnf for chave in chaves)

    @staticmethod
    def _is_espelho(chaves: List[ChaveAcesso]) -> bool:
        return all(chave.cnf == chave.nnf for chave in chaves)
