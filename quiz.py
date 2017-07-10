import os # Used for finding the proper path and working file directory (cwd)
import linecache # Used for reading specific lines from the text files

exitMainGameLoop = False # Be the main loop for the program. If this is equal to true, the program ends
cwd = os.getcwd() # Get's the programs working directory
print()
print("Welcome to this python quiz. Would you like to play or make your own quiz? (Please Select a number)")
print("1. Play ")
print("2. Make")
print("3. About")
gameMode = input()

userInput = "n"

if gameMode == "1":

    while exitMainGameLoop == False:

        userInput = ""
        print()
        print("Now in quiz play mode")
        print()


        currentQuestionSet = []

        fileIndex = 1

        files = []
        for entry in os.scandir(cwd + "\\Question Sets"): # Checks for the files inside of the Questions Sets folder which is located in the source folder of this program
            if entry.is_file:
                files.append(str(fileIndex) + ". " + entry.name) # Add the names of the files that has been found to the files[] list so it can be printed later in a neat fashion and displayed to the user
                fileIndex = fileIndex + 1

        for doc in files: # Print out all of the files that has been found
            print(doc)

        print()
        print("Here are your available quizes")
        fileName = input("Please choose the number next to your quiz to select it: ")
        print()




        fileName = files[int(fileName) - 1]
        fileName = fileName[3:] # Slices of '#. ' i.e '1. Random.txt' becomes 'Random.txt' This is done becomes the files do not have numbers attached to them like it is desplayed to the user.

        i = 1 # For the while loop. Can be zero, but chose one so I don't have to do math more than I need to
        line = 2 # Used for getting the proper lines to display to the user. These lines will be the question followed by it's respective answers.
                #sThe line number and the answer number will not be displayed. And only one questions/answer will show at a time


        rightAnswerLine = 7 # This is the line number for the right answer (The first one)

        while i <= int(linecache.getline(cwd + "/Question Sets/" + fileName, 1)): # Get's the first line of the file and converts it to an int
            print()
            print(linecache.getline(cwd + "/Question Sets/" + fileName, line)) # This line will show the question being asked
            line = line + 1
            print(linecache.getline(cwd + "/Question Sets/" + fileName, line)) # This line will display answer choice one
            line = line + 1
            print(linecache.getline(cwd + "/Question Sets/" + fileName, line)) # This line will display answer choice Two
            line = line + 1
            print(linecache.getline(cwd + "/Question Sets/" + fileName, line)) # This line will display answer choice Three
            line = line + 1
            print(linecache.getline(cwd + "/Question Sets/" + fileName, line)) # This line will display answer choice Four

            rightAnswer = linecache.getline(cwd + "/Question Sets/" + fileName, rightAnswerLine) # Sets the rightAnswer to the proper line. Python doesn't read the line if this isn't done this way

            userInput = ""
            userInput = input("Which is the right answer? (Please select the number you want)")



            # These were type casted to int as leaving them as strings would cause an error. Even if the right answre was chosen, it woud still be wrong
            # Having them as int fixes that problem.
            userInput = int(userInput)
            rightAnswer = int(rightAnswer)

            print("The right answer is {}".format(rightAnswer))

            if userInput == rightAnswer:
                print("{} is the right answer!".format(userInput))
                print("Moving on to the next question")
                line = line + 2
                rightAnswerLine = rightAnswerLine + 6
                i = i + 1
            else:
                print("{} is not the right answer.".format(userInput))
                print("Moving on to the next question")
                line = line + 2
                rightAnswerLine = rightAnswerLine + 6
                i = i + 1

        userInput = ""
        exitMainGameLoop = True

elif gameMode == "2":

    while exitMainGameLoop == False:

        question = " " # This will store the question
        i = 1 # Used for iterating through while loop that creates the question sets
        j = 0 # Used for iterating thorugh the while loop that stores and saves the answers
        answerList = [0, 0, 0, 0] # Going to store the answers to the questions


        filesInDir = []
        for entry in os.scandir(cwd + "/Question Sets"):
            if entry.is_file:
                filesInDir.append(entry.name)

        for f in filesInDir:
            print(f)


        fileName = input("Please enter the name of this Question Set: ")
        fileName = fileName + ".txt" # This will make sure the file created is a text file by adding .txt to fileName
        path = os.path.exists(cwd + "/Question Sets/" + fileName) # This will be used to see if the file has already been created when writing the questions to the file.




        if path == True: # checks if the user wants to rewrite an existing file
            userInput = input("'{}' already exists. Do you wish to rewrite it? ( y / n)".format(fileName))

            # check what the user types then runs the proper message. This only runs if path == True
            if userInput == "y":
                print("The file has been overwritten")
                numberOfQuestions = input("How many questions do you want? ") # Asks for the number of desired questions
                numberOfQuestions = int(numberOfQuestions) # Converts the string into and int (integer)
                with open("Question Sets/" + fileName, 'w') as f: # Writes the number of questiosn to the file before the loop begins
                    f.write(str(numberOfQuestions) + "\n")

            elif userInput == "n":
                print("The file will not be overwritten")
            else:
                print("You did not either 'y'  or 'n'. The program will now close.")
                quit()

        else:
            with open("Question Sets/" + fileName, 'w') as f: # Writes the number of questiosn to the file before the loop begins
                numberOfQuestions = input("How many questions do you want? ") # Asks for the number of desired questions
                numberOfQuestions = int(numberOfQuestions) # Converts the string into and int (integer)
                f.write(str(numberOfQuestions) + "\n")



        while i <= numberOfQuestions:
            userQuestion = input("Please enter your question: ") # Ask user for quesetion



            while j < len(answerList):
                answerList[j] = input("What is your {} answer (Please make sure one of these contains the write answer)".format(j + 1)) # Promts the user to enter a new answer. Is stored in the answerList at index 'i'
                answerList[j] = str(j + 1) + ". " + answerList[j]
                j = j + 1 # Increases i by one each after you enter an aswer

            for answer in answerList:
                print(answer)

            rightAnswer = 0
            rightAnswer = input("Which one of the answers above is the right answr? (please choose the number next to the question i.e '1' for {})".format(answerList[0])) # Ask the user to select the right answer



            j = 0
            if path == True: # If the file exists, and the player wants to rewrite it, remake it so it's empty then write the needed contents
                if userInput == "y":
                    with open(cwd + "/Question Sets/" + fileName, 'a+') as f:
                        f.write(userQuestion + "\n") # Saves question
                        for answer in answerList: # saves the answers in answerList to one line
                            f.write(answerList[j] + "\n")
                            j = j + 1
                            userInput = "n" # change the user input to 'n' otherwise the file will be overwritten again for the second question
                        f.write(rightAnswer + "\n") # Saves the number to the right answer.
                elif userInput == "n":
                    with open("Question Sets/" + fileName, 'a+') as f: # Creates a new file called 'test.txt' and uses append mode. Called f for naming convention
                        f.write(userQuestion + "\n") # Saves question
                        for answer in answerList: # saves the answers in answerList to one line
                            f.write(answerList[j] + "\n")
                            j = j + 1
                        f.write(rightAnswer + "\n") # Saves the number to the right answer

            else: # if the file doesn't exist, create it with the contents needed
                with open("Question Sets/" + fileName, 'a+') as f: # Creates a new file called 'test.txt' and uses append mode. Called f for naming convention
                    f.write(userQuestion + "\n") # Saves question
                    for answer in answerList: # saves the answers in answerList to one line
                        f.write(answerList[j] + "\n")
                        j = j + 1
                    f.write(rightAnswer + "\n") # Saves the number to the right answer

            j = 0

            i = i + 1

        i = 0






        exitMainGameLoop = True # END OF MAIN GAME LOOP

elif gameMode == "3":
    print("Hello Everyone, I'm Anguel Esperanza, the developer of this small python script.")
    print("I made this in the hopes that it can help me study while I'm at college.")
    print("I figured I'd release this script and post it online in case anyone else wants to look at it, use it, or modify it.")
    print("This isn't a feature packed script. All you can do is make questions sets, and play those questions sets.")
    print("I would love to add more features in the future. I have plans to do so, however I'm going to need to learn more python before than.")
    print("Making this was a lot of fun. I did my best to document the code so it's easy to understand.")
    print("I hope you all enjoy this program and find it useful in your studies.")

    print("----------------COPY RIGHT INFORMATION-----------------")
    print("You are free to use this code in any project you want, both commerical and non-commercial use.")
    print("I only ask that you give me credit and link to either one or both of the following links")
    print("Github: ")
    print("Pastebin: ")
    print("These are the places that this soucre code has been published too. If this changes in the future, these links will be updated as such.")


