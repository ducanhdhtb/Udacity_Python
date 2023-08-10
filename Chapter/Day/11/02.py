class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

    def __str__(self):
        return f"{self.name} ({self.age} years old)"


person = Person("Alice", 30)

print(repr(person))  # Gọi phương thức __repr__
print(str(person))  # Gọi phương thức __str__

# Kết quả:
# Person('Alice', 30)
# Alice (30 years old)
