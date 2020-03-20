# with constructor


class Point:
    def __init__(self, x, y):  # << constructor to initialize variables
        self.x = x
        self.x = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)

print(point.x)
