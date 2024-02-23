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
    Welcome in the world of physics, where the physics is theoretical but the fun is real!
    You are in a world where you can control gravity, initially there is no gravity. You start in a room with a bunch of stuff floating around.
    There is a locked door, the key is floating on the other side of the room.
    Would you like to open the door with brute force, or try and get the key?
    option A: brute force
    option B: try get key
    """
    keyforce_choice = input(welcome_text_room1)

def w1r1_get_key():
    pass

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

