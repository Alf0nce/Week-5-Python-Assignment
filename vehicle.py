class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def power_toggle(self):
        print(f"{self.brand} {self.model} is now powered on.")

    def use(self):
        print(f"Using {self.brand} {self.model} smartphone.")

class CameraPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_megapixels):
        super().__init__(brand, model, storage, battery)
        self.camera_megapixels = camera_megapixels

    def use(self):
        print(f"Taking photos with {self.camera_megapixels} MP camera.")

class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        super().__init__(brand, model, storage, battery)
        self.gpu = gpu

    def use(self):
        print(f"Playing games with {self.gpu} GPU.")

    def power_toggle(self):
        print(f"{self.brand} {self.model} is now powered on.")

    def use(self):
        print(f"Playing games with {self.gpu} GPU.")

def demonstrate_polymorphism():
    print("\n=== Smartphone Polymorphism ===")
    phones = [
        Smartphone("Apple", "iPhone 15", 128, 4000),
        GamingPhone("ASUS", "ROG Phone 6", 256, 6000, "Adreno 660"),
        CameraPhone("Samsung", "Galaxy S23", 256, 5000, 200)
    ]

    for phone in phones:
        phone.power_toggle()
        phone.use()  # Calls the overridden method in each subclass
        print("---")

    print("\n=== Vehicle Polymorphism ===")

    class Car:
        def move(self):
            print("The car is driving on the road.")

    class Plane:
        def move(self):
            print("The plane is flying in the sky.")

    class Boat:
        def move(self):
            print("The boat is sailing on the water.")

    class Bicycle:
        def move(self):
            print("The bicycle is being pedaled on the path.")

    vehicles = [Car(), Plane(), Boat(), Bicycle()]

    for vehicle in vehicles:
        vehicle.move()  # Same method, different outputs

if __name__ == "__main__":
    demonstrate_polymorphism()
    # The main function to demonstrate polymorphism
    # in both Smartphone and Vehicle classes
    # Uncomment the following line to run the demonstration
    # demonstrate_polymorphism()
    # Uncomment the following line to run the demonstration
    # demonstrate_polymorphism()

    