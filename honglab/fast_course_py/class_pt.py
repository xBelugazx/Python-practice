class MyInt:
    def __init__(self, value):
        self.value = value  # instance variable

    def print(self):  # method
        print("내가 만든 정수형", self.value)


a = MyInt(123)
a.print()
