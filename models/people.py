from pydantic import BaseModel, validator


class People(BaseModel):
    name: str
    height: str
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: str
    films: list
    species: list
    vehicles: list
    starships: list
    created: str
    edited: str
    url: str

    @validator('gender')
    def check_gender(cls, gender: str) -> str:
        """
        Check gender - female or male

        :param gender: str
        :return: str
        """
        if gender not in ['female', 'male']:
            raise ValueError(f'gender - Wrong format, correct gender "female" or "male" >>> {gender} <<<')
        return gender

    @validator('mass')
    def check_mass(cls, mass: int) -> int:
        """
        Check mass people, what mass between 35 and 200
        :param mass: int
        :return: int
        """
        if not 35 < mass < 200:
            raise ValueError(f'Wrong mass, correct mass between 35 and 200 ---> {mass} <---')
        return mass
