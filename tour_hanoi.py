from _typeshed import Self
import sys


# A structure to represent a stack
class Stack:
    # Constructor to set the data of
    # the newly created tree node
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.array = [0] * capacity


# function to create a stack of given capacity.
def createStack(capacity):
    stack = Stack(capacity)
    return stack


# Stack is full when top is equal to the last index
def isFull(stack):
    return (stack.top == (stack.capacity - 1))


# Stack is empty when top is equal to -1
def isEmpty(stack):
    return (stack.top == -1)


# Function to add an item to stack.
# It increases top by 1
def push(stack, item):
    if (isFull(stack)):
        return
    stack.top += 1
    stack.array[stack.top] = item


# Function to remove an item from stack.
# It decreases top by 1
def Pop(stack):
    if (isEmpty(stack)):
        return -sys.maxsize
    Top = stack.top
    stack.top -= 1
    return stack.array[Top]


# Function to implement legal
# movement between two poles
def moveDisksBetweenTwoPoles(src, dest, s, d):
    pole1TopDisk = Pop(src)
    pole2TopDisk = Pop(dest)

    # When pole 1 is empty
    if (pole1TopDisk == -sys.maxsize):
        push(src, pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)

    # When pole2 pole is empty
    elif (pole2TopDisk == -sys.maxsize):
        push(dest, pole1TopDisk)
        moveDisk(s, d, pole1TopDisk)

    # When top disk of pole1 > top disk of pole2
    elif (pole1TopDisk > pole2TopDisk):
        push(src, pole1TopDisk)
        push(src, pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)

    # When top disk of pole1 < top disk of pole2
    else:
        push(dest, pole2TopDisk)
        push(dest, pole1TopDisk)
        moveDisk(s, d, pole1TopDisk)


# Function to show the movement of disks
def moveDisk(fromPeg, toPeg, disk):
    print("Move the disk", disk, "from '", fromPeg, "' to '", toPeg, "'")


# Function to implement TOH puzzle
def tohIterative(num_of_disks, src, aux, dest):
    s, d, a = 'S', 'D', 'A'

    # If number of disks is even, then interchange
    # destination pole and auxiliary pole
    if (num_of_disks % 2 == 0):
        temp = d
        d = a
        a = temp
    total_num_of_moves = int(pow(2, num_of_disks) - 1)

    # Larger disks will be pushed first
    for i in range(num_of_disks, 0, -1):
        push(src, i)

    for i in range(1, total_num_of_moves + 1):
        if (i % 3 == 1):
            moveDisksBetweenTwoPoles(src, dest, s, d)

        elif (i % 3 == 2):
            moveDisksBetweenTwoPoles(src, aux, s, a)

        elif (i % 3 == 0):
            moveDisksBetweenTwoPoles(aux, dest, a, d)


# predicate model checker(semantique, predicate)

def guarde_def(s,t):
    return lambda c: len(c.stacks[s]) and len(c.stacks[t])==0 or c.stacks[s][-1] < c.stacks[t][-1]

def action_def(s,t):
    def action(c):
        disk = c.stacks[s].pop()
        c.stacks[t].append(dist)
        return action

def hanoi_soup(nb_stacks, nb_disks):
    i_conf = HanoiConfiguration(nb_stacks, nb_stacks) # c'est un classe HanoiConfiguration
    programSrc = BehaviourSoup(i_conf)
    for i in range(nb_stacks):
        for j in range(nb_stacks):
            programSrc.add(f'{i}-{j}', guarde_def(i,j), action_def(i,j))
    return programSrc

def is_accepting(c):
    ........

# soup et soup behaviour doivent etre dans un fichier soup language
class BehaviourSoup:
    def __init__(conf):
        self.initial = conf
        self.behaviours = []
        
    def add(n, g, a):
        Self.behaviours.append(Behaviour(n,g,a))


class Behaviour:
    def __init__(name, g, a):
        self.name = name
        self.action = a
        self.guard = g


# Input: number of disks
num_of_disks = 4

# Create three stacks of size 'num_of_disks'
# to hold the disks
src = createStack(num_of_disks)
dest = createStack(num_of_disks)
tmp = createStack(num_of_disks)

tohIterative(num_of_disks, src, tmp, dest)