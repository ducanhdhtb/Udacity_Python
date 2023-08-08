from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(Account):

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} into Savings Account {self.account_number}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount} from Savings Account {self.account_number}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

class CheckingAccount(Account):

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} into Checking Account {self.account_number}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount} from Checking Account {self.account_number}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

savings_account = SavingsAccount("SA123", 1000)
checking_account = CheckingAccount("CA456", 2000)

savings_account.deposit(500)
savings_account.withdraw(200)
savings_account.withdraw(1500)

checking_account.deposit(1000)
checking_account.withdraw(800)
checking_account.withdraw(1500)
'''
Trong ví dụ này:

Lớp Account là lớp cơ sở có hai phương thức trừu tượng deposit và withdraw.
Lớp con SavingsAccount và CheckingAccount kế thừa từ Account và cung cấp triển khai cụ thể cho các phương thức trừu tượng.
Chúng ta tạo ra một tài khoản tiết kiệm và một tài khoản kiểm tra, sau đó thực hiện các giao dịch như gửi tiền và rút tiền.
Tất nhiên, đây chỉ là một ví dụ đơn giản. Trong thực tế, các ứng dụng ngân hàng thường có nhiều chức năng phức tạp hơn như xử lý giao dịch, quản lý tài khoản, tính lãi suất và nhiều khía cạnh khác. Tuy nhiên, ví dụ này giúp bạn thấy cách sử dụng abstractmethod để xây dựng các lớp và triển khai các phương thức cần thiết cho một ứng dụng ngân hàng đơn giản.


'''