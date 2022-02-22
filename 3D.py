from vpython import *
import random
RADIUS = 0.75
PI = 3.141592653
EDGE_LENGTH = 2
NUM_OF_POINTS = 100
box(length = EDGE_LENGTH, height = EDGE_LENGTH,
    width = EDGE_LENGTH, color = color.cyan, opacity = 0.5)
sphere(radius = RADIUS, color = color.white, opacity= 0.75)

def volumeOfCube(edge):
    volume = edge**3
    return volume


def volumeOfSphere(r):
    volume = ((4/3) * PI) * r**3
    return volume


def randomPoints(x,y,z):
    randX = random.randint(-1,x)
    randY = random.randint(-1,y)
    randZ = random.randint(-1,z)
    return randX, randY, randZ


def inSphere(r, point):
    if point[0] < r and point[1] < r and point[2] < r:
        return True
    return False


cube_volume = volumeOfCube(EDGE_LENGTH)
sphere_volume = volumeOfSphere(RADIUS)
actual_ratio = sphere_volume / cube_volume
hits = 0

for i in range(NUM_OF_POINTS):
    x, y, z = randomPoints(1, 1, 1)
    listCoor = [x, y, z]
    sphere(radius=0.05, pos=vector(x, y, z), color=color.red)
    print(listCoor)
    if inSphere(RADIUS, listCoor):
        hits += 1

print(hits)
calculated_ratio = hits / NUM_OF_POINTS
print("Volume of cube:", cube_volume, "Volume of sphere:", sphere_volume)
print("Actual ratio:", actual_ratio, "Calculated ratio with dots:", calculated_ratio)
