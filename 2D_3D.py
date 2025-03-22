import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def rotation_with_x_axis(self):
        return math.degrees(math.atan2(self.y, self.x))

    def display(self):
        print(f"Vector2D: ({self.x}, {self.y})")

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        return self.x * other.y - self.y * other.x

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def display(self):
        print(f"Vector3D: ({self.x}, {self.y}, {self.z})")

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

def main():
    while True:
        print("\nChoose vector type:")
        print("1. Vector2D")
        print("2. Vector3D")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            x = float(input("Enter x: "))
            y = float(input("Enter y: "))
            vector = Vector2D(x, y)
            vector.display()
            print("Magnitude:", vector.magnitude())
            print("Rotation with X-axis:", vector.rotation_with_x_axis())

        elif choice == 2:
            x = float(input("Enter x: "))
            y = float(input("Enter y: "))
            z = float(input("Enter z: "))
            vector = Vector3D(x, y, z)
            vector.display()
            print("Magnitude:", vector.magnitude())

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
