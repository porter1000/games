import random
import pickle

class Character:
    def __init__(self, name, attributes, special_abilities, starting_location, age=0):
        self.name = name
        self.attributes = attributes
        self.special_abilities = special_abilities
        self.starting_location = starting_location
        self.credits = 100  # Starting credits
        self.current_location = starting_location
        self.missions = []
        self.inventory = {}
        self.age = age
        self.houses = []
        self.businesses = []
        self.relationships = {}

    def attack(self, target):
        damage = random.randint(1, self.attributes['Attack Power'])
        target.attributes['Health'] -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage.")

    def heal(self):
        heal_amount = random.randint(5, 15)
        self.attributes['Health'] = min(self.attributes['Health'] + heal_amount, 100)
        print(f"{self.name} heals for {heal_amount} health points.")

    def defend(self):
        defense_bonus = random.randint(1, 5)
        self.attributes['Defense'] += defense_bonus
        print(f"{self.name} braces for impact, increasing Defense by {defense_bonus}.")

    def add_to_inventory(self, item, quantity=1):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        print(f"{self.name} obtained {quantity} {item}.")

    def age_up(self):
        self.age += 1
        print(f"{self.name} is now {self.age} year(s) old.")

    def build_house(self):
        if self.can_afford('House'):
            new_house = House()
            self.houses.append(new_house)
            self.credits -= new_house.cost
            print(f"{self.name} built a new house.")
        else:
            print(f"{self.name} does not have enough credits to build a house.")

    def start_business(self):
        if self.can_afford('Business'):
            new_business = Business()
            self.businesses.append(new_business)
            self.credits -= new_business.cost
            print(f"{self.name} started a new business.")
        else:
            print(f"{self.name} does not have enough credits to start a business.")

    def earn_credits(self, amount):
        self.credits += amount
        print(f"{self.name} earned {amount} credits.")

    def can_afford(self, item):
        if item == 'House':
            return self.credits >= House.cost
        elif item == 'Business':
            return self.credits >= Business.cost
        else:
            return False

class Pioneer(Character):
    def __init__(self, name, attributes, special_abilities, starting_location, age=0):
        super().__init__(name, attributes, special_abilities, starting_location, age)

class Cowboy(Character):
    def __init__(self, name, attributes, special_abilities, starting_location, age=0):
        super().__init__(name, attributes, special_abilities, starting_location, age)

class NativeWarrior(Character):
    def __init__(self, name, attributes, special_abilities, starting_location, age=0):
        super().__init__(name, attributes, special_abilities, starting_location, age)

class Frontiersman(Character):
    def __init__(self, name, attributes, special_abilities, starting_location, age=0):
        super().__init__(name, attributes, special_abilities, starting_location, age)


class House:
    cost = 100

    def __init__(self):
        self.size = random.choice(['Small', 'Medium', 'Large'])
        self.condition = 100
        self.expansion_level = 1

    def upgrade(self):
        if self.expansion_level < 3:
            self.expansion_level += 1
            print("House expanded!")

class Business:
    cost = 200

    def __init__(self):
        self.type = random.choice(['Saloon', 'General Store', 'Blacksmith', 'Hotel'])
        self.condition = 100
        self.expansion_level = 1

    def upgrade(self):
        if self.expansion_level < 3:
            self.expansion_level += 1
            print("Business expanded!")

class Location:
    def __init__(self, name, description, events, npcs=None):
        self.name = name
        self.description = description
        self.events = events
        self.npcs = npcs if npcs else []

    def explore(self):
        print(f"You are at {self.name}: {self.description}")
        for event in self.events:
            print(event)

    def add_npc(self, npc):
        self.npcs.append(npc)

    def remove_npc(self, npc):
        if npc in self.npcs:
            self.npcs.remove(npc)

class Mission:
    def __init__(self, title, description, required_archetype, reward):
        self.title = title
        self.description = description
        self.required_archetype = required_archetype
        self.reward = reward
        self.completed = False

    def complete(self):
        self.completed = True
        print(f"Mission '{self.title}' completed! You earned {self.reward} credits.")

class NPC:
    def __init__(self, name, dialogue, missions):
        self.name = name
        self.dialogue = dialogue
        self.missions = missions

    def offer_mission(self, player):
        for mission in self.missions:
            if not mission.completed and mission.required_archetype == player.__class__.__name__:
                accept = input(f"{self.name}: {self.dialogue} Do you accept this mission? (yes/no): ").lower()
                if accept == "yes":
                    player.missions.append(mission)
                    print(f"You accepted the mission: {mission.title}")
                else:
                    print("Mission declined.")

    def dialogue(self):
        print(f"{self.name}: {self.dialogue}")

class Relationship:
    def __init__(self, npc, level=0):
        self.npc = npc
        self.level = level

    def increase_level(self):
        self.level += 1

    def decrease_level(self):
        self.level -= 1

class Bartender(NPC):
    def __init__(self, name, dialogue, missions):
        super().__init__(name, dialogue, missions)

class Blacksmith(NPC):
    def __init__(self, name, dialogue, missions):
        super().__init__(name, dialogue, missions)

class NativeChief(NPC):
    def __init__(self, name, dialogue, missions):
        super().__init__(name, dialogue, missions)

class Outlaw(NPC):
    def __init__(self, name, dialogue, missions):
        super().__init__(name, dialogue, missions)

def populate_npcs(locations):
    for location in locations.values():
        if location.name == "Saloons and Gambling Dens":
            bartender = Bartender("Bartender Bob", "Welcome to the saloon! Care for a drink?", [])
            location.add_npc(bartender)
            outlaw_mission = Mission("Clear Outlaws", "Outlaws have been causing trouble. Can you take care of them?", "Cowboy", 50)
            outlaw = Outlaw("Dangerous Dan", "I heard there's a bounty on my head. What are you gonna do about it?", [outlaw_mission])
            location.add_npc(outlaw)
        elif location.name == "Trading Post":
            blacksmith = Blacksmith("Smithy", "Need anything forged? I'm your man.", [])
            location.add_npc(blacksmith)
            trade_mission = Mission("Trade Deal", "We need supplies from the next town. Can you help us with the trade?", "Pioneer", 50)
            chief = NativeChief("Chief Running Bear", "Our people are in need of aid. Will you help us?", [trade_mission])
            location.add_npc(chief)

def create_character():
    print("Character Creation")
    name = input("Enter your character's name: ")

    attributes = {'Health': 100, 'Attack Power': 20, 'Defense': 10, 'Speed': 15}  # Initial attributes setup

    print("\nChoose your archetype:")
    print("1. Pioneer")
    print("2. Cowboy")
    print("3. Native Warrior")
    print("4. Frontiersman")
    archetype_choice = input("Enter the number of your chosen archetype: ")

    special_abilities = []
    starting_location = None

    if archetype_choice == "1":
        special_abilities = ['Homestead Building', 'Trailblazing']
        starting_location = Location("Homestead", "Your family's homestead on the prairie.", [])
        character_class = Pioneer
    elif archetype_choice == "2":
        special_abilities = ['Quick Draw', 'Horse Riding']
        starting_location = Location("Saloons and Gambling Dens", "A rowdy place full of cowboys and outlaws.", [])
        character_class = Cowboy
    elif archetype_choice == "3":
        special_abilities = ['Stealth', 'Spear Mastery']
        starting_location = Location("Native American Reservation", "Home to indigenous tribes trying to preserve their way of life.", [])
        character_class = NativeWarrior
    elif archetype_choice == "4":
        special_abilities = ['Survival Skills', 'Trapping']
        starting_location = Location("Frontier Town", "A small settlement trying to make a living on the edge of civilization.", [])
        character_class = Frontiersman

    character = character_class(name, attributes, special_abilities, starting_location)
    print(f"Character created: {name}, Archetype: {character_class.__name__}, Attributes: {attributes}, Special Abilities: {special_abilities}, Starting Location: {starting_location.name}")
    return character

def explore_location(player):
    current_location = player.current_location
    print(f"\nExploring {current_location.name}: {current_location.description}")
    current_location.explore()

def interact_with_npcs(player):
    current_location = player.current_location
    print(f"\nInteracting with NPCs at {current_location.name}:")
    for npc in current_location.npcs:
        npc.dialogue()
        npc.offer_mission(player)

def complete_missions(player):
    for mission in player.missions:
        if not mission.completed:
            mission.complete()
            player.earn_credits(mission.reward)

def travel_between_locations(player, regions):
    print("\nChoose a location to travel:")
    index = 1
    for region_name, locations in regions.items():
        print(f"\n{region_name}:")
        for location in locations:
            print(f"{index}. {location.name}")
            index += 1

    chosen_location_index = int(input("\nEnter the number of your chosen location: "))
    total_locations = sum(len(locations) for locations in regions.values())
    if 1 <= chosen_location_index <= total_locations:
        index = 1
        for region_name, locations in regions.items():
            for location in locations:
                if index == chosen_location_index:
                    player.current_location = location
                    print(f"\nTraveling to {location.name} in {region_name}...")
                    return
                index += 1
    else:
        print("Invalid location choice.")

def save_game(player):
    with open("save_game.pickle", "wb") as save_file:
        pickle.dump(player, save_file)
    print("Game saved successfully.")

def load_game():
    try:
        with open("save_game.pickle", "rb") as save_file:
            player = pickle.load(save_file)
        print("Game loaded successfully.")
        return player
    except FileNotFoundError:
        print("No saved game found.")
        return None

def main():
    print("Welcome to the American Frontier Adventure Game!")

    load_choice = input("Do you want to load a saved game? (yes/no): ").lower()
    if load_choice == "yes":
        player = load_game()
        if not player:
            player = create_character()
    else:
        player = create_character()

    regions = {
        "Wild West": [
            Location("Saloons and Gambling Dens", "A rowdy place full of cowboys and outlaws.", []),
            Location("Frontier Town", "A small settlement trying to make a living on the edge of civilization.", []),
            Location("Native American Reservation", "Home to indigenous tribes trying to preserve their way of life.", []),
            Location("Gold Mine", "A source of wealth and danger for those seeking their fortune.", [])
        ],
        "Prairie": [
            Location("Homestead", "A family farm struggling against the harsh conditions of the prairie.", []),
            Location("Bison Herd", "Massive herds of bison roam the plains, a vital resource for survival.", []),
            Location("Trading Post", "A hub of commerce and interaction between settlers and natives.", []),
            Location("Tornado Alley", "A dangerous region prone to devastating storms.", [])
        ],
        # Define more regions as needed
    }

    populate_npcs(regions)
    player.current_location = player.starting_location
    while True:
        print("\nOptions:")
        print("1. Explore current location")
        print("2. Interact with NPCs")
        print("3. Complete Missions")
        print("4. Travel to another location")
        print("5. Heal")
        print("6. Defend")
        print("7. Attack")
        print("8. Build House")
        print("9. Start Business")
        print("10. Save game")
        print("11. Quit game")
        choice = input("\nEnter the number of your choice: ")

        if choice == "1":
            explore_location(player)
        elif choice == "2":
            interact_with_npcs(player)
        elif choice == "3":
            complete_missions(player)
        elif choice == "4":
            travel_between_locations(player, regions)
        elif choice == "5":
            player.heal()
        elif choice == "6":
            player.defend()
        elif choice == "7":
            print("Select a target to attack:")
            for npc in player.current_location.npcs:
                print(f"{npc.name}")
            target_name = input("Enter the name of the target: ")
            target = None
            for npc in player.current_location.npcs:
                if npc.name.lower() == target_name.lower():
                    target = npc
                    break
            if target:
                player.attack(target)
            else:
                print("Target not found.")
        elif choice == "8":
            player.build_house()
        elif choice == "9":
            player.start_business()
        elif choice == "10":
            save_game(player)
        elif choice == "11":
            print("Quitting game...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")

if __name__ == "__main__":
    main()
