import random

class Character:
    def __init__(self, name, attributes, special_abilities, starting_planet):
        self.name = name
        self.attributes = attributes
        self.special_abilities = special_abilities
        self.starting_planet = starting_planet
        self.credits = 0  # Initialize credits attribute

    def attack(self, target):
        damage = random.randint(1, self.attributes['Attack Power'])
        target.attributes['Health'] -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage.")
class Jedi(Character):
    def __init__(self, name, attributes, special_abilities, starting_planet):
        super().__init__(name, attributes, special_abilities, starting_planet)
class Sith(Character):
    def __init__(self, name, attributes, special_abilities, starting_planet):
        super().__init__(name, attributes, special_abilities, starting_planet)
class BountyHunter(Character):
    def __init__(self, name, attributes, special_abilities, starting_planet):
        super().__init__(name, attributes, special_abilities, starting_planet)
class Droid(Character):
    def __init__(self, name, attributes, special_abilities, starting_planet):
        super().__init__(name, attributes, special_abilities, starting_planet)
class Location:
    def __init__(self, name, description, events):
        self.name = name
        self.description = description
        self.events = events

    def explore(self):
        print(f"You are at {self.name}: {self.description}")
        for event in self.events:
            print(event)
def create_character():
    print("Character Creation")
    name = input("Enter your character's name: ")

    # Initial attributes setup
    attributes = {'Health': 10, 'Attack Power': 10, 'Defense': 10, 'Speed': 10}

    # Character class and starting planet choice
    print("\nChoose your class:")
    print("1. Jedi - Starting Planet: Coruscant")
    print("2. Sith - Starting Planet: Korriban")
    print("3. Bounty Hunter - Starting Planet: Tatooine")
    print("4. Droid - Starting Planet: Mechis III")
    class_choice = input("Enter the number of your chosen class: ")

    special_abilities = []
    starting_planet = ""
    if class_choice == "1":
        attributes['Health'] += 20
        attributes['Defense'] += 5
        special_abilities = ['Force Push', 'Lightsaber Mastery']
        starting_planet = "Coruscant"
        character_class = Jedi
    elif class_choice == "2":
        attributes['Attack Power'] += 20
        attributes['Speed'] += 5
        special_abilities = ['Force Lightning', 'Sith Rage']
        starting_planet = "Korriban"
        character_class = Sith
    elif class_choice == "3":
        attributes['Attack Power'] += 15
        attributes['Defense'] += 10
        special_abilities = ['Marksmanship', 'Gadgets']
        starting_planet = "Tatooine"
        character_class = BountyHunter
    elif class_choice == "4":
        attributes['Health'] += 30
        attributes['Defense'] += 15
        special_abilities = ['Repair', 'System Hacking']
        starting_planet = "Mechis III"
        character_class = Droid

    character = character_class(name, attributes, special_abilities, starting_planet)
    print(f"Character created: {name}, Class: {character_class.__name__}, Attributes: {attributes}, Special Abilities: {special_abilities}, Starting Planet: {starting_planet}")
    return character
class Transport:
    def __init__(self, name, description):
        self.name = name
        self.description = description
class Mission:
    def __init__(self, title, description, required_archetype):
        self.title = title
        self.description = description
        self.required_archetype = required_archetype
class NPC:
    def __init__(self, name, dialogue, missions):
        self.name = name
        self.dialogue = dialogue
        self.missions = missions
class Job:

    def __init__(self, title, description, required_archetype, duration, reward, requirements=None):
        self.title = title
        self.description = description
        self.required_archetype = required_archetype
        self.duration = duration
        self.reward = reward
        self.requirements = requirements if requirements else {}
class Planet:
    def __init__(self, name, locations, transports, npcs, jobs):
        self.name = name
        self.locations = locations
        self.transports = transports
        self.npcs = npcs
        self.jobs = jobs

    def display_locations(self, player):
        print(f"Exploring {self.name}: Available locations:")
        for i, location in enumerate(self.locations, 1):
            print(f"{i}. {location.name} - {location.description}")
        choice = int(input("Choose a location to explore: ")) - 1
        if 0 <= choice < len(self.locations):
            self.locations[choice].explore(player)
        else:
            print("Invalid location selection.")

    def display_jobs(self, player):
        # Filter jobs for the player's archetype
        available_jobs = [job for job in self.jobs if job.required_archetype == player.__class__.__name__]

        if not available_jobs:
            print("There are no jobs available for you at the moment.")
            return

        print(f"\nAvailable jobs on {self.name}:")
        for i, job in enumerate(available_jobs, start=1):
            print(f"{i}. {job.title}: {job.description} - Reward: {job.reward} credits")

        job_choice = int(input("Choose a job to work on (enter number): ")) - 1
        if 0 <= job_choice < len(available_jobs):
            self.work(player, available_jobs[job_choice])
        else:
            print("Invalid job selection.")

    def work(self, player, job):
        # Check if player meets the job requirements (if any)
        if all(player.attributes.get(attr, 0) >= value for attr, value in job.requirements.items()):
            print(f"{player.name} starts working on '{job.title}' for {job.duration} hours.")
            # Simulate work duration
            print(f"Work completed! You earned {job.reward} credits.")
            player.credits += job.reward  # Assume player object has a 'credits' attribute
        else:
            print("You do not meet the requirements for this job.")

    def travel(self, player):
        print(f"Welcome to planet {self.name}")
        print("Available transports:")
        for i, transport in enumerate(self.transports, 1):
            print(f"{i}. {transport.name}: {transport.description}")
        choice = int(input("Choose a transport: ")) - 1
        print(f"Boarding {self.transports[choice].name}...")
        # Code to handle travel using the chosen transport

        # Interact with NPCs and offer missions
        self.interact_with_npcs(player)

    def interact_with_npcs(self, player):
        print("\nNPCs on this planet:")
        for npc in self.npcs:
            print(f"{npc.name}: {npc.dialogue}")
            for mission in npc.missions:
                print(f"- {mission.title}: {mission.description}")
                if mission.required_archetype == player.__class__.__name__:
                    accept = input("Do you accept this mission? (yes/no): ").lower()
                    if accept == "yes":
                        # Handle accepting the mission
                        player.add_mission(mission)
                        print(f"You accepted the mission: {mission.title}")
                    else:
                        print("Mission declined.")

        # Interact with NPCs for job assignments
        print("\nJobs available on this planet:")
        for job in self.jobs:
            print(f"- {job.title}: {job.description}")
            if job.required_archetype == player.__class__.__name__:
                accept = input("Do you want to take this job? (yes/no): ").lower()
                if accept == "yes":
                    # Handle job assignment
                    player.add_job(job)
                    print(f"You accepted the job: {job.title}")
                else:
                    print("Job declined.")

        # Additional interactions
        print("\nOther interactions:")
        print("1. Explore the planet")
        print("2. Build bonds with locals")
        print("3. Earn credits through local activities")
        print("4. Leave the planet")

        while True:
            choice = input("Choose an action: ")
            if choice == "1":
                self.explore_planet(player)
            elif choice == "2":
                self.build_bonds(player)
            elif choice == "3":
                self.earn_credits(player)
            elif choice == "4":
                print("Leaving the planet...")
                break
            else:
                print("Invalid choice. Please try again.")

    def explore_planet(self, player):
        print(f"You explore {self.name} and discover new places and secrets.")

    def build_bonds(self, player):
        print("You spend time getting to know the locals and building friendships.")

    def earn_credits(self, player):
        print("You engage in local activities and earn credits.")
def choose_destination(player):
    transports = [
        {"name": "Galactic Shuttle Service", "cost": 100, "risk": 0.05, "risk_entity": "Space Pirates", "travel_time": 2, "description": "Standard, reliable service across the galaxy. Discounts for Droids as navigational aids."},
        {"name": "The Millennium Falcon (Special Charter)", "cost": 150, "risk": 0.04, "risk_entity": "Imperial Entanglements", "travel_time": 1, "description": "Han Solo's legendary ship. Faster travel, with a discount for Bounty Hunters seeking discretion."},
        {"name": "Merchant Freighter Convoy", "cost": 75, "risk": 0.10, "risk_entity": "Pirate Attack", "travel_time": 4, "description": "Travel in numbers for safety. Sith gain a cost reduction due to influence."},
        {"name": "Rebel Blockade Runner", "cost": 130, "risk": 0.07, "risk_entity": "Imperial Blockades", "travel_time": 2, "description": "Fast and stealthy, preferred by those opposing the Empire. Jedi receive a discount."},
        {"name": "Imperial Transport", "cost": 90, "risk": 0.20, "risk_entity": "Rebel Sabotage", "travel_time": 3, "description": "Direct and authoritative, with increased risk from rebel activities. Sith have a risk offset."},
        {"name": "Local Starhopper", "cost": 50, "risk": 0.15, "risk_entity": "Mechanical Failures", "travel_time": 5, "description": "Cheap and cheerful but not the most reliable. Droids get a 50% discount due to their repair capabilities."},
        {"name": "Undercover Smuggler's Ship", "cost": 200, "risk": 0.05, "risk_entity": "Customs Inspection", "travel_time": 1, "description": "Expensive but offers the utmost discretion and speed. Bounty Hunters enjoy a reduced risk."},
        {"name": "Luxury Cruise Liner", "cost": 250, "risk": 0.02, "risk_entity": "Space Weather", "travel_time": 2, "description": "The pinnacle of space travel comfort. Jedi and Sith receive a ceremonial discount."},
    ]


    print("Choose a mode of transport:")
    for i, transport in enumerate(transports, 1):
        print(f"{i}. {transport['name']} - Cost: {transport['cost']} credits, Travel Time: {transport['travel_time']} hours")

    transport_choice = int(input("Enter your choice: ")) - 1
    transport = transports[transport_choice]

    # Check if player can afford the chosen transport
    if player.credits < transport['cost']:
        print(f"You need {transport['cost']} credits to use this transport. You currently have {player.credits} credits.")
        return "not_enough_credits", None

    # Simulate travel risk
    if random.random() < transport['risk']:
        print(f"Travel Alert: You were intercepted by {transport['risk_entity']} during your journey!")
        # Implement handling of interception, e.g., losing additional credits, items, or having to fight.
        return "intercepted", None

    player.credits -= transport['cost']  # Deduct transport cost from player's credits
    print(f"Travel initiated using {transport['name']}...")

    # Assuming the game has a way to select or input the destination planet
    print("Choose your destination planet:")
    for i, planet in enumerate(planets.keys(), 1):
        print(f"{i}. {planet}")
    planet_choice = int(input("Enter your choice: ")) - 1
    destination = list(planets.values())[planet_choice]

    print(f"Arriving at {destination.name} after {transport['travel_time']} hours. You have {player.credits} credits remaining.")
    player.current_planet = destination  # Update player's current planet to the new destination

    return "success", destination
tatooine_locations = [
        Location("Mos Eisley Cantina", "A wretched hive of scum and villainy.", ["Meet Han Solo", "Encounter a Sand Person"]),
        Location("Jedi Temple Ruins", "Remnants of an ancient order.", ["Find a lightsaber crystal", "Battle Sith acolytes"]),
        # Define more locations for Tatooine if needed
    ]

    # Define NPCs for Tatooine
tatooine_npcs = [
        NPC("Han Solo", "Hey there! Looking for some adventure?", []),
        NPC("Jawa Trader", "Utinni! Have a look at my wares.", []),
        # Define more NPCs for Tatooine if needed
    ]
tatooine_transports = [
    Transport("Commercial Shuttle", "Purchase a ticket for a safe and comfortable journey."),
    Transport("Sneak onto a Cargo Ship", "Riskier option but no need to purchase a ticket."),
    # Define more transports for Tatooine if needed
]
tatooine_jobs = [
    # Beginner
    Job("Patrol the Outer Rim", "Keep the outskirts safe from raiders.", "Jedi", 1, 50, {}),
    Job("Artifact Recovery", "Retrieve ancient artifacts from a cave.", "Sith", 1, 50, {}),
    Job("Local Bounty", "Capture a wanted thief hiding in Mos Eisley.", "Bounty Hunter", 1, 50, {}),
    Job("Droid Repair", "Assist in repairing droids at a local shop.", "Droid", 1, 50, {}),
    
    # Intermediate
    Job("Escort Diplomats", "Ensure the safety of diplomats visiting Tatooine.", "Jedi", 2, 100, {}),
    Job("Secrets of the Sith", "Uncover hidden Sith relics in the desert.", "Sith", 2, 100, {}),
    Job("Hunt the Krayt Dragon", "Track and hunt a dangerous Krayt Dragon.", "Bounty Hunter", 2, 100, {}),
    Job("Upgrade the Cantina's Security System", "Implement advanced security protocols.", "Droid", 2, 100, {}),
    
    # Hard
    Job("Negotiate with Tusken Raiders", "Prevent attacks by negotiating a peace treaty.", "Jedi", 4, 200, {}),
    Job("Dark Side Influence", "Spread the influence of the Dark Side among locals.", "Sith", 4, 200, {}),
    Job("Intercept Rebel Smugglers", "Stop smugglers from delivering supplies to the Rebels.", "Bounty Hunter", 4, 200, {}),
    Job("Sabotage Imperial Equipment", "Disrupt Imperial operations discreetly.", "Droid", 4, 200, {}),
]



    # Create planet instance for Tatooine
planet_tatooine = Planet("Tatooine", tatooine_locations, tatooine_transports, tatooine_npcs, tatooine_jobs)
coruscant_locations = [
        Location("Senate Building", "Center of political power.", ["Negotiate with senators", "Encounter a corrupt official"]),
        Location("Galactic Museum", "Showcasing the galaxy's history.", ["Discover ancient artifacts", "Fight off museum thieves"]),
        # Define more locations for Coruscant if needed
    ]

    # Define NPCs for Coruscant
coruscant_npcs = [
        NPC("Senator Amidala", "Welcome to Coruscant. How may I assist you?", []),
        NPC("Underworld Informant", "Psst... Heard you're looking for something.", []),
        # Define more NPCs for Coruscant if needed
    ]
coruscant_transports = [
    Transport("Public Speeder", "Available for hire for quick travel around the city."),
    Transport("Republic Shuttle", "Government-regulated transport between planets."),
    # Define more transports for Coruscant if needed
]
coruscant_jobs = [
    # Beginner
    Job("Patrol the Senate District", "Maintain peace in the Senate District.", "Jedi", 1, 60, {}),
    Job("Infiltrate a Political Rally", "Gather intel at a political gathering.", "Sith", 1, 60, {}),
    Job("Apprehend a Corrupt Official", "Capture a corrupt official for the local authorities.", "Bounty Hunter", 1, 60, {}),
    Job("Data Retrieval", "Retrieve data from a secure government facility.", "Droid", 1, 60, {}),
    
    # Intermediate
    Job("Escort Key Witnesses", "Protect witnesses en route to the Galactic Senate.", "Jedi", 2, 120, {}),
    Job("Undermine Jedi Influence", "Secretly undermine the efforts of the Jedi.", "Sith", 2, 120, {}),
    Job("Track Down a Gang Leader", "Locate and capture a notorious gang leader.", "Bounty Hunter", 2, 120, {}),
    Job("Hack Into the City's Mainframe", "Access confidential information for your employer.", "Droid", 2, 120, {}),
    
    # Hard
    Job("Resolve a Hostage Crisis", "Lead a delicate operation to save hostages.", "Jedi", 4, 240, {}),
    Job("Dark Ritual in the Undercity", "Conduct a forbidden ritual in the depths of Coruscant.", "Sith", 4, 240, {}),
    Job("Eliminate a Rival Syndicate Leader", "Take out the leader of a rival criminal syndicate.", "Bounty Hunter", 4, 240, {}),
    Job("Infiltrate the Jedi Temple Archives", "Steal ancient texts from the Jedi archives.", "Droid", 4, 240, {}),
]
planet_coruscant = Planet("Coruscant", coruscant_locations, coruscant_transports, coruscant_npcs, coruscant_jobs)
naboo_locations = [
        Location("Theed Palace", "Seat of the Naboo monarchy.", ["Meet with Queen Amidala", "Explore the palace gardens"]),
        Location("Swamp Ruins", "Ancient ruins hidden in the swamps.", ["Discover hidden artifacts", "Defend against local creatures"]),
        # Define more locations for Naboo if needed
    ]

    # Define NPCs for Naboo
naboo_npcs = [
        NPC("Queen Amidala", "Greetings, traveler. How may I assist you?", []),
        NPC("Gungan Guide", "Meesa show yousa around, okeday?", []),
        # Define more NPCs for Naboo if needed
    ]
naboo_transports = [
    Transport("Royal Starship", "Luxurious transport fit for royalty."),
    Transport("Gungan Submarine", "Traditional Gungan underwater vehicle."),
    # Define more transports for Naboo if needed
]
naboo_jobs = [
    # Beginner
    Job("Guardian of Theed", "Protect the streets of Theed from petty criminals.", "Jedi", 1, 55, {}),
    Job("Sith Artifact Retrieval", "Recover a Sith artifact from the depths of Naboo.", "Sith", 1, 55, {}),
    Job("Capture a Gungan Outlaw", "Track down a rogue Gungan causing trouble.", "Bounty Hunter", 1, 55, {}),
    Job("Repair Gungan Technology", "Assist in repairing Gungan tech that's malfunctioning.", "Droid", 1, 55, {}),
    
    # Intermediate
    Job("Secure Trade Routes", "Ensure that trade routes to Naboo are safe from pirates.", "Jedi", 2, 110, {}),
    Job("Influence Gungan Politics", "Covertly sway Gungan politics to favor Sith interests.", "Sith", 2, 110, {}),
    Job("Eliminate a Political Rival", "Discreetly remove a rival threatening peace talks.", "Bounty Hunter", 2, 110, {}),
    Job("Upgrade Theed's Defense Systems", "Implement advanced defense systems for Naboo.", "Droid", 2, 110, {}),
    
    # Hard
    Job("Mediate a Dispute", "Resolve a land dispute between Naboo settlers and the Gungans.", "Jedi", 4, 220, {}),
    Job("Dark Side Corruption", "Spread the influence of the Dark Side among key Naboo officials.", "Sith", 4, 220, {}),
    Job("High-Profile Kidnapping", "Kidnap a prominent figure for ransom without leaving traces.", "Bounty Hunter", 4, 220, {}),
    Job("Subvert Naboo's Security", "Infiltrate and subvert Naboo's citywide security network.", "Droid", 4, 220, {}),
]
planet_naboo = Planet("Naboo", naboo_locations, naboo_transports, naboo_npcs, naboo_jobs)
kashyyyk_locations = [
        Location("Wookiee Village", "Home of the mighty Wookiees.", ["Assist in a traditional Wookiee ceremony", "Explore the forests"]),
        Location("Imperial Outpost", "Imperial presence in the shadow of the trees.", ["Infiltrate the outpost", "Rescue imprisoned Wookiees"]),
        # Define more locations for Kashyyyk if needed
    ]

    # Define NPCs for Kashyyyk
kashyyyk_npcs = [
        NPC("Chieftain Grrooarrgg", "Welcome, outsider. What brings you to our home?", []),
        NPC("Imperial Officer", "This area is restricted. Move along.", []),
        # Define more NPCs for Kashyyyk if needed
    ]
kashyyyk_transports = [
    Transport("Wookiee Starcruiser", "Built to withstand the rigors of space travel."),
    Transport("Canopy Speeder", "Navigate the dense forest from the treetops."),
    # Define more transports for Kashyyyk if needed
]
kashyyyk_jobs = [
    # Beginner
    Job("Wookiee Village Defense", "Help defend a Wookiee village from Trandoshan slavers.", "Jedi", 1, 65, {}),
    Job("Sith Influence Among Wookiees", "Spread Sith teachings discreetly among the Wookiee population.", "Sith", 1, 65, {}),
    Job("Trandoshan Tracker", "Track down Trandoshan slavers operating on Kashyyyk.", "Bounty Hunter", 1, 65, {}),
    Job("Forest Navigation Aid", "Assist Wookiees in navigating and mapping the dense forests.", "Droid", 1, 65, {}),
    
    # Intermediate
    Job("Escort Wookiee Elders", "Ensure the safety of Wookiee elders during their journey.", "Jedi", 2, 130, {}),
    Job("Secret Sith Camp Setup", "Establish a hidden Sith training camp in the Shadowlands.", "Sith", 2, 130, {}),
    Job("Hunt for the Shadowlands Beast", "Hunt a dangerous beast threatening Wookiee villages.", "Bounty Hunter", 2, 130, {}),
    Job("Recover Lost Technology", "Retrieve ancient technology lost in the Shadowlands.", "Droid", 2, 130, {}),
    
    # Hard
    Job("Mediate Clan Disputes", "Resolve disputes among Wookiee clans diplomatically.", "Jedi", 4, 260, {}),
    Job("Dark Side Ritual in the Shadowlands", "Conduct a powerful Sith ritual deep within the Shadowlands.", "Sith", 4, 260, {}),
    Job("Disrupt Imperial Operations", "Sabotage Imperial logging operations without being detected.", "Bounty Hunter", 4, 260, {}),
    Job("Decipher Ancient Wookiee Texts", "Decode ancient texts that could hold the key to powerful technology.", "Droid", 4, 260, {}),
]
planet_kashyyyk = Planet("Kashyyyk", kashyyyk_locations, kashyyyk_transports, kashyyyk_npcs, kashyyyk_jobs)
planets = {
    "Coruscant": planet_coruscant,
    "Naboo": planet_naboo,
    "Tatooine": planet_tatooine,
    "Kashyyyk": planet_kashyyyk
}
def main():
    print("Welcome to the Galactic Adventure Game!")
    player = create_character()  # Just get the player object
    current_planet = planets[player.starting_planet] 
    
    credits = 0  # Initialize credits earned by the player

    while True:
        print("\nCurrent Location:", current_planet.name)
        print("1. Explore current planet")
        print("2. Visit different locations on the planet")
        print("3. Visit stores")
        print("4. Work")
        print("5. Meet people")
        print("6. Travel to another planet (requires credits)")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            current_planet.explore_planet(player)
        elif choice == "2":
            current_planet.visit_locations(player)
        elif choice == "3":
            current_planet.visit_stores(player)
        elif choice == "4":
            current_planet.display_jobs(player)
        elif choice == "5":
            current_planet.interact_with_npcs(player)
        elif choice == "6":
            if player.credits >= 100:  # Assuming a flat rate of 100 credits for travel
                print("Traveling to another planet...")
                # Assuming a function that allows the player to choose a destination and returns the new planet object
                # For simplicity, let's assume choose_destination() is implemented to handle this
                destination_name = input("Enter the name of the planet you wish to travel to: ")
                if destination_name in planets:
                    current_planet = planets[destination_name]
                    player.credits -= 100  # Deduct credits for travel
                    print(f"You have traveled to {destination_name}. You have {player.credits} credits remaining.")
                else:
                    print("Invalid destination.")
            else:
                print(f"You need 100 credits to travel to another planet. You currently have {player.credits} credits.")
        elif choice == "7":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()