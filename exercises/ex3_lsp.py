"""
Exercise 3 - Liskov Substitution Principle (LSP)

Every Vehicle in this module must honor the same contract (see Track's
own docstring/engine.track.Racer): move() always leaves position >= its
previous value, and move() never raises. Track relies on this contract
to run any race safely -- anything that can't honor it should not be a
Vehicle.

UnreliableCar below breaks that contract on purpose: run it a few times
and watch it either crash the race or roll backwards.

YOUR TASK: redesign UnreliableCar's move() so "being unreliable" no
longer violates the contract. Model unreliability as something the
contract allows -- for example, some ticks it simply does not advance
(stays exactly where it is) -- instead of raising or moving backwards.
Do not change the Vehicle base class or Track.

Run it to see the current (broken) behavior:
    python -m exercises.ex3_lsp

Check your work:
    pytest tests/test_ex3_lsp.py -v
"""
import random

from engine.track import Track


class Vehicle:
    """Contract every vehicle here must honor:
    - move() must leave position >= its previous value (never backwards).
    - move() must never raise.
    Any subclass that cannot honor this contract must not be a Vehicle.
    """

    symbol = "?"

    def __init__(self, name: str):
        self.name = name
        self.position = 0

    def move(self) -> None:
        raise NotImplementedError


class SteadyCar(Vehicle):
    symbol = "\U0001F697"

    def move(self) -> None:
        self.position += 4


class UnreliableCar(Vehicle):
    """Unreliable, but it still honors the Vehicle contract.

    Its unreliability is modeled as something the contract ALLOWS:
    some ticks it simply does not advance (position stays exactly the
    same). It never raises and never moves backwards, so Track (or any
    other caller) can use it exactly like any other Vehicle.
    """

    symbol = "\U0001F699"

    def move(self) -> None:
        roll = random.random()
        if roll < 0.15:
            return  # broke down: stays in place instead of raising
        elif roll < 0.30:
            return  # ran out of gas: stays in place instead of rolling back
        else:
            self.position += 5


def main():
    vehicles = [SteadyCar("Reliable Rex"), UnreliableCar("Shaky Sam")]
    Track(length=30).run(vehicles)  # <-- may crash or derail until you fix it


if __name__ == "__main__":
    main()
