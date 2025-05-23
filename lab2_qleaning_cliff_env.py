import numpy as np

class Env:
    def __init__(self):
        self.height = 4
        self.width = 12
        self.posX = 0
        self.posY = self.height -1 # make the bot start from bottom left corner
        self.endX = self.width-1
        self.endY = self.height-1
        self.actions = [0, 1, 2, 3]
        self.stateCount = self.height*self.width
        self.actionCount = len(self.actions)
        self.cliff = [(X, self.height-1) for X in range(1,self.width-1)]
        # set cliff from (1,3) to (10,3)

    def reset(self):
        self.posX = 0
        self.posY = self.height-1
        self.done = False
        return 0, 0, False

    # take action
    def step(self, action):
        if action == 0: # left
            self.posX = self.posX-1 if self.posX > 0 else self.posX
        if action == 1: # right
            self.posX = self.posX+1 if self.posX < self.width - 1 else self.posX
            #if bot is at position X and position X is less than the width then move right, else stay at position X
        if action == 2: # up
            self.posY = self.posY-1 if self.posY > 0 else self.posY
        if action == 3: # down
            self.posY = self.posY+1 if self.posY < self.height - 1 else self.posY

        done = self.posX == self.endX and self.posY == self.endY
        # if the bot reach the goal, that means done=True

            # Check if agent falls into cliff
        if (self.posX, self.posY) in self.cliff:
            reward = -100 # big penalty for falling of the cliff
            done = False
            self.posX, self.posY = 0, self.height - 1  # Reset to start
        elif self.posX == self.endX and self.posY == self.endY:
            reward = 1
            done = True
        else:
            reward = -1  # Small penalty for every move
            done = False

        # mapping (x,y) position to number between 0 and 12x4-1=47
        nextState = self.width * self.posY + self.posX
        reward = 1 if done else 0
        return nextState, reward, done

    # return a random action
    def randomAction(self):
        return np.random.choice(self.actions)

    # display environment
    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.posY == i and self.posX == j:
                    print("O", end='')
                elif self.endY == i and self.endX == j:
                    print("T", end='')
                elif (j,i) in self.cliff:
                    print("X", end='')
                else:
                    print(".", end='')
            print("")