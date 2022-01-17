import copy
import sys

from Kernel import *
from SoupLanguage import *


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
    return stack.top == (stack.capacity - 1)


# Stack is empty when top is equal to -1
def isEmpty(stack):
    return stack.top == -1


# Function to add an item to stack.
# It increases top by 1
def push(stack, item):
    if isFull(stack):
        return
    stack.top += 1
    stack.array[stack.top] = item


# Function to remove an item from stack.
# It decreases top by 1
def Pop(stack):
    if isEmpty(stack):
        return -sys.maxsize
    Top = stack.top
    stack.top -= 1
    return stack.array[Top]


# Function to implement legal
# movement between two poles
def moveDisksBetweenTwoPoles(src, dest, s, d):
    pole1TopDisk = Pop(src)
    pole2TopDisk = Pop(dest)

    # Pole 1 is empty
    if pole1TopDisk == -sys.maxsize:
        push(src, pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)

    # Pole2 pole is empty
    elif pole2TopDisk == -sys.maxsize:
        push(dest, pole1TopDisk)
        moveDisk(s, d, pole1TopDisk)

    # Top disk of pole1 > top disk of pole2
    elif pole1TopDisk > pole2TopDisk:
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

    # If number of disks is even, then interchange destination pole and auxiliary pole
    if num_of_disks % 2 == 0:
        temp = d
        d = a
        a = temp
    total_num_of_moves = int(pow(2, num_of_disks) - 1)

    # Larger disks will be pushed first
    for i in range(num_of_disks, 0, -1):
        push(src, i)

    for i in range(1, total_num_of_moves + 1):
        if i % 3 == 1:
            moveDisksBetweenTwoPoles(src, dest, s, d)

        elif i % 3 == 2:
            moveDisksBetweenTwoPoles(src, aux, s, a)

        elif i % 3 == 0:
            moveDisksBetweenTwoPoles(aux, dest, a, d)


# predicate model checker(semantic, predicate)

def guarde_def(s, t):
    return lambda c: len(c.stacks[s]) and len(c.stacks[t]) == 0 or c.stacks[s][-1] < c.stacks[t][-1]


def action_def(s, t):
    def action(c):
        disk = c.stacks[s].pop()
        c.stacks[t].append(disk)
        return action


def is_accepted(c):
    nb_disks = max(max(c))

    if len(c[-1]) != nb_disks:
        return False
    for k in range(nb_disks):
        if c[-1][k] != nb_disks - k:
            return False
    return True


def hanoi_soup(nb_stacks, nb_disks):
    i_conf = HanoiConfiguration(nb_stacks, nb_disks)  # Classe HanoiConfiguration
    programSrc = BehaviourSoup(i_conf)
    for i in range(nb_stacks):
        for j in range(nb_stacks):
            programSrc.add(f'{i}-{j}', guarde_def(i, j), action_def(i, j))
    return programSrc


class Hanoi(TransitionRelation, AcceptingSet):
    def __init__(self, nb_stacks, nb_disks):
        super().__init__()
        self.nbDisks = nb_disks
        self.nbStacks = nb_stacks

    def initial(self):
        return [HanoiConfiguration(self.nbStacks, self.nbDisks)]

    def next(self, n):
        next_states = []
        for i in range(self.nbStacks):
            new_node = copy.deepcopy(n)
            if new_node[i]:
                disk = new_node[i].pop()
                for j in range(self.nbStacks):
                    if i != j and (not new_node[j] or new_node[j][-1] > disk):
                        temp = copy.deepcopy(new_node)
                        temp[j].append(disk)
                        next_states.append(temp)
        return next_states

    def is_accepting(self, c):
        k = 0
        if not c[-1]:
            return False
        for disk in c[-1]:
            if disk != self.nbDisks - k:
                return False
            k = k + 1
        return True


class HanoiConfiguration(list):
    def __init__(self, nb_stacks, nb_disks):
        list.__init__(self, [[(nb_disks - i) for i in range(nb_disks)]] + [[] for _ in range(nb_stacks - 1)])

    def __hash__(self):
        hash = 0
        maxi = max(self)[0]
        for stack in self:
            hash += sum(stack) * maxi
            maxi *= 2
        return hash

    def __eq__(self, conf):
        if len(self) != len(conf):
            return False
        for i in range(len(self)):
            if len(self[i]) != len(conf[i]):
                return False
        for j in range(len(self[i])):
            if conf[i][j] != self[i][j]:
                return False


# Input: number of disks
num_of_disks = 4

# Create three stacks of size 'num_of_disks'
# to hold the disks
src = createStack(num_of_disks)
dest = createStack(num_of_disks)
tmp = createStack(num_of_disks)

tohIterative(num_of_disks, src, tmp, dest)
