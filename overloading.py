
class Box:
    def __init__(self, volume):
        self.volume = volume

   
    def __add__(self, other):
        return Box(self.volume + other.volume)

    def show(self):
        print("Box volume:", self.volume)


box1 = Box(10)
box2 = Box(20)


box3 = box1 + box2


box1.show()
box2.show()
box3.show()
