import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

# Main code to interact with the user
def main():
    while True:
        print("\nShape Operations:")
        print("1. Calculate Rectangle Area and Perimeter")
        print("2. Calculate Circle Area and Perimeter")
        print("3. Exit")
        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            width = float(input("Enter width of the rectangle: "))
            height = float(input("Enter height of the rectangle: "))
            rectangle = Rectangle(width, height)
            print(f"Rectangle Area: {rectangle.area()}")
            print(f"Rectangle Perimeter: {rectangle.perimeter()}")
        elif choice == 2:
            radius = float(input("Enter radius of the circle: "))
            circle = Circle(radius)
            print(f"Circle Area: {circle.area()}")
            print(f"Circle Perimeter: {circle.perimeter()}")
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()

