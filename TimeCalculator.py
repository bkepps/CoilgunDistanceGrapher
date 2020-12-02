import matplotlib.pyplot as plt
import numpy as np
import array as arr
#import pdb
import math

def sign(x):
    if x == 0:
        return 0
    else:
        return abs(x)/x

pi = 3.14159
area = .003
mass = 4.7

voltage = 25.0

sTime = 0.0
eTime = 0.1
tStep = 0.0001
asdfghjkl = int((eTime - sTime) / tStep)
outputT = np.zeros(shape=(asdfghjkl))
outputD = np.zeros(shape=(asdfghjkl))
i = sTime

testv = np.zeros(shape=0)
testa = np.zeros(shape=0)
testx = np.zeros(shape=0)

cStep = .001
coilOnTime = sTime
nStartPos = .034

iInt = 0

lol = 0


#while coilOnTime <= eTime:
coilOnTime += tStep
curPos = nStartPos
velocity = 0.0
acceleration = 0.0
curTime = 0.0

coilOnTime = 0.1

while curTime <= coilOnTime:
    #breakpoint()
    acceleration = (((200*(voltage/0.8))**2)*(4*pi*10**-7)*(area**2))/(2*((curPos)**2)*mass)*sign(curPos)
    velocity = velocity + acceleration * tStep
    curPos = curPos - velocity * tStep

    testv = np.append(testv, curPos)
    testa = np.append(testa, acceleration)
    testx = np.append(testx, lol)
    lol += 1
    curTime += tStep
breakpoint()
#if curPos < 0 or iInt == 0:
 #  breakpoint()
outputT[iInt] = coilOnTime
outputD[iInt] = acceleration
iInt += 1





#breakpoint()
plt.xlabel("Time (s)")
plt.ylabel("Launch Distance (m)")
plt.title("title")
#plt.plot(outputT, outputD, color ="red")
plt.plot(testx, testa, color="red")
plt.plot(testx, testv, color="green")
plt.show()