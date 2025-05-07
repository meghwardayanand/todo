import pytest
from rest_framework import status

from todo.models import TodoItem


@pytest.mark.django_db
def test_get_empty_todos(api_client):
    """Get Empty List."""
    url = '/todos/v1/todos/'
    response = api_client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []

@pytest.mark.django_db
def test_create_todo_item(api_client, user):
    """Create Todo Item."""
    url = '/todos/v1/todos/'
    payload = {
        'title': 'Buy Milk',
        'description': 'Buy 2 gallons of milk',
    }

    response = api_client.post(url, data=payload, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['title'] == payload['title']
    assert response.data['description'] == payload['description']
    assert response.data['owner'] == user.id

    # Verify
    todo_item_id = response.data['id']
    response = api_client.get(f'{url}{todo_item_id}/', format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == payload['title']
    assert response.data['description'] == payload['description']
    assert response.data['owner'] == user.id

@pytest.mark.django_db
def test_update_todo_item(api_client, user):
    """Create Todo Item."""
    url = '/todos/v1/todos/'
    payload = {
        'title': 'Buy Milk',
        'description': 'Buy 2 gallons of milk',
    }

    # CREATE
    response = api_client.post(url, data=payload, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['title'] == payload['title']
    assert response.data['description'] == payload['description']
    assert response.data['owner'] == user.id

    todo_item_id = response.data['id']
    # ACCESS
    response = api_client.get(f'{url}{todo_item_id}/', format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == payload['title']
    assert response.data['description'] == payload['description']
    assert response.data['owner'] == user.id

    # UPDATE
    payload['title'] = 'Sell Milk'
    payload['description'] = 'Sell 2 gallons of milk'
    update_url = f'/todos/v1/todos/{todo_item_id}/'
    response = api_client.put(update_url, data=payload, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == payload['title']
    assert response.data['description'] == payload['description']
    assert response.data['owner'] == user.id

    # ACCESS AGAIN
    response = api_client.get(f'{url}{todo_item_id}/', format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == payload['title']
    assert response.data['description'] == payload['description']
    assert response.data['owner'] == user.id

@pytest.mark.django_db
def test_delete_todo_item(api_client, user):
    """Create Todo Item."""
    url = '/todos/v1/todos/'
    payload = {
        'title': 'Buy Milk',
        'description': 'Buy 2 gallons of milk',
    }

    # CREATE
    response = api_client.post(url, data=payload, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['title'] == payload['title']
    assert response.data['description'] == payload['description']
    assert response.data['owner'] == user.id

    todo_item_id = response.data['id']
    # ACCESS
    response = api_client.get(f'{url}{todo_item_id}/', format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == payload['title']
    assert response.data['description'] == payload['description']
    assert response.data['owner'] == user.id

    # DELETE
    delete_url = f'/todos/v1/todos/{todo_item_id}/'
    response = api_client.delete(delete_url, format='json')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.data == None

    # ACCESS AGAIN
    response = api_client.get(f'{url}{todo_item_id}/', format='json')
    assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
def test_get_todos_list(api_client, user):
    url = '/todos/v1/todos/'
    payloads = [
        {
            'title': 'Buy Milk',
            'description': 'Buy 2 gallons of milk',
        },
        {
            'title': 'Buy Eggs',
            'description': 'Buy 2 dozen of eggs',
        },
    ]

    created_ids = []
    for payload in payloads:
        response = api_client.post(url, data=payload, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == payload['title']
        assert response.data['description'] == payload['description']
        assert response.data['owner'] == user.id

        todo_item_id = response.data['id']
        response = api_client.get(f'{url}{todo_item_id}/', format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == payload['title']
        assert response.data['description'] == payload['description']
        assert response.data['owner'] == user.id
        created_ids.append(todo_item_id)

    response = api_client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['title'] == payloads[0]['title']
    assert response.data[0]['description'] == payloads[0]['description']
    assert response.data[0]['owner'] == user.id
    assert response.data[1]['title'] == payloads[1]['title']
    assert response.data[1]['description'] == payloads[1]['description']
    assert response.data[1]['owner'] == user.id

@pytest.mark.django_db
def test_todo_item_str(api_client, user):
    """Create Todo Item."""
    url = '/todos/v1/todos/'
    payload = {
        'title': 'Buy Milk',
        'description': 'Buy 2 gallons of milk',
    }

    response = api_client.post(url, data=payload, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['title'] == payload['title']
    assert response.data['description'] == payload['description']
    assert response.data['owner'] == user.id

    todo_item_id = response.data['id']
    response = api_client.get(f'{url}{todo_item_id}/', format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == payload['title']
    assert response.data['description'] == payload['description']
    assert response.data['status'] == TodoItem.Status.CREATED.value
    assert response.data['owner'] == user.id

    todo_item = TodoItem.objects.filter(id=todo_item_id).first()
    assert str(todo_item).startswith(f'{todo_item_id} | Buy Milk | {user}')
