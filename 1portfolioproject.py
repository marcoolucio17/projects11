#Jeopardy Game!
from doctest import ELLIPSIS_MARKER
from os import name
import random 

class Contestants:
    def __init__(self, name):
        self.name = name
        self.points = []


# questions
# science
# 100 =  What does a seismologist study? Earthquakes; At what temperature does water first boil? 212 F or 100 C; What is group of cells that work together and form an organ called? Tissue
# 200 = What caused the Irish potato famine of the 1840's? Blight; What do we call the lower chambers of the human heart? Ventricles; What is the term for the capacity of a body or system to do work? Energy
# 300 = What is the name for the boundary around a black hole, beyond which events cannot affect the observer? Event Horizon; In which year did the first space shuttle launch? 1981; What is the fastest fish in the sea? Sailfish
# 400 = What is Gregor Mendel known to be the father of? Genetics; What is the tendency of Earth's rotation to turn winds called? Coriolis Effect; What is the piece of metal on a bridle that goes into the horse's mouth? Bit
# 500 = If an explosive liquid is 74 degrees Fahrenheit, what is its Centigrade temperature? 23 1/3; Which animal has a gestation period of only 13 days? Opossum; What is the very bottom soil horizon called? Bedrock
# geography 
# 100 = Jamaica is closest to which state in the U.S.? Florida; Mitsubishi, Sony and Toyota are all companies with roots in what country? Japan; Tijuana, Ensenada, Acapulco and Cancun are cities in what country? Mexico
# 200 = What is the lowest point below sea level in the Western Hemisphere? Death Valley; What Arkansas city is the origin of 47 natural hot springs? Hot Springs: What area were potatoes originally from? Peru
# 300 = What country is bordered by Pakistan to the south and Iran to the west? Afghanistan; The Rhine River runs through what country? Germany; In which country are the large islands New Britain and New Ireland located? Papua New Guinea
# 400 = What country is bordered by Somalia, Ethiopia, Tanzania and Uganda? Kenya; What country has the eighth-largest population in Europe with approximately 38.5 million residents? Poland; What is the capital city of Sierra Leone on the western coast of Africa? Freetown
# 500 = Which Asian capital was formerly known as Batavia? Jakarta; In which country would you find fried meatballs served with potatoes and gravy called frikadeller? Denmark; Which country has Bishkek as its capital? Kyrgyzstan

class Questions: 
    def __init__(self, section, points, question, answer):
        self.section = section
        self.points = points
        self.question = question
        self.answer = answer
        self.question = []
                
#points_selection = input("Write the amount of points for the question")
                #if points_selection == int:
                    #points_selection 
                    #self.question.append()
            

gq100 = ["Jamaica is closest to which state in the U.S.?", "Mitsubishi, Sony and Toyota are all companies with roots in what country?", "Tijuana, Ensenada, Acapulco and Cancun are cities in what country?"]
ga100 = ["Florida", "Japan", "Mexico"]

gq200 = ["What is the lowest point below sea level in the Western Hemisphere?", "What Arkansas city is the origin of 47 natural hot springs?", "What area were potatoes originally from?"]
ga200 = ["Death Valley", "Hot Springs", "Peru"]

gq300 = ["What country is bordered by Pakistan to the south and Iran to the west?", "The Rhine River runs through what country?", "In which country are the large islands New Britain and New Ireland located? "]
ga300 = ["Afghanistan", "Germany", "Papua New Guinea"]

gq400 = ["What country is bordered by Somalia, Ethiopia, Tanzania and Uganda?", "What country has the eighth-largest population in Europe with approximately 38.5 million residents?", "What is the capital city of Sierra Leone on the western coast of Africa?"]
ga400 = ["Kenya", "Poland", "Freetown"]

gq500 = ["Which Asian capital was formerly known as Batavia?", "In which country would you find fried meatballs served with potatoes and gravy called frikadeller?", "Which country has Bishkek as its capital?"]
ga500 = ["Jakarta", "Denmark", "Kyrgyzstan"]

#SCIENCE SECTION
# 100 =  What does a seismologist study? Earthquakes; At what temperature does water first boil? 212 F or 100 C; What is group of cells that work together and form an organ called? Tissue
# 200 = What caused the Irish potato famine of the 1840's? Blight; What do we call the lower chambers of the human heart? Ventricles; What is the term for the capacity of a body or system to do work? Energy
# 300 = What is the name for the boundary around a black hole, beyond which events cannot affect the observer? Event Horizon; In which year did the first space shuttle launch? 1981; What is the fastest fish in the sea? Sailfish
# 400 = What is Gregor Mendel known to be the father of? Genetics; What is the tendency of Earth's rotation to turn winds called? Coriolis Effect; What is the piece of metal on a bridle that goes into the horse's mouth? Bit
# 500 = If an explosive liquid is 74 degrees Fahrenheit, what is its Centigrade temperature? 23 1/3; Which animal has a gestation period of only 13 days? Opossum; What is the very bottom soil horizon called? Bedrock
# geography 

sq500 = ["If an explosive liquid is 74 degrees Fahrenheit, what is its Centigrade temperature?", "Which animal has a gestation period of only 13 days?", "What is the very bottom soil horizon called?"]
sa500 = ["23 1/3", "Opossum", "Bedrock"]

sq400 = ["What is Gregor Mendel known to be the father of? ", "What is the tendency of Earth's rotation to turn winds called?", "What is the piece of metal on a bridle that goes into the horse's mouth?"]
sa400 = ["Genetics", "Coriolis Effect", "Bit"]

sq300 = ["What is the name for the boundary around a black hole, beyond which events cannot affect the observer? ", "In which year did the first space shuttle launch? ", "What is the fastest fish in the sea?"]
sa300 = ["Event Horizon", "1981", "Sailfish"]

sq200 = ["What caused the Irish potato famine of the 1840's?", "What do we call the lower chambers of the human heart?", "What is the term for the capacity of a body or system to do work?"]
sa200 = ["Blight", "Ventricles", "Energy"]

sq100 = ["What does a seismologist study?", "At what temperature (fahrenheit) does water first boil? Write only the number", "What is group of cells that work together and form an organ called?"]
sa100 = ["Earthquakes", "212", "Tissue"]


geodict = {# 100 = Jamaica is closest to which state in the U.S.? Florida; Mitsubishi, Sony and Toyota are all companies with roots in what country? Japan; Tijuana, Ensenada, Acapulco and Cancun are cities in what country? Mexico
# 200 = What is the lowest point below sea level in the Western Hemisphere? Death Valley; What Arkansas city is the origin of 47 natural hot springs? Hot Springs: What area were potatoes originally from? Peru
# 300 = What country is bordered by Pakistan to the south and Iran to the west? Afghanistan; The Rhine River runs through what country? Germany; In which country are the large islands New Britain and New Ireland located? Papua New Guinea
# 400 = What country is bordered by Somalia, Ethiopia, Tanzania and Uganda? Kenya; What country has the eighth-largest population in Europe with approximately 38.5 million residents? Poland; What is the capital city of Sierra Leone on the western coast of Africa? Freetown
# 500 = Which Asian capital was formerly known as Batavia? Jakarta; In which country would you find fried meatballs served with potatoes and gravy called frikadeller? Denmark; Which country has Bishkek as its capital? Kyrgyzstan
}
        
print("Let's play Jeopardy!")
name1 = input("Please write Player1's name... ")
name2 = input("Please write Player2's name... ")
print("{name} will start to play, next will be {name2}'s turn".format(name = name1, name2 = name2))
print("""Instructions are the following: Select a Jeopardy section as you will stay within that section for the rest of the game.
 When its your turn to play, write an amount of points in order to get a question. 
 Points go as following: 
 100, 
 200, 
 300, 
 400, 
 500.
 The bigger the amount of points the harder the question is. Remember to type everything correctly, good luck!""")
section1 = input("{name} please write Geography or Science... ".format(name=name1))
while section1 != "Geography" and section1 != "geography" and section1 != "Science" and section1 != "science":
    section1 = input("Please type the name of the section correctly")


question_for_section1 = []
user_answer = []

total_points_p1 = 0
total_points_p2 = 0

class Points:
    def __init__(self, pts, pts_to_win):
        self.pts = pts
        self.pts_to_win = pts_to_win

class Player:
    def __init__(self, name):
        self.name = name
        self.pts = 0
        
    def counter(self, pts_to_add):
        self.pts += pts_to_add
            

player1 = Player(name1)
player2 = Player(name2)
players = [player1, player2]
    

def play(player):
    points_for_the_question = 0
    random_index = random.randint(0,2)
    if section1 == "Geography" or section1 == "geography":
        points_selected = int(input("For how many points would you like to go?"))
        while points_selected != 100 and points_selected != 200 and points_selected != 300 and points_selected != 400 and points_selected != 500 and points_selected == '':
            points_selected = int(input("Please type a valid amount.. "))
        if points_selected == 500:
            question_for_section1.append(gq500[random_index])
            user_answer = input(question_for_section1)
            question_for_section1.pop(0)
            gq500.pop(random_index)
            if user_answer == ga500[random_index]:
                points_for_the_question += 500
                player.counter(500)
                print("Correct!! You have: 500 points.")
            else:
                print("Wrong answer! You have 0 points")
        if points_selected == 400:
            question_for_section1.append(gq400[random_index])
            user_answer = input(question_for_section1)
            question_for_section1.pop(0)
            gq400.pop(random_index)
            if user_answer == ga400[random_index]: 
                points_for_the_question += 400
                player.counter(400)
                print("Correct! You have: 400 points.")
            else: 
                print("Wrong! You have: 0 points.")
        if points_selected == 300:
            question_for_section1.append(gq300[random_index])
            user_answer = input(question_for_section1)
            question_for_section1.pop(0)
            gq300.pop(random_index)
            if user_answer == ga300[random_index]:
                points_for_the_question += 300
                player.counter(300)
                print("Correct! You have 300 points.")
            else:
                print("Incorrect!! You have 0 points")
        if points_selected == 200:
            question_for_section1.append(gq200[random_index])
            user_answer = input(question_for_section1)
            question_for_section1.pop(0)
            gq200.pop(random_index)
            if user_answer == ga200[random_index]:
                points_for_the_question += 200
                player.counter(200)
                print("Correct!! You have 200 points")
            else:
                print("Wrong! You have 0 points")
        if points_selected == 100:
            question_for_section1.append(gq100[random_index])
            user_answer = input(question_for_section1)
            question_for_section1.pop(0)
            gq100.pop(random_index)
            if user_answer == ga100[random_index]:
                points_for_the_question += 100
                player.counter(100)
                print("Correct!! You have 100 points.")
            else:
                print("Wrong!! You have 0 points")
    if section1 == "Science" or section1 == "science":
        points_selected = int(input("For how many points would you like to go?.. "))
        while points_selected != 100 and points_selected != 200 and points_selected != 300 and points_selected != 400 and points_selected != 500 and points_selected == '':
            points_selected = int(input("Please type a valid amount.. "))
        if points_selected == 500:
            question_for_section1.append(sq500[random_index])
            user_answer = input(question_for_section1)
            question_for_section1.pop(0)
            sq500.pop(random_index)
            if user_answer == sa500[random_index]:
                points_for_the_question += 500
                player.counter(500)
                print("Correct!! You have: 500 points")
            else: 
                print("Wrong!! You have 0 points")
        if points_selected == 400:
            question_for_section1.append(sq400[random_index])
            user_answer = input(question_for_section1)
            question_for_section1.pop(0)
            sq400.pop(random_index)
            if user_answer == sa400[random_index]:
                points_for_the_question += 400
                player.counter(400)
                print("Correct!! You have 400 points")
            else:
                print("Wrong!! You have 0 points")
        if points_selected == 300:
            question_for_section1.append(sq300[random_index])
            user_answer = input(question_for_section1)
            question_for_section1.pop(0)
            sq300.pop(random_index)
            if user_answer == input(question_for_section1):
                points_for_the_question += 300
                player.counter(300)
                print("Correct!! You have 300 points")
            else:
                print("Wrong!! You have 0 points")
        if points_selected == 200:
            question_for_section1.append(sq200[random_index])
            user_answer = input(question_for_section1)
            question_for_section1.pop(0)
            sq200.pop(random_index)
            if user_answer == sa200[random_index]:
                points_for_the_question += 200
                player.counter(200)
                print("Correct!! You got 200 points")
            else:
                print("Wrong!! You have 0 points")
        if points_selected == 100:
            question_for_section1.append(sq100[random_index])
            user_answer = input(question_for_section1)
            question_for_section1.pop(0)
            sq100.pop(random_index)
            if user_answer == sa100[random_index]:
                points_for_the_question += 100
                player.counter(100)
                print("Correct!! You have 100 points")
            else:
                print("Wrong!! You have 0 points")


#to avoid repeating the same questions, use .pop on gq, sq with[random_index]
#if the question is already used, ask user to write another score
        
play(players[0])
print("Player2's turn!")
play(players[1])
print("Player1's turn!")
play(players[0])
print("Player2's turn!")
play(players[1])
print("Player1's turn!")
play(players[0])
print("Player2's turn!")
play(players[1])
print(name1 + "'s points are: " + str(players[0].pts))
print(name2 + "'s points are: " + str(players[1].pts))
if players[0].pts > players[1].pts:
    print(name1 + ' won the game!!')
else: 
    print(name2 + ' won the game!!')

            
        






            

        
    