import random

class Gym:
    def __init__(self):
        self.split = ["push", "pull", "legs"]

    def sort(self, name):
        print(name, "is hitting", random.choice(self.split))

lift = Gym()
lift.sort("zanman")
