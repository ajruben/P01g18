#----------------------------------------------------------------------------------------------------------------------------------------------------
#main menu and controlling choice flow 
#TODO req3: When the player has completed all worlds successfully, the main program congratulates them and ends the game. (use flags)


def main(name, flag=[]): #req2
    choice = input(f"Hi {name}!\nPlease select a world! You can choose out of 1 2 3 4")
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
    elif choice == '4':
        run_world_4()
        return 4
    else:
        print("ERROR: Please enter either 1, 2, 3, or 4")
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
    You are in a world where you can control gravity with a gravity gadget, initially there is no gravity. You start in a room with a bunch of stuff floating about.
    There is a locked door, the key is floating on the other side of the room.
    Would you like to open the door with brute force, or try and get the key?
    option A: brute force
    option B: try get the key
    """
    keyforce_choice = None
    while keyforce_choice == None:
        keyforce_choice = input(welcome_text_room1)
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
            print("Our gravity gadget inlcudes other features! We could also use the gravity ray to pull objects towards us (and us towards the object, considering Newtons third law). (story to be developed)")

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
            print("Maybe we could smash the bowling ball through the door... (story to be developed)")
        elif brute_choice == "B":
            print("WHAAAM, what a collision! The bowling ball blew a huge hole in the door. we can escape. hurray. the end.")
    
#----------------------------------------------------------------------------------------------------------------------------------------------------
#world two
            

def run_world_2(): #bram dhalloSSS
    #variables
    w=2
    #body
    choice = input("Welkom in wereld 2, wat wil je doen?")
    #finish


#----------------------------------------------------------------------------------------------------------------------------------------------------
#world three

def run_world_3(): #jade
    #variables
    w=3
    #body
    choice = input("Welkom in wereld 3, wat wil je doen?")
    #finish


#----------------------------------------------------------------------------------------------------------------------------------------------------
#world four
    
def run_world_4(): #michelle
    #variables
    w=4
    #body
    choice = input("Welkom in wereld 4, wat wil je doen?")
    #finish


def end_of_world(choice):
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

