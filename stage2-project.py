#Stage 2 Project for Chris Rhudy:

#A FILL-IN-THE-BLANKS QUIZ for PYTHON



#Lists of acceptable user-provided responses:

affirmative_answers = ["yes", "Yes", "YES", "yes.", "Yes.", "YES.", "yes!", "Yes!", "YES!", "yep", "yup", "Yep", "Yup", "yep!", "Yep!", "YEP!", "Of course", "of course", "Of course!", "sure", "sure!", "Sure", "Sure!", "Sure.", "sure."]

difficulty_levels = ["easy", "EASY", "Easy", "easy!", "Easy!", "EASY!", "easy.", "Easy.", "EASY.", "medium", "MEDIUM", "Medium", "medium.", "MEDIUM.", "Medium.", "medium!", "MEDIUM!", "Medium!", "hard", "Hard", "HARD", "hard.", "Hard.", "HARD.", "hard!", "Hard!", "HARD!"]

#Three levels of quizzes, with four blanks in each:

quiz_easy = """Hypertext Markup Language, or ___1___, is the basis for most documents found on the web. In ___1___,  each ___2___ is like a word in ___1___ language. Alternatively, ___2___s (such as <head> or <em>) can be looked at as elements in a tree. This tree-like structure of a page is also known as a ___3___ Object Model, or DOM. CSS (or ___4___ Style Sheets) allows you to use syntax and rules to change the look of an ___1___ page; in CSS, for example, including "border radius 50%" will change squares to circles!"""

quiz_medium = """An ___1___ is a conceptual idea, while a program is a concrete instantiation of an ___1___. Programming is the core of computer science. A ___2___ is simply a machine that can ___3___ (or "run") a program. With the right program, a ___2___ can do any mechanical computation you can imagine. A programming ___4___ is a ___4___ designed for producing ___2___ programs. Python is a programming ___4___."""

quiz_hard = """A procedure, also known in Python as a ___1___, enables you to abstract code from its inputs; an ___2___ statement allows you to write code that executes differently depending on the data, and is often paired with an ___3___ statement; and ___4___ loops (as well as for loops) provide a convenient way to repeat the same operations many times. Combining these procedures allows a programmer to, for example, solve the problem of finding all of the links on a web page!"""

#Dictionaries for storing {blank:answers} pairs for each level of difficulty:

dict_easy = {"___1___":("HTML", "html", "Html"), "___2___":("tag", "Tag", "TAG"), "___3___":("Document", "document", "DOCUMENT"), "___4___":("Cascading", "cascading", "CASCADING")}
dict_medium = {"___1___":("algorithm", "Algorithm", "ALGORITHM"), "___2___":("computer", "Computer", "COMPUTER"), "___3___":("execute", "Execute", "EXECUTE"), "___4___":("language", "Language", "LANGUAGE")}
dict_hard = {"___1___":("function", "Function", "FUNCTION"), "___2___":("if", "If", "IF"), "___3___":("else", "Else", "ELSE"), "___4___":("while", "While", "WHILE")}

#Dictionary for storing player name and chossen level of difficulty:
dict_other = {"name":"", "quiz_level":""}


#FUNCTIONS

def game_intro():
    #Serves as entry into the quiz; gets player's name, which is stored in dict_other
    print "Welcome to ***PYTHON TRIVIA***"
    \
    user_input = raw_input("What's your name?  ")
    dict_other["name"] = user_input #Stores player's name in dict_other
    print "Hello, " + dict_other["name"] + "!"
    user_input = raw_input("Would you like to play now?  ")
    if user_input in affirmative_answers:
        print "Great!"
    else:
        print "That's fine, too! Just input ctl-c at any time to exit." #Lets player exit from game at any time

def game_level():
    #Prompts for and stores difficulty level in dict_other; explains scoring; leads into game itself
    user_input = raw_input("Would you prefer an easy, medium, or hard level of difficulty?  ")
    if user_input in difficulty_levels:
        dict_other["quiz_level"] = user_input
        print "You have chosen the " + dict_other["quiz_level"] + " level, " + dict_other["name"] + ". Scoring works as follows: 2.5 points for a correct answer on the first try, 1 point for a correct answer on the second try, and 0 points otherwise. Good luck!"
    else:
        user_input = raw_input("I'm sorry but I don't recognize that level--please choose your level again: type easy, medium, or hard. ")
        if user_input in difficulty_levels:
            dict_other["quiz_level"] = user_input #Stores player's chosen difficulty level in dict_other
            print "You have chosen the " + dict_other["quiz_level"] + " level, " + dict_other["name"] + ". Scoring works as follows: 2.5 points for a correct answer on the first try, 1 point for a correct answer on the second try, and 0 points otherwise. Good luck!"
        else:
            print "That's fine, too! Just input ctl-c to exit."
    \
    print "Let's get started: press <enter> to see your fill-in-the-blanks quiz: "
    user_input=raw_input()

def game_play(quiz, dic):
    #The primary mechanism of question-and-answer. Takes user input from above functions, which is stored in the above dictionaries. Inputs required are the level of quiz and level of dictionary.
    spot = 1
    score = 0
    while spot <= 4:
        blank = "___" + str(spot) + "___" #To find each numbered blank
        if blank in quiz:
            print quiz
            \
            user_input = raw_input("Please write your answer for blank " + str(spot) + " here:  ")
            \
            if user_input in dic[blank]: #For correct answer on first try
                print "Correct!"
                score += 2.5
                print "Your score is now: " + str(score) + " point(s). Press <enter> to advance."
                user_input = raw_input()
                quiz = quiz.replace(blank, dic[blank][0]) #To fill in blank w/answer
                spot += 1
            else: #If wrong answer, player gets one more try
                user_input = raw_input("I'm sorry but that's incorrect, " + dict_other["name"] + ". Try again!  ")
                \
                if user_input in dic[blank]: #Correct answer on second try
                    print "Correct!"
                    score += 1.0
                    print "Your score is now: " + str(score) + " point(s). Press <enter> to advance."
                    user_input = raw_input()
                    quiz = quiz.replace(blank, dic[blank][0])
                    spot += 1
                else: #If two wrong answers, moves on to next q or end of game
                    print "Wrong again! The correct answer is '" + dic[blank][0] + ".' Let's try the next blank. Press <enter> to move on."
                    user_input = raw_input()
                    quiz = quiz.replace(blank, dic[blank][0])
                    spot += 1
    print "And that's it. Your final score is " + str(score) + " point(s). Thanks for playing!"

def the_complete_game():
    #This combines the above functions and runs the whole game!
    game_intro()
    game_level()
    easy_level = difficulty_levels[:9] #Combines 9 "easy" values into one
    medium_level = difficulty_levels[9:18] #Combines 9 "medium" values into one
    hard_level =  difficulty_levels[18:27] #COmbines 9 "hard" into one
    if dict_other["quiz_level"] in easy_level:
        game_play(quiz_easy, dict_easy)
    if dict_other["quiz_level"] in medium_level:
        game_play(quiz_medium, dict_medium)
    if dict_other["quiz_level"] in hard_level:
        game_play(quiz_hard, dict_hard)

the_complete_game()
