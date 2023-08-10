class Dog():

    def __init__(self, name: str, age: int,
                 breed: str, weight: int):
        """Create a new dog"""
        self.breed = breed
        self.weight = weight
        self.name = name
        self.age = age

    def speak(self) -> None:
        """Make the dog bark"""
        print(f'{self.name} says, "woof"')

    def __str__(self) -> str:
        """Return a string representation of the dog"""
        return self.name

    def __gt__(self, other) -> bool:
        """Compare dogs based on age"""
        return self.age > other.age

    def __eq__(self, other) -> bool:
        """Check if dogs are the same age"""
        return self.age == other.age


if __name__ == "__main__":
    sally = Dog('Sally', 6, 'chihuahua', 7)
    henry = Dog('Henry', 7, 'terrier', 15)

    if sally > henry:
        print(f'{sally} is older than {henry}')
    else:
        print(f'{henry} is older than {sally}')

    if sally == henry:
        print(f'{sally} and {henry} are the same age')
    else:
        print(f'{sally} and {henry} are different ages')
