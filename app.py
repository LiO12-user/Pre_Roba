import random

human_win_count=0

def play():

            human = input('r pre KAMEN, p pre PAPIER, s pre NOZNICE\n')
            computer = random.choice(['r', 'p', 's'])
            print(computer)

            if human == computer:
                return 'REMIZA'



            if ac(human, computer):

                return 'YOU WON'

            return 'YOU LOST'


def ac(user, comp):
    # r > s, p > r, s > p
    if (user == 'r' and comp == 's') or (user == 'p' and comp == 'r') or (user == 's' and comp == 'p'):

        return True


while human_win_count != 3:
    print(play())
    print(human_win_count)

