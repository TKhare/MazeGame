import random
from random import shuffle
import pygame
import pygame.display
import time
pygame.init()
class Maze:
    def __init__(self,size):
        self.size = size
        self.maze = []
        self.visitedPoints = []
        self.x = str(input("Enter screen resolution:"))
        self.splitIndex = self.x.index("x")
        self.screenW = int(self.x[0:self.splitIndex])
        self.screenH = int(self.x[self.splitIndex+1:len(self.x)])
        self.time1 = 0
    def run(self):
        self.fillGrid()
        self.genMaze()
        self.animGrid()
    def fillGrid(self):
        self.maze = [[0 for self.x in range(self.size)] for self.y in range(self.size)]
    def fillRemainder(self,coordVis):
        print("Filling remainder")
        dirs = ["N","W","S","E"]
        i = len(coordVis)
        end = len(coordVis)/10
        curA = [0,0]
        cur = [0,0]
        startPoints = []
        while len(coordVis)>0:
            i+=1
            curA[0] = int(coordVis[len(coordVis)-1][1:coordVis[len(coordVis)-1].index(",")])
            curA[1] = int(coordVis[len(coordVis)-1][coordVis[len(coordVis)-1].index(",")+1:len(coordVis[len(coordVis)-1])-1])
            coordVis.pop(len(coordVis)-1)
            try:
                coordVis.pop(len(coordVis)-1)
            except:
                continue
            try:
                coordVis.pop(len(coordVis)-1)
            except:
                continue
            tries = 0
            try:
                if self.maze[curA[1]][curA[0]+1] != 1 and self.maze[curA[1]][curA[0]+2] != 1:
                    startPoints.append(curA[1])
                    startPoints.append(curA[0]+1)
            except:
                print("failed")
            try:
                if self.maze[curA[1]][curA[0]-1] != 1 and self.maze[curA[1]][curA[0]-2] != 1:
                    startPoints.append(curA[1])
                    startPoints.append(curA[0]-1)
            except:
                print("failed")
            try:
                if self.maze[curA[1]-1][curA[0]] != 1 and self.maze[curA[1]-2][curA[0]] != 1:
                    startPoints.append(curA[1]-1)
                    startPoints.append(curA[0])
            except:
                print("failed")
            try:
                if self.maze[curA[1]+1][curA[0]] != 1 and self.maze[curA[1]+2][curA[0]] != 1:
                    startPoints.append(curA[1]+1)
                    startPoints.append(curA[0])
            except:       
                print("failed")
            while len(startPoints)>0:
                cur[1] = startPoints[len(startPoints)-1]
                cur[0] = startPoints[len(startPoints)-2]
                startPoints.pop()
                startPoints.pop()
                while tries < 3:
                    self.maze[cur[1]][cur[0]] = 1
                    if tries == 0:
                        random.shuffle(dirs)
                    if dirs[tries] == "N":
                        cur[1] -= 1
                        if (cur[1]<0) or (cur[0]>0 and self.maze[cur[1]][cur[0]-1]==1) or (cur[0]<self.size-1 and self.maze[cur[1]][cur[0]+1]==1) or (cur[1]>0 and self.maze[cur[1]-1][cur[0]]==1):
                            cur[1] +=1
                            tries+=1
                        else:
                            tries = 0
                        continue
                    if dirs[tries] == "S":
                        cur[1]+=1
                        if (cur[1]>self.size-1) or (cur[0]>0 and self.maze[cur[1]][cur[0]-1]==1) or (cur[0]<self.size-1 and self.maze[cur[1]][cur[0]+1]==1) or (cur[1]<self.size-1 and self.maze[cur[1]+1][cur[0]]==1):
                            cur[1] -=1
                            tries+=1
                        else:
                            tries = 0
                        continue
                    if dirs[tries] == "E":
                        cur[0] +=1
                        if (cur[0]>self.size-1) or (cur[1]>0 and self.maze[cur[1]-1][cur[0]]==1) or (cur[1]<self.size-1 and self.maze[cur[1]+1][cur[0]]==1) or (cur[0]<self.size-1 and self.maze[cur[1]][cur[0]+1]==1):
                            cur[0] -=1
                            tries+=1
                        else:
                            tries = 0
                        continue
                    if dirs[tries] == "W":
                        cur[0]-=1
                        if (cur[0]<0) or (cur[1]>0 and self.maze[cur[1]-1][cur[0]]==1) or (cur[1]<self.size-1 and self.maze[cur[1]+1][cur[0]]==1) or (cur[0]>0 and self.maze[cur[1]][cur[0]-1]==1):
                            cur[0] +=1
                            tries+=1
                        else:
                            tries = 0
                        continue
    def fillremainder2(self):
        print("fillremainder2")
        for self.k in range(0,self.size-1):
            for self.l in range(0,self.size-1):
                if(self.k<self.size-2 and self.l<self.size-2):
                    if(self.maze[self.k][self.l]==0 and self.maze[self.k+1][self.l]==0 and self.maze[self.k+2][self.l]==0 and self.maze[self.k][self.l+1]==0 and self.maze[self.k+1][self.l+1]==0 and self.maze[self.k+2][self.l+1]==0 and self.maze[self.k][self.l+2]==0 and self.maze[self.k+1][self.l]==0 and self.maze[self.k+2][self.l]==0):
                        n = 2
                    if(self.maze[self.k][self.l]==0 and self.maze[self.k+1][self.l]==0 and self.maze[self.k][self.l+1]==0 and self.maze[self.k+1][self.l+1]==0):
                        choice = random.randint(0,9)
                        if choice==0:
                            self.maze[self.k][self.l]=1
                            self.maze[self.k+1][self.l]=1
                        if choice==1:
                            self.maze[self.k][self.l]=1
                            self.maze[self.k][self.l+1]=1
                        if choice==2:
                            self.maze[self.k][self.l]=1
                            self.maze[self.k+1][self.l+1]=1
                        if choice==3:
                            self.maze[self.k+1][self.l]=1
                            self.maze[self.k][self.l+1]=1
                        if choice==4:
                            self.maze[self.k+1][self.l]=1
                            self.maze[self.k+1][self.l+1]=1
                        if choice==5:
                            self.maze[self.k][self.l+1]=1
                            self.maze[self.k+1][self.l+1]=1


    def getSize(self):
        return self.size
    def genMaze(self):
        coordVis = ["(0,0)"]
        cur = [0,0]
        tries = 0
        self.maze[0][0] = 1
        dirs = ["N","W","S","E"]
        while self.maze[self.size-1][self.size-1] != 1:
            if ("("+str(cur[0])+","+str(cur[1])+")") not in coordVis: 
                coordVis.append("("+str(cur[0])+","+str(cur[1])+")")
            self.maze[cur[1]][cur[0]] = 1
            if cur == [self.size-2,self.size-1] or cur == [self.size-1,self.size-2]:
                self.maze[self.size-1][self.size-1] = 1
                break
            if tries == 0:
                random.shuffle(dirs)
            if tries == 4:
                curString = coordVis[coordVis.index("("+str(cur[0])+","+str(cur[1])+")")-1]
                cur[0] = int(curString[1:curString.index(",")])
                cur[1] = int(curString[curString.index(",")+1:len(curString)-1])
                tries = 0
                coordVis.pop(len(coordVis)-1)
                coordVis.pop(len(coordVis)-1)
            if dirs[tries] == "N":
                cur[1] -= 1
                if (cur[1]<0) or (cur[0]>0 and self.maze[cur[1]][cur[0]-1]==1) or (cur[0]<self.size-1 and self.maze[cur[1]][cur[0]+1]==1) or (cur[1]>0 and self.maze[cur[1]-1][cur[0]]==1):
                    cur[1] +=1
                    tries+=1
                else:
                    tries = 0
                continue
            if dirs[tries] == "S":
                cur[1]+=1
                if (cur[1]>self.size-1) or (cur[0]>0 and self.maze[cur[1]][cur[0]-1]==1) or (cur[0]<self.size-1 and self.maze[cur[1]][cur[0]+1]==1) or (cur[1]<self.size-1 and self.maze[cur[1]+1][cur[0]]==1):
                    cur[1] -=1
                    tries+=1
                else:
                    tries = 0
                continue
            if dirs[tries] == "E":
                cur[0] +=1
                if (cur[0]>self.size-1) or (cur[1]>0 and self.maze[cur[1]-1][cur[0]]==1) or (cur[1]<self.size-1 and self.maze[cur[1]+1][cur[0]]==1) or (cur[0]<self.size-1 and self.maze[cur[1]][cur[0]+1]==1):
                    cur[0] -=1
                    tries+=1
                else:
                    tries = 0
                continue
            if dirs[tries] == "W":
                cur[0]-=1
                if (cur[0]<0) or (cur[1]>0 and self.maze[cur[1]-1][cur[0]]==1) or (cur[1]<self.size-1 and self.maze[cur[1]+1][cur[0]]==1) or (cur[0]>0 and self.maze[cur[1]][cur[0]-1]==1):
                    cur[0] +=1
                    tries+=1
                else:
                    tries = 0
                continue
        self.fillRemainder(coordVis)
        self.fillRemainder(coordVis)        
        self.fillremainder2()
    def createPathways(self, tileH, tileW, screen):
        for i in range(0,self.size):
            for k in range(0,self.size):
                tileSize = 100
                if self.maze[k][i] == 1 and not(((i == 0 and k==0) or (i == self.size-1 and k == self.size-1))):
                    pygame.draw.rect(screen,(255,255,255),[i*tileW,k*tileH,tileW+1,tileH+1])
                elif (i == 0 and k == 0):
                    pygame.draw.rect(screen,(0,255,0),[i*tileW,k*tileH,tileW+1,tileH+1])
                elif (i == self.size-1 and k == self.size-1):
                    pygame.draw.rect(screen,(255,0,0),[i*tileW,k*tileH,tileW+1,tileH+1])
                else:
                    pygame.draw.rect(screen,(0,0,0),[i*tileW,k*tileH,tileW+1,tileH+1])
        self.time1 = time.time()
                
    def animGrid(self):
        pygame.display.init()
        print(pygame.display.Info())

        screen = pygame.display.set_mode((self.screenW+200, self.screenH))
        tileH = self.screenH/self.size
        tileW = self.screenW/self.size
        pygame.draw.rect(screen, (0,255,0), [self.screenW+30, self.screenH/5, 140,50])
        Font1 = pygame.font.SysFont('monaco', 24)
        resetSurface = Font1.render('Create New Maze',True, (0,0,0))
        resetRect = resetSurface.get_rect()
        resetRect.midtop = (self.screenW+100, self.screenH/5+5)
        screen.blit(resetSurface,resetRect)
        pygame.draw.rect(screen, (0,255,0), [self.screenW+30, self.screenH/3, 140,50])
        Font2 = pygame.font.SysFont('monaco', 22)
        mazeSurface = Font2.render('Change Maze Size',True, (0,0,0))
        mazeRect = mazeSurface.get_rect()
        mazeRect.midtop = (self.screenW+100, self.screenH/3+5)
        screen.blit(mazeSurface,mazeRect)


        running = True
        originalMaze = self.maze.copy()
        self.createPathways(tileH, tileW, screen)
        pygame.display.update()  
        cur = [0,0]
        coordVis =[]  

        try:
            while running:
                for event in pygame.event.get():
                    try:
                        if(cur[0] == self.size-1 and cur[1] == self.size-1):
                            print("started finishing")
                            self.time1 = int(time.time() - self.time1)
                            print("Finished after "+str(self.time1)+" seconds")
                            cur = [0,0]
                            timerSurface = Font2.render("Finish Time: "+str(self.time1),True,(0,0,0))
                            pygame.draw.rect(screen, (0,255,0), [self.screenW+30, self.screenH/16, 140,50])
                            timerRect = timerSurface.get_rect()
                            timerRect.midtop = (self.screenW+100,self.screenH/16+5)
                            screen.blit(timerSurface,timerRect)
                            pygame.display.update()
                            time.sleep(5)
                    except:
                        garbage = 1
                    try:
                        if(((self.maze[cur[1]][cur[0]+1] !=1) and (self.maze[cur[1]][cur[0]-1] !=1) and (self.maze[cur[1]+1][cur[0]] !=1) and (self.maze[cur[1]-1][cur[0]] !=1)) or ((self.maze[cur[1]][cur[0]+1]!= 1) and (self.maze[cur[1]][cur[0]-1]!= 1) and (self.maze[cur[1]+1][cur[0]]!= 1) and (cur[1]-1==-1)) or((self.maze[cur[1]][cur[0]+1]!= 1) and (self.maze[cur[1]][cur[0]-1]!= 1) and (self.maze[cur[1]-1][cur[0]]!= 1) and (cur[1]+1==self.size)) or((self.maze[cur[1]][cur[0]+1]!= 1) and (cur[0]-1==-1) and (self.maze[cur[1]+1][cur[0]]!= 1) and (self.maze[cur[1]-1][cur[0]]!= 1)) or((self.maze[cur[1]][cur[0]-1]!= 1) and (cur[0]+1==-1) and (self.maze[cur[1]+1][cur[0]]!= 1) and (self.maze[cur[1]-1][cur[0]!= 1]))):
                            print("Failed")
                            while len(coordVis)>0:
                                self.maze[coordVis[len(coordVis)-1]][coordVis[len(coordVis)-2]] = 1
                                coordVis.pop()
                                coordVis.pop()
                            cur = [0,0]
                            self.animGrid()
                    except:
                        gabage = 1
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        mousePos = pygame.mouse.get_pos()
                        if mousePos[0]>self.screenW+30 and mousePos[0]<self.screenW+170 and mousePos[1]>self.screenH/5 and mousePos[1]<self.screenH/5+50:
                            try:
                                pygame.draw.rect(screen, (0,0,0), [self.screenW+30, self.screenH/16, 140,50])
                                print("button1 pressed")
                                maze = [[0 for self.x in range(self.size)] for self.y in range(self.size)]
                                pygame.draw.rect(screen, (0,0,0), [0,0,self.screenW+2,self.screenH])
                                self.fillGrid()
                                print("filled grid")
                                self.genMaze()
                                print("generated maze")
                                self.createPathways(tileH,tileW,screen)
                                print("created Pathways!")
                                originalMaze = self.maze
                                pygame.display.update()
                                cur = [0,0]
                                coordVis = []
                            except:
                                print("button 1 pressed")
                                maze = [[0 for self.x in range(self.size)] for self.y in range(self.size)]
                                pygame.draw.rect(screen, (0,0,0), [0,0,self.screenW+2,self.screenH])
                                self.fillGrid()
                                print("filled grid")
                                self.genMaze()
                                print("generated maze")
                                self.createPathways(tileH,tileW,screen)
                                originalMaze = self.maze
                                print("created Pathways!")
                                pygame.display.update()  
                                cur = [0,0]
                                coordVis = [] 
                        if mousePos[0]>self.screenW+30 and mousePos[0]<self.screenW+170 and mousePos[1]>self.screenH/3 and mousePos[1]<self.screenH/3+50:
                            try:
                                print("button2 pressed")
                                maze = [[0 for self.x in range(self.size)] for self.y in range(self.size)]
                                pygame.draw.rect(screen, (0,0,0), [0,0,self.screenW+2,self.screenH])
                                self.fillGrid()
                                print("filled grid")
                                self.genMaze()
                                print("generated maze")
                                self.createPathways(tileH,tileW,screen)
                                print("created Pathways!")
                                originalMaze = self.maze
                                pygame.display.update()
                                cur = [0,0]
                                coordVis = []
                            except:
                                print("button2 pressed")
                                maze = [[0 for self.x in range(self.size)] for self.y in range(self.size)]
                                pygame.draw.rect(screen, (0,0,0), [0,0,self.screenW+2,self.screenH])
                                self.fillGrid()
                                print("filled grid")
                                self.genMaze()
                                print("generated maze")
                                self.createPathways(tileH,tileW,screen)
                                originalMaze = self.maze
                                print("created Pathways!")
                                pygame.display.update()  
                                cur = [0,0]
                                coordVis = [] 
                            pygame.draw.rect(screen, (0,0,0), [0,0,self.screenW+2,self.screenH])
                            print("button2 pressed")
                            newMazeSize = input("Enter new maze size: ")
                            self.size = int(newMazeSize)
                            tileH=self.screenH/self.size
                            tileW = self.screenW/self.size
                            originalMaze = self.maze
                            cur = [0,0]
                            coordVis = []
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            if self.maze[cur[1]+1][cur[0]] == 1:
                                cur[1] += 1
                                pygame.draw.rect(screen,(64,224,208),[cur[0]*tileW,(cur[1]-1)*tileH,tileW+1,tileH+1])
                                pygame.draw.rect(screen,(0,255,0),[cur[0]*tileW,cur[1]*tileH,tileW+1,tileH+1])
                        elif event.key == pygame.K_UP:
                            if self.maze[cur[1]-1][cur[0]] == 1:
                                cur[1] -= 1
                                pygame.draw.rect(screen,(0,255,0),[cur[0]*tileW,cur[1]*tileH,tileW+1,tileH+1])
                                pygame.draw.rect(screen,(64,224,208),[cur[0]*tileW,(cur[1]+1)*tileH,tileW+1,tileH+1])
                        elif event.key == pygame.K_LEFT:
                            if self.maze[cur[1]][cur[0]-1] == 1:
                                cur[0] -= 1
                                pygame.draw.rect(screen,(0,255,0),[cur[0]*tileW,cur[1]*tileH,tileW+1,tileH+1])
                                pygame.draw.rect(screen,(64,224,208),[(cur[0]+1)*tileW,cur[1]*tileH,tileW+1,tileH+1])
                        elif event.key == pygame.K_RIGHT:
                            if self.maze[cur[1]][cur[0]+1] == 1:
                                cur[0] += 1
                                pygame.draw.rect(screen,(0,255,0),[cur[0]*tileW,cur[1]*tileH,tileW+1,tileH+1])
                                pygame.draw.rect(screen,(64,224,208),[(cur[0]-1)*tileW,cur[1]*tileH,tileW+1,tileH+1])
                        self.maze[cur[1]][cur[0]] = 2
                        coordVis.append(cur[0])
                        coordVis.append(cur[1])
                    pygame.display.update()
            pygame.quit()
        except SystemExit:
            pygame.quit()
grid = Maze(int(input("Enter length of individual side: ")))
grid.run()
