from random import randint, choice
from time import sleep
import os

from characters import Knight, Archer, Mage, MeleeGoblin, RangedGoblin
from stats import *

class Game:
    def __init__(self):
        self.player = None
        self.enemies = []
        self.level = 1
        self.turn = 0
    
    def select_character(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("Select your character:")
            print(f"1. Knight(HP: {KNIGHT_HP}, Damage: {KNIGHT_DAMAGE_RANGE}, Armor: {KNIGHT_ARMOR}, Range: {KNIGHT_RANGE})")
            print(f"2. Archer(HP: {ARCHER_HP}, Damage: {ARCHER_ATTACK_RANGE}, Armor: {ARCHER_ARMOR}, Range: {ARCHER_RANGE})")
            print(f"3. Mage(HP: {MAGE_HP}, Damage: {MAGE_ATTACK_RANGE}, Armor: {MAGE_ARMOR}, Range: {MAGE_RANGE})")
            
            choice = input("Enter the number of your choice: ").strip().lower()
            
            if choice == "1" or choice == "knight":
                name = input("Enter your Knight's name: ")
                self.player = Knight(name)
                return
            elif choice == "2" or choice == "archer":
                name = input("Enter your Archer's name: ")
                self.player = Archer(name)
                return
            elif choice == "3" or choice == "mage":
                name = input("Enter your Mage's name: ")
                self.player = Mage(name)
                return
            else:
                input("Invalid choice, try again.")
                
    def start_screen(self):
        print("Welcome to the RPG Game!")
        print("Defeat all enemies to progress through levels.")
        input("Press Enter to start the game...\n")
    
    def initialize_enemies(self):
        for _ in range(self.level):
            enemy_type = choice([MeleeGoblin, RangedGoblin])
            self.enemies.append(enemy_type())
        self.enemies.sort(key=lambda enemy: enemy.position)

    def refresh_player(self):
        self.player.refresh_attributes()

    def change_level(self):
        self.level += 1
        self.enemies.clear()
    
    def show_battle_info(self):
        os.system("cls" if os.name == "nt" else "clear") 
        print(f"--- Level {self.level} ---")
        print(f"Player: {self.player.player_name}")
        print(f"Class: {self.player.name}")
        print(f"  HP: {self.player.hp}/{self.player.MAX_HP}")
        print(f"  Armor: {self.player.armor}")
        print(f"  Position: {self.player.position}")
        print("\nEnemies:")
        for idx, enemy in enumerate(self.enemies, start=1):
            status = "Alive" if enemy.is_alive() else "Dead"
            print(f" {idx}. {enemy.name} ({status})")
            print(f"    HP: {enemy.hp}, Armor: {enemy.armor}, Position: {enemy.position}")
        print("\n" + "-"*30 + "\n")

    def fight(self):
        while self.player.is_alive() and any([enemy.is_alive() for enemy in self.enemies]):
            self.show_battle_info()
            
            # Player Turn
        
            target = self.enemies[0]
            
            if target:
                choice = input(f"It is your turn!\nEnter one of the moves:{self.player.ACTIONS}\n").strip().lower()
                if choice not in self.player.ACTIONS:
                    input("Invalid move! Try again.")
                    continue

                self.player.do_action(choice, target)
                    
                if not target.is_alive():
                    self.enemies.pop(0)

                if self.enemies == []:
                    break

            # Enemy Turn
            input("\nNow turn is in the enemy!")
            for enemy in self.enemies:
                enemy.do_action(self.player)

    def start(self):
        self.start_screen()
        self.select_character()
        print(f"Our Brave Friend {self.player.name} is entering to dangerous Dungeon...")
        
        while True:
            self.initialize_enemies()
            self.fight()
            if self.player.is_alive():
                input(f"Congratulations! You succesfully passed level {self.level}! Going deeper...\n")
                input(f"{self.player.player_name} rested between floors and refrenished!")
                self.refresh_player()
                self.change_level()
            else:
                os.system("cls" if os.name == "nt" else "clear")
                input("You Died!")

            

        
    