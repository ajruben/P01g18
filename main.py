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
    
def run_world_1(): #ruben
    #variables
    w=1
    #body
    choice = input("Welkom in wereld 1, wat wil je doen?")
    #finish
    end_of_world(w)

def run_world_2(): #bram dhalloSSS
    #variables
    w=2
    #body
    choice = input("Welkom in wereld 2, wat wil je doen?")
    #finish
    end_of_world(w)

def run_world_3(): #jade
    #variables
    w=3
    #body
    choice = input("Welkom in wereld 3, wat wil je doen?")
    #finish
    end_of_world(w)

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

