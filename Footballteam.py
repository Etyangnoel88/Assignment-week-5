# Base class
class Player:
    def __init__(self, name, age, position, skill):
        self.name = name
        self.age = age
        self.position = position
        self.skill = skill
        self.__stamina = 100  # Encapsulated attribute

    def display_info(self):
        print(f"{self.position} - {self.name}, Age: {self.age}, Skill: {self.skill}, Stamina: {self.__stamina}")

    def train(self):
        self.skill += 1
        self.__stamina -= 10
        print(f"{self.name} trains hard! Skill is now {self.skill}, stamina is {self.__stamina}")

    def rest(self):
        self.__stamina = 100
        print(f"{self.name} is fully rested. Stamina restored!")

    def play(self):
        print(f"{self.name} is playing as a {self.position}.")

# Subclasses with polymorphism
class Goalkeeper(Player):
    def play(self):
        print(f"{self.name} guards the goal with lightning reflexes! 🧤")

class Striker(Player):
    def play(self):
        print(f"{self.name} strikes the ball with precision and power! ⚽")

class Midfielder(Player):
    def play(self):
        print(f"{self.name} controls the midfield, passing and creating chances! 🎯")

class Defender(Player):
    def play(self):
        print(f"{self.name} blocks attacks and defends the line! 🛡️")

# Create instances
gk = Goalkeeper("Sam", 30, "Goalkeeper", 85)
striker = Striker("Leo", 28, "Striker", 92)
midfielder = Midfielder("Alex", 26, "Midfielder", 88)
defender = Defender("John", 29, "Defender", 80)

# Use methods
players = [gk, striker, midfielder, defender]
for player in players:
    player.display_info()
    player.train()
    player.play()
    player.rest()
    print("---")
