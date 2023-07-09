import random

def play():
    while True:
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        if user not in ['r', 'p', 's']:
            print("Invalid input! Please enter 'r', 'p', or 's'")
        else:
            break

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

# r > s, s > p, p > r
    
def is_win(player, opponent):
    # return True if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or \
       (player == 's' and opponent == 'p') or \
       (player == 'p' and opponent == 'r'):
        return True

while True:
    result = play()
    print(result)
    response = input("Do you want to play again? Enter 'y' for yes or 'q' to quit\n")
    while response not in ['y', 'q']:
        print("Invalid input! Please enter 'y' or 'q'")
        response = input("Do you want to play again? Enter 'y' for yes or 'q' to quit\n")
    if response == 'q':
        break
