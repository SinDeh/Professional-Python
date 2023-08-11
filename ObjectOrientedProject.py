import random


# names must be type with space between each name.
# sample of input: 
# Hossein Maziar Akbar Nima Mehdi Farhad Mohammad Khashayar Milad Mostafa Amin Saeid Pouya Pouria Reza Ali Behzad Soheil Behrouz Shahrouz Saman Mohsen
# حسین مازیار اکبر نیما مهدی فرهاد محمد خشایار میلاد مصطفی امین سعید پویا پوریا رضا علی بهزاد سهیل بهروز شهروز سامان محسن

name = input()
name = name.split()

class Person:
    """ 
    Just get name of players from user through input.
    """
    def __init__(self, name: list) -> None:
        self.name = name

class Player(Person):
    """
    Show teams with different members. each teams have 11 players.
    """
    def create_team(self):
        """
        creating two teams with players name that got from previous class.
        """
        team_A = []
        team_B = []
        A = random.sample(range(22), k= 11)
        for i in A:
            team_A.append(self.name[i])
        for j in self.name:
            if j not in team_A:
                team_B.append(j)

        print(f'team_A : {team_A}')
        print(f'team_B : {team_B}')
    
Football_player = Player(name)
Football_player.create_team()