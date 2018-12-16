#!/usr/bin/env python3
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    slist = []

    def learn(self, my_move, their_move):
        self.lmove = [my_move, their_move]
        self.slist.append(self.lmove)
        return self.slist


def beats(one, two):

    if one == "rock" and two == "scissors":
        result = "You wins"
        return result

    elif one == "rock" and two == "paper":
        result = "Computer wins"
        return result

    elif one == "scissors" and two == "rock":
        result = "Computer wins"
        return result

    elif one == "scissors" and two == "paper":
        result = "You wins"
        return result

    elif one == "paper" and two == "rock":
        result = "You wins"
        return result

    elif one == "paper" and two == "scissors":
        result = "Computer wins"
        return result

    else:
        result = "It's a tie!"
        return result


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You: {move1}  Computer: {move2}")
        fresult = beats(move1, move2)
        print(fresult)
        if fresult == "You wins":
            self.plr1 += 1
            print("You = ", self.plr1, "Computer = ", self.plr2)
        elif fresult == "Computer wins":
            self.plr2 += 1
            print("You = ", self.plr1, "Computer = ", self.plr2)
        else:
            print("You = ", self.plr1, "Computer = ", self.plr2)

        self.p1.learn(move1, move2)

    def play_game(self):
        print("Game start!")
        self.plr1 = 0
        self.plr2 = 0

        while True:
            try:
                Round = int(input("how many round?"))
                if Round > 0:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid number")
                continue

        for round in range(Round):
            print("---------------------------------------")
            print(f"Round {round}:")
            self.play_round()

        print("=======================================")
        print("\t\tGame over!")
        print("Final Score", "You = ", self.plr1, "Computer = ", self.plr2)
        if self.plr1 > self.plr2:
            print("You are the winner")
        elif self.plr1 > self.plr2:
            print("Computer is the winner")
        else:
            print("It's a tie")


class RandomPlayer(Player):
    def __init__(self):
        Player.__init__(self)

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self)

    def move(self):
        listhmove = ["rock", "paper", "scissors", "z"]
        while True:
            try:
                Hmove = input("What would you like to throw?  ")
                self.hmove = Hmove.lower()
                if self.hmove in listhmove:
                    break
                else:
                    raise TypeError
            except TypeError:
                print("""Please enter a valid throw: rock, paper, scissors,
        To exit enter z""")
                continue

        if self.hmove == "z":
            quit()

        return self.hmove


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)

    n = -1

    def move(self):
        self.n += 1
        if self.n == 0:
            self.rmove = random.choice(moves)
        elif self.n > 0:
            self.y = self.n - 1
            self.rmove = self.slist[self.y][0]
        return self.rmove


class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)

    n = -1

    def move(self):
        if self.n == -1:
            self.cmove = random.choice(moves)
            self.n = moves.index(self.cmove)

        elif self.n > -1:
            if self.n == 3:
                self.n = 0
            self.cmove = moves[self.n]

        self.n += 1
        return self.cmove


class RepeatPlayer(Player):
    def __init__(self):
        Player.__init__(self)


if __name__ == '__main__':
    print("""Here are the rules of the game:
    scissor cuts paper,paper covers rock, and rock crushes scissors.
    Play either "rock", "paper", or "scissors"
    If you want to stop playing, enter a "z".\n""")

    players = ["cycle", "random", "reflect", "repeat", "z"]
    while True:
        try:
            Type = input("""Who would you like to play with?
    Please enter "random", "reflect", "repeat", or "cycle" """)
            type = Type.lower()
            if type in players:
                break
            else:
                raise TypeError
        except TypeError:
            print("\nPlease select a valid player. To exit enter z")
            continue

    if type == "cycle":
        game = Game(HumanPlayer(), CyclePlayer())

    elif type == "random":
        game = Game(HumanPlayer(), RandomPlayer())

    elif type == "reflect":
        game = Game(HumanPlayer(), ReflectPlayer())

    elif type == "repeat":
        game = Game(HumanPlayer(), RepeatPlayer())

    elif type == "z":
        quit()

    game.play_game()
