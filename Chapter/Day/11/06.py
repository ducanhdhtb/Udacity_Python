class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.age == other.age


if __name__ == "__main__":
    dog1 = Dog("Buddy", 5)
    dog2 = Dog("Charlie", 7)
    dog3 = Dog("Max", 5)

    print(dog1 > dog2)  # False (5 is not greater than 7)
    print(dog1 < dog2)  # True (5 is less than 7)

    print(dog1 == dog3)  # True (both are 5 years old)
    print(dog2 != dog3)  # True (7 is not equal to 5)
