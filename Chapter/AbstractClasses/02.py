from abc import ABC, abstractmethod

class MenuItem(ABC):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def serve(self):
        pass

class Dish(MenuItem):

    def prepare(self):
        print(f"Preparing {self.name}")

    def serve(self):
        print(f"Serving {self.name} for ${self.price}")

class Drink(MenuItem):

    def prepare(self):
        print(f"Preparing {self.name}")

    def serve(self):
        print(f"Serving {self.name} for ${self.price}")

menu_items = [Dish("Pasta", 12.99), Drink("Soda", 2.99)]

for item in menu_items:
    item.prepare()
    item.serve()


# Trong ví dụ này:
#
# Lớp MenuItem là lớp cơ sở có hai phương thức trừu tượng prepare và serve.
# Lớp con Dish và Drink kế thừa từ MenuItem và cung cấp triển khai cụ thể cho các phương thức trừu tượng.
# Chúng ta tạo ra danh sách các món ăn và thức uống, và thực hiện các bước chuẩn bị và phục vụ.
# Mặc dù ví dụ này còn đơn giản, nó thể hiện cách bạn có thể sử dụng abstractmethod để xây dựng một hệ thống mã nguồn linh hoạt và dễ bảo trì trong các dự án thực tế, đặc biệt là khi cần thiết phải áp dụng các hành vi chung cho nhiều lớp con khác nhau.