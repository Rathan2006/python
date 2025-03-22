class Converter:
    conversion_factors = {
        'inches': 1,
        'feet': 1 / 12,
        'yards': 1 / 36,
        'miles': 1 / 63360,
        'millimeters': 25.4,
        'centimeters': 2.54,
        'meters': 0.0254,
        'kilometers': 0.0000254
    }

    def __init__(self, length, unit):
        self.length = length
        self.unit = unit.lower()

    def convert_to_inches(self):
        if self.unit in self.conversion_factors:
            return self.length / self.conversion_factors[self.unit]
        raise ValueError("Unsupported Input unit")

    def convert_to(self, target_unit):
        target_unit = target_unit.lower()
        if target_unit in self.conversion_factors:
            return self.convert_to_inches() * self.conversion_factors[target_unit]
        raise ValueError("Unsupported target unit")

length = float(input("Enter the length: "))
unit = input("Enter the unit (inches, feet, yards, miles, kilometers, meters, centimeters, millimeters): ")
converter = Converter(length, unit)

while True:
    target_unit = input("\nEnter the target unit (inches, feet, yards, miles, kilometers, meters, centimeters, millimeters) or 'exit' to stop: ").lower()
    if target_unit == 'exit':
        break
    try:
        converted_length = converter.convert_to(target_unit)
        print(f"{length} {unit} is equal to {converted_length} {target_unit}")
    except ValueError as e:
        print(e)
