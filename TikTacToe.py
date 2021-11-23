#Tic-Tac-Toe


theSet = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

theMoves = []

for move in theSet:
    theMoves.append(move)


def printSet(move):
    print(move['7'] + '\t|\t' + move['8'] + '\t|\t' + move['9'])
    print('\n--------+---------------+--------\n')
    print(move['4'] + '\t|\t' + move['5'] + '\t|\t' + move['6'])
    print('\n--------+---------------+--------\n')
    print(move['1'] + '\t|\t' + move['2'] + '\t|\t' + move['3'])


def game():

    turn = 'X'
    count = 0


    for i in range(9):
        printSet(theSet)
        print("\nIT's YOUR TURN, * " + turn + " *")
        move = input("Move to which place? : ")
        print("\n")

        if theSet[move] == ' ':
            theSet[move] = turn
            count += 1
        else:
            print("\n**PLACE IS ALREADY FILLED**\n")
            continue

        #check the WINNER
        if count >= 5:
            if theSet['7'] == theSet['8'] == theSet['9'] != ' ':
                printSet(theSet)
                print("\n**GAME OVER**\n")
                print("****" +turn + "**** WINS :)\n")
                break
            elif theSet['4'] == theSet['5'] == theSet['6'] != ' ':
                printSet(theSet)
                print("\n**GAME OVER**\n")
                print("****" +turn + "**** WINS :)\n")
                break
            elif theSet['1'] == theSet['2'] == theSet['3'] != ' ':
                printSet(theSet)
                print("\n**GAME OVER**\n")
                print("****" +turn + "**** WINS :)\n")
                break
            elif theSet['1'] == theSet['4'] == theSet['7'] != ' ':
                printSet(theSet)
                print("\n**GAME OVER**\n")
                print("****" +turn + "**** WINS :)\n")
                break
            elif theSet['2'] == theSet['5'] == theSet['8'] != ' ':
                printSet(theSet)
                print("\n**GAME OVER**\n")
                print("****" +turn + "**** WINS :)\n")
                break
            elif theSet['3'] == theSet['6'] == theSet['9'] != ' ':
                printSet(theSet)
                print("\n**GAME OVER**\n")
                print("****" +turn + "**** WINS :)\n")
                break 
            elif theSet['7'] == theSet['5'] == theSet['3'] != ' ':
                printSet(theSet)
                print("\n**GAME OVER**\n")
                print("****" +turn + "**** WINS :)\n")
                break
            elif theSet['1'] == theSet['5'] == theSet['9'] != ' ':
                printSet(theSet)
                print("\n**GAME OVER**\n")
                print("****" +turn + "**** WINS :)\n")
                break 

        #Declare TIE
        if count == 9:
            print("\n**GAME OVER**\n")
            print("**IT's A TIE**")

        #change the player
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    #restart the game or not
    restart = input("\nREPLAY?(Y/N) : ")
    print("\n")
    if restart == "y" or restart == "Y":  
        for move in theMoves:
            theSet[move] = " "
        game()

if __name__ == "__main__":
    game()