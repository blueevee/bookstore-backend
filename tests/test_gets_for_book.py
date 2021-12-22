
def test_get_must_have_return_success(client):
    response = client.get('/obras')

    assert response.status_code == 200

def test_get_to_registered_book_must_have_return_book(client):
    response = client.get('/obras/1')

    assert response.json == {'book':{'authors': 'K Rowling',
                                    'company': 'Rocco',
                                    'id': 1,
                                    'image': 'https://i.imgur.com/UH3IPXw.jpg',
                                    'title': 'Harry Potter'}
                                    }

def test_get_to_unregistered_book_must_have_return_error(client):
    response = client.get('/obras/9999')

    assert response.json == {'message': 'Obra não encontrada.'}

def test_delete_must_have_return_deleted(client):
    response = client.delete('/obras/6')

    assert response.json == {'message': 'Obra deletada com sucesso!'}