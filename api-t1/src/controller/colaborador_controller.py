# Blueprint 
from flask import Blueprint, request, jsonify
from src.model.colaborador_model import Colaborador
from src.model import db

bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador')

dados = [
    {'id': 1, 'nome': 'Samuel Silvério', 'cargo': 'Desenvolvedor Back-end', 'cracha': 'BE12310'},
    {'id': 2, 'nome': 'Karynne Moreira', 'cargo': 'Desenvolvedora Front-end', 'cracha': 'FE21310'},
    {'id': 3, 'nome': 'Joy Assis', 'cargo': 'Desenvolvedora Fullstack', 'cracha': 'FS12110'},
]

@bp_colaborador.route('/pegar-dados', methods=['GET'])
def pegar_dados():
    return dados


# TAREFA -> VALIDAÇÃO DO CAMPO CRACHA. NÃO PODEMOS TER DUPLICATAS

@bp_colaborador.route('/cadastrar', methods=['POST'])
def cadastrar_colaborador():
    
    dados_requisicao = request.get_json()
    
    novo_colaborador = Colaborador(
        nome=dados_requisicao['nome'],
        email=dados_requisicao['email'],
        senha=dados_requisicao['senha'],
        cargo=dados_requisicao['cargo'],
        salario=dados_requisicao['salario']
    )
# INSERT INTO tb_colaborador (nome, email, senha, cargo, salario) VALUES ('samuel', 'samueltigrao@gmail.com', '1234', 'Cliente', 120)
    db.session.add(novo_colaborador) 
    db.session.commit() # Clique no raio do Workbench
    
    return jsonify({'mensagem': 'Colaborador cadastrado com sucesso'}), 201
    
# # TAREFA -> VALIDAÇÃO DO USUARIO. VERIFICAÇÃO DE USUARIO NO BANCO DE DADOS (MOCKADO)

@bp_colaborador.route('/atualizar/<int:id_colaborador>', methods=['PUT'])
def atualizar_dados_colaborador(id_colaborador):
    
    dados_colaborador = request.get_json()
    
    for colaborador in dados:
        if colaborador['id'] == id_colaborador:
            colaborador_encontrado = colaborador
            break
    
    if 'nome' in dados_colaborador:
        colaborador_encontrado['nome'] = dados_colaborador['nome']
    if 'cargo' in dados_colaborador:
        colaborador_encontrado['cargo'] = dados_colaborador['cargo']
    if 'cracha' in dados_colaborador:
        colaborador_encontrado['cracha'] = dados_colaborador['cracha']

    return jsonify( {'mensagem': 'Dados do colaborador atualizados com sucesso'}  ), 200
