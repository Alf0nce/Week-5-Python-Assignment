# Base Smartphone Class
class Smartphone:
    def __init__(self, brand, model, storage_gb, battery_mah):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_mah = battery_mah
        self.power_on = False
        self.current_volume = 50

    def power_toggle(self):
        self.power_on = not self.power_on
        status = "on" if self.power_on else "off"
        print(f"{self.brand} {self.model} is now {status}")

    def use(self):
        print(f"Using {self.brand} {self.model} smartphone")

    def set_volume(self, volume):
        if 0 <= volume <= 100:
            self.current_volume = volume
            print(f"Volume set to {self.current_volume}%")
        else:
            print("Volume must be between 0 and 100")

    def get_volume(self):
        return self.current_volume
    adjust_volume = set_volume  # Alias for set_volume
    def get_battery_status(self):
        return self.battery_mah

# Derived Smartphone Classes
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage_gb, battery_mah, gpu_model):
        super().__init__(brand, model, storage_gb, battery_mah)
        self.gpu_model = gpu_model

    def use(self):  # Polymorphism: Override the base method
        print(f"Playing high-performance games on {self.brand} {self.model}")

class CameraPhone(Smartphone):
    def __init__(self, brand, model, storage_gb, battery_mah, camera_mp):
        super().__init__(brand, model, storage_gb, battery_mah)
        self.camera_mp = camera_mp

    def use(self):  # Polymorphism: Override the base method
        print(f"Taking professional photos with {self.brand} {self.model}")

# Base Vehicle Class (for polymorphism demo)
class Vehicle:
    def move(self):
        pass

# Derived Vehicle Classes
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚲")

# Function to demonstrate polymorphism
def demonstrate_polymorphism(vehicle):
    vehicle.move()

# Main function to demonstrate the classes and polymorphism
def main():
    # Create instances of Smartphone classes
    gaming_phone = GamingPhone("Asus", "ROG Phone 5", 512, 6000, "Adreno 660")
    camera_phone = CameraPhone("Samsung", "Galaxy S21 Ultra", 256, 5000, 108)

    # Use the smartphones
    gaming_phone.power_toggle()
    gaming_phone.use()
    gaming_phone.set_volume(75)
    print(f"Gaming phone volume: {gaming_phone.get_volume()}%")
    print(f"Gaming phone battery: {gaming_phone.get_battery_status()} mAh")

    camera_phone.power_toggle()
    camera_phone.use()
    camera_phone.set_volume(30)
    print(f"Camera phone volume: {camera_phone.get_volume()}%")
    print(f"Camera phone battery: {camera_phone.get_battery_status()} mAh")

    # Create instances of Vehicle classes
    vehicles = [Car(), Plane(), Boat(), Bicycle()]

    # Demonstrate polymorphism
    for vehicle in vehicles:
        demonstrate_polymorphism(vehicle)
        print("---")

    # Demonstrate smartphone usage
    smartphones = [gaming_phone, camera_phone]
    for smartphone in smartphones:
        smartphone.use()
        print("---")
        
        
