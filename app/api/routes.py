from flask import Blueprint, request, jsonify
from app.models.chave_acesso import ChaveAcesso
from app.services.analisador_service import AnalisadorService

bp = Blueprint('api', __name__)

@bp.route('/analisar', methods=['POST'])
def analisar_chaves():
    try:
        data = request.get_json()
        
        if not data or 'chaves' not in data:
            return jsonify({'error': 'Campo "chaves" é obrigatório'}), 400

        chaves = [ChaveAcesso(chave) for chave in data['chaves']]
        resultado = AnalisadorService.analisar_padrao(chaves)
        
        return jsonify(resultado.to_dict)

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Erro interno do servidor'}), 500
