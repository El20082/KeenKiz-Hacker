
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


def battle_of_the_green_forest():

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

def battle_of_the_wet_snow_biome():

    potion = 20

    Dwarf_A = Dwarf(150, 50, 10)
    Dwarf_B = Dwarf(150, 50, 10)

    Elf_A = Elf(120, 20, 50)

    Dwarf_B.attack(Elf_A)
    Dwarf_A.attack(Dwarf_B)
    Elf_A.heal(potion)

    print(Dwarf_A.health)
    print(Dwarf_B.health)
    print(Elf_A.health)

def battle_of_grassy_plains():

    Elf_A = Elf(120, 20, 50)
    Elf_B = Elf(120, 20, 50)
    Elf_C = Elf(120, 20, 50)
    Elf_D = Elf(120, 20, 50)

    Hobbit_A = Hobbit(100, 10, 100)

    Dwarf_A = Dwarf(150, 50, 10)

    Orc_A = Orc(150, 50, 25)
    Orc_B = Orc(150, 50, 25)
    Orc_C = Orc(150, 50, 25)
    Orc_D = Orc(150, 50, 25)
    Orc_E = Orc(150, 50, 25)

    # From left to right
    Elf_C.attack(Orc_A)
    Dwarf_A.attack(Orc_A)
    Hobbit_A.attack(Orc_E)

    Orc_A.attack(Elf_A)
    Orc_A.attack(Elf_B)
    Orc_B.attack(Elf_B)
    Orc_D.attack(Orc_A)

    print(Elf_C.health)
    print(Elf_D.health)
    print(Elf_A.health)
    print(Elf_B.health)
    print(Dwarf_A.health)
    print(Hobbit_A.health)
    print(Orc_A.health)
    print(Orc_B.health)
    print(Orc_C.health)
    print(Orc_D.health)
    print(Orc_E.health)

battle_of_grassy_plains()