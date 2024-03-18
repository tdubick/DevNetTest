#Classes are to objects as biueprints are to houses
class Circle:
    Id = 0
    color = 0
    color = ""
    display = True

    def __init__(self, id, r, c, d):
        self.ID = id
        self.radius = r
        self.color = c
        self.display = d
    #Below is a method - a method is a function that belongs to a class
    def circumfrence(self):
        return 3.141 * 2 * self.radius

circle1 = Circle(1, 10, "Blue", True)
circle2 = Circle(2, 8, "Yellow", True)
circle3 = Circle(3, 17, "Red", False)

print("Circle 1 circumfrence is: " + (3.141 * 2 * circle1.circumfrence))
print("Circle 2 circumfrence is: " + (3.141 * 2 * circle2.circumfrence))
print("Circle 3 circumfrence is: " + (3.141 * 2 * circle3.circumfrence))
        
