import random
import sys


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

    def heal(self):
        self.health += 5
        self.mana -= 1


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
        else:
            print "must enter [n/e/s/w]"

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


paths = [((0, 0), (1, 0)), ((1, 0), (1, 1)), ((1, 1),
                                              (2, 1)), ((1, 1), (1, 2)), ((0, 2), (1, 2)), ((1, 2), (2, 2)),
         ((0, 2), (0, 3)), ((0, 3), (1, 3)), ((1, 3), (2, 3)), ((2, 3),
                                                                (3, 3))]
m = Map(4, 4, 0, 0, paths)


def show_stats(character):
    print "name: " + character.name
    print "health: " + str(character.health)
    print "attack: " + str(character.attack_damage)
    print "defense: " + str(character.defense)
    print "mana: " + str(character.mana)


def create_player():
    name = raw_input("What is your hero's name? ")
    return Player(name)
    print show_stats(player)


def is_present():
    present = random.randint(0, 1)
    if present == 1:
        return True
    else:
        return False


def turn(enemy_present, player, enemy):
    def enemy_turn(enemy, player):
        chance = random.randint(1, 7)

        if chance <= 4:
            enemy.do_attack(player)
        elif chance == 5 or chance == 6:
            enemy.defend(player)
        else:
            enemy.heal()

    if enemy_present:
        if enemy.name == 'Dragon Lord':
            print "You are about to battle The Dragon Lord... Good Luck."

        else:
            print "There's a %s in this room... What will you do? " % enemy.name
        while enemy.health > 0:
            move = raw_input("1. Attack\n"
                             "2. Defend\n"
                             "3. Heal\n")
            if player.health <= 0:
                print "You have failed, the Dragon Lord will take over the world..."
                exit()
            elif move == '1':
                player.do_attack(enemy)
                enemy_turn(enemy, player)
                show_stats(player)
                show_stats(enemy)
            elif move == '2':
                player.defend(enemy)
                show_stats(player)
                show_stats(enemy)
            elif move == '3':
                player.heal()
                show_stats(player)
                show_stats(enemy)
            else:
                print "This room appears to be empty."
        if enemy.name == 'Dragon Lord':
            print "Congratulations! You defeated the Dragon Lord and saved the World!"
            exit()
        else:
            print "You defeated the %s! You are indeed a great warrior. Continue on to the next room." % enemy.name


def show_map(map, enemy_names, player):
    playing = True
    while playing:
        map.print_map()
        direction = raw_input("What direction do you want to move? [n/e/s/w] ")
        map.move(direction)
        enemy_present = is_present()
        if enemy_present:
            enemy = enemy_names.pop()
            turn(enemy_present, player, enemy)
        else:
            playing = True


def game():
    print "You are in a dark dungeon, there are many rooms, but somewhere \n" \
          "within lies the Dragon Lord. Defeating him is the goal of your quest. \n" \
          "Good luck! "
    show_map(m, enemy_names, player)


Goblin = Player("Goblin", 70, 0, 0)
Troll = Player("Troll", 75, 0, 0)
Orc = Player("Orc", 80, 0, 0)
Dragon_Lord = Player("Dragon Lord", 90, 1, 1)


enemy_names = [Dragon_Lord, Orc, Troll, Goblin]
player = create_player()
game()

