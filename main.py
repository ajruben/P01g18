#----------------------------------------------------------------------------------------------------------------------------------------------------
#main menu and controlling choice flow
def main(flag=[]):
    choice = input("Hi user!\nPlease select a world! You can choose out of 1 2 3 4")
    choice_flow(choice) #from here world handling is done, always ends at end_of_world()

def choice_flow(choice):
    #ifelse statements
    if choice == '1':
        run_world_1()
    elif choice == '2':
        run_world_2()
    elif choice == '3':
        run_world_3()
    elif choice == '4':
        run_world_4()
    else:
        print("ERROR: Please enter either 1, 2, 3, or 4")
        main()

#----------------------------------------------------------------------------------------------------------------------------------------------------
#world one
            
def run_world_1(): #ruben
    #variables
    w=1
    #body
    w1_r1() #first room

    
    #finish
    end_of_world(w)

#global variable for world1
gravity_active = False

#helper functions world 1
def toggle_gravity():
        global gravity_active
        gravity_active = not gravity_active

def show_gravity_activity():
    if gravity_active:
        print("Gravity activated. Normal gravity in effect.")
    else:
        print("Gravity deactivated. Zero gravity in effect.")

#rooms world 1
def w1_r1(): #world one room one
    welcome_text_room1 = """
    Welcome in the world of theoretical physics, where the physics is theoretical but the fun is real!
    You are in a world where you can control gravity, initially there is no gravity. You start in a room with a bunch of stuff floating about.
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
            print("Error: please enter either 'A' or 'B'.")
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
            print("Everything falls to the ground. Including you (ouch). Luckily we can still walk, lets grab the key!")
        elif toggle_choice == "B":
            print("Our gravity gadget inlcudes other features! We could also use the gravity ray to pull objects towards us (and us towards the object, considering Newtons third law).")
            
def w1r1_brute():
    pass

#----------------------------------------------------------------------------------------------------------------------------------------------------
#world two
            

def run_world_2(): #bram dhalloSSS
    #variables
    w=2
    #body
    choice = input("Welkom in wereld 2, wat wil je doen?")
    #finish
    end_of_world(w)

#----------------------------------------------------------------------------------------------------------------------------------------------------
#world three

def run_world_3(): #jade
    #variables
    w=3
    #body
    choice = input("Welkom in wereld 3, wat wil je doen?")
    #finish
    end_of_world(w)

#----------------------------------------------------------------------------------------------------------------------------------------------------
#world four
    
def run_world_4(): #michelle
    #variables
    w=4
    #body
    choice = input("Welkom in wereld 4, wat wil je doen?")
    #finish
    end_of_world(w)

def end_of_world(choice):
    play_again_choice = input(f"You did great in world {choice}, want to play again in another world? (yes or no)")
    if play_again_choice == "yes":
        main()
    elif play_again_choice == "no":
        print("Thanks for playing!")
        return None
    else:
        print("Error: Please enter yes or no. not capitalized.")
        end_of_world(choice)

if __name__ == "__main__":
    main()

