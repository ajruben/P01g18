#----------------------------------------------------------------------------------------------------------------------------------------------------
#main menu and controlling choice flow 
#TODO req3: When the player has completed all worlds successfully, the main program congratulates them and ends the game. (use flags)
#comment for git
global_start_time = 0

import time
def main(name, flag=[]): #req2
    
    
    choice = input(f"Hi {name}!\nPlease select a world! You can choose out of 1 2 3")
    #from here world handling is done, always ends at end_of_world()
    w = choice_flow(choice) 
    end_of_world(w)

def choice_flow(choice):
    #ifelse statements
    if choice == '1':
        run_world_1()
        return 1
    elif choice == '2':
        run_world_2()
        return 2
    elif choice == '3':
        run_world_3()
        return 3
    else: #errorhandling
        print("ERROR: Please enter either 1, 2 or 3")
        main()

#----------------------------------------------------------------------------------------------------------------------------------------------------
#world one, req 5: d can be completed by the player, if necessary by starting the world again and trying another route. There is no ultimate “game over” state.
            
def run_world_1(): #ruben
    #variables
    #body
    w1_r1() #first room

    
    #finish
    

#global variable for world1
gravity_active = False

#helper functions world 1
def toggle_gravity():
        global gravity_active
        gravity_active = not gravity_active

def show_gravity_activity():
    if gravity_active:
        print("Normal gravity in effect.")
    else:
        print("Zero gravity in effect.")

#rooms world 1
def w1_r1(): #world one room one, #TODO: include time: can you set record? write and load from text file.
    welcome_text_room1 = """
    Welcome in the world of theoretical physics, where the physics is theoretical but the fun is real!
    You are in a room where you can control gravity with a gravity gadget, initially there is no gravity. 
    It's an escape room, as soon as you make your first choice, you will be timed. Can you beat the record?
    You're in a room with a bunch of stuff floating about.
    There is a locked door, the key is floating on the other side of the room.
    Would you like to open the door with brute force, or try and get the key?
    option A: brute force
    option B: try get the key
    """
    keyforce_choice = None
    while keyforce_choice == None:
        keyforce_choice = input(welcome_text_room1)
        
        start_timer()
        if keyforce_choice == "A":
            w1r1_brute()
        elif keyforce_choice == "B":
            w1r1_get_key()
        else:
            print("Error: please enter either 'A' or 'B'. Restarting game.")
            keyforce_choice = None


def w1r1_get_key():
    first_text_key = """
    Right now we can't reach the key. Luckily we can control the gravity with our gravity gadget.
    One of the features is the gravity toggler, which can toggle gravity on and off.
    Do you want to turn the gravity on? (a = g =  9.81 ms^2)
    Option A: yes
    Option B: no
    please type 'A' or 'B' to confirm your choice.
    """
    toggle_choice = None
    while toggle_choice == None:
        toggle_choice = input(first_text_key)
        if toggle_choice == "A":
            toggle_gravity()
            show_gravity_activity()
            print("Everything falls to the ground. Including you (ouch). Luckily we can still walk, lets grab the key and unlock the door! hurray we escaped.")
        elif toggle_choice == "B":
            show_gravity_activity()
            print("Our gravity gadget inlcudes other features! We could also use the gravity ray to pull objects towards us (and us towards the object, considering Newtons third law).")
            toggle_choice_()
        else:
            print("Error: please enter either 'A' or 'B'. Restarting option.")
            toggle_choice = None

def toggle_choice_():
    string = """
    We could take two approaches, each takes a different amount of time. Remember, you're being clocked!.
    Option A: Use the gravity ray to pull the key and the lock together.
    Option B: We pull the key towards us, and pull ourselves towards the key.
    """
    pull_choice = None
    import random
    approach_A = random.randint(2,4)
    approach_B = random.randint(1,3)
    while pull_choice == None:
        pull_choice = input(string)
        
        if pull_choice == "A":
            print("Carrying out option A...")
            time.sleep(approach_A)
            print(f"Well done, the key went right into the lock and opened the door, it took {approach_A} seconds")
        elif pull_choice == "B":
            print("Carrying out option B...")
            time.sleep(approach_B)
            print(f"Well done, the key went right into the lock and opened the door, it took {approach_B} seconds")
        else:
            print("Error: please enter either 'A' or 'B'. Restarting option.")
            pull_choice = None

def w1r1_brute():
    first_text_brute = """
    Trying to get the key is going to be difficult, so I understand your choice.
    We notice that there are several more objects floating about in this room, one of which is a bowling ball.
    Hmm...
    Lets use our gravity gadget!
    Option A: turn gravity on
    Option B: Change the direction of the gravity towards the door, activate the gravity in intense mode (a=100ms^2, i.e., everything accelerates ten times faster than on earth!)
    """
    brute_choice = None
    while brute_choice == None:
        brute_choice = input(first_text_brute)
        if brute_choice == "A":
            w1r1_smash_brute_choice()
        elif brute_choice == "B":
            print("WHAAAM, what a collision! The bowling ball blew a huge hole in the door. we can escape. hurray. the end.")
        else:
            print("Error: please enter either 'A' or 'B'. Restarting option.")
            brute_choice = None

def w1r1_smash_brute_choice():
    string = """
    Maybe we could smash the bowling ball through the door...
    Option A: Use our muscles to throw the ball through the door.
    Option B: Use our gravity gadget to throw ourselves while holding the ball through the door.
    """
    smash_choice = None
    while smash_choice == None:
        smash_choice = input(string)
        if smash_choice == "A":
            print("Hmm... That didnt work. Gotta eat more spinach.")
            print("But hey look, there is the key!")
            key_choice_smash()
        elif smash_choice == "B":
            print("Somehow that worked, well done!")
        else:
            print("Error: please enter either 'A' or 'B'. Restarting option.")
            smash_choice = None    
        
def key_choice_smash():
    string = """
    Maybe we could smash the key through the door...
    Option A: Use our muscles to throw the key through the door.
    Option B: Use the key like a normal human being.
    """
    key_choice = None
    while key_choice == None:
        key_choice = input(string)
        if key_choice == "A":
            print("Wow, you threw the key exactly in the lock! The door unlocked and you escaped!")
        elif key_choice == "B":
            print("Wow you unlocked the door like a normal human being! You made it out!")
        else:
            print("Error: please enter either 'A' or 'B'. Restarting option.")
            key_choice = None




#----------------------------------------------------------------------------------------------------------------------------------------------------
#world two
            

def run_world_2(): #bram 
    #variables
    w=2
    #body
    #welcome the player
    introduction = """"
    Welcome to the world of economic decision making! While you’re here you will explore more about 
    yourself and how you think.
    
    In this world there live both econs and humans. Today you are going to visit the city where all the econs live. 
    A long time assumption in the world of economic decision making is that every person behaves rational.
    But actually in real lif we see that most people behave biased. We call biased people ‘humans’ and rational people ‘econs’.
    """
    #set variable for explenation rationality
    rationality = """
    Economists assume that people will make choices in their own self-interest. They will choose those things that provide the greatest personal benefit,\
     and they'll avoid things that aren't as personally valuable and compelling. That's what we mean by the assumption of rationality."""
    
    print(f'{introduction}')
    
    #Does the player know rationality? 
    know_rationality = input("Do you know what the concept of rationality in economics is? (yes/no) ")
    while(not(know_rationality == 'yes' or know_rationality == 'no')):
        print('ERROR, please answer the question with yes or no')
        know_rationality = input("Do you know what the concept of rationality in economics is? (yes/no) ")
    if know_rationality == 'yes':
        print("Great! let's start.")
    elif know_rationality == 'no':
        print(f'{rationality}')
    #need to add a loop to go back to the question for both elif and else statement
        
    #What do you think you are?
    print(" ")
    own_choice = input("Now that you have read the introduction, do you consider yourself an 'econ' or a 'human' (econ/human) ")
    while(not(own_choice == 'econ' or own_choice == 'human')):
        print('ERROR, please answer the question with econ or human (without capital letters)')
        own_choice = input("Now that you have read the introduction, do you consider yourself an 'econ' or a 'human' (econ/human) ")
    if own_choice == 'econ' or 'human':
        print("Alright, let's check that!")
    
    #set a formula for the suspicion level    
    suspicion = 0
    
    #Introduction in the city and the first encounter
    print(f"""You entered the city of where all of the so called econs live. To stay here you have to\
     act rationally. Otherwise the econs in the city will grow suspicious of you. currently your\
     level is {suspicion} There don't live a lot of people in the city of the econs. And immediately a woman comes up to you and says that she doesn't regognize you.
    
    The woman says: 'You are only allowed to visit the city if you are a real rational thinker.'\
     And she asks you a question.""")
    print(' ')
    euros = int(input("She asks: If you have 100 euros and you had to divide it between you and someone else.\
     How much would you give to the other person? (in whole euros) "))
    while (not(euros >= 1 and euros <= 100)):
        print('ERROR, please enter an integer between 1 and 100.')
        euros = int(input("She asks: If you have 100 euros and you had to divide it between you and someone else.\
     How much would you give to the other person? (in whole euros) "))
    print('')
    if euros == 1:
        print("Woman: 'Correct! I did not regognize you but it seems like you belong here.'")
        print(f"Your suspicion level is {suspicion}")  
    elif euros > 1 and euros <= 100:
        suspicion += 1
        print("Woman: 'You know it is actually 1 right? Because you want to give the minimal amount\
     you can give to the other person")
        print(f"Your suspicion level is {suspicion}")
    
    #second encounter and second question
    print()
    print("""You walk away from the weird woman and go further explore the city. You get thirsty and you go to a corner shop to buy\
    a bottle of water. The bottle costs €1.95, and you pay with a €2 coin. Before you walk away \
    the cashier says: 'Do you not want your 5 cents back? No one ever walks away withour asking \
    for their change in this city.' You nervously ask your 5 cents back but the cashier still \
    wants to test if you really belong in the city. """)
           
    flip_coin_certainty = input("""He asks: 'If I would give you two choices:
    A. Flip a coin. If it lands on heads, you win 100 euros, if it lands on tails, you win nothing.
    B. You are certain to get 46 euros.
    Which one would you choose? (A/B)' """)
    while (not(flip_coin_certainty == 'A' or flip_coin_certainty == 'B')):
        print('ERROR, please enter either A or B (in capital letters)')
        flip_coin_certainty = input("""He asks: If I would give you two choices:
    A. Flip a coin. If it lands on heads, you win 100 euros, if it lands on tails, you win nothing.
    B. You are certain to get 46 euros.
    Which one would you choose? (A/B) """)
    if flip_coin_certainty == 'A':
        print("That's the right choice, have a nice rest of your day!")
        print(f"Your supsicion level is {suspicion}")
        print("You thank the cashier and walk away.")
    elif flip_coin_certainty == 'B':
        print("That's is not correct, option A has a higher expected outcome. Do you really belong in this city?")
        suspicion += 1
        print(f"Your suspicion level is {suspicion}")
        print("Because you are not yet done exploring the city, you thank the cashier for the water and walk away.")
    
    #third encounter and third question
    print('')
    print(""""While walking in the street to your next location, you get a newspaper from a man in the street. \
    on the back there is a daily rationality test question. It reads:
    Linda is 31 years old, single, outspoken, and very bright. She majored in philosophy.\
     As a student she was deeply concerned with issues of discrimination and social justice \
    and also participated in anti-nuclear demonstrations.
    
    Now which of two alternatives is more probable?
    A. Linda is a bank teller
    B. Linda is a bank teller who is active in the feminist movement
    """)
    linda_choice = input("Seeing that you read the question on the back of the newspaper, a passerby taps you on the shoulder and asks: \
    'Which one would you choose?' (A/B) ")
    while (not(linda_choice == 'A' or linda_choice == 'B')):
        print('ERROR, please enter either A or B (in capital letters)')
        linda_choice = input("Seeing that you read the question on the back of the newspaper a passerby taps you on the shoulder and says: \
        'Which one would you choose?' (A/B) ")
    if linda_choice == 'A':
        print("Yes that's correct!")
        print(f"Your supsicion level is {suspicion}")
    else:
        print("That's not correct, being solely a bankteller is always more probable.")
        suspicion += 1
        print(f"Your supsicion level is {suspicion}")
    
    #maybe make a function of this that you can run after every question
    print('')
    if suspicion >= 2:
        print("Your suspicion level is too high and the econs realise that you do not belong in the \
    city of econs. You have been kicked out.")
    elif suspicion == 1:
        print("You are for now allowed to stay in the city but the people in the city are becoming suspicious of you.")
    else:
        print("You blend in perfectly. You are allowed to stay in the city.")
    
    #set variable for if the trst classify the player as a human or econ
    print('')
    print("Thank you for visiting the city of econs.")
    print('')
    if suspicion >= 1:
        test_choice = 'human'
        print("From the tests presented to you in the city of econs we can conclude that you can be \
    classified as a human.")
    else:
        test_choice = 'econ'
        print("from the questions we can conclude that you can be classified as an econ.")
        
    #make function to say if the player was correct in the beginning
    print('')
    print("Let's compare your results to the answer you gave in the beginning.")
    print('')
    if test_choice == 'human' and own_choice == 'human':
        print("You know yourself well! You were right from the start!")
    elif test_choice == 'human' and own_choice =='econ':
        print("Your guessed wrong at the start :( , but now you know!")
    elif test_choice == 'econ' and own_choice =='human':
        print("Your guessed wrong at the start :( , but now you know!")
    elif test_choice == 'econ' and own_choice =='econ':
        print("You know yourself well! You were right from the start!")
      
    #thank player for playing and return to the main menu
    print('')
    print("Thank you for playing the world of economic decision making. I hope you enjoyed visiting the city of econs.")
    #put in function that makes player go back to the choice of the worlds
    #finish



#----------------------------------------------------------------------------------------------------------------------------------------------------
#world three

def run_world_3(): #jade
    print("Welcome to the molecular life sciences world!")
    print("You need to collect letters everytime you are done with a question, at the end you need to make a correct word with these letters to finish this world.")

    while True:
        exited = input("Are you exited to learn about biology, chemistry and pharmacy? (y/n)")
        if exited == "n":
            print("Think again")
        elif exited == "y":
            print("Great! Let's get started. (The first letter is: e)")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            
    #biology part

    max_attempts = 3
    wrong_guesses = 0

    while wrong_guesses < max_attempts:
        question_1 = int(input("How many amino acids are there? "))
        if question_1 == 20:
            print("Good job! (The second letter is: l)")
            break
        else:
            wrong_guesses += 1
            remaining_attempts = max_attempts - wrong_guesses
            if remaining_attempts > 0:
                print(f"Sorry, that's incorrect. You have {remaining_attempts} attempts remaining.")
            else:
                print(f"Sorry, you've used all your attempts. The correct answer is 20. (The second letter is: l)")
                break
    while True:
        question_2 = input("What is the process by which a diploid cell splits into four haploid cells? (a. Mitosis b. Meiosis c. Binary fission d. Budding) ")
        if question_2 == "a" or question_2 == "c" or question_2 == "d":
            print("Think again")
        elif question_2 == "b":
            print("Great! Let's continue. (The third letter is: m)")
            break
        else:
            print("Invalid input. Please enter 'a' or 'b' or 'c' or 'd'.")

    #chemistry part        
    question_3 = input("What is the charge of a proton? (+/-)")
    if question_3 == "+":
        print("You are correct! (The fourth letter is: u)")
    elif question_3 == "-":
        print("No, a proton has a positive charge. (The fourth letter is: u)")
    else:
        print("Invalid input. Please enter '+' or '-'.")
        
    while True:
        question_4 = input("What type of bond is formed between two atoms that share electrons equally? (a. Ionic bond b. Covalent bond c. Metallic bond d. Hydrogen bond) ")
        if question_4 == "a" or question_2 == "c" or question_2 == "d":
            print("Think again")
        elif question_4 == "b":
            print("Great! Let's continue (The fifth letter is: o)")
            break
        else:
            print("Invalid input. Please enter 'a' or 'b' or 'c' or 'd'.")

    #pharmacy part
    max_attempts = 3
    wrong_guesses = 0

    while wrong_guesses < max_attempts:
        question_5 = int(input("What is the total volume of a 5% dextrose solution containing 250 grams of dextrose in 1000 milliliters (ml)? "))
        if question_5 == 1000:
            print("Good job! (The sixth letter is: c)")
            break
        if question_5 > 1000:
            print("The answer is lower, guess again")
        if question_5 < 1000:
            print("The answer is higher, guess again")
        wrong_guesses += 1
        remaining_attempts = max_attempts - wrong_guesses
        if remaining_attempts > 0:
            print(f"You have {remaining_attempts} attempts remaining.")
        else:
            print(f"Sorry, you've used all your attempts. The correct answer is 1000. (The sixth letter is: c)")
            break
        
    while True:
        question_6 = input("Which dosage form is designed to release the drug gradually over an extended period, providing sustained therapeutic effect? (a. Capsule b. Tablet c. Transdermal patch d. Solution) ")
        if question_6 == "a" or question_6 == "b" or question_6 == "d":
            print("Think again")
        elif question_6 == "c":
            print("Great! Let's continue (The sevent letter is: e)")
            break
        else:
            print("Invalid input. Please enter 'a' or 'b' or 'c' or 'd'.")

    #story question        
    while True:
        question_7 = input("In the town of Evergreen, a group of researchers has discovered a new species of plant in the nearby forest. The plant, named Glowleaf, emits a faint bioluminescent glow at night. Excited by this discovery, the researchers want to investigate the biochemical mechanism responsible for the glow. After conducting experiments, they identify an enzyme called 'luciferase' that catalyzes the reaction producing light. What type of biomolecule is luciferase? (a. Carbohydrate b. Lipid c. Protein d. Nucleic acid) ")
        if question_7 == "a" or question_7 == "b" or question_7 == "d":
            print("Think again")
        elif question_7 == "c":
            print("Great! Let's continue (The last letter is: l)")
            break
        else:
            print("Invalid input. Please enter 'a' or 'b' or 'c' or 'd'.")
            
    #code word
    max_attempts = 3
    wrong_guesses = 0

    while wrong_guesses < max_attempts:
        code_word = input("To finish this world fill in the correct code word:")
        if code_word == "molecule":
            print("Congatualations! You successfully completed this world")
            break
        wrong_guesses += 1
        remaining_attempts = max_attempts - wrong_guesses
        if remaining_attempts > 0:
            print(f"Sorry, that's incorrect. You have {remaining_attempts} attempts remaining.")
        else:
            print(f"Sorry, you've used all your attempts. The correct answer is molecule. Thank you for participating")
            break
    #finish
    #variables
    w=3
    #body
    #introduction


#---------------------------------------------------------------------------------------------------------------------------------------------------
def start_timer():
    global global_start_time
    print("Starting Timer...")
    global_start_time = time.time()

def stop_timer():
    global global_start_time
    elapsed_time = time.time() - global_start_time
    return elapsed_time   


def write_player_time_to_file(player_name, time_set, file_path):
    with open(file_path, 'a') as file:
        file.write(f"{player_name}\t{time_set}\n")


def get_highest_score(file_path):
    highest_score = 1000
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            player_name, time_set = line.strip().split('\t')
            if float(time_set) < float(highest_score):
                highest_score = float(time_set)
                record_holder = player_name
    return highest_score, record_holder

def end_of_world(choice):
    if global_start_time != 0:
        time= stop_timer()

        write_player_time_to_file(player_name=name, time_set=time, file_path='records.txt')
        highest_score, record_holder = get_highest_score(file_path='records.txt')
        print(f"You scored {time:.2f}, the current highest score is: {highest_score:.2f} set by {record_holder}")
        

    play_again_choice = input(f"You did great in world {choice}, want to play again in another world? (yes or no)")
    if play_again_choice == "yes":
        main(name)
    elif play_again_choice == "no":
        print("Thanks for playing!")
    else:
        print("Error: Please enter yes or no. not capitalized.")
        end_of_world(choice)

if __name__ == "__main__":
    name = input("Welcome to our game! Can you please give your name?") #req 1
    main(name)

