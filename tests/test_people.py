import pytest
from models.people import People


class _1TestPeople:

    @pytest.mark.parametrize('people_id,', (1, 4))
    def test_people(self, get_people):
        response = get_people
        people = People.parse_obj(response.json())
        assert response.status_code == 200
        print(f'\n=======Parse OK======={people.name}')
