import pytest
from models.planet import Planet
from constants.other import Other as const


class TestPlanets:

    @pytest.mark.parametrize('planet_id,planet_name', const.PLANETS)
    def test_get_planets(self, get_planet, planet_name):
        response = get_planet
        plnt = Planet.parse_obj(response.json())
        assert response.status_code == 200
        assert plnt.name == planet_name
