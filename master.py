"""
System launcher
"""
from sys_car import RootCar


def main():
    my_car = RootCar("Audi", "A6", "X1", "2008")
    print(my_car)
    pass


if __name__ == "__main__":
    main()
