# Smart Device Management System

A menu-driven Python console application that models a smart home device management system. Built for **EL 162 / 234 - Object Oriented Programming Mini Project**, it demonstrates the four core OOP pillars: classes/objects, inheritance, encapsulation, and polymorphism.

## OOP Concepts Demonstrated

- **Classes & Objects** — a `SmartDevice` base class with three specialized device types.
- **Inheritance** — `SecurityCamera`, `SmartLight`, and `TemperatureSensor` all inherit shared behavior from `SmartDevice`.
- **Encapsulation** — private attributes (`__device_id`, `__power_status`, `__brightness`) are accessed and validated through `@property` getters/setters.
- **Polymorphism** — each subclass overrides `display_info()` to extend the base implementation with its own details, while `super()` calls preserve the shared logic.

## Device Types

| Device | Class | Key Behavior |
|---|---|---|
| Temperature Sensor | `TemperatureSensor` | Reads an ambient temperature (°C) when powered on |
| Smart Light | `SmartLight` | Adjustable brightness (0–100), validated via a setter |
| Security Camera | `SecurityCamera` | Starts/stops recording; requires power to be ON |

All devices inherit:
- `device_id` — validated on creation and update (cannot be empty)
- `power_status` — read-only outside the class; toggled only via `turn_on()` / `turn_off()`
- `display_info()` — base output, extended by each subclass

## Requirements

- Python 3.x (no external dependencies)

## Usage

Run the script directly:

```bash
python smart_device_system.py
```

On startup, three demo devices are created automatically:
- Living Room Sensor (`TS-001`)
- Bedroom Light (`SL-001`)
- Front Door Camera (`SC-001`)

You'll then see a menu:

```
===== Smart Device Management System =====
1. Display Device Information
2. Turn Device On
3. Turn Device Off
4. Read Temperature
5. Adjust Brightness
6. Start Recording
7. Exit
```

Enter a number to perform that action, and select a device by number when prompted.

## Example Session

```
Welcome! The following devices have been created for you:
Name: Living Room Sensor | Device ID: TS-001 | Power: OFF
    Temperature: 23.5°C
Name: Bedroom Light | Device ID: SL-001 | Power: OFF
    Brightness: 40%
Name: Front Door Camera | Device ID: SC-001 | Power: OFF
    Recording Status: Not Recording

===== Smart Device Management System =====
...
Enter your choice (1-7): 2

Select a device:
  1. Living Room Sensor (TemperatureSensor)
  2. Bedroom Light (SmartLight)
  3. Front Door Camera (SecurityCamera)
Enter device number: 3
[Front Door Camera] is now ON.
```

## Project Structure

```
smart_device_system.py   # All classes and the menu-driven interface
```

## Author

BLANKSON GABRIEL
