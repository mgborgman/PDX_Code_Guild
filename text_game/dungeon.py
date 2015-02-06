import random
import math
import sys


rooms = {"red room": "dark and creepy", "blue room": "foggy"}


class Player():
    def __init__(self, name, health=100, attack=3, defense=1):
        self.health = health
        self.attack_damage = 0
        self.defense_block = 0
        self.mana = 10
        self.name = name
        self.defense = defense
        self.attack = attack
        self.is_defending = False

    def do_attack(self, character):
        if character.is_defending:
            self.attack_damage = self.attack + random.randint(1, 10)
            self.attack_damage *= .75
            character.health -= self.attack_damage
        else:
            self.attack_damage = self.attack + random.randint(1, 10)
            character.health -= self.attack_damage
        self.is_defending = False

    def defend(self, character):
        self.defense_block = self.defense + random.randint(1, 10)
        if self.defense_block > character.attack_damage:
            self.is_defending = True
        else:
            print "You can't defend yourself against " + character.name + "!"


class Map():
    def __init__(self, height, width, player_x, player_y, paths):
        self.height = height
        self.width = width
        self.x = player_x
        self.y = player_y
        self.paths = paths

    def move(self, direction):
        if direction == 'n':
            if ((self.x, self.y - 1), (self.x, self.y)) not in self.paths:
                print "Cannot go north"
            else:
                self.y -= 1
        if direction == 's':
            if ((self.x, self.y), (self.x, self.y + 1)) not in self.paths:
                print "Cannot go south"
            else:
                self.y += 1
        if direction == 'e':
            if ((self.x, self.y), (self.x + 1, self.y)) not in self.paths:
                print "Cannot go east"
            else:
                self.x += 1
        if direction == 'w':
            if ((self.x - 1, self.y), (self.x, self.y)) not in self.paths:
                print "Cannot go west"
            else:
                self.x -= 1

    def print_map(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.x == x and self.y == y:
                    sys.stdout.write("[H]")
                else:
                    sys.stdout.write("[ ]")
                if ((x, y), (x + 1, y)) in self.paths:
                    sys.stdout.write("-")
                else:
                    sys.stdout.write(" ")
            print
            for x in range(0, self.width):
                sys.stdout.write(" ")
                if ((x, y), (x, y + 1)) in self.paths:
                    sys.stdout.write("|  ")
                else:
                    sys.stdout.write("   ")
            print


def show_stats(character):
    print "name: " + character.name
    print "health: " + str(character.health)
    print "attack: " + str(character.attack)
    print "defense: " + str(character.defense)
    print "mana: " + str(character.mana)


def heal(character):
    character.health += 5
    character.mana -= 1


def create_player():
    name = raw_input("What is your hero's name? ")
    player = Player(name)
    print show_stats(player)


def create_enemies():
    enemy_names = ['Goblin', 'Troll', 'Orc', 'Dragon Lord']
    for name in enemy_names:
        if name == 'Goblin':
            name = Player(name, 70, 0, 0)
        elif name == 'Troll':
            name = Player(name, 75, 0, 0)
        elif name == 'Orc':
            name = Player(name, 80, 0, 0)
        elif name == 'Dragon Lord':
            name = Player(name, 90, 1, 1)
        print show_stats(name)


def enemy_present():
    present = random.randint(0, 1)
    if present == 1:


def show_map():
    turn = True
    m = Map(4, 4, 0, 0, paths)
    while turn:
        m.print_map()
        direction = raw_input("What direction do you want to move? [n/e/s/w] ")
        m.move(direction)
        turn = False

def game():
    create_enemies()
    create_player()
    show_map()
    




paths = [((0, 0), (1, 0)), ((1, 0), (1, 1)), ((1, 1),
         (2, 1)), ((1, 1), (1, 2)), ((0, 2), (1, 2)), ((1, 2), (2, 2)),
         ((0, 2), (0, 3)), ((0, 3), (1, 3)), ((1, 3), (2, 3)), ((2, 3),
         (3, 3))]



game()









#
#
# player.defend(Goblin)
# Goblin.do_attack(player)
# show_stats(player)
# show_stats(Goblin)
