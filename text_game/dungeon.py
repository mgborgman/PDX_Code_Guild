import random
import math


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

    def defend(self,character):
        self.defense_block = self.defense + random.randint(1, 10)
        if self.defense_block > character.attack_damage:
            self.is_defending = True
        else:
            print "You can't defend yourself against "+character.name+"!"


def show_stats(character):
    print "name: " + character.name
    print "health: " + str(character.health)
    print "attack: " + str(character.attack_damage)
    print "defense: " + str(character.defense_block)
    print "mana: " + str(character.mana)


def heal(character):
    character.health += 5
    character.mana -= 1


Goblin = Player('goblin', 75, 0, 0)
name = raw_input("What is your hero's name? ")
player = Player(name)
player.defend(Goblin)
Goblin.do_attack(player)
show_stats(player)
show_stats(Goblin)
