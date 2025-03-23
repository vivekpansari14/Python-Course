import random
import time

# Base Character Class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        damage = random.randint(self.attack_power - 2, self.attack_power + 2)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage! 💥")

    def is_alive(self):
        return self.health > 0

    def display_status(self):
        print(f"{self.name} | Health: {self.health} ❤️")


# Subclass: Warrior
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=15)
        self.armor = 5  # Damage reduction

    def attack(self, target):
        print(f"⚔️ {self.name} swings a mighty sword!")
        super().attack(target)

    def take_damage(self, damage):
        reduced_damage = max(damage - self.armor, 0)
        self.health -= reduced_damage
        print(f"{self.name} blocks with armor! Damage taken: {reduced_damage} 🛡️")


# Subclass: Mage
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=20)
        self.mana = 50  # Special energy for magic attacks

    def cast_spell(self, target):
        if self.mana >= 10:
            spell_damage = self.attack_power + random.randint(5, 10)
            target.health -= spell_damage
            self.mana -= 10
            print(f"✨ {self.name} casts a powerful spell on {target.name} for {spell_damage} damage! 🔥")
        else:
            print(f"❌ {self.name} is out of mana!")

    def display_status(self):
        print(f"{self.name} | Health: {self.health} ❤️ | Mana: {self.mana} 🔵")


# Game Loop Simulation
def battle(player1, player2):
    print("\n⚔️ Battle Begins! ⚔️")
    time.sleep(1)

    while player1.is_alive() and player2.is_alive():
        player1.attack(player2)
        if player2.is_alive():
            player2.attack(player1)
        print("\n--- Status Update ---")
        player1.display_status()
        player2.display_status()
        time.sleep(1)

    winner = player1 if player1.is_alive() else player2
    print(f"\n🏆 {winner.name} wins the battle!")


# Creating Characters
hero = Warrior("Arthur")
enemy = Mage("Dark Sorcerer")

# Start Battle
battle(hero, enemy)
