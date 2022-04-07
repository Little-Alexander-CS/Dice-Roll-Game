# Alexander Little April 2022
import random
class DiceRollGame: #This is the main DiceRollGame class, contains the entitre game
    def __init__(self): #This is the default init function, it sets all my variables
        global round
        global listOfPlayers
        listOfPlayers = []
        global listOfScores
        listOfScores = []
        global diceRollOne
        global diceRollTwo
        
    def setup(self): #This is the setup function, it asks for the number of players and the number of rounds while using a while try catch to check for non integers
        while True: #While loop which repeats every time an integer is not entered for the number of players
           numPlayers = input("Please enter the number of players: ")
           try:
               numPlayers = int(numPlayers)
           except ValueError as e:
               print ("Number of players must be an integer please try again")
           else:
               break
           
        for i in range(numPlayers): #For loop which asks the players for their names and puts them into the players list
            listOfPlayers.append(input("Please enter player " + str(i + 1) + " name:"))
        
        while True: #While loop which repeats every time an integer is not entered for the number of rounds
           global numRounds
           numRounds = input("Please enter the number of rounds the players wish to play: ")
           try:
               numRounds = int(numRounds)
           except ValueError as f:
               print ("Number of rounds must be an integer please try again")
           else:
               break
           
        game.board() #At the end of setup, it calls the board function to display the empty board and continue the game
    
    def board(self): #This is the board function, it displays the board at the begining of the game and after every round, the round order is displayed left to right
        global round
        round = 0
        count = 0
        listOfScores.clear()
        for i in range(((len(listOfPlayers)) * numRounds)): #This for loop creates the blank board by appending '-' to the new list, listOfScores for the amount of players * the amount of rounds
            listOfScores.append("-")
            
        print("***********************Round " + str(round) + "************************") #This block prints out the blank listOfScores once 
        print("~\t", end =" ")
        print("")
        for a in range(len(listOfPlayers)): #This for loop prints the correct amount of '-'s for each player by printing the list from count to count + numRounds and then incrementing count by numRounds
            print(listOfPlayers[a], end="")
            print(listOfScores[int(count):int(count + numRounds)])
            count += numRounds
        print("******************************************************")
        
        i = 0 
        while i < numRounds: #This while loop calls the dice roll function once for every round and uses the same method from before to display the results
            game.diceRoll(i)
            round += 1
            print("***********************Round " + str(round) + "************************")
            print("~\t", end =" ")
            print("")
            count = 0
            for a in range(len(listOfPlayers)): #This for loop prints the correct amount of '-'s for each player by printing the list from count to count + numRounds and then incrementing count by numRounds
                print(listOfPlayers[a], end="")
                print(listOfScores[int(count):int(count + numRounds)])
                count += numRounds
            print("******************************************************")
            i += 1
        game.endGame()
        
    def diceRoll(self, i): #This is the function that rolls the die, it uses random to generate a number between 1-6 inclusive
        count = i
        for i in range (len(listOfPlayers)): #For every player the loop repeats 
            input(print(listOfPlayers[i], "Hit enter once you are ready to roll your die!")) #input for the enter key
            diceRollOne = random.randint(1, 6) #Two random numbers are generated between 1-6 inclusive
            diceRollTwo = random.randint(1, 6)
            listOfScores[count] = (diceRollOne + diceRollTwo) #They are inserted into the scores list at count
            print(listOfPlayers[i], "rolled a", diceRollOne, "and", diceRollTwo) #Printed out
            count += numRounds #count is incremented by numRounds
        print(listOfScores) #The list was printed for testing purposes
    
    def endGame(self): #This is the function that is called when the game ends, it calcuates the winner, congratulates them, and asks if the players would like to play again
        count = 0
        totalScore = [] #A new list is created which will store the list of all the final scores
        for a in range(len(listOfPlayers)): #This for loop appends the final score to the totalScore using the sum function
            totalScore.append(sum(listOfScores[int(count):int(count + numRounds)]))
            count += numRounds #count is incremented 
        print(totalScore) #The totalScore was printed for testing purposes
        winnerIndex = totalScore.index(max(totalScore)) #The winnerIndex is calculated based on the index function of the maximum value of totalScore
        print("Congratulations to", listOfPlayers[winnerIndex]) #The winner is congratulated
        playAgain = 0
        while (playAgain != "1" and playAgain != "2"): #While the user input is not 1 or 2, the loop repeats
            playAgain = input("Would you like to play another game? [1:Yes 2:No]")
        if(playAgain == "1"): #If 1 is selected, the game restarts with the same players by calling the board function
            game.board()
        elif(playAgain == "2"): #If 2 is selected, the game ends
            print("Thank you and see you later!")

game = DiceRollGame() #I created a new instance of DiceRollGame
game.setup() #Then called the setup function to start the game
