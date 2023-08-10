class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."


if __name__ == "__main__":
    dog = Dog("Buddy", 5)
    print(dog)  # Khi in đối tượng, phương thức __str__ sẽ được gọi tự động
