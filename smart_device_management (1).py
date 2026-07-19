"""
Smart Device Management System
--------------------------------
EL 162 / 234 - Object Oriented Programming Mini Project

This program models a smart home device management system using
core OOP concepts: classes/objects, constructors, inheritance,
encapsulation (with getters/setters via @property), and
polymorphism through overridden display_info() methods.

Author: <BLANKSON GABRIEL>
"""


# ----------------------------------------------------------------------
# Parent Class: SmartDevice
# ----------------------------------------------------------------------
class SmartDevice:
    """
    Base class representing a generic smart home device.

    Private (encapsulated) attributes:
        __device_id      - unique identifier for the device (cannot be empty)
        __power_status    - whether the device is currently ON or OFF

    Public attribute:
        name              - a human-friendly name for the device
    """

    def __init__(self, name, device_id):
        self.name = name                  # public attribute
        self.__device_id = None           # private attribute, set via setter below
        self.__power_status = False       # private attribute, device starts OFF

        # Route through the property setter so validation runs on creation too
        self.device_id = device_id

    # ---------------- device_id: getter & setter (encapsulation) ----------------
    @property
    def device_id(self):
        """Getter for the private __device_id attribute."""
        return self.__device_id

    @device_id.setter
    def device_id(self, value):
        """Setter that validates device_id cannot be empty before assigning it."""
        if not value or not str(value).strip():
            raise ValueError("Device ID cannot be empty.")
        self.__device_id = value

    # ---------------- power_status: getter only (read-only outside class) -------
    @property
    def power_status(self):
        """Getter for the private __power_status attribute."""
        return self.__power_status

    # ---------------- Public methods ----------------
    def turn_on(self):
        """Turn the device on. Power status can only change through this method."""
        self.__power_status = True
        print(f"[{self.name}] is now ON.")

    def turn_off(self):
        """Turn the device off. Power status can only change through this method."""
        self.__power_status = False
        print(f"[{self.name}] is now OFF.")

    def display_info(self):
        """Display basic information common to all smart devices."""
        status = "ON" if self.__power_status else "OFF"
        print(f"Name: {self.name} | Device ID: {self.__device_id} | Power: {status}")


# ----------------------------------------------------------------------
# Child Class: SecurityCamera
# ----------------------------------------------------------------------
class SecurityCamera(SmartDevice):
    """A smart security camera that can start/stop recording."""

    def __init__(self, name, device_id):
        super().__init__(name, device_id)     # initialize inherited attributes
        self.recording_status = False         # additional attribute

    def start_recording(self):
        if not self.power_status:
            print(f"[{self.name}] cannot record while powered OFF. Turn it on first.")
            return
        self.recording_status = True
        print(f"[{self.name}] has started recording.")

    def stop_recording(self):
        self.recording_status = False
        print(f"[{self.name}] has stopped recording.")

    def display_info(self):
        """Override to include recording status alongside base device info."""
        super().display_info()
        rec = "Recording" if self.recording_status else "Not Recording"
        print(f"    Recording Status: {rec}")


# ----------------------------------------------------------------------
# Child Class: SmartLight
# ----------------------------------------------------------------------
class SmartLight(SmartDevice):
    """A smart light bulb with adjustable brightness (0-100)."""

    def __init__(self, name, device_id, brightness=50):
        super().__init__(name, device_id)     # initialize inherited attributes
        self.__brightness = 0
        self.brightness = brightness          # goes through the validating setter

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, value):
        """Encapsulation: brightness must stay between 0 and 100."""
        if value < 0 or value > 100:
            raise ValueError("Brightness must be between 0 and 100.")
        self.__brightness = value

    def increase_brightness(self, amount=10):
        new_value = min(100, self.__brightness + amount)
        self.brightness = new_value
        print(f"[{self.name}] brightness increased to {self.__brightness}.")

    def decrease_brightness(self, amount=10):
        new_value = max(0, self.__brightness - amount)
        self.brightness = new_value
        print(f"[{self.name}] brightness decreased to {self.__brightness}.")

    def display_info(self):
        """Override to include brightness alongside base device info."""
        super().display_info()
        print(f"    Brightness: {self.__brightness}%")


# ----------------------------------------------------------------------
# Child Class: TemperatureSensor
# ----------------------------------------------------------------------
class TemperatureSensor(SmartDevice):
    """A smart sensor that reads ambient temperature."""

    def __init__(self, name, device_id, temperature=25.0):
        super().__init__(name, device_id)     # initialize inherited attributes
        self.temperature = temperature        # additional attribute (Celsius)

    def read_temperature(self):
        if not self.power_status:
            print(f"[{self.name}] is OFF. Turn it on to read temperature.")
            return
        print(f"[{self.name}] current temperature reading: {self.temperature}°C")

    def display_info(self):
        """Override to include temperature alongside base device info."""
        super().display_info()
        print(f"    Temperature: {self.temperature}°C")


# ----------------------------------------------------------------------
# Menu-Driven Interface
# ----------------------------------------------------------------------
def build_devices():
    """Create the required demo objects: one of each device type."""
    devices = [
        TemperatureSensor(name="Living Room Sensor", device_id="TS-001", temperature=23.5),
        SmartLight(name="Bedroom Light", device_id="SL-001", brightness=40),
        SecurityCamera(name="Front Door Camera", device_id="SC-001"),
    ]
    return devices


def choose_device(devices):
    """Helper to let the user pick which device to act on."""
    print("\nSelect a device:")
    for index, device in enumerate(devices, start=1):
        print(f"  {index}. {device.name} ({device.__class__.__name__})")
    try:
        choice = int(input("Enter device number: "))
        if 1 <= choice <= len(devices):
            return devices[choice - 1]
        print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")
    return None


def display_menu():
    print("\n===== Smart Device Management System =====")
    print("1. Display Device Information")
    print("2. Turn Device On")
    print("3. Turn Device Off")
    print("4. Read Temperature")
    print("5. Adjust Brightness")
    print("6. Start Recording")
    print("7. Exit")


def main():
    devices = build_devices()
    print("Welcome! The following devices have been created for you:")
    for device in devices:
        device.display_info()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            device = choose_device(devices)
            if device:
                device.display_info()

        elif choice == "2":
            device = choose_device(devices)
            if device:
                device.turn_on()

        elif choice == "3":
            device = choose_device(devices)
            if device:
                device.turn_off()

        elif choice == "4":
            sensors = [d for d in devices if isinstance(d, TemperatureSensor)]
            if not sensors:
                print("No temperature sensors available.")
                continue
            for sensor in sensors:
                sensor.read_temperature()

        elif choice == "5":
            lights = [d for d in devices if isinstance(d, SmartLight)]
            if not lights:
                print("No smart lights available.")
                continue
            light = lights[0] if len(lights) == 1 else choose_device(lights)
            if light:
                action = input("Type 'i' to increase or 'd' to decrease brightness: ").strip().lower()
                if action == "i":
                    light.increase_brightness()
                elif action == "d":
                    light.decrease_brightness()
                else:
                    print("Invalid option.")

        elif choice == "6":
            cameras = [d for d in devices if isinstance(d, SecurityCamera)]
            if not cameras:
                print("No security cameras available.")
                continue
            camera = cameras[0] if len(cameras) == 1 else choose_device(cameras)
            if camera:
                camera.start_recording()

        elif choice == "7":
            print("Exiting Smart Device Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 7.")


if __name__ == "__main__":
    main()
