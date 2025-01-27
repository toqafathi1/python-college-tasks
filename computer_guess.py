

# using oop concetps

import random


class ComputerGuesser:
    def __init__(self, max_value):

        self.low = 1
        self.high = max_value
        self.feedback = ''

    def make_guess(self):
        if self.low != self.high:
            return random.randint(self.low, self.high)
        else:
            return self.low

    def update_range(self, feedback, guess):
        if feedback == 'h':
            self.high = guess-1
        elif feedback == 'l':
            self.low = guess+1

    def play_game(self):
        while self.feedback != 'c':
            guess = self.make_guess()
            self.feedback = input(
                f"Is {guess} too high(H), too low(L) or correct(C)??").lower()

            self.update_range(self.feedback, guess)

        print(f"Yay! The computer guessed the number, {guess} correctly!")


def main():
    max_value = int(input("Enter the maximum value:  "))
    computer_guesser = ComputerGuesser(max_value)
    computer_guesser.play_game()


if __name__ == '__main__':
    main()
