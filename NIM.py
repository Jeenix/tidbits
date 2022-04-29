"""Two students can play a game of NIM against this program.
To play the game, the first player determines the number of stones to be used (between 30 to 50)
Then the players take turns removing between 1 to 3 stones
until the player who takes the finally stone is declared the winner.
"""
#set game constants are set here so they can be quickly changed without having to find in the code itself
MAX_STONES = 50
MIN_STONES = 30

def main():
    """all new games start with newgame and newplayers set to yes to allow the game to play through all dialoge options.
    When the game repeats, it will give players choice whether they want to reset the players' names or not.
    """
    newgame='Y'
    newplayers='Y'
    while newgame == 'Y':
        if newplayers == 'Y':
            player_1, player_1_mit, player_2, player_2_mit = player_info()
        current_stones = check_stones(player_1)
        play_game(player_1,player_1_mit, player_2, player_2_mit, current_stones)
        newgame, newplayers = play_again(player_1, player_2)

def player_info():
    #ask human players for their names and MIT ID
    player_1 = input("Player 1, what is your name? ")
    player_1 = player_1.capitalize()
    player_1_mit = input(str(player_1) +" what is your MIT ID? ")
    player_2 = input("Player 2, what is your name? ")
    player_2 = player_2.capitalize()
    player_2_mit = input(str(player_2) +" what is your MIT ID? ")
    print("Welcome ", str(player_1)," and ", str(player_2), " to the game of Taking Stones (aka NIM)")
    return player_1, player_1_mit, player_2, player_2_mit

def check_stones(player_1):
    #asks player 1 how many stones they want to start the game with
    starting_stones = int(input((player_1 +" please nominate the number of stones (between 30 to 50) to start the game with: ")))
    while starting_stones < MIN_STONES or starting_stones > MAX_STONES:
        starting_stones = int(input("Incorrect. Please pick a number between 30 to 50 to start the game."))
    return starting_stones

def play_game(player_1,player_1_mit, player_2, player_2_mit, current_stones):
    #this function loops through the each player's turns until no stones remaining, then prints the corresponding winner
    while current_stones != 0:
        current_stones = turn(player_1,player_1_mit, current_stones)
        if current_stones == 0:
            winner = 1
            break
        current_stones = turn(player_2,player_2_mit,current_stones)
        if current_stones == 0:
            winner = 2
            break
        current_stones = computer_turn(current_stones)
        if current_stones == 0:
            winner = 3
            break
    if winner == 1:
        print("Game over! " + player_1 + " (" + player_1_mit + ") has won! ")
    elif winner == 2:
        print("Game over! " + player_2 + " (" + player_2_mit + ") has won! ")
    else:
        print("Game over! The computer has won!")

def turn(player_1, player_1_mit, current_stones):
    #this function is a further breakdown of an individual's turn which returns the new current stones value.
    #It re-prompts the player for an input, if input is incorrect.
    remove_stones = int(input(player_1+ " (" + player_1_mit + ") please remove 1, 2 or 3 stones: "))
    while remove_stones > 3 or remove_stones < 1:
        remove_stones = int(input(player_1+ ", that input is not correct. Please input 1, 2 or 3 stones to remove: "))
    while remove_stones > current_stones:
        remove_stones = int(input(player_1 + ", you cannot remove more stones than there are stones left. How many stones do you want to remove? "))
    current_stones = current_stones - remove_stones
    print("There are " + str(current_stones) + " stones remaining. ")
    return current_stones

def computer_turn(current_stones):
    #computers turn includes calculating the optimal turn based on the provided rule and prints new current stones value
    if current_stones % 3 == 0:
        taken_stones = 2
    else:
        taken_stones = 1
    current_stones = current_stones - taken_stones
    print("Computer's turn. Computer takes "+ str(taken_stones) +" there are " + str(current_stones) + " stones remaining. ")
    return current_stones

def play_again(player_1, player_2):
    #asks players if they want to play again
    newgame = input("Do you want to play again? <Y/N?>")
    newgame = newgame.capitalize()
    if newgame == 'N':
        quit()
    newplayers = input("Will " + player_1 +" and " + player_2 + " be playing? <Y/N?>")
    if newplayers.capitalize() == 'Y':
        newplayers = 'N'
    else:
        newplayers = 'Y'
    return newgame, newplayers

if __name__ == '__main__':
    main()