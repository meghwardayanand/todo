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

@pytest.mark.django_db
def test_get_todos_list_by_users(api_client, user, super_user, staff_user):
    url = '/todos/v1/todos/'
    user_payload = {
        'title': 'Buy Milk',
        'description': 'Buy 2 gallons of milk',
    }
    staff_payload = {
        'title': 'Buy Eggs',
        'description': 'Buy 2 dozen of eggs',
    }


    # Add by normal user
    response = api_client.post(url, data=user_payload, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['title'] == user_payload['title']
    assert response.data['description'] == user_payload['description']
    assert response.data['owner'] == user.id

    # Get by normal user (for successful verification)
    user_todo_item_id = response.data['id']
    response = api_client.get(f'{url}{user_todo_item_id}/', format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == user_payload['title']
    assert response.data['description'] == user_payload['description']
    assert response.data['owner'] == user.id

    # Authenticate Staff User
    api_client.force_authenticate(user=staff_user)
    # Add by staff user
    response = api_client.post(url, data=staff_payload, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['title'] == staff_payload['title']
    assert response.data['description'] == staff_payload['description']
    assert response.data['owner'] == staff_user.id

    # Get by staff user (for successful verification)
    staff_user_todo_item_id = response.data['id']
    response = api_client.get(f'{url}{staff_user_todo_item_id}/', format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == staff_payload['title']
    assert response.data['description'] == staff_payload['description']
    assert response.data['owner'] == staff_user.id
    assert response.data['owner'] != user.id
    assert response.data['owner'] != super_user.id


    # Test list by normal user
    api_client.force_authenticate(user=user)
    response = api_client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['title'] == user_payload['title']
    assert response.data[0]['description'] == user_payload['description']
    assert response.data[0]['owner'] == user.id


    # Test list by staff user
    api_client.force_authenticate(user=staff_user)
    response = api_client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['title'] == user_payload['title']
    assert response.data[0]['description'] == user_payload['description']
    assert response.data[0]['owner'] == user.id
    assert response.data[1]['title'] == staff_payload['title']
    assert response.data[1]['description'] == staff_payload['description']
    assert response.data[1]['owner'] == staff_user.id


    # Test list by superuser user
    api_client.force_authenticate(user=super_user)
    response = api_client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['title'] == user_payload['title']
    assert response.data[0]['description'] == user_payload['description']
    assert response.data[0]['owner'] == user.id
    assert response.data[1]['title'] == staff_payload['title']
    assert response.data[1]['description'] == staff_payload['description']
    assert response.data[1]['owner'] == staff_user.id
