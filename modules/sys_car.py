from sys_engine import ElectricEngine
"""
Car Class
"""


class RootCar:
    """
    this is a primary car class
    """

    def __init__(self, xmaker, xmodel, xsubmodel, x_prod_year, x_engine: ElectricEngine):
        """
        Root car class
        :param xmaker:
        Defines car maker
        :param xmodel:
        Defines car model
        :param xsubmodel:
        Defines car submodel as manufacturer describes
        :param x_prod_year:
        Defines car production year
        """

        self._engine = x_engine
        self._maker = xmaker
        self._model = xmodel
        self._submodel = xsubmodel
        self._year = x_prod_year


    # ToDo research core characteristics

    def __str__(self):
        self.x_repr_str = f'This is an {self._maker} {self._model}, ' \
                          f'submodel {self._submodel} produced in {self._year}, ' \
                          f'Engine type {self._engine._make}'
        return self.x_repr_str
