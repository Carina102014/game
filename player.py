import tool


class Player:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        self.tool = tool.Tool("white")

    def test(self):
        self.tool.change_color("red")