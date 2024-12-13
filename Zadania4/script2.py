from enum import Enum

class Fruit(Enum):
    APPLE = 0
    BANANA = 1
    PEAR = 2


if __name__ == "__main__":
    for fruit in Fruit:
        print(fruit.value,fruit.name)