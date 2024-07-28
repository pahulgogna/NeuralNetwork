import pygame
import sys
from utils import generateRandomPoints, Team, guess, RandomWeights, train
from config import height, width, screen_size

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# initialize pygame
pygame.init()

# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")
 
SizeOfTrainingDataset = 1000 # Higher the size, higher the accuracy.
LearningRate = .1   #this represents how much will the values vary on each iteration of training.       
                    #Higher values generally leads to unstable results.


NumberOfPointsOnScreen = 500 

randomPoints = generateRandomPoints(NumberOfPointsOnScreen)

trainingData = generateRandomPoints(SizeOfTrainingDataset) 

trainedWeights = train(RandomWeights, trainingData, LearningRate)

print("Trained Weights - ",trainedWeights)

print('Press "Enter" to redraw the random dots and see the accuracy of the Neural Network')
print('Press "Space" to Train the Neural Network further')

TotalRightGuesses = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                randomPoints = generateRandomPoints(NumberOfPointsOnScreen)
                print(str((TotalRightGuesses/NumberOfPointsOnScreen)*100) + "% Accuracy")
            
            if event.key == pygame.K_SPACE:
                trainingData = generateRandomPoints(SizeOfTrainingDataset)
                trainedWeights = train(trainedWeights,trainingData, LearningRate)
                print("Trained Weights - ",trainedWeights)


    #clear the screen
    screen.fill(WHITE)
    randomWeight = RandomWeights
    
    TotalRightGuesses = 0
    for point in randomPoints:
        guessTeam = guess(trainedWeights,point)
        ActualTeam = Team(point)
        
        TotalRightGuesses += 1 if ActualTeam == guessTeam else 0

        color = RED if guessTeam > 0 else BLUE
        pygame.draw.circle(screen, color,point,2)
    
     
    start_pos = (0, 0)
    end_pos = (width, height)
    pygame.draw.line(screen, BLACK, start_pos, end_pos, 1)

    pygame.display.update()