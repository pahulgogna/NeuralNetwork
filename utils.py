import random
from config import height, width

def Point() -> tuple[int, int]:
    return (random.randint(10, width - 10), random.randint(10, height - 10))

def generateRandomPoints(n:int):
    return [Point() for _ in range(n)]

def Team(point: tuple[int, int]) -> int:  # returns the correct team of the point
    return 1 if width/point[0] > height/point[1] else -1

RandomWeights = [random.randint(-1, 1), random.randint(-1, 1)]

def guess(weights: list, point: tuple) -> int:
    sum = point[0]*weights[0] + point[1]*weights[1]
    return 1 if sum > 0 else -1


def train(RandomTrainingWeights,TrainingData:list[tuple[int, int]], learningRate) -> list[int, int]:
    trainedWeights = RandomTrainingWeights

    for point in TrainingData:
        error = Team(point) - guess(trainedWeights, point)
        trainedWeights = [
                trainedWeights[0] + point[0]*error*learningRate,
                trainedWeights[1] + point[1]*error*learningRate
            ]
        
    return trainedWeights
