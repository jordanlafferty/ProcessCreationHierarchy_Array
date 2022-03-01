from datetime import datetime


def startPCB():
    pcb = [[0, None, None, None]]
    return pcb


def create(p, pcb):
    # create a new process array
    child = [len(pcb), p[0], None, None]

    # index of the child parent
    parent = p[0]

    # checking to see if the child just created has any siblings
    if parent is not None:
        y = len(pcb) - 1
        for x in range(len(pcb)):
            if x != len(pcb):
                # if two processes have the same parent
                if parent == pcb[y][1]:
                    # set younger sibling
                    child[2] = pcb[y][0]
                    # set older sibling
                    pcb[y][3] = child[0]

    # add the child to the array
    pcb.append(child)

    print("Process [", child[1], "] created process [", child[0], "]")
    return pcb


def destroy(p, pcb):
    # index of the process that is going to be deleted
    y = len(pcb) - 1
    z = y - p[0]
    for x in range(z):
        # does the process have a child
        if pcb[y][1] == p[0]:
            destroy(pcb[y], pcb)
        y -= 1

    # prints out what is going to be deleted
    if p[1] is not None:
        print("Process [", p[0], "] is deleted from process [", p[1], "]")
    else:
        print("Process [", p[0], "] is deleted")

    # rearranges the siblings
    y = 0
    youngerSib = p[2]
    olderSib = p[3]
    if p[1] is not None:
        # see if the process has any younger or older siblings
        # if the process has both then set the younger child's older sibling to
        # the processes' older sibling and visa versa
        if p[2] is not None:
            if p[3] is not None:
                #pcb[youngerSib][3] = olderSib
                pcb[olderSib][2] = youngerSib
                y = 1

    if y == 0:
        # no older sibling -- set the processes younger sibling to have no older sibling
        if p[2] is not None:
            pcb[youngerSib][3] = None
        # no younger sibling -- set the processes older sibling to have no younger sibling
        elif p[3] is not None:
            pcb[olderSib][2] = None

    #delete the process from the array
    pcb.remove(p)
    return pcb


def restoreIndexes(pcb):
    # corrects the indices so destroy and create can be used again
    for x in range(len(pcb)):
        if x != pcb[x][0]:
            before = pcb[x][0]
            actual = x
            pcb[x][0] = x

            for y in range(len(pcb)):
                for z in range(4):
                    #if x <= y:
                        if pcb[y][z] == before:
                            pcb[y][z] = actual
    return pcb

print("*** \nThe processes are structured as [child, parent, older sibling, younger sibling]\n***")
# gets the time to see how long it takes
begin_time = datetime.now()

for x in range(100):
    PCB = startPCB()
    PCB = create(PCB[0], PCB)
    PCB = create(PCB[0], PCB)
    PCB = create(PCB[0], PCB)
    PCB = create(PCB[2], PCB)
    print("Updated PCB:", PCB)
    PCB = destroy(PCB[0], PCB)
    #PCB = restoreIndexes(PCB)
    print("Updated PCB:", PCB)
    print("************************************")  # so you can differentiate each round

print(datetime.now() - begin_time)
