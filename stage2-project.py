#Stage 2 Project for Chris Rhudy:

#A FILL-IN-THE-BLANKS QUIZ for PYTHON

#Three levels of quizzes, with four blanks in each:
quiz_easy = """Hypertext Markup Language, or ___1___, is the basis for most documents found on the web. In ___1___,  each ___2___ is like a word in ___1___ language. Alternatively, ___2___s (such as <head> or <em>) can be looked at as elements in a tree. This tree-like structure of a page is also known as a ___3___ Object Model, or DOM. CSS (or ___4___ Style Sheets) allows you to use syntax and rules to change the look of an ___1___ page; in CSS, for example, including "border radius 50%" will change squares to circles!"""\

quiz_medium = """An ___1___ is a conceptual idea, while a program is a concrete instantiation of an ___1___. Programming is the core of computer science. A ___2___ is simply a machine that can ___3___ (or "run") a program. With the right program, a ___2___ can do any mechanical computation you can imagine. A programming ___4___ is a ___4___ designed for producing ___2___ programs. Python is a programming ___4___."""\

quiz_hard = """A procedure, also known in Python as a ___1___, enables you to abstract code from its inputs; an ___2___ statement allows you to write code that executes differently depending on the data, and is often paired with an ___3___ statement; and ___4___ loops (as well as for loops) provide a convenient way to repeat the same operations many times. Combining these procedures allows a programmer to, for example, solve the problem of finding all of the links on a web page!"""\

#Lists of acceptable user-provided responses:
affirmative_answers = ["yes", "Yes", "YES", "yes.", "Yes.", "YES.", "yes!", "Yes!", "YES!", "yep", "yup", "Yep", "Yup", "yep!", "Yep!", "YEP!", "Of course", "of course", "Of course!", "sure", "sure!", "Sure", "Sure!", "Sure.", "sure."]

difficulty_levels = ["easy", "medium", "hard"]

#Dictionaries for storing {blank:answers} pairs for each level of difficulty:
dict_easy = {"___1___":"html", "___2___":"tag", "___3___":"document", "___4___":"cascading"}
dict_medium = {"___1___":"algorithm", "___2___":"computer", "___3___":"execute", "___4___":"language"}
dict_hard = {"___1___":"function", "___2___":"if", "___3___":"else", "___4___":"while"}

#Dictionary for storing player name, chosen level of difficulty, other info:
dict_other = {"name":"", "quiz_level":"", "score":0, "nth_blank":1, "total_blanks":4, "blank":"", "maximum_points":25, "minimum_points":10}

#FUNCTIONS

def game_intro():
#   Behavior: Serves as entry into the quiz; gets player's name, which is stored in dict_other
#   Inputs: User input re name and difficulty level
#   Outputs: Explanatory text to user, determines difficulty level from user responses
    print "Welcome to ***PYTHON TRIVIA*** "
    user_name = raw_input("What's your name?  ")
    dict_other["name"] = user_name #Stores player's name in dict_other
    print "Hello, " + user_name + "!"
    user_wants_to_play = raw_input("Would you like to play now?  ")
    if user_wants_to_play in affirmative_answers:
        print "Great!"
    else:
        print "That's fine, too! Just input ctl-c at any time to exit." #Lets player exit from game at any time, but assumes the player actually does want to play

def game_level():
#   Behavior: Prompts for and stores difficulty level in dict_other; explains scoring; leads into game itself
#   Inputs: Only user input to determine game difficulty level
#   Outputs: Game explanation to user, plus determination of difficulty level
    user_difficulty_choice = raw_input("Would you prefer an easy, medium, or hard level of difficulty?  ")
    if user_difficulty_choice.lower() in difficulty_levels:
        dict_other["quiz_level"] = user_difficulty_choice.lower() #Stores user's chosen level of difficulty
        print "You have chosen the " + dict_other["quiz_level"] + " level, " + dict_other["name"] + ". Scoring works as follows: " + str(dict_other["maximum_points"]) + " points for a correct answer on the first try, " + str(dict_other["minimum_points"]) + " points for a correct answer on the second try, and 0 points otherwise. Good luck!"
    else:
        print "That's fine, too! Just type ctl-c and <enter> to exit."
        dict_other["quiz_level"] = "easy"
    \
    print "Let's get started: press <enter> to see your fill-in-the-blanks quiz: "
    pressed_enter=raw_input()

def correct_answer(quiz, dic):
#   Behavior: Judges first successful guesses for each blank
#   Inputs: Takes quiz level and dictionary level, plus the user pressing <enter>
#   Outputs: Outputs are scorekeeping and enthusiastic responses
    dict_other["score"] += dict_other["maximum_points"]
    print "Correct! Your score is now: " + str(dict_other["score"]) + " point(s). Press <enter> to advance."
    pressed_enter = raw_input()
    dict_other["nth_blank"] += 1

def wrong_answer(quiz, dic):
#   Behavior: Judges second chance guesses for each blank
#   Inputs: Takes quiz level and dictionary level, plus user input
#   Outputs: Outputs are responses, judgments, and scorekeeping
    next_guess = raw_input("I'm sorry but that's incorrect, " + dict_other["name"] + ". Try again!  ")
    if next_guess.lower() == dic[dict_other["blank"]]: #Correct answer on second try
        print "Correct!"
        dict_other["score"] += dict_other["minimum_points"]
        print "Your score is now: " + str(dict_other["score"]) + " point(s). Press <enter> to advance."
    else: #If two wrong answers, moves on to next q or end of game
        if dict_other["nth_blank"] == dict_other["total_blanks"]:
            print "Wrong again! The correct answer is '" + dic[dict_other["blank"]] + ".' Press <enter>."
        else:
            print "Wrong again! The correct answer is '" + dic[dict_other["blank"]] + ".' Let's try the next blank. Press <enter> to move on."
    pressed_enter = raw_input()
    dict_other["nth_blank"] += 1

def game_play(quiz, dic):
#   Behavior: The primary mechanism of question-and-answer. Takes user input from above functions, which is stored in the above dictionaries. Inputs required are the level of quiz and level of dictionary.
#   Inputs: Takes quiz level and dictionary level, as well as user input.
#   Outputs: Outputs are responses, judgments, and scorekeeping
    while dict_other["nth_blank"] <= dict_other["total_blanks"]:
        dict_other["blank"] = "___" + str(dict_other["nth_blank"]) + "___" #To find each numbered blank
        if dict_other["blank"] in quiz:
            print quiz
            user_guess = raw_input("Please write your answer for blank " + str(dict_other["nth_blank"]) + " here:  ")
            if user_guess.lower() == dic[dict_other["blank"]]: #For correct answer on first try
                correct_answer(quiz, dic)
                quiz = quiz.replace(dict_other["blank"], dic[dict_other["blank"]])#updates quiz
            else: #If wrong answer, player gets one more try
                wrong_answer(quiz, dic)
                quiz = quiz.replace(dict_other["blank"], dic[dict_other["blank"]])#updates quiz
    print "And that's it. Your final score is " + str(dict_other["score"]) + " point(s). Thanks for playing!"

def the_complete_game():
#   Behavior: This combines the above functions and runs the whole game
#   Inputs: Takes no inputs
#   Outputs: Outputs are the responses, judgments, and scorekeeping for the whole game
    game_intro()
    game_level()
    if dict_other["quiz_level"].lower() == "easy":
        game_play(quiz_easy, dict_easy)
    elif dict_other["quiz_level"].lower() == "medium":
        game_play(quiz_medium, dict_medium)
    elif dict_other["quiz_level"].lower() == "hard":
        game_play(quiz_hard, dict_hard)

the_complete_game()
