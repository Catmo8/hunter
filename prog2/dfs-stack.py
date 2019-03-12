def isStackEmpty(s):
    return len(s) == 0


def createMatrix(v):
    y = []
    for i in range(v):
        y.append([])
        for j in range(v):
            y[i].append(0)
    return y


def displayMatrix(g):
    print("Creating Graph G Adjancency Matrix:")
    for i in range(len(g)):
        for j in range(len(g)):
            print(g[i][j], end=" ")
        print()


def StackDFS(g, node):
    s = []
    visited = []
    for i in range(len(g)):
        visited.append(False)
    s.append(node)
    print("S: ", s)
    while not isStackEmpty(s):
        c = s.pop()
        visited[c] = True
        for i in range(len(g[c])):
            if g[i][c] == 1 and not visited[i]:
                s.append(i)
                print("S: ", s)
    return visited


v_size = int(input("Type in vertices you want for matrix: "))

graph = createMatrix(v_size)

i = 0
j = 0

while(True):
    displayMatrix(graph)
    i, j = input("Designate vertex (i,j) or (-1,-1) to finish: ").split(",")
    try:
        i = int(i)
        j = int(j)
    except:
        print("Please type a number for both vertex points")
        continue
    if (i == -1 and j == -1):
        break
    if (i < 0 or j < 0):
        print("Invalid input")
        continue
    if (i >= v_size or j >= v_size):
        print("Invalid input")
        continue
    graph[i][j] = 1
    graph[j][i] = 1


i, j = input("Designate the starting node in G: ").split(",")
i = int(i)
j = int(j)
print(StackDFS(graph, graph[i][j]))

