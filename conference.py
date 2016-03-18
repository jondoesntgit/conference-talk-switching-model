#!/usr/bin/python

#import time
from Tkinter import *
import numpy
import random

master = Tk()

personRadius = 5

energyLevels = 2
numRooms = 2

roomHeight = 300
padding = 25
roomWidth = 100

roomEnergyArray = numpy.empty((numRooms, energyLevels), dtype=type([]))
for r in range(0,numRooms):
    for e in range(0, energyLevels):
        roomEnergyArray[r][e] = []

w = Canvas(master, width=numRooms * roomWidth + (numRooms + 1) * padding, height=2 * padding + roomHeight)

w.pack()
person01 = w.create_oval(-personRadius, -personRadius, personRadius, personRadius)
person02 = w.create_oval(-personRadius, -personRadius, personRadius, personRadius)
person03 = w.create_oval(-personRadius, -personRadius, personRadius, personRadius)
person04 = w.create_oval(-personRadius, -personRadius, personRadius, personRadius)
person05 = w.create_oval(-personRadius, -personRadius, personRadius, personRadius)
person06 = w.create_oval(-personRadius, -personRadius, personRadius, personRadius)
person11 = w.create_oval(-personRadius, -personRadius, personRadius, personRadius)
person12 = w.create_oval(-personRadius, -personRadius, personRadius, personRadius)
person13 = w.create_oval(-personRadius, -personRadius, personRadius, personRadius)
person14 = w.create_oval(-personRadius, -personRadius, personRadius, personRadius)
person15 = w.create_oval(-personRadius, -personRadius, personRadius, personRadius)
person16 = w.create_oval(-personRadius, -personRadius, personRadius, personRadius)
roomEnergyArray[0][0].append(person01)
roomEnergyArray[1][0].append(person02)
#roomEnergyArray[2][0].append(person03)
#roomEnergyArray[3][0].append(person04)
#roomEnergyArray[4][0].append(person05)
#roomEnergyArray[5][0].append(person06)
roomEnergyArray[0][0].append(person11)
roomEnergyArray[1][0].append(person12)
#roomEnergyArray[2][0].append(person13)
#roomEnergyArray[3][0].append(person14)
#roomEnergyArray[4][0].append(person15)
#roomEnergyArray[5][0].append(person16)


# Show rooms
for i in range(0, numRooms):
    w.create_rectangle(padding * (i + 1) + i * roomWidth, padding, (i + 1) * padding + (i + 1) * roomWidth, padding + roomHeight, dash=(4, 4));

def updateGraph():
    for room in range(0, numRooms):
        for energyLevel in range(0, energyLevels):
            if type(roomEnergyArray[room][energyLevel]) is not int:
                count = len(roomEnergyArray[room][energyLevel])
                for personNumber in reversed(range(0, count)):
                    person = roomEnergyArray[room][energyLevel][personNumber]
                    coord = w.coords(person)
                    currentX = (coord[2] + coord[0])/2
                    currentY = (coord[3] + coord[1])/2
                    targetX = padding * (room) + roomWidth * (room - 1) + (roomWidth/2) - (count - 1)/2.0 * (2.0 * personRadius + 1) + (personNumber) * (personRadius * 2 + 1)
                    targetY = padding + (energyLevels - energyLevel) * roomHeight/(energyLevels+1)
                    deltaX = targetX - currentX
                    deltaY = targetY - currentY
                    w.move(person, deltaX, deltaY)
                    randomNumber = random.random()
                    if randomNumber < e/20.0:
                        if random.random() > .5:
                            moveToRoom(person, room + 1)
                        else:
                            moveToRoom(person, room - 1)
    if random.random() < .2:
        badTalk(random.randint(0,numRooms-1))
    if random.random() < .1:
        goodTalk(random.randint(0,numRooms-1))
    print roomEnergyArray
    w.after(2000, updateGraph)

def goodTalk(roomNumber):
    # Decrement energy
    for energyLevel in range(0, energyLevels):
        print("decrement energy")
        if (energyLevel == 0):
            pass
        else:
            roomEnergyArray[roomNumber][energyLevel - 1] = roomEnergyArray[roomNumber][energyLevel - 1] + roomEnergyArray[roomNumber][energyLevel]
            roomEnergyArray[roomNumber][energyLevel] = []

def badTalk(roomNumber):
    print("Increment energy")
    # Increment energy
    for energyLevel in reversed(range(0, energyLevels)):
        if (energyLevel == energyLevels - 1):
            pass
        else:
            roomEnergyArray[roomNumber][energyLevel + 1] = roomEnergyLevel[roomNumber][energyLevel+1] + roomEnergyArray[roomNumber][energyLevel]
            roomEnergyArray[roomNumber][energyLevel] = []

def moveToRoom(person, room):
    if room <= 0:
        room = 0
    if room >= numRooms:
        room = numRooms - 1
    # Find where he was and remove him
    energy = 0
    for r in range(0,numRooms):
        for e in range(0, energyLevels):
            if person in roomEnergyArray[r][e]:
#                i = roomEnergyArray[r][e].index(person)
                roomEnergyArray[r][e].remove(person)
                energy = e
    roomEnergyArray[room][e] = roomEnergyArray[room][e]+[person]

w.after(1000, updateGraph)

mainloop()
