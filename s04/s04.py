
class Father:
    def __init__(self, name):
        self.name = name
        self.age = None

    def __str__(self):
        return f"father class->my name is {self.name}"

    def get_id(self):
        return 1


class Child(Father):

    def __init__(self, name, age):
        super().__init__(name)
        super().get_id()
        self.get_id()
        self.age = age

    def __str__(self):
        return f"child class->my name is {self.name}"

    def get_id(self):
        return 2


f = Father("mohammad")
ch = Child("ali", 20)

print(f)
print(ch)
