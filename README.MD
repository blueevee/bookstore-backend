[get-image]: https://img.shields.io/badge/-GET-green
[post-image]: https://img.shields.io/badge/-POST-yellow
[del-image]: https://img.shields.io/badge/-DELETE-critical
[put-image]: https://img.shields.io/badge/-PUT-blue
# Backend para uma livraria fictícia me**a
## Rodar o projeto localmente
```sh
export FLASK_APP=app.app
export FLASK_ENV=Development
flask run
```
## tasks
- [X] Estrutura inicial do crud
- [X] Fazer testes
- [ ] Ver como está rolando pro pytest ter um db dele e derrubar apos os testes
- [ ] Colocar pra rodar no docker
- [ ] Concluir rota que depende do envio de arquivos
- [ ] Consluir rota que envia email


# Endpoints  

## __Obras__
***
### ![GET][get-image] */obras*
> Retorna todas as obras cadastradas
### ![GET][get-image] */obras/:id*
> Retorna a obra que possui o id informado  

>**Ex:** */obras/3*
 ```json
 {
    "id": 1,
    "authors": "K Rowling",
    "company": "Rocco",
    "image": "https://i.imgur.com/UH3IPXw.jpg",
    "title": "Harry Potter"
 }
```
### ![POST][post-image] */obras*
> Insere uma nova obra  
 ```json
 {
    "authors": "K Rowling",
    "company": "Rocco",
    "image": "https://i.imgur.com/UH3IPXw.jpg",
    "title": "Harry Potter"
 }
```
### ![DEL][del-image] */obras/:id*
> Exclui uma obra da base

### ![PUT][put-image] */obras/:id*
> Edita uma obra da base

========

coverage run --source=app -m pytest -s tests/
coverage report
coverege html
chrome htmlcov/index.html