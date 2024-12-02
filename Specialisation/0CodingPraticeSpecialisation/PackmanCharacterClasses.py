from PackmanSuperClass import Entity

class Player(Entity):
    max_health = 100
    def __init__(self, x, y, name, damage ):
        super.__init__(x, y)

    def collision(self):
        self.damage -= Player.max_health

    def game_over(self):
        if Player.max_health == 0:
            print("Game Over")

class Monster(Entity):
    def __init__(self, name, damage):
        super.__init__(name, damage)

    def collision(self):
        self.damage = 15




