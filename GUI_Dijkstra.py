import sys
import tkinter as tk
from tkinter import *

def printCost(cost,letters): #printing the last result

    myWindow = [Label(root)] 
    
    r = 1
    c = 7
    for i in range(0,len(cost),1):
        myWindow = [Label(root,text=letters[i])]
        myWindow[0].grid(row=r,column=c,pady=2)

        myWindow = [Label(root,text='%.1f' %(cost[i]))]
        myWindow[0].grid(row=r,column=c+1,pady=2)
        r+=1


def dijkstra(list, source,letters):

    cost = [sys.maxsize for i in range(len(list))] #list to store last cost. assuming infinity at the beginning
    visited = [FALSE for j in range(len(list))] #tracking visited and not visited cities

    cost[source] = 0 #marking the source as 0 cost

    for l in range(0,len(list)-1,1): #iterate through the 2D matrix
        vertex = 0 #to store picked index
        leastCost = sys.maxsize #comparission purpose

        for k in range(0,len(list),1): #to pick the unvisited and lowest cost city
            if(visited[k] == FALSE and cost[k] < leastCost):
                vertex = k
                leastCost = cost[k]
        
        visited[vertex] = TRUE #marking the picked city true

        for z in range(0,len(list),1): #iterate through every edge of the picked city
            if(list[vertex][z] == 0.0): # 0 = no edge, so we skip over those city
                continue

            if(cost[vertex]+list[vertex][z] < cost[z]): #comparing cost of the city with assumed cost at the beginning
                cost[z] = cost[vertex]+list[vertex][z] #if the cost is less we update the cost
    
    printCost(cost,letters)

def readData():

    list = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]] #list to store data
    i = 0 #row
    j = 0 #column
    f = 0 #flag

    for z in range(0,4*4,1): #iterate through the entries and generate 2D matrix
        list[i][j] = myEntry[z].get()

        if(list[i][j]==''): #if the entry is blank then it must be 0
            list[i][j] = 0.0
        else:
            list[i][j] = float(list[i][j]) #change the string input to floats
            
        if(f==3): #flag to change row and column
            i += 1
            j = 0
            f = 0

        else:
            f += 1
            j += 1
    
    #add try and catch statement
    source = mySource.get() #read the source from the user
    num = letters.index(source) #finding the index of that user input

    print(list)
    dijkstra(list,num,letters)








root = tk.Tk()
root.geometry("500x500")
root.title("GUI_Dijkstra")

letters = ['A','B','C','D']#name of the cities
myLabel = [Label(root)] #used for storing and putting the cities on the screen

r = 1 #row
c = 1 #column

for j in range(0,len(letters),1):
    myLabel = [Label(root,text=letters[j])]
    myLabel[0].grid(row = r, column = 0, pady = 5 ) #verticle label
    r += 1

for i in range(0,len(letters),1):
    myLabel = [Label(root,text=letters[i])]
    myLabel[0].grid(row=0, column=c, pady=5) #horizontal label
    c+=1


myEntry = [Entry(root,width=5) for k in range(len(letters)**2)] #windows to take input from the users
r = 1
c = 1
f = 0

for k in range(0,len(letters)**2,1):
    myEntry[k].grid(row=r, column= c, pady=5)

    if(f == 3):
        r += 1
        c = 1
        f = 0
    else:
        f += 1
        c += 1

#for source entry
s = Label(root, text='Source: ')
s.grid(row=5, column=0, pady=5)
mySource = Entry(root,width = 5)
mySource.grid(row=5, column=c, pady=5)

#button related code
myButton = tk.Button(root, text='Start', command=readData)
myButton.grid(row = 7, columnspan=15, pady = 10)
root.mainloop()