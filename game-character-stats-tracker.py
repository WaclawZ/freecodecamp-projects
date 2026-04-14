class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, new_health):
        if new_health > 100 or new_health < 0:
            raise ValueError("Health must be a value greater than 0 and lesser than 100")
        self._health = new_health

    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, new_mana):
        if new_mana > 50 or new_mana < 0:
            raise ValueError("Mana must be a value greater than 0 and lesser than 60")
        self._mana = new_mana