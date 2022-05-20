import random

import pytest
from model_bakery import baker
from rest_framework import status

from airplane.services import calculate_fuel_consumption
from airplane.services import calculate_fuel_tank


@pytest.mark.django_db
def test_list_airplane(client):
    plane_count = 10
    [baker.make('airplane.AirPlane') for _ in range(plane_count)]

    response = client.get('/api/airplanes/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == plane_count


@pytest.mark.django_db
def test_create_airplane(client):
    data = {
        'id': random.randint(0, 100_000),
        'passenger_capacity': random.randint(0, 32_767),
    }
    response = client.post(
        '/api/airplanes/',
        data=data,
        content_type='application/json'
    )
    assert response.status_code == status.HTTP_201_CREATED, response.data
    data = response.data
    assert data['fuel_tank'] == calculate_fuel_tank(data['id'])
    assert data['fuel_consumption_per_minute'] == calculate_fuel_consumption(
        data['id'], data['passenger_capacity'])


@pytest.mark.django_db
def test_update_airplane(client):
    new_passenger_capacity_count = 100
    air_plane = baker.make('airplane.AirPlane')
    assert new_passenger_capacity_count != air_plane.passenger_capacity

    response = client.put(
        f'/api/airplanes/{air_plane.id}/',
        data={'id': air_plane.id, 'passenger_capacity': new_passenger_capacity_count},
        content_type='application/json'
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data['passenger_capacity'] == new_passenger_capacity_count


@pytest.mark.django_db
def test_delete_airplane(client):
    air_plane = baker.make('airplane.AirPlane')

    response = client.get('/api/airplanes/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

    response = client.delete(f'/api/airplanes/{air_plane.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT

    response = client.get('/api/airplanes/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0

