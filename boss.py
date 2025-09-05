from enemy import Enemy
import random

class boss(Enemy):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level
        self.health = 200 + (level * 50)
        self.attack_power = random.randint(10, 25) + (level * 5)

    def roar(self):
        print(f"{self.name} lets out a terrifying roar!")