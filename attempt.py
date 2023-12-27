#project DSA
import pygame
import sys
fps=30
fpsclock=pygame.time.Clock()

pygame.init()
window=pygame.display.set_mode((600,600))
pygame.display.set_caption("Maze")

def draw():
    x=0
    y=0
    width=40
    height=40
    for row in range(len(lev_1)):
        for col in range(len(lev_1[row])):
            if lev_1[row][col]==1:
                pygame.draw.rect(window,(255,0,0),(x,y,width,height))


            x+=width
        x=0
        y+=height
    pygame.display.update()
lev_1=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #a
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1], #b
    [1,0,1,0,0,0,1,0,1,1,1,1,1,1,1], #c
    [1,0,1,1,1,1,1,0,1,0,0,0,0,0,1], #d
    [1,0,1,0,0,0,0,0,0,0,1,1,1,0,1], #e
    [1,1,1,0,1,1,0,1,1,1,1,0,0,0,1], #f
    [1,0,0,0,1,0,0,1,0,0,0,0,1,1,1], #g
    [1,1,1,1,1,1,0,1,0,1,0,1,1,0,1], #h
    [1,1,0,0,0,0,0,1,0,1,1,1,1,1,1], #i
    [1,1,0,1,1,1,0,1,0,0,1,0,0,0,1], #j
    [1,1,0,0,0,1,1,1,1,0,0,0,1,1,1], #k
    [1,0,0,1,0,0,0,0,1,0,1,1,1,0,1], #l
    [1,0,1,1,1,1,1,1,1,0,0,0,0,0,1], #m
    [1,0,0,0,0,0,0,0,0,0,1,1,1,0,0], #n
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]] #o

visited=[]
lives=3
font_details=pygame.font.Font(None,32)
text =font_details.render("GAME OVER",True,(0,0,0))#takes three parameters, text, antialias, colour
def conversion(nested_list):
    num = 0
    column = 0
    for i in nested_list:
        row = 0
        for j in i:
            if j==1:
                nested_list[column][row] = 0
            else:
                num+=1
                nested_list[column][row] = num
            row+=1
        column+=1
    return nested_list, num

lst, max = conversion(lev_1)

def adjacency_list_maker(adj_matrix):
    G = {}
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j]!=0:
                G[adj_matrix[i][j]] = []
                if i>0:
                    if adj_matrix[i-1][j]!=0:
                        G[adj_matrix[i][j]].append((adj_matrix[i-1][j],1))
                if j>0:
                    if adj_matrix[i][j-1]!=0:
                        G[adj_matrix[i][j]].append((adj_matrix[i][j-1],1))
                if j<=(len(adj_matrix)-2):
                    if adj_matrix[i][j+1]!=0:
                        G[adj_matrix[i][j]].append((adj_matrix[i][j+1],1))
                if i<=(len(adj_matrix)-2):
                    if adj_matrix[i+1][j]!=0:
                        G[adj_matrix[i][j]].append((adj_matrix[i+1][j],1))
    return G

G = adjacency_list_maker(lst)

def dijkstra(G,start,end):
    shortest_distance = {}
    DaWay = {}
    track_DaWay = []
    unvisited = G
    for i in unvisited:
        shortest_distance[i] = 9999999
    shortest_distance[start] = 0
    while unvisited:
        min_dist = None
        for i in unvisited:
            if not min_dist:
                min_dist = i
            elif shortest_distance[i] < shortest_distance[min_dist]:
                min_dist = i
        further_path = G[min_dist]
        for x,y in further_path:
            if y+shortest_distance[min_dist] < shortest_distance[x]:
                shortest_distance[x] = y+shortest_distance[min_dist]
                DaWay[x] = min_dist
        unvisited.pop(min_dist)
    #right here
    currentNode = end
    while currentNode!=start:
        try:
            track_DaWay.insert(0,(DaWay[currentNode],currentNode))
            currentNode = DaWay[currentNode]
        except:
            break
    if shortest_distance[end]!=9999999:
        return shortest_distance[end],track_DaWay

bruh1, bruh2 = dijkstra(G,1,max)
print(bruh2)

run=True
x1=0
y1=80
countx=0
county=0
def move():
    global x1
    global y1
    global run
    global visited
    global lives
    width=40
    height=40
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        if lev_1[y1//width][(x1-width)//40]==1:
          if lives!=0:
            visited=[]
            x1=0
            y1=80
            window.fill((0,0,0))
            pygame.display.update()
            lives-=1
        elif (x1 -width,y1) not in visited:
            x1 = x1 -width
            visited.append((x1,y1))
            print(visited)
        else:
            print("don't backtrack")

    if key_input[pygame.K_DOWN]:
        if lev_1[(y1+height)//width][x1//40]==1:
          if lives!=0:
            visited=[]
            x1=0
            y1=80
            window.fill((0,0,0))
            pygame.display.update()
            lives-=1
          else:
              print("game over")
              run=False
        elif (x1,y1 + height) not in visited:
            y1 = y1 + height
            visited.append((x1,y1))
            print(visited)
        else:
            print("don't backtrack")
    if key_input[pygame.K_UP]:
        if lev_1[(y1-height)//width][x1//40]==1:
          if lives!=0:
            visited=[]
            x1=0
            y1=80
            window.fill((0,0,0))
            pygame.display.update()
            lives-=1
          else:
              print(lives,"game over")
              run=False
        elif (x1,y1-height) not in visited:
            y1 = y1-height
            visited.append((x1,y1))
            print(visited)
        else:
            print("don't backtrack")
    if key_input[pygame.K_RIGHT]:
        if lev_1[y1//width][(x1+width)//40]==1:
          if lives!=0:
            visited=[]
            x1=0
            y1=80
            window.fill((0,0,0))
            pygame.display.update()
            lives-=1
          else:
              print("game overS")
              run=False
        elif (x1 + width,y1) not in visited:
            x1 = x1 + width
            visited.append((x1,y1))
            print(visited)
        else:
            print("don't backtrack")
    pygame.draw.rect(window,(0,225,0),(x1,y1,width,height))
    pygame.display.update()


while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        else:
            if lives!=0:
               draw()
               move()
            else:
                print(lives)
                window.fill((225,225,225))
                window.blit(text,(300,300))
    pygame.display.update()
quit()
