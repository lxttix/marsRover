class Rover:
    def __init__(self, num, x, y, heading): # Sets initial position of the rover
        self.num = num # 1, 2, 3 or 4th rover
        self.x = x
        self.y = y
        self.heading = heading # Orientation, represented by a letter

    def getInstructions(self, instructions):
        instructions = instructions.replace(" ", "")
        return instructions

    def move_n(self):
        self.y += 1
    
    def move_s(self):
        self.y -= 1
     
    def move_e(self):
        self.x += 1
    
    def move_w(self):
        self.x -= 1
    
    