import math
from random import random
from random import randrange


def my_decorator(func):
    def wrapper(self):
        print(f"{func.__name__} is running")
        return func(self)

    return wrapper


class Car:
    _speed_increment: float = 10

    count: int = 0
    _price_coeff: float = 100

    def __init__(self, name: str = "Ford f-150", max_speed: float = 250):
        if max_speed < 0:
            raise Exception("Max speed is < 0")
        if len(name) == 0:
            raise Exception("Name is not defined")
        self.__name = name
        self._max_speed = max_speed
        Car.count += 1

    @property
    def get_speed_increment(self) -> float:
        return Car._speed_increment

    @property
    def price_coeff(self) -> float:
        return Car._price_coeff

    def set_name(self, val):
        if len(val) == 0:
            raise Exception()
        else:
            self.__name = val

    @property
    def name(self) -> str:
        return self.__name


    def price(self) -> float:
        return self._max_speed * Car._price_coeff

    @my_decorator
    def update_model(self) -> None:
        self._max_speed += Car._speed_increment

    @staticmethod
    def randomCar() -> "Car":
        word_dict: {} = {
            1: "Ford f-150",
            2: "Ford focus",
            3: "Mercedes Unimog",
            4: "Kia Soul",
            5: "Genesis k80"
        }
        return Car(word_dict[(randrange(1, 6))], random() * 256)

    def __lt__(self, other) -> bool:
        return self._max_speed < other._max_speed

    def __gt__(self, other) -> bool:
        return self._max_speed > other._max_speed

    def __le__(self, other) -> bool:
        return self._max_speed <= other._max_speed

    def __ge__(self, other) -> bool:
        return self._max_speed >= other._max_speed

    def __ne__(self, other) -> bool:
        return \
            self._max_speed != other._max_speed \
            and self.__name != other.__name

    def __eq__(self, other) -> bool:
        return \
            self._max_speed == other._max_speed \
            and self.__name == other.__name

    def __add__(self, other) -> "Car":
        return Car(self.__name + " " + other.__name, self._max_speed + other._max_speed)

    def __truediv__(self, other) -> "Car":
        return Car(max_speed=self._max_speed / other._max_speed)

    def __sub__(self, other) -> "Car":
        return Car(max_speed=self._max_speed - other._max_speed)

    def __mul__(self, other) -> "Car":
        return Car(max_speed=self._max_speed * other._max_speed)

    def __str__(self) -> str:
        return "Name: " + str(self.__name) + "\n" + \
               "Max Speed: " + str(self._max_speed)

    @property
    def max_speed(self):
        return self._max_speed

    @max_speed.setter
    def max_speed(self, value):
        self._max_speed = value

    @classmethod
    def get_count_of_obj(cls) -> float:
        return cls.count

class ExecutiveCar(Car):
    _speed_increment: float = 5

    _price_coeff: float = 250

    def __init__(self, name: str = "Ford f-150", max_speed: float = 250):
        super(ExecutiveCar, self).__init__(name, max_speed)

    @property
    def get_speed_increment(self) -> float:
        return ExecutiveCar._speed_increment

    @property
    def get_price_coeff(self) -> float:
        return ExecutiveCar._price_coeff

    @staticmethod
    def randomCar() -> "ExecutiveCar":
        return ExecutiveCar(*(Car
                              .randomCar()
                              .__dict__
                              .values()
                              ))

    def price(self) -> float:
        return super(ExecutiveCar, self).price() * (ExecutiveCar._price_coeff / super(ExecutiveCar, self).price_coeff)

    @my_decorator
    def update_model(self) -> None:
        tmp = super(ExecutiveCar, self).max_speed + ExecutiveCar._speed_increment
        super(ExecutiveCar, self).__setattr__("_max_speed", tmp)


    def __add__(self, other) -> "ExecutiveCar":
        return ExecutiveCar(*super(ExecutiveCar, self).__add__(other).__dict__.values())

    def __truediv__(self, other) -> "ExecutiveCar":
        return ExecutiveCar(*super(ExecutiveCar, self).__truediv__(other).__dict__.values())

    def __sub__(self, other) -> "ExecutiveCar":
        return ExecutiveCar(*super(ExecutiveCar, self).__sub__(other).__dict__.values())

    def __mul__(self, other) -> "ExecutiveCar":
        return ExecutiveCar(*super(ExecutiveCar, self).__mul__(other).__dict__.values())


def main():
    excar1 = ExecutiveCar()
    excar2 = ExecutiveCar()
    print(excar1 == excar2)
    print(excar1 > excar2)
    print(excar1 >= excar2)
    print(excar1 < excar2)
    print(excar1 <= excar2)
    print(excar1 != excar2)
    print(excar1/excar2)
    print(excar1.price())
    print(excar1.max_speed)
    excar1.update_model()
    print(excar1.max_speed)
    print(excar2.get_count_of_obj())


if __name__ == '__main__':
    main()
#pppp