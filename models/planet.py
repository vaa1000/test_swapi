from pydantic import BaseModel, validator
from constants.other import Other


class Planet(BaseModel):
    name: str
    rotation_period: int
    orbital_period: int
    diameter: int
    climate: str
    gravity: str
    terrain: str
    surface_water: int
    population: int
    residents: list
    films: list
    created: str
    edited: str
    url: str

    @validator('diameter')
    def ckeck_diameter(cls, diameter: int) ->str:
        """
        Checking the diameter of the planet relative to the diameter of the Earth
        :param diameter:
        :return:
        """
        relative = diameter / Other.DIAMETER_EARTH
        if not (0.1 < relative < 10):
            raise ValueError(f'd differs more than 10 times from the d Earth >>> {diameter} <<<')
        return diameter
