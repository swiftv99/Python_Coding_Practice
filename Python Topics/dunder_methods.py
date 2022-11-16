class String():
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f"Object: {self.string}"

    def __add__(self, other):
        return self.string + other

    # def __repr__(self):
    #     return "You just called __repr__"


if __name__ == '__main__':
    str1 = String('Hello World.')
    print(str1)
    # print(str1 + " I'm fine!")