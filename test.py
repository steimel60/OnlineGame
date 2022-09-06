class Base():
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def hi(self):
        print(f"hi im {self.name}")
    def print_level(self):
        print(f"{self.name} is level {self.level}")

class Dragonborn(Base):
    def __init__(self, Base, color):
        super().__init__(Base.name, Base.level)
        self.color = color
    def hi(self):
        print(f"hi im {self.name} a {self.color} dragonborn")

bob = Dragonborn(Base("bob", 5),"silver")
bob.hi()
bob.print_level()
