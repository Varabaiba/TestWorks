"""
System launcher
"""
from sys_car import RootCar
from sys_car import ElectricEngine


def main():
    my_engine = ElectricEngine("A","B", 1990)
    my_car = RootCar("Audi", "A6", "X1", "2008", my_engine)
    print(my_car)
    pass


if __name__ == "__main__":
    main()
