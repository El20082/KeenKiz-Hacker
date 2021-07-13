
'''
Hobbit:
100hp
10dmg
100speed

Elf:
150hp
20dmg
50speed

Dwarf:
150hp
50dmg
10speed

Orc:
150hp
50dmg
25speed

'''

# Parent Character class
class Character():

    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
        
    def attack(self, enemy):
        enemy.health = enemy.health - self.damage

    def heal(self, potion):
        self.health = self.health + potion

    def buff_attack(self, potion):
        self.damage = self.damage + potion

# Hobbit class
class Hobbit(Character):

    def __init__(self, health, damage, speed):
        super(Hobbit, self).__init__(health, damage, speed)

# Elf class
class Elf(Character):

    def __init__(self, health, damage, speed):
        super(Elf, self).__init__(health, damage, speed)

    def double_damange_shot(self, enemy):
        enemy.health = enemy.health - self.damage * 2

    def double_enemy_shot(self, enemy_1, enemy_2):
        self.attack(enemy_1)
        self.attack(enemy_2)

# Dwarf class
class Dwarf(Character):

    def __init__(self, health, damage, speed):
        super(Dwarf, self).__init__(health, damage, speed)

# Orc class
class Orc(Character):

    def __init__(self, health, damage, speed):
        super(Orc, self).__init__(health, damage, speed)

Elf_A = Elf(120, 20, 50)
Elf_B = Elf(120, 20, 50)
Elf_C = Elf(120, 20, 50)

Orc_A = Orc(150, 50, 25)
Orc_B = Orc(150, 50, 25)

Orc_B.attack(Elf_B)
Elf_A.attack(Orc_A)

print(Elf_A.health)
print(Elf_B.health)
print(Elf_C.health)
print(Orc_A.health)
print(Orc_B.health)