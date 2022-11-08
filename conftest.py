import pytest
from constants.other import Other as const
from helpers.requester import CustomRequest as cr


@pytest.fixture
def get_planet(planet_id):
    return cr.custom_request('get', const.BASE_URL_PLANETS + str(planet_id))


@pytest.fixture
def get_people(people_id):
    return cr.custom_request('get', const.BASE_URL_PEOPLES + str(people_id))
