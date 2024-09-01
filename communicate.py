from rover import Rover

# Capture User input
x_r = 0 # Coordinates of upper right 
y_r = 0

def invalid_instruction():
    print("An instruction was invalid as the rover has reached the boundary of the plateau.")
    print("This instruction was disregarded.")

# Captures user input and catches any errors with validation
def get_user_input():
    global pos_x 
    global pos_y 
    global pos_l  # Letter of orientation e.g. N = North
    global instructions

    coordinates = False # True if all coordinates have been captured
    while coordinates == False:
        try:
            print("Please enter the rover's position.")
            print("This should be the x, y coordinates,")
            print("In addition to the letter of the rover's orientation, e.g. N = North.\n")
            
            # Ensures rover's starting position is within the plateau
            pos_x = int(input("X coordinate: "))
            while pos_x < 0 or pos_x > x_r:
                print("Please enter a coordinate within the plateau.\n")
                pos_x = int(input("X coordinate: "))

            pos_y = int(input("Y coordinate: "))
            while pos_y < 0 or pos_y > y_r:
                print("Please enter a coordinate within the plateau.\n")
                pos_y = int(input("Y coordinate: "))

            pos_l = input("Letter: ")
            valid_letters = ["N", "E", "S", "W"]
            while pos_l not in valid_letters:
                print("Please enter a valid orientation.")
                pos_l = str(input("Letter: "))
            print("Stored! \n")

            print("Please enter the instructions for the rover, separated by a space each.")
            print("L = Left 90 degrees, R = Right 90 degrees, M = Move forward.\n")
            instructions = input("Instructions: \n")
            valid_input = [" ", "M", "L", "R"]
            for i in range(0, len(instructions)):
                if instructions[i] not in valid_input:
                    print("Instructions were not valid! Please enter using the correct format. \n")
                    coordinates = False
                elif i + 1 == len(instructions):
                    print("Everything was valid!")
                    coordinates = True
            
        except:
            print("Coordinates invalid, please enter coordinates as an integer.\n")
            
            coordinates = False

print("Welcome to the Mars Rover Controller Room!\n")
default_rovers = [1, 2, 3, 4]

# Gets coordinates for upper right plateau
try:
    print("Please enter the coordinates for the upper right plateau.")
    x_r = int(input("The x coordinate: "))
    y_r = int(input("The y coordinate: "))
    print("Success!\n")
except:
    print("Please enter a valid integer for the coordinates.")

while len(default_rovers) != 0: # Ask user which rover they would like to control first
    print("Which rover would you like to control:")
    print(default_rovers)
    rover_num = input("Number: ")
    if rover_num.isdigit() == True: rover_num = int(rover_num) # Converts to int
    if rover_num in default_rovers: # Checks if user has already selected it
        print(f"Wonderful! You are now controlling rover {rover_num}. \n")

        get_user_input()
        print("Your input has been successfully recieved!\n")

        rover = Rover(rover_num, pos_x, pos_y, pos_l)
        instructions = rover.getInstructions(instructions)
        
        # Moves rover according to instructions
        # Make sure you always validate each move
        # Can't go into negative numbers, 0,0 is lowest position on plateau
        # Can't go above upper right plateau
        compass = ["N", "E", "S", "W"]

        print(f"Rover {rover.num} starting position:", rover.x, rover.y, rover.heading)
        compass_pos = compass.index(rover.heading)
        for i in instructions:
            if i == "L":
                compass_pos -= 1
                if compass_pos < 0: # Makes sure that it doesn't go into negative numbers
                    compass_pos = len(compass) - 1
            elif i == "R":
                compass_pos += 1
                if compass_pos >= len(compass): # Makes sure that it is still valid
                    compass_pos = 0
            elif i == "M":
                direction = compass[compass_pos]
                # Check if reaches lower bound
                if (rover.x == 0 and direction == "W") or (rover.y == 0 and direction == "S"):
                    invalid_instruction()
                # Check if reaches upper bound
                elif (rover.x == x_r and direction == "E") or (rover.y == y_r and direction == "N"):
                    invalid_instruction()
                else:
                    if direction == "N":
                        rover.move_n()
                    elif direction == "E":
                        rover.move_e()
                    elif direction == "S":
                        rover.move_s()
                    elif direction == "W":
                        rover.move_w()

        # OUTPUTS rover's final position
        print(f"Rover {rover.num} final position:", rover.x, rover.y, rover.heading + "\n")
        default_rovers.remove(rover_num) # Removes rover from list after it has been positioned
    else:
        print("Please enter a valid number!\n")
