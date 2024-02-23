#TODO
chagne if else to mapping
def main(name, flag=[]): 
    choice = input(f"Hi {name}!\nPlease select a world! You can choose out of 1 2 3 4: ")

    world_mapping = {
        '1': run_world_1,
        '2': run_world_2,
        '3': run_world_3,
        '4': run_world_4
    }

    if choice in world_mapping:
        w = choice_flow(world_mapping[choice])
        end_of_world(w)
    else:
        print("ERROR: Please enter either 1, 2, 3, or 4")
        main(name)

def choice_flow(world_function):
    return world_function()
