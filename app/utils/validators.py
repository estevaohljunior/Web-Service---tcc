def validate_chave_acesso(chave: str) -> None:
    """Valida a estrutura da chave de acesso."""
    if not chave or not isinstance(chave, str):
        raise ValueError("Chave de acesso inválida")
    
    if len(chave) != 44:
        raise ValueError("Chave de acesso deve ter 44 dígitos")
    
    if not chave.isdigit():
        raise ValueError("Chave de acesso deve conter apenas números")


