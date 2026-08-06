from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")


class UPIPayment(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


class CashPayment(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using Cash")


# Creating objects
credit = CreditCardPayment()
upi = UPIPayment()
cash = CashPayment()

credit.pay(1000)
upi.pay(500)
cash.pay(200)