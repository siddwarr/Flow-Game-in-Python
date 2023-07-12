import pygame,time
import pickle

def time1(username,password,lvl,timetaken):
    f = open("user_details.bin", 'rb')
    nlist = []
    while True:
        try:
            d = pickle.load(f)
            if d['username']==username and d['password']==password:
                if (d[lvl]>timetaken or d[lvl]==0) and timetaken!=0:
                    d[lvl]=timetaken
            nlist.append(d)
        except EOFError:
            break
    
    f.close()
    f = open("user_details.bin",'wb')
    for row in nlist:
        pickle.dump(row,f)
    f.close()
f = open('login_details.txt','r')
dat = f.read()
dat1 = eval(dat)
username = dat1[0]
password = dat1[1]
f.close()
pygame.init()

a=pygame.display.set_mode((700,500))
pygame.display.set_caption(("Flow game:"))
def grid(i):
    l,m,n,o=100,100,60*i+100,100
    for ii in range(i+1):
        pygame.draw.line(a,(255,255,255),(l,m),(n,o))
        m+=60
        o+=60
    l,m,n,o=100,100,100,60*i+100
    for jj in range(i+1):
        pygame.draw.line(a,(255,255,255),(l,m),(n,o))       
        l+=60
        n+=60
Lsolution=[[1,1,1,1,1],[2,2,2,2,1],[2,3,3,3,3],[4,4,4,4,5],[4,5,5,5,5]]
game=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]


font=pygame.font.Font('freesansbold.ttf',19)
f=open("instructions.txt",'r')
g=f.readlines()
kl,op,qr=-55,-40,295

for i in g:                                #colour page
    kl+=75
    op+=40
    qr-=40
    text=font.render(i,True,(op,0,qr))
    rectangle1=text.get_rect()
    rectangle1.center=(350,kl)
    a.blit(text,rectangle1)
    pygame.time.delay(1500)
    pygame.display.update()
    
    
f.close()

pygame.time.delay(3000)
t1 = time.time()
time_taken=0
yolo=True
x1=0
y1=0
p=(0,255,0)
border=400
square=5
level=1
a.fill((0,0,0))
font=pygame.font.Font('freesansbold.ttf',36)
font1=pygame.font.Font('freesansbold.ttf',20)
text=font.render("LEVEL 1 (5x5)",True,(255,0,0))
rules=font1.render("CLICK ON THE MAIN CIRCLE YOU WANT TO MOVE",True,(255,255,255))
rules2=font1.render("USE THE ARROW KEYS TO DRAW CIRCLES FROM THAT POSITION ",True,(255,255,255))
rectangle1=rules.get_rect()
rectangle1.center=(310,40)
rectangle=text.get_rect()
rectangle.center=(250,85)
rectangle2=rules2.get_rect()
rectangle2.center=(350,450)
ab=5

L=[(130,130),(190,370),(190,310),(250,130),(250,190),(250,370),(370,130),(310,310),(370,190),(310,370)]
def circle(z,y=p,q=30,x=a):
    global x1,y1,ab,L
    pygame.draw.circle(x,y,z,q)
    if z in L:
        pygame.draw.circle(x,(0,0,0),z,5)# to show main circles
    x1=z[0]
    y1=z[1]
    q={130:0,190:1,250:2,310:3,370:4,430:5,490:6,550:7}
   
    m={(0,255,0):1,(255,0,0):2,(0,0,255):3,(255,255,0):4,(255,90,0):5,(128,0,128):6,(255,190,200):7,(100,100,100):8}
    if x1==130:
        for j in q:
            if y1==j:
                s=q[y1]
                for k in m:
                    if y==k:
                        game[0][s]=m[y]
    if x1==190:
        for j in q:
            if y1==j:
                s=q[y1]
                for k in m:
                    if y==k:
                        game[1][s]=m[y]
    if x1==250:
        for j in q:
            if y1==j:
                s=q[y1]
                for k in m:
                    if y==k:
                        game[2][s]=m[y]
    if x1==310:
        for j in q:
            if y1==j:
                s=q[y1]
                for k in m:
                    if y==k:
                        game[3][s]=m[y]
    if x1==370:
        for j in q:
            if y1==j:
                s=q[y1]
                for k in m:
                    if y==k:
                        game[4][s]=m[y]

    if x1==430:
        for j in q:
            if y1==j:
                s=q[y1]
                for k in m:
                    if y==k:
                        game[5][s]=m[y]

    if x1==490:
        for j in q:
            if y1==j:
                s=q[y1]
                for k in m:
                    if y==k:
                        game[6][s]=m[y]


    if x1==550:
        for j in q:
            if y1==j:
                s=q[y1]
                for k in m:
                    if y==k:
                        game[7][s]=m[y]
 


        
        

    
def maincircles(level):
    if level==1:
        circle((130,130),(0,255,0),30)#green
        circle((190,370),(0,255,0),30)
        circle((190,310),(255,0,0),30)#red
        circle((250,130),(255,0,0),30)
        circle((250,190),(0,0,255),30)#blue
        circle((250,370),(0,0,255),30)
        circle((370,130),(255,255,0),30)#yellow
        circle((310,310),(255,255,0),30)
        circle((370,190),(255,90,0),30)#orange
        circle((310,370),(255,90,0),30)
        grid(square)
    if level==2:
        circle((130,370),(0,255,0),30)#green
        circle((250,250),(0,255,0),30)
        circle((190,250),(255,0,0),30)#red
        circle((190,370),(255,0,0),30)
        circle((130,130),(0,0,255),30)#blue
        circle((250,310),(0,0,255),30)
        circle((370,130),(255,255,0),30)#yellow
        circle((250,370),(255,255,0),30)
##      circle((370,190),(255,90,0),30)#orange
##      circle((310,370),(255,90,0),30)
        grid(square)
    if level==3:
        circle((130,250),(0,255,0),30)#green
        circle((310,130),(0,255,0),30)
        circle((130,310),(255,0,0),30)#red
        circle((370,310),(255,0,0),30)
        circle((190,310),(0,0,255),30)#blue
        circle((250,190),(0,0,255),30)
        circle((310,190),(255,255,0),30)#yellow
        circle((370,130),(255,255,0),30)
        circle((310,310),(255,90,0),30)#orange
        circle((370,370),(255,90,0),30)
        grid(square)
    if level==4:
        circle((130,130),(0,255,0),30)#green
        circle((370,430),(0,255,0),30)
        circle((310,250),(255,0,0),30)#red
        circle((370,370),(255,0,0),30)
        circle((190,370),(0,0,255),30)#blue
        circle((370,310),(0,0,255),30)
        circle((130,250),(255,255,0),30)#yellow
        circle((370,250),(255,255,0),30)
    ##    circle((370,190),(255,90,0),30)#orange
    ##    circle((310,370),(255,90,0),30)
        grid(square)
    if level==5:
        circle((250,370),(0,255,0),30)#green
        circle((430,250),(0,255,0),30)
        circle((310,130),(255,0,0),30)#red
        circle((430,130),(255,0,0),30)
        circle((250,250),(0,0,255),30)#blue
        circle((370,370),(0,0,255),30)
        circle((130,430),(255,255,0),30)#yellow
        circle((430,310),(255,255,0),30)
        circle((190,190),(255,90,0),30)#orange
        circle((310,370),(255,90,0),30)
        grid(square)
    if level==6:
        circle((130,130),(0,255,0),30)#green
        circle((430,130),(0,255,0),30)
        circle((130,190),(255,0,0),30)#red
        circle((190,430),(255,0,0),30)
        circle((130,250),(0,0,255),30)#blue
        circle((250,250),(0,0,255),30)
        circle((130,430),(255,255,0),30)#yellow
        circle((250,310),(255,255,0),30)
        circle((310,310),(255,90,0),30)#orange
        circle((370,250),(255,90,0),30)
        circle((250,430),(128,0,128),30)#purple
        circle((430,370),(128,0,128),30)
        grid(square)
    if level==7:
        circle((310,190),(0,255,0),30)#green
        circle((370,490),(0,255,0),30)
        circle((310,310),(255,0,0),30)#red
        circle((430,370),(255,0,0),30)
        circle((190,490),(0,0,255),30)#blue
        circle((490,130),(0,0,255),30)
        circle((490,250),(255,255,0),30)#yellow
        circle((490,490),(255,255,0),30)
        circle((430,250),(255,90,0),30)#orange
        circle((490,430),(255,90,0),30)
        grid(square)
    if level==8:
        circle((130,310),(0,255,0),30)#green
        circle((370,370),(0,255,0),30)
        circle((130,490),(255,0,0),30)#red
        circle((190,190),(255,0,0),30)
        circle((370,250),(0,0,255),30)#blue
        circle((490,310),(0,0,255),30)
        circle((190,370),(255,255,0),30)#yellow
        circle((370,310),(255,255,0),30)
        circle((370,490),(255,90,0),30)#orange
        circle((490,370),(255,90,0),30)
        grid(square)
    if level==9:
        circle((370,130),(0,255,0),30)#green
        circle((250,370),(0,255,0),30)
        circle((130,490),(255,0,0),30)#red
        circle((430,370),(255,0,0),30)
        circle((430,130),(0,0,255),30)#blue
        circle((310,310),(0,0,255),30)
        circle((190,490),(255,255,0),30)#yellow
        circle((310,370),(255,255,0),30)
        circle((250,250),(255,90,0),30)#orange
        circle((490,130),(255,90,0),30)
        grid(square)
    if level==10:
        circle((190,130),(0,255,0),30)#green
        circle((310,370),(0,255,0),30)
        circle((190,190),(255,0,0),30)#red
        circle((190,430),(255,0,0),30)
        circle((130,550),(0,0,255),30)#blue
        circle((550,550),(0,0,255),30)
        circle((250,430),(255,255,0),30)#yellow
        circle((490,190),(255,255,0),30)
        circle((310,310),(255,90,0),30)#orange
        circle((490,250),(255,90,0),30)
        circle((370,250),(128,0,128),30)#purple
        circle((370,490),(128,0,128),30)
        circle((370,370),(255,190,200),30)#pink
        circle((490,430),(255,190,200),30)
        circle((490,310),(100,100,100),30)#grey
        circle((550,130),(100,100,100),30)
        grid(square)
    if level==11:
        circle((130,130),(0,255,0),30)#green
        circle((250,190),(0,255,0),30)
        circle((190,190),(255,0,0),30)#red
        circle((370,250),(255,0,0),30)
        circle((310,190),(0,0,255),30)#blue
        circle((310,490),(0,0,255),30)
        circle((190,430),(255,255,0),30)#yellow
        circle((430,250),(255,255,0),30)
        circle((190,490),(255,90,0),30)#orange
        circle((430,130),(255,90,0),30)
        circle((370,550),(128,0,128),30)#purple
        circle((550,430),(128,0,128),30)
        circle((490,130),(255,190,200),30)#pink
        circle((550,370),(255,190,200),30)
        circle((430,550),(100,100,100),30)#grey
        circle((550,490),(100,100,100),30)
        grid(square)
    if level==12:
        circle((130,130),(0,255,0),30)#green
        circle((250,430),(0,255,0),30)
        circle((190,130),(255,0,0),30)#red
        circle((190,310),(255,0,0),30)
        circle((490,130),(0,0,255),30)#blue
        circle((250,490),(0,0,255),30)
        circle((250,310),(255,255,0),30)#yellow
        circle((490,490),(255,255,0),30)
        circle((310,190),(255,90,0),30)#orange
        circle((550,130),(255,90,0),30)
        circle((370,430),(128,0,128),30)#purple
        circle((370,550),(128,0,128),30)
    ##    circle((490,130),(255,190,200),30)#pink
    ##    circle((550,370),(255,190,200),30)
    ##    circle((430,550),(100,100,100),30)#grey
    ##    circle((550,490),(100,100,100),30)
        grid(square)
        
            
                
            
            
            
        
                
                
                


maincircles(level)
L=[(130,130),(190,370),(190,310),(250,130),(250,190),(250,370),(370,130),(310,310),(370,190),(310,370)]
def levelloop():
    global yolo,p,game,border,x1,y1,level
    while yolo and Lsolution!=game:
        a.blit(text,rectangle)
        a.blit(rules,rectangle1)
        a.blit(rules2,rectangle2)
    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                yolo=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and x1-60>100:
                    if (x1-60,y1) in L:       #to check overlap of main points
                        pass
                    else:
                        circle((x1-60,y1),p)
                if event.key==pygame.K_RIGHT and x1+60<border:
                    if (x1+60,y1) in L:
                        pass
                    else:
                        circle((x1+60,y1),p)
                if event.key==pygame.K_UP and y1-60>100:
                    if (x1,y1-60) in L:
                        pass
                    else:
                        circle((x1,y1-60),p)
                if event.key==pygame.K_DOWN and y1+60<border:
                    if (x1,y1+60) in L:
                        pass
                    else:
                        circle((x1,y1+60),p)
             
                
                if event.key==pygame.K_r:# to restart level     
                    a.fill((0,0,0))
                    restart()
                   
            if event.type==pygame.MOUSEBUTTONDOWN:
                nm,mk=[],0
                for i in event.pos:
                    nm.append(i)
                for j in L:
                    ok=0
                    if nm[0]-j[0]<=30 and nm[0]-j[0]>=-30:
                        ok=1
                    if nm[1]-j[1]<=30 and nm[1]-j[1]>=-30:
                        ok+=1
                    if ok==2:
                        x1,y1=j[0],j[1]
                        if mk==0 or mk==1:
                            p=(0,255,0)
                        if mk==2 or mk==3:
                            p=(255,0,0)
                        if mk==4 or mk==5:
                            p=(0,0,255)
                        if mk==6 or mk==7:
                            p=(255,255,0)
                        if mk==8 or mk==9:
                            p=(255,90,0)
                        if mk==10 or mk==11:
                            p=(128,0,128)
                        if mk==12 or mk==13:
                            p=(255,190,200)
                        if mk==14 or mk==15:
                            p=(100,100,100)
                    mk+=1
        pygame.display.update()
congrats="CONGRATS ON FINISHING LEVEL 1!!"
newcon="CONGRATS ON FINISHING LEVEL 1!!"
def restart():
    global square,level,game
    if square==5:
        game=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        maincircles(level)
    if square==6:
        game=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        maincircles(level)
    if square==7:
        game=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        maincircles(level)
    if square==8:
        game=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        maincircles(level)
def change():
    global newcon,congrats
    newcon=""
    for i in congrats:
        if i.isdigit():
            newcon+=str(int(i)+1)
        else:
            newcon+=i
    congrats=newcon
def congratswin():
    global time_taken
    global t1
    if Lsolution==game:
        if level!=1:
            change()
        a.fill((0,0,0))
        t2 = time.time()
        time_taken = ((t2-t1)//.01)/100
        time_taken1 = str(time_taken)
        end=pygame.font.Font('freesansbold.ttf',70)
        text3=font.render(newcon,True,(255,255,255))
        rect4=text3.get_rect()
        rect4.center=350,250
        a.blit(text3,rect4)
        text4=font.render("time taken-",True,(255,255,255))
        text5=font.render(time_taken1 +' sec' ,True,(255,255,255))
        rect5 = text4.get_rect()
        rect5.center=350,350
        rect6=text5.get_rect()
        rect6.center=350,400
        a.blit(text4,rect5)
        a.blit(text5,rect6)
        pygame.display.update()
        pygame.time.delay(3000)

levelloop()
congratswin()
time1(username,password,'level1',time_taken)
time_taken = 0
#LEVEL2
level+=1

t1 = time.time()
a.fill((0,0,0))
pygame.display.update()

Lsolution=[[3,1,1,1,1],[3,1,2,2,2],[3,1,1,3,4],[3,3,3,3,4],[4,4,4,4,4]]
game=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
L=[(130,370),(250,250),(190,250),(190,370),(130,130),(250,310),(370,130),(250,370)]
maincircles(level)
text=font.render("LEVEL 2(5x5)",True,(255,0,0))
levelloop()
congratswin()
time1(username,password,'level2',time_taken)
time_taken = 0
#LEVEL3
level+=1
t1 = time.time()
a.fill((0,0,0))
pygame.display.update()
Lsolution=[[1,1,1,2,2],[1,3,3,3,2],[1,3,2,2,2],[1,4,2,5,5],[4,4,2,2,5]]
game=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
L=[(130,250),(310,130),(130,310),(370,310),(190,310),(250,190),(310,190),(370,130),(310,310),(370,370)]
maincircles(level)
L=[(130,250),(310,130),(130,310),(370,310),(190,310),(250,190),(310,190),(370,130),(310,310),(370,370)]
text=font.render("LEVEL 3(5x5)",True,(255,0,0))
levelloop()
congratswin()
time1(username,password,'level3',time_taken)
time_taken = 0

##leve4(6x6)
level+=1
border+=60
square+=1
t1 = time.time()
a.fill((0,0,0))
pygame.display.update()
ab=6
L=[(130,130),(370,430),(310,250),(370,370),(190,370),(370,310),(130,250),(370,250)]
Lsolution=[[1,4,4,2,2,2],[1,4,2,2,3,2],[1,4,2,3,3,2],[1,4,2,3,2,2],[1,4,4,3,2,1],[1,1,1,1,1,1]]
game=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
maincircles(level)
text=font.render("LEVEL 4(6x6)",True,(255,0,0))
rectangle2.center=(350,480)
levelloop()
congratswin()
time1(username,password,'level4',time_taken)
time_taken = 0

##level5
level+=1
t1 = time.time()
a.fill((0,0,0))
pygame.display.update()
Lsolution=[[1,1,1,1,1,4],[1,5,5,5,1,4],[1,1,3,5,1,4],[2,1,3,5,5,4],[2,1,3,3,3,4],[2,1,1,4,4,4]]
game=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
L=[(250,370),(430,250),(310,130),(430,130),(250,250),(370,370),(130,430),(430,310),(190,190),(310,370)]
maincircles(level)
text=font.render("LEVEL 5(6x6)",True,(255,0,0))
levelloop()
congratswin()
time1(username,password,'level5',time_taken)
time_taken = 0

##level6
level+=1
t1 = time.time()
a.fill((0,0,0))
pygame.display.update()
Lsolution=[[1,2,3,4,4,4],[1,2,3,4,2,2],[1,2,3,4,2,6],[1,2,5,5,2,6],[1,2,5,2,2,6],[1,2,2,2,6,6]]
game=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
L=[(130,130),(430,130),(130,190),(190,430),(130,250),(250,250),(130,430),(250,310),(310,310),(370,250),(250,430),(430,370)]
maincircles(level)
text=font.render("LEVEL 6(6x6)",True,(255,0,0))
levelloop()
congratswin()
time1(username,password,'level6',time_taken)
time_taken = 0



##level7(7x7)
level+=1
border+=60
square+=1
pygame.display.set_mode((700,620))
t1 = time.time()
a.fill((0,0,0))
pygame.display.update()
Lsolution=[[3,3,3,3,3,3,3],[3,1,1,1,1,1,3],[3,1,4,4,4,1,1],[3,1,4,2,4,4,1],[3,4,4,2,2,4,1],[3,4,5,5,2,4,4],[3,4,4,5,5,5,4]]
game=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
L=[(310,190),(370,490),(310,310),(430,370),(190,490),(490,130),(490,250),(490,490),(430,250),(490,430)]
maincircles(level)
text=font.render("LEVEL 7(7x7)",True,(255,0,0))
rectangle2.center=(350,570)
levelloop()
congratswin()
time1(username,password,'level7',time_taken)
time_taken = 0


##level 8
level+=1
t1 = time.time()
a.fill((0,0,0))
pygame.display.update()
Lsolution=[[3,3,3,1,1,1,2],[3,2,3,4,4,1,2],[3,2,3,4,1,1,2],[3,2,3,4,1,2,2],[3,2,3,4,1,2,5],[3,2,2,2,2,2,5],[3,3,3,3,5,5,5]]
game=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
L=[(130,310),(370,370),(130,490),(190,190),(370,250),(490,310),(190,370),(370,310),(370,490),(490,370)]
maincircles(level)
text=font.render("LEVEL 8 (7x7)",True,(255,0,0))
levelloop()
congratswin()
time1(username,password,'level8',time_taken)
time_taken = 0

##level 9
level+=1
t1 = time.time()
a.fill((0,0,0))
pygame.display.update()

L=[(370,130),(250,370),(130,490),(430,370),(430,130),(310,310),(190,490),(310,370),(250,250),(490,130)]
Lsolution=[[1,1,1,1,1,2,2],[1,3,3,3,1,2,4],[1,3,5,3,1,2,4],[1,3,5,3,4,2,4],[1,3,5,4,4,2,4],[3,3,5,4,2,2,4],[5,5,5,4,4,4,4]]
game=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
maincircles(level)
text=font.render("LEVEL 9 (7x7)",True,(255,0,0))
levelloop()
congratswin()
time1(username,password,'level9',time_taken)
time_taken = 0

##leve10(8x8)
level+=1
border+=60
square+=1
a=pygame.display.set_mode((700,730))
t1 = time.time()
a.fill((0,0,0))
pygame.display.update()
rectangle2.center=(350,630)
L=[(190,130),(310,370),(190,190),(190,430),(130,550),(550,550),(250,430),(490,190),(310,310),(490,250),(370,250),(370,490),(370,370),(490,430),(490,310),(550,130)]
Lsolution=[[1,1,1,1,1,1,1,3],[1,2,2,2,2,2,1,3],[4,4,4,4,4,4,1,3],[4,5,5,5,1,1,1,3],[4,5,6,6,7,7,6,3],[4,5,5,6,6,7,6,3],[4,4,5,8,6,7,6,3],[8,8,8,8,6,6,6,3]]
game=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
maincircles(level)
text=font.render("LEVEL 10(8x8)",True,(255,0,0))
levelloop()
congratswin()
time1(username,password,'level10',time_taken)    
time_taken = 0



##level 11
level+=1
a=pygame.display.set_mode((700,730))
t1 = time.time()
a.fill((0,0,0))
pygame.display.update()
ab=6
rectangle2.center=(350,630)
L=[(130,130),(250,190),(190,190),(370,250),(310,190),(310,490),(190,430),(430,250),(190,490),(430,130),(370,550),(550,430),(490,130),(550,370),(430,550),(550,490)]

Lsolution=[[1,1,1,3,3,3,3,3],[2,2,1,3,4,4,5,3],[2,1,1,3,4,5,5,3],[2,3,3,3,4,5,3,3],[2,2,2,4,4,5,6,6],[5,5,4,4,5,5,6,8],[7,5,5,5,5,6,6,8],[7,7,7,7,7,6,8,8]]
game=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
maincircles(level)
text=font.render("LEVEL 11(8x8)",True,(255,0,0))
levelloop()
congratswin()
time1(username,password,'level11',time_taken)
time_taken = 0

##level 12
level+=1
a=pygame.display.set_mode((700,730))
t1 = time.time()
a.fill((0,0,0))
pygame.display.update()
ab=6
rectangle2.center=(350,630)
L=[(130,130),(250,430),(190,130),(190,310),(490,130),(250,490),(250,310),(490,490),(310,190),(550,130),(370,430),(370,550)]
Lsolution=[[1,1,1,1,1,1,1,1],[2,2,2,2,3,3,3,1],[3,3,3,4,3,1,3,1],[3,5,3,4,3,1,1,1],[3,5,3,4,3,6,6,6],[3,5,3,4,3,3,3,3],[3,5,3,4,4,4,4,3],[5,5,3,3,3,3,3,3]]
game=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
maincircles(level)
text=font.render("LEVEL 12(8x8)",True,(255,0,0))
levelloop()
congratswin()
time1(username,password,'level12',time_taken)
time_taken = 0

pygame.quit()

