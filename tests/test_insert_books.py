
def test_insert_masterpiece_sending_full_payload(client):
    book = {
        'title': 'Título teste',
        'company': 'ABC',
        'image': 'https://i.imgur.com/UM3DPXw.jpg', 
        'authors': 'A. b.c.'
    }
    response = client.post('/obras', json=book)

    response = response.json.get('book')
    response.pop('id')

    assert book == response

def test_modify_masterpiece_sending_full_payload(client):
    initial_book = {
        'title': 'Título teste',
        'company': 'ABC',
        'image': 'https://i.imgur.com/UM3DPXw.jpg', 
        'authors': 'A. b.c.'
    }
    response = client.post('/obras', json=initial_book)
    response = response.json.get('book')

    pk = response['id']

    final_book = {
        'title': 'MODIFIED',
        'company': 'EVEVEVE',
        'image': 'https://i.imgur.com/bIbbPgq.jpeg', 
        'authors': 'eve. blue.'
    }
    response = client.put(f'/obras/{pk}', json=final_book)
    response = response.json.get('book')

    assert pk == response['id']

    response.pop('id')
    assert final_book == response

def test_insert_must_have_return_error_when_empty_title(client):
    book = {
        'company': 'ABC',
        'image': 'https://i.imgur.com/UM3DPXw.jpg', 
        'authors': 'A. b.c.'
    }
    response = client.post('/obras', json=book)
    expected = { "title": ["Missing data for required field."] }

    assert expected == response.json

def test_insert_must_have_return_error_when_empty_company(client):
    book = {
        'title': 'Título teste',
        'image': 'https://i.imgur.com/UM3DPXw.jpg', 
        'authors': 'A. b.c.'
    }
    response = client.post('/obras', json=book)
    expected = { "company": ["Missing data for required field."] }

    assert expected == response.json

def test_insert_must_have_return_error_when_empty_image(client):
    book = {
        'title': 'Título teste',
        'company': 'ABC',
        'authors': 'A. b.c.'
    }
    response = client.post('/obras', json=book)
    expected = { "image": ["Missing data for required field."] }

    assert expected == response.json

def test_insert_must_have_return_error_when_empty_authors(client):
    book = {
        'title': 'Título teste',
        'company': 'ABC',
        'image': 'https://i.imgur.com/UM3DPXw.jpg'
    }
    response = client.post('/obras', json=book)
    expected = { "authors": ["Missing data for required field."] }

    assert expected == response.json

def test_insert_must_have_return_error_when_send_id(client):
    book = {
        'id': 1,
        'title': 'Título teste',
        'company': 'ABC',
        'image': 'https://i.imgur.com/UM3DPXw.jpg',
        'authors': 'A. b.c.'
    }
    response = client.post('/obras', json=book)
    expected = { "id": ["Tá enviando ID pra que?? PARE AGORA"] }

    assert expected == response.json

def test_insert_must_have_return_error_when_empty_payload(client):
    
    response = client.post('/obras', json=None)

    assert response.status_code == 400