#Magician.py


from Novice import Novice



class Magician(Novice):
    def __init__(self,username):
        super().__init__(username)
        self.setInt(10)
        self.setVit(5)
        self.setHp(self.getHp() + self.getVit())

    def heal(self):
        self.addHp(self.getInt())
        print(f'{self.getUsername()} performed healing + {self.getInt()}')

    def magicAttack(self,character):
        self.new_damage = self.getDamage() + self.getInt()
        character.reduceHp(self.new_damage)
        print(f'{self.getUsername()} performed magic attack -{self.getDamage()} to {character.getUsername}')

