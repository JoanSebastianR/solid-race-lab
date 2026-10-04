"""
Exercise 2 - Open/Closed Principle (OCP)

Vehicle, Car and Truck below are COMPLETE and WORKING -- treat them as
"closed for modification". Do not change them (or Track).

YOUR TASK: implement Motorcycle and Bicycle purely by EXTENSION (new
subclasses of Vehicle), so the race in main() ends up showing four very
different movement patterns:

  - Motorcycle: fast but erratic -- its step size should vary a lot from
    tick to tick (e.g. sometimes a small wobble, sometimes a big burst).
  - Bicycle: starts strong but gets slower over time as the rider tires
    out (its step size should shrink, but never drop below 1).

If finishing this exercise ever makes you want to edit Vehicle, Car,
Truck or Track, that's a sign your design isn't using OCP yet --
polymorphism (new subclasses) should be enough.

Run it to watch the race:
    python -m exercises.ex2_ocp

Check your work:
    pytest tests/test_ex2_ocp.py -v
"""
import random

from engine.track import Track


class Vehicle:
    """Base type every racer in this exercise extends."""

    symbol = "?"

    def __init__(self, name: str):
        self.name = name
        self.position = 0

    def move(self) -> None:
        raise NotImplementedError


class Car(Vehicle):
    symbol = "\U0001F697"

    def move(self) -> None:
        self.position += 4


class Truck(Vehicle):
    symbol = "\U0001F69A"

    def move(self) -> None:
        self.position += 2


class Motorcycle(Vehicle):
    symbol = "\U0001F3CD"

    # Small wobbles (1-3) mixed with big bursts (8-10): erratic but always > 0.
    STEPS = (1, 2, 3, 8, 9, 10)

    def move(self) -> None:
        self.position += random.choice(self.STEPS)


class Bicycle(Vehicle):
    symbol = "\U0001F6B2"

    def __init__(self, name: str):
        super().__init__(name)
        self.ticks = 0  # how many times it has pedaled so far (fatigue)

    def move(self) -> None:
        # Starts at 5 and loses 1 every 2 ticks, but never drops below 1.
        step = max(1, 5 - self.ticks // 2)
        self.position += step
        self.ticks += 1


def main():
    vehicles = [
        Car("Red Car"),
        Truck("Big Rig"),
        Motorcycle("Ghost Rider"),
        Bicycle("Pedal Pete"),
    ]
    Track(length=35).run(vehicles)


if __name__ == "__main__":
    main()
