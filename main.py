import random
import time

class Character:
    def __init__(self, name, health=100, attack_power=10, item=None, lore=""):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.item = item
        self.lore = lore

    def attack(self, opponent):
        damage = random.randint(1, self.attack_power)
        if self.item == "lightsaber":
            damage += 5  # Lightsaber bonus damage
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} with {damage} damage points.")
        time.sleep(1)  # Add a delay for dramatic effect

    def special_ability(self, opponent):
        pass  # Placeholder for special ability

    def defend(self):
        print(f"{self.name} takes a defensive stance, reducing incoming damage.")
        time.sleep(1)  # Add a delay for dramatic effect

class Jedi(Character):
    def special_ability(self, opponent):
        damage = self.attack_power * 2
        if self.item == "Force amulet":
            damage += 10  # Force amulet bonus damage
        opponent.health -= damage
        print(f"{self.name} executes a Force move on {opponent.name}, dealing {damage} damage points!")
        time.sleep(2)  # Add a delay for dramatic effect

class Sith(Character):
    def special_ability(self, opponent):
        damage = self.attack_power * 1.5
        if self.item == "Dark amulet":
            damage += 8  # Dark amulet bonus damage
        opponent.health -= damage
        print(f"{self.name} uses Sith Lightning on {opponent.name}, dealing {damage} damage points!")
        time.sleep(2)  # Add a delay for dramatic effect

class BountyHunter(Character):
    def special_ability(self, opponent):
        damage = random.randint(10, 20)
        if self.item == "Blaster":
            damage += 5  # Blaster bonus damage
        opponent.health -= damage
        print(f"{self.name} fires a blaster shot at {opponent.name}, dealing {damage} damage points!")
        time.sleep(2)  # Add a delay for dramatic effect

class Droid(Character):
    def special_ability(self, opponent):
        damage = self.attack_power
        if self.item == "Electroshock arm":
            damage += 7  # Electroshock arm bonus damage
        opponent.health -= damage
        print(f"{self.name} shocks {opponent.name} with an electric charge, dealing {damage} damage points!")
        time.sleep(2)  # Add a delay for dramatic effect

class Vehicle:
    def __init__(self, name, attack_power=20, lore=""):
        self.name = name
        self.attack_power = attack_power
        self.lore = lore

    def attack(self, opponent):
        damage = random.randint(1, self.attack_power)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} with {damage} damage points.")
        time.sleep(1)  # Add a delay for dramatic effect

class Planet:
    def __init__(self, name, geographical_buff="", lore=""):
        self.name = name
        self.geographical_buff = geographical_buff
        self.lore = lore

jedi_characters = [
    Jedi("Luke Skywalker", health=120, attack_power=12, item="lightsaber", lore="One of the greatest Jedi Knights, trained by Obi-Wan Kenobi and Yoda."),
    Jedi("Obi-Wan Kenobi", health=130, attack_power=14, item="Force amulet", lore="Wise and experienced Jedi Master, mentor to Anakin Skywalker."),
    Jedi("Rey", health=110, attack_power=10, item=None, lore="A scavenger from Jakku, discovered her Force sensitivity and trained under Luke Skywalker.")
]

sith_characters = [
    Sith("Darth Vader", health=140, attack_power=14, item="Dark amulet", lore="Once a heroic Jedi Knight Anakin Skywalker, turned to the dark side and became Sith Lord."),
    Sith("Darth Maul", health=130, attack_power=13, item=None, lore="Zabrak Sith Lord trained by Darth Sidious, known for his double-bladed lightsaber."),
    Sith("Emperor Palpatine", health=150, attack_power=15, item=None, lore="The Sith Lord Darth Sidious, manipulator of the Galactic Empire.")
]

bounty_hunter_characters = [
    BountyHunter("Boba Fett", health=100, attack_power=15, item="Blaster", lore="Notorious Mandalorian bounty hunter, known for his iconic armor and skills."),
    BountyHunter("Cad Bane", health=110, attack_power=12, item=None, lore="Ruthless Duros bounty hunter, specializing in kidnapping and assassination."),
    BountyHunter("IG-88", health=120, attack_power=14, item=None, lore="Lethal assassin droid, one of the most deadly bounty hunters in the galaxy.")
]

droid_characters = [
    Droid("R2-D2", health=80, attack_power=8, item="Electroshock arm", lore="Astro-mech droid and loyal companion to many heroes of the Rebellion and Resistance."),
    Droid("C-3PO", health=90, attack_power=9, item=None, lore="Protocol droid fluent in over six million forms of communication, often found in the midst of galactic adventures."),
    Droid("BB-8", health=100, attack_power=10, item=None, lore="Brave and resourceful astromech droid, carrying vital information for the Resistance.")
]
# Define geographical buffs for each character class
jedi_buffs = {
    "Dagobah": "Enhanced connection to the Force, increasing attack power by 20%.",
    "Coruscant": "Access to Jedi archives, gaining knowledge to boost defense by 30%."
}

sith_buffs = {
    "Mustafar": "Fueled by dark side energies, attack power increased by 25%.",
    "Korriban": "Home of the Sith, gain strength from the ancient Sith temples, increasing health by 20%."
}

bounty_hunter_buffs = {
    "Tatooine": "Knowledge of the desert terrain grants tactical advantage, increasing attack power by 15%.",
    "Nar Shaddaa": "Connections in the criminal underworld provide access to better equipment, increasing defense by 20%."
}

droid_buffs = {
    "Kashyyyk": "Blend in with the native environment, gaining camouflage to reduce damage taken by 25%.",
    "Mechis III": "Access to advanced droid technology, increasing attack power by 20%."
}

# Create planets with lore and geographical buffs
planets = [
    Planet("Dagobah", geographical_buff=jedi_buffs["Dagobah"], lore="Swampy planet strong in the Force, once home to Yoda."),
    Planet("Coruscant", geographical_buff=jedi_buffs["Coruscant"], lore="Capital of the Galactic Republic and later the Galactic Empire."),
    Planet("Mustafar", geographical_buff=sith_buffs["Mustafar"], lore="Volcanic planet where Anakin Skywalker fought Obi-Wan Kenobi."),
    Planet("Korriban", geographical_buff=sith_buffs["Korriban"], lore="Ancient homeworld of the Sith species, steeped in dark side energy."),
    Planet("Tatooine", geographical_buff=bounty_hunter_buffs["Tatooine"], lore="Desert planet known for its pod racing and criminal activity."),
    Planet("Nar Shaddaa", geographical_buff=bounty_hunter_buffs["Nar Shaddaa"], lore="Smuggler's moon, home to numerous criminal organizations."),
    Planet("Kashyyyk", geographical_buff=droid_buffs["Kashyyyk"], lore="Homeworld of the Wookiees, covered in dense forests."),
    Planet("Mechis III", geographical_buff=droid_buffs["Mechis III"], lore="Industrial planet known for droid manufacturing and research.")
]
vehicles = [
    Vehicle("X-Wing Fighter", attack_power=25, lore="Versatile starfighter used by the Rebel Alliance and Resistance."),
    Vehicle("TIE Fighter", attack_power=22, lore="Iconic starfighter employed by the Galactic Empire and First Order."),
    Vehicle("Millennium Falcon", attack_power=30, lore="Legendary Corellian freighter, famously piloted by Han Solo and Chewbacca.")
]
# Combine all characters, vehicles, and planets
all_entities = jedi_characters + sith_characters + bounty_hunter_characters + droid_characters + vehicles + planets

def lightsaber_duel(character1, character2):
    print(f"\n***A duel begins between {character1.name} and {character2.name}!***\n")
    print(f"**{character1.lore}\n\n{character2.lore}**\n")
    while character1.health > 0 and character2.health > 0:
        time.sleep(1)  # Add a delay for dramatic effect
        print(f"{character1.name}'s health: {character1.health}")
        print(f"{character2.name}'s health: {character2.health}\n")
        print(f"***It's {character1.name}'s turn!***")
        action = random.choice(["attack", "special_ability", "defend", "explore"])
        if action == "attack":
            character1.attack(character2)
        elif action == "special_ability":
            character1.special_ability(character2)
        elif action == "explore":
            explore(character1)
        else:
            character1.defend()

        if character2.health <= 0:
            print(f"\n***{character1.name} wins the duel!***")
            break

        time.sleep(1)  # Add a delay for dramatic effect
        print(f"{character1.name}'s health: {character1.health}")
        print(f"{character2.name}'s health: {character2.health}\n")
        print(f"***It's {character2.name}'s turn!***")
        action = random.choice(["attack", "special_ability", "defend", "explore"])
        if action == "attack":
            character2.attack(character1)
        elif action == "special_ability":
            character2.special_ability(character1)
        elif action == "explore":
            explore(character2)
        else:
            character2.defend()

        if character1.health <= 0:
            print(f"\n***{character2.name} wins the duel!***")
            break

def explore(character):
    print(f"\n***{character.name} explores the surroundings...***\n")
    time.sleep(2)
    event = random.choice(["nothing", "find_item", "find_entity"])
    if event == "nothing":
        print("***Nothing of interest found.***")
    elif event == "find_item":
        found_item = random.choice(["medkit", "weapon"])
        print(f"***{character.name} found a {found_item}!***")
    else:
        found_entity = random.choice(all_entities)
        if isinstance(found_entity, Character):
            if found_entity != character:
                print(f"\n***{character.name} encounters {found_entity.name}!***")
                if isinstance(found_entity, Jedi) or isinstance(found_entity, BountyHunter):
                    print(f"\n***{found_entity.name} decides to join {character.name} in the fight!***")
                    lightsaber_duel(character, found_entity)
                else:
                    print(f"\n***{found_entity.name} is not interested in helping.***")
            else:
                print("***It's just another version of yourself. Weird.***")
        
        else:
            print(f"\n***{character.name} arrives at {found_entity.name}!***")
            print(f"***{found_entity.name}: {found_entity.geographical_buff}***")
            time.sleep(2)  # Add a delay for dramatic effect

# Randomly select two characters for the lightsaber duel
character1, character2 = random.sample(jedi_characters + sith_characters + bounty_hunter_characters + droid_characters, 2)

# Start the lightsaber duel
lightsaber_duel(character1, character2)