import linecache    

# This is a simple python program to help with making a quiz application
# I hope this works. I'm not good with pythonn so I hope it will be easier to do than in Java

# This program will be broken down into four stages:
# Stage One (COMPLETED): Get a simple functioning quiz program 
# Stage Two (COMPLETED): Get quiz to work with premade quiz questions from a file 
# Stage Three (COMPLETED): Get program to save custom quiz sets 
# Stage Four (CURRENT): Give program a Graphical User Interface (Gui)
# Stage Five (): Make sure the progrem runs as it's intended

# Game loop, used for when the quiz starts
exit = False

# the name of the text file I want to read. Will be able to be changed by the user to select quizes
fileName = ""

#
#   LOOPS
#
# Counts how many times the loop is run. When it's hits the number specified in the first line, the program ends.
loop = 1;

# Counts how many times the loop for making quiz questions is run. Ends loop after the number has been reached
qMakingLoop = 1;

# Counts how many times the inner loop for making quiz questions is run. Ends loop after the number has been reached
innerQMakingLoop = 1;


# Points to be displayed to the user
points = 0

# Used for the correct answer. Checks with user input.
userAnswer = ""
rightAnswer = ""

# Used to tell which line is to be read --- Starts off on One and NOT ZERO
line = 2;

lineAnswer = 7

# Used to make sure when selecting the right answer, the answer for the proper question is choosen and not for the first questions set.
numVar = 2

# Used to get the number of the previously selected question
prevSet = 0;


gameChoice = ""

# Block of text the user sees when the program first runs
print("")
print("Hello, Welcome to a quiz program made in python: ")
gameChoice = input("Would you like to play or make your own questions? (p/m) ")
print("")


#
# QUESTIN MAKING BLOCK
#
if gameChoice == "m":
    gameChoice = ""
    print("Welcome to the quiz making section of this program.")
    print("Here you will be allowed to make questions with answers that can later be used in the play section of this quiz program.")
    print("You can make any number of questions with any number of question sets (questions including answers) as long as the following format is followed.")
    print("Total number of question sets you would like to make")
    print("------------------------------------------------")
    print("")
    print("Total number of questions (must at the top and only needs to appear once)")
    print("Question ")
    print("1. Answer One")
    print("2. Answer Two")
    print("3. Answer Three")
    print("4. Answer Four")
    print("Actaual answer (must be exact copy of one of the answer choices)")
    print("------------------------------------------------")
    print("")
    print("The format must be in this order or else the program will crash.")
    print("There are no spaces in the questions. Everything must be line by line")
    print("DO NOT WORRY: The program will ask you a few questions. As long as you supply the proper answers, the program will format the text file for you with your responses.")
    print("If you wish, you do not need to use this program to make the quiz questions.")
    print("If you choose not to use this program for quiz making questionss, the above format is needed.")
    print("Now, time to begin making questions")
    print("")

    fileName = input("What would you like to call this file that will contain all of your questions? (include .txt in the file name)")


    gameChoice = input("How many questions would you like to have?")
    questionSetNumber = gameChoice


    while(qMakingLoop <= int(questionSetNumber)):
        questionString = input("What is the question? ")
        properAnswerChoice = input("What is the proper answer to the question? ")
        fakeQuestionOne = input("Please enter a fake answer. ")
        fakeQuestionTwo = input("Please enter another fake answer. ")
        fakeQuestionThree = input("Please enter a third fake answer. ")
        fakeQuestionFour = input("Please enter a fourth fake answer. ")

        if innerQMakingLoop == 1:
            with open(fileName, 'a+') as f:
                f.write(questionSetNumber + "\n")
                f.write(questionString + "\n")
                f.write(fakeQuestionOne + "\n")
                f.write(fakeQuestionTwo + "\n")
                f.write(fakeQuestionThree + "\n")
                f.write(fakeQuestionFour + "\n")
                f.write(properAnswerChoice + "\n")
                innerQMakingLoop = innerQMakingLoop + 1
        else:
            with open(fileName, 'a+') as f:
                f.write(questionString + "\n")
                f.write(fakeQuestionOne + "\n")
                f.write(fakeQuestionTwo + "\n")
                f.write(fakeQuestionThree + "\n")
                f.write(fakeQuestionFour + "\n")
                f.write(properAnswerChoice + "\n")


        qMakingLoop = qMakingLoop + 1;

#
# QUIZ PLAYING BLOCK
#
elif gameChoice == "p":



    print("Here you will be presented with a few basic questions with answers")
    print("If you get the right answer, you will get a point, and move onto the next question.")
    print("If you get the wrong answer, you will move onto the next question but will not get a point")
    print("Please seledt the numbers next to the answer choices when deciding what answer you want")
    print("If you enter anything other than an accepted number, it will count as a wrong answer")
    print("")

    # Prompts user for a 'y' or a 'n' to decide if the quiz is to start or not
    choice = input("Are you ready? (y/n) ")

    fileName = input("Enter the file name you wish to play from (include .txt): ")

    # Used to decide what quiz quistion to display -- Currently moves to the next question and does not go back question
    quizNumber = int(linecache.getline(fileName, 1))


    if(choice == "y"):
        print("Let us begin")
        print("")

        # Quiz loop here ---- I'm not sure if I should move this here, or at an earlier point. Will stay here for now
        while(exit == False):


                if loop <= quizNumber:
                    print(linecache.getline(fileName, line)) # Line 2
                    line = line + 1;
                    print(linecache.getline(fileName, line)) # Line 3
                    line = line + 1;
                    print(linecache.getline(fileName, line)) # Line 4
                    line = line + 1;
                    print(linecache.getline(fileName, line)) # Line 5
                    line = line + 1;
                    print(linecache.getline(fileName, line)) # Line 6
                    line = line + 1;

                    rightAnswer = linecache.getline(fileName, lineAnswer) # Line 7 (+ 6 after first loop)

                    print("-------------DEBUG WINDOW-------------")
                    print('The current right answer is: {}', rightAnswer)



                    print("-------------END OF WINDOW-------------")
                   
                    # asks user to choose an answer. 
                    userAnswer = input("Your answer is? ")

                    # converts the answer, which is a number, to an in and then sets the user's choice to the answer string answer they choose.
                    # First checks to make sure user entered a valid input. This will prevent crashing if the user enters a character and not a number
                    if userAnswer == "1" or userAnswer == "2" or userAnswer == "3" or userAnswer == "4":
                        prevSet = int(userAnswer) + numVar;
                        userAnswer =  linecache.getline(fileName, prevSet)
                        if(userAnswer == rightAnswer):
                            loop = loop + 1
                            points = points + 1
                            numVar = numVar + 6
                            lineAnswer = lineAnswer + 6
                            line = line + 1
                        else:
                            print("Wrong Answer")
                            loop = loop + 1;
                            print('Your answer is {}, the correct answer is'.format(userAnswer, rightAnswer))
                            numVar = numVar + 6
                            lineAnswer = lineAnswer + 6
                            line = line + 1

                    else:
                        print("Will not do conversion. Quiz will now exit")
                        break
                else:
                    exit = True


        print("---------------------RESULTS---------------------")
        print("You have finished the quiz.")
        print('You have {} points'.format(points))
        print("Congragulations.")




        
    elif(choice == "n"):
        print("When you are ready, please run the program again")
    else:
        print("Those are not progper commands. Please restart the quiz and use either 'y' or 'n' ")

else:
    print("That is not an option. Please relaunch the program and choose either 'p' or 'm'")





print("")
print("The contents of the file are: ")
with open(fileName, 'r') as f:
    print(f.read())


