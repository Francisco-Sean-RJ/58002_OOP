class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be provided")
    def area(self):
        return 3.14159 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14159 * self.radius
radius = None
diameter = None
while radius is None and diameter is None:
    choice = input("Enter 'r' for radius or 'd' for diameter: ")
    if choice == 'r':
        radius = float(input("Enter the radius: "))
    elif choice == 'd':
        diameter = float(input("Enter the diameter: "))
    else:
        print("Invalid choice, please try again.")
circle = Circle(radius=radius, diameter=diameter)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
