from django.contrib.auth.models import User

import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    """DRF test client with no authentication by default."""
    yield APIClient()

@pytest.fixture
def user():
    """Create and return a test user."""
    return User.objects.create_user(username="test_user", password="testpass")

@pytest.fixture
def super_user():
    """Create and return a test user."""
    return User.objects.create_user(
        username="test_super_user",
        password="testpass",
        is_superuser=True
    )

@pytest.fixture
def staff_user():
    """Create and return a test user."""
    return User.objects.create_user(
        username="test_staff_user",
        password="testpass",
        is_staff=True
    )

@pytest.fixture(autouse=True)
def authenticate(api_client, user):
    """Authenticate every request by default."""
    api_client.force_authenticate(user=user)
    return api_client
