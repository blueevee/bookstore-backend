# from os import error
from flask import Blueprint, current_app, Response, request
from marshmallow import ValidationError

from .serializer import MasterpieceSchema
from .model import Masterpiece


bp = Blueprint('masterpieces', __name__)

# [POST] /obras : A rota deverá receber titulo, editora, foto, e autores dentro do corpo da requisição. Ao cadastrar um novo projeto, ele deverá ser armazenado dentro de um objeto no seguinte formato: { title: ‘Harry Potter’, company: ‘Rocco’,image: ‘https://i.imgur.com/UH3IPXw.jpg’, authors: “JK Rowling...”};

@bp.route('/obras', methods=['POST'])
def insert_masterpiece():
    model = MasterpieceSchema()
    json_data = request.json
    if not json_data:
        return {'message': 'No input data provided'}, 400
    try:
        book = model.load(json_data, session=current_app.db.session)
        current_app.db.session.add(book)
    except ValidationError as err:
        return err.messages, 422
    current_app.db.session.commit()
    result = model.dump(Masterpiece.query.get(book.id))
    return {'message': 'Obra adicionada', 'book': result}, 201

# [GET] /obras/ : A rota deverá listar todas as obras cadastradas
@bp.route('/obras', methods=['GET'])
def get_all_masterpiecies():
    books = Masterpiece.query.all()
    model = MasterpieceSchema(many=True)
    result = model.dump(books)
    return {'books': result}, 200

@bp.route('/obras/<int:pk>', methods=['GET'])
def get_book(pk):
    model = MasterpieceSchema()
    try:
        book = Masterpiece.query.filter(Masterpiece.id == pk).one()
    except:
        return {'message': 'Obra não encontrada.'}, 404
    result = model.dump(book)
    return {'book': result}
    
# [DELETE] /obras/:id: : A rota deverá deletar a obra com o id presente nos parâmetros da rota
@bp.route('/obras/<int:pk>', methods=['DELETE'])
def delete_masterpiecie(pk):
    try:
        Masterpiece.query.filter(Masterpiece.id == pk).delete()
    except:
        return {'message': 'Obra não encontrada.'}, 404
    current_app.db.session.commit()
    return {'message':'Obra deletada com sucesso!'}, 200
    
# [PUT] /obras/:id: : A rota deverá atualizar as informações de titulo, editora, foto e autores da obra com o id presente nos parâmetros da rota
@bp.route('/obras/<int:pk>', methods=['PUT'])
def edit_masterpiecie(pk):
    model = MasterpieceSchema()
    try:
        book = Masterpiece.query.filter(Masterpiece.id == pk)
        book.update(request.json)
        result = model.dump(book.one())
    except:
        return {'message': 'Obra não encontrada.'}, 404
    current_app.db.session.commit()
    return {'message':'Obra atualizada!','book': result}

# [POST] /upload-obras: está rota deverá receber um arquivo csv contendo os mesmos parâmetros da rota anterior mas podendo ser salvo em massa no banco de dados
# [POST] /file-obras/ : A rota deverá solicitar um email e após enviar uma solicitação para uma Fila de Mensagens gerando um arquivo contendo todos as obras cadastradas que seja enviado para o e-mail informado.