from random import randint, choice
from stats import *


class Character:
    def __init__(self, name, hp, damage_range, armor, attack_range, position=0):
        self.name = name
        self.hp = hp
        self.damage_range = damage_range
        self.armor = armor
        self.attack_range = attack_range
        self.position = position
    
    def take_damage(self, dmg):
        if self.armor > 0:
            if dmg <= self.armor:
                self.armor -= dmg
                dmg = 0
            else:
                dmg -= self.armor
                self.armor = 0
        
        self.hp -= dmg

        if self.hp < 0:
            self.hp = 0

    def move_towards(self, target):
        if self.position < target.position:  # Player movement
            self.position += 1
        elif self.position > target.position:  # Enemy movement
            self.position -= 1
        print(f"{self.name} moves to position {self.position} towards {target.name}")
    
    def calculate_distance(self, target):
        distance = abs(self.position - target.position)
        return distance
    
    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}(HP: {self.hp}, Armor: {self.armor})"
    
    def __repr__(self):
        return f"{self.name}(HP: {self.hp}, Armor: {self.armor})"


class Knight(Character):
    ACTIONS = ["attack", "defend", "move"]
    MAX_HP = KNIGHT_HP

    def __init__(self, player_name):
        super().__init__(
            name=KNIGHT_CLASS, 
            hp=KNIGHT_HP, 
            damage_range=KNIGHT_DAMAGE_RANGE, 
            armor=KNIGHT_ARMOR, 
            attack_range=KNIGHT_RANGE
        )
        self.player_name = player_name

    def do_action(self, choice ,target):
        
        if choice == "attack":
            if self.calculate_distance(target) <= self.attack_range:
                dmg = randint(*self.damage_range)
                target.take_damage(dmg)
                print(f"{self.name} attacks {target.name} for {dmg} damage!")
            else:
                self.move_towards(target)
                
        elif choice == "defend":
            self.armor += 10
            print(f"{self.name} raises shield, increasing armor to {self.armor}!")

        elif choice == "move":
            self.position += 1
            print(f"{self.name} moves forward to position {self.position}!")
        
        else:
            print("Please choose a valid action")
            
    def refresh_attributes(self):
        self.hp = KNIGHT_HP
        self.armor = KNIGHT_ARMOR
        self.position = 0
   
class Archer(Character):
    ACTIONS = ["attack", "evade"]
    MAX_HP = ARCHER_HP

    def __init__(self, player_name):
        super().__init__(
            name=ARCHER_CLASS, 
            hp=ARCHER_HP, 
            damage_range=ARCHER_ATTACK_RANGE, 
            armor=ARCHER_ARMOR, 
            attack_range=ARCHER_RANGE
        )
        self.player_name = player_name
        self.evade = 0

    def do_action(self, choice, target):

        if choice == "attack":
            if self.calculate_distance(target) <= self.attack_range:
                dmg = randint(*self.damage_range)
                target.take_damage(dmg)
                print(f"{self.name} shoots an arrow at {target.name} for {dmg} damage!")
            else:
                self.move_towards(target)
            
        elif choice == "evade":
            self.evade = 1
            print(f"{self.name} is ready to evade the next attack!")
        
        else:
            print("Please choose a valid action")
    
    def take_damage(self, dmg):
        if not self.evade:
            if self.armor > 0:
                if dmg <= self.armor:
                    self.armor -= dmg
                    return
                else:
                    dmg -= self.armor
                    self.armor = 0
            
            self.hp -= dmg

            if self.hp < 0:
                self.hp = 0
            return
        
        print(f"{self.name} evaded the attack!")
        self.evade = 0

    def refresh_attributes(self):
        self.hp = ARCHER_HP
        self.armor = ARCHER_ARMOR
        self.position = 0

    
class Mage(Character):
    ACTIONS = ["fireball", "heal", "move"]
    MAX_HP = MAGE_HP

    def __init__(self, player_name):
        super().__init__(
            name=MAGE_CLASS, 
            hp=MAGE_HP, 
            damage_range=MAGE_ATTACK_RANGE, 
            armor=MAGE_ARMOR, 
            attack_range=MAGE_RANGE
        )
        self.player_name = player_name
    
    def do_action(self, choice, target):
        if choice == "fireball":
            if self.calculate_distance(target) <= self.attack_range:
                dmg = randint(*self.damage_range)
                target.take_damage(dmg)
                print(f"{self.name} casts Fireball on {target.name} for {dmg} damage!")
            else:
                self.move_towards(target)
        
        elif choice == "heal":
            self.hp += MAGE_HEAL
            if self.hp > self.MAX_HP:
                self.hp = self.MAX_HP
                print("HP is full!")
            else:
                print(f"{self.name} healed 20 HP!")
        
        elif choice == "move":
            self.position += 1
            print(f"{self.name} moves forward to position {self.position}!")

        else:
            print("Please choose a valid action")

    def refresh_attributes(self):
        self.hp = MAGE_HP
        self.armor = MAGE_ARMOR
        self.position = 0


class MeleeGoblin(Character):
    def __init__(self):
        super().__init__(
            name=MELEE_GOBLIN_NAME, 
            hp=MELEE_GOBLIN_HP, 
            damage_range=MELEE_GOBLIN_ATTACK_RANGE, 
            armor=MELEE_GOBLIN_ARMOR, 
            attack_range=MELEE_GOBLIN_RANGE
        )
        self.position = randint(*MELEE_GOBLIN_POSITION_RANGE)
    
    def do_action(self, target):
        
        if self.calculate_distance(target) <= self.attack_range:
            dmg = randint(*self.damage_range)
            target.take_damage(dmg)
            input(f"{self.name} attacks {target.name} for {dmg} damage!")

        else:
            self.move_towards(target)
            


class RangedGoblin(Character):
    def __init__(self):
        super().__init__(
            name=RANGED_GOBLIN_NAME, 
            hp=RANGED_GOBLIN_HP, 
            damage_range=RANGED_GOBLIN_ATTACK_RANGE,
            armor=RANGED_GOBLIN_ARMOR,
            attack_range=RANGED_GOBLIN_RANGE
        )
        self.position = randint(*RANGED_GOBLIN_POSITION_RANGE)


    def do_action(self, target):
        
        if self.calculate_distance(target) <= self.attack_range:
            dmg = randint(*self.damage_range)
            input(f"{self.name} throws rock at {target.name} for {dmg} damage!")
            target.take_damage(dmg)
            

        else:
            self.move_towards(target)
        
