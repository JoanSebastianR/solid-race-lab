from engine.track import Track


class SportsCar:
    symbol = "\U0001F3CE"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 6


class DeliveryVan:
    symbol = "\U0001F690"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 3


class RocketSled:
    symbol = "\U0001F680"

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += 10


class Race:
    def __init__(self, racers, track=None):
        self.racers = racers
        self.track = track if track else Track(length=30)

    def start(self):
        return self.track.run(self.racers)


def main():
    roster_a = [SportsCar("Flash"), DeliveryVan("Steady Eddie")]
    Race(roster_a).start()

    roster_b = [RocketSled("Comet"), DeliveryVan("Steady Eddie II")]
    Race(roster_b).start()


if __name__ == "__main__":
    main()
