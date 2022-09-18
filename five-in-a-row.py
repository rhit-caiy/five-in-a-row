#coding=utf8
import random
import time
import math
from tkinter import *
import tkinter.filedialog
import hashlib
window=Tk()
canvas=Canvas(window,bg="black",width=1440,height=810)
window.title('五子棋')
def isnumber(a):
    try:
        float(a)
        return 1
    except ValueError:
        return 0
def findnum(a,b):
    position=a.index(b)
    c=0
    for i in range(position,len(a)):
        if c==0:
            if isnumber(a[i])==1:
                first=i
                c=1
        elif c==1:
            if isnumber(a[i])==0:
                last=i
                break
    c=a[first:last]
    return c
def findallnumbetween(a,b,c):
    d=[]
    la=len(a)
    lb=len(b)
    lc=len(c)
    for i in range(la-lb):
        if a[i:i+lb]==b:
            for j in range(i+lb,la):
                if a[j:j+lc]==c:
                    d.append(int(a[i+lb:j]))
                    break
    return d
def grid(a):#axa矩阵
    b=[[0 for i in range(a)] for i in range(a)]
    return b
def edge(a,b,c,d):#a矩阵边长b，周围多c格填充d
    grid=[[d for i in range(b+2*c)] for i in range(b+2*c)]
    for i in range(c,b+c):
        for j in range(c,b+c):
            grid[i][j]=a[i-c][j-c]
    return grid
def create(num):#不同格子数对应边长，画棋盘
    global l
    canvas.create_rectangle(0,0,810,810,fill='#FFDD44')
    if num==11:
        l=67
    elif num==13:
        l=58
    elif num==15:
        l=50
    elif num==17:
        l=45
    elif num==19:
        l=40
    elif num==21:
        l=36
    for i in range(l,(num+1)*l,l):
        canvas.create_line(l,i,num*l,i)
        canvas.create_line(i,l,i,num*l)
    canvas.create_oval((num+0.75)*l/2,(num+0.75)*l/2,(num+1.25)*l/2,(num+1.25)*l/2,fill='black')
def startpage():#初始选择界面
    global helpon,step,page,pagechange,num,l,hardness,player,computer
    canvas.create_rectangle(0,0,1440,810,fill='#D0D0D0')
    canvas.create_text(720,50,text='five-in-a-row game')
    canvas.create_text(720,70,text='五子棋')
    canvas.create_rectangle(640,700,800,740,fill='#808080')
    canvas.create_text(720,720,text='start')
    
    canvas.create_text(50,150,text='size:')
    canvas.create_text(50,170,text='棋盘边长')
    canvas.create_rectangle(890,90,1010,210,tag='sizechoice')
    canvas.create_rectangle(100,100,200,200)
    canvas.create_text(150,150,text='11')
    canvas.create_rectangle(300,100,400,200)
    canvas.create_text(350,150,text='13')
    canvas.create_rectangle(500,100,600,200)
    canvas.create_text(550,150,text='15')
    canvas.create_rectangle(700,100,800,200)
    canvas.create_text(750,150,text='17')
    canvas.create_rectangle(900,100,1000,200)
    canvas.create_text(950,150,text='19')
    canvas.create_rectangle(1100,100,1200,200)
    canvas.create_text(1150,150,text='21')
    
    canvas.create_text(50,275,text='level:')
    canvas.create_text(50,295,text='难度')
    canvas.create_rectangle(1065,240,1135,310,tag='levelchoice')
    canvas.create_rectangle(75,250,125,300)
    canvas.create_text(100,275,text='0')
    canvas.create_rectangle(175,250,225,300)
    canvas.create_text(200,275,text='1')
    canvas.create_rectangle(275,250,325,300)
    canvas.create_text(300,275,text='2')
    canvas.create_rectangle(375,250,425,300)
    canvas.create_text(400,275,text='3')
    canvas.create_rectangle(475,250,525,300)
    canvas.create_text(500,275,text='4')
    canvas.create_rectangle(575,250,625,300)
    canvas.create_text(600,275,text='5')
    canvas.create_rectangle(675,250,725,300)
    canvas.create_text(700,275,text='6')
    canvas.create_rectangle(775,250,825,300)
    canvas.create_text(800,275,text='7')
    canvas.create_rectangle(875,250,925,300)
    canvas.create_text(900,275,text='8')
    canvas.create_rectangle(975,250,1025,300)
    canvas.create_text(1000,275,text='9')
    canvas.create_rectangle(1075,250,1125,300)
    canvas.create_text(1100,275,text='10')
    
    canvas.create_text(50,400,text='who first:')
    canvas.create_text(50,420,text='先手')
    canvas.create_rectangle(190,340,310,460,tag='first')
    canvas.create_rectangle(200,350,300,450)
    canvas.create_text(250,400,text='player')
    canvas.create_rectangle(400,350,500,450)
    canvas.create_text(450,400,text='computer')
    
    canvas.create_text(50,550,text='mode:')
    canvas.create_text(50,570,text='模式')
    canvas.create_rectangle(190,490,310,610,tag='mode')
    canvas.create_rectangle(200,500,300,600)
    canvas.create_text(250,550,text='player vs computer')
    canvas.create_rectangle(400,500,500,600)
    canvas.create_text(450,550,text='2 player')
    canvas.create_rectangle(600,500,700,600)
    canvas.create_text(650,550,text='3 player')
    canvas.create_rectangle(800,500,1000,600)
    canvas.create_text(900,550,text='reload the saved game')
    
    canvas.create_rectangle(1350,700,1400,750,fill='red')
    canvas.create_text(1375,725,text='help')
    helpon=0
    board=grid(13)
    step=0
    page=0
    pagechange=1
    num=19
    l=40
    hardness=10
    player=1
    computer=2
startpage()
def playpage():#下棋界面
    global black,white,red,green,blue,stepnum,c,p,board,step
    canvas.create_rectangle(0,0,810,810,fill='#FFDD44')
    canvas.create_rectangle(810,0,1440,810,fill='#F0F0F0')
    create(num)
    board=grid(num)
    canvas.create_rectangle(1350,700,1400,750,fill='red')
    canvas.create_text(1375,725,text='help')
    canvas.create_rectangle(1100,700,1300,750,fill='#C0C0C0')
    canvas.create_text(1200,715,text='restart with same options')
    canvas.create_text(1200,735,text='重新开始')
    canvas.create_rectangle(890,700,1090,750,fill='#C0C0C0')
    canvas.create_text(990,715,text='restart with different options')
    canvas.create_text(990,735,text='重选模式')
    canvas.create_rectangle(900,550,1300,650,fill='#A0A0A0')
    canvas.create_text(1100,580,text='save the coordinates of the chess in txt file')
    canvas.create_text(1100,620,text='将棋子坐标存为文本文档')
    canvas.create_rectangle(950,450,1000,500,fill='#A0A0A0')
    canvas.create_text(975,460,text='regret')
    canvas.create_text(975,490,text='悔棋')
    canvas.create_rectangle(1100,450,1300,500,fill='#A0A0A0')
    canvas.create_text(1200,460,text='replay the game')
    canvas.create_text(1200,490,text='复盘')
    canvas.create_rectangle(1140,350,1300,420,fill='#A0A0A0')
    canvas.create_text(1220,370,text='show step numbers')
    canvas.create_text(1220,400,text='显示手数')    
    black=[]
    white=[]
    red=[]
    green=[]
    blue=[]
    stepnum=grid(num)
    step=0
def put(x,y,colour):
    if colour==1:
        canvas.create_oval(l*x+0.6*l,l*y+0.6*l,l*x+1.4*l,l*y+1.4*l,fill='black')
    elif colour==2:
        canvas.create_oval(l*x+0.6*l,l*y+0.6*l,l*x+1.4*l,l*y+1.4*l,fill='white')
    elif colour==3:
        canvas.create_oval(l*x+0.6*l,l*y+0.6*l,l*x+1.4*l,l*y+1.4*l,fill='red')
    elif colour==4:
        canvas.create_oval(l*x+0.6*l,l*y+0.6*l,l*x+1.4*l,l*y+1.4*l,fill='green')
    elif colour==5:
        canvas.create_oval(l*x+0.6*l,l*y+0.6*l,l*x+1.4*l,l*y+1.4*l,fill='blue')
def chess(x,y,colour):
    global board,stepnum,step
    step+=1
    board[x][y]=colour
    stepnum[x][y]=step
    if colour==1:
        canvas.create_oval(l*x+0.6*l,l*y+0.6*l,l*x+1.4*l,l*y+1.4*l,fill='black')
        black.append([x,y])
    elif colour==2:
        canvas.create_oval(l*x+0.6*l,l*y+0.6*l,l*x+1.4*l,l*y+1.4*l,fill='white')
        white.append([x,y])
    elif colour==3:
        canvas.create_oval(l*x+0.6*l,l*y+0.6*l,l*x+1.4*l,l*y+1.4*l,fill='red')
        red.append([x,y])
    elif colour==4:
        canvas.create_oval(l*x+0.6*l,l*y+0.6*l,l*x+1.4*l,l*y+1.4*l,fill='green')
        green.append([x,y])
    elif colour==5:
        canvas.create_oval(l*x+0.6*l,l*y+0.6*l,l*x+1.4*l,l*y+1.4*l,fill='blue')
        blue.append([x,y])
    if colour==1 or colour==2:
        blackboard=edge(board,num,4,0)
        for i in range(-1,2):
            for j in range(0,2):
                if i==-1 and j==0 or j==1:
                    line=[0,0,0,0,0,0,0,0,0]
                    for k in range(-4,5):
                        line[k+4]=blackboard[x+4+k*i][y+4+k*j]
                    for m in range(5):
                        win=1
                        for n in range(5):
                            if line[m+n]!=colour:
                                win=0
                        if win==1:
                            canvas.create_text(1000,200,text='if you want to continue, keep clicking the board')
                            if colour==1:
                                print('black win')
                                canvas.create_text(900,70,text='black win')
                                if page==1:
                                    if p==1:
                                        print('player win')
                                        canvas.create_text(900,100,text='player win')
                                    else:
                                        print('computer win')
                                        canvas.create_text(900,100,text='computer win')
                            elif colour==2:
                                print('white win')
                                canvas.create_text(1100,70,text='white win')
                                if page==1:
                                    if p==2:
                                        print('player win')
                                        canvas.create_text(1100,100,text='player win')
                                    else:
                                        print('computer win')
                                        canvas.create_text(1100,100,text='computer win')
    else:
        blackboard=edge(board,num,3,0)
        for i in range(-1,2):
            for j in range(0,2):
                if i==-1 and j==0 or j==1:
                    line=[0,0,0,0,0,0,0]
                    for k in range(-3,4):
                        line[k+3]=blackboard[x+3+k*i][y+3+k*j]
                    for m in range(4):
                        win=1
                        for n in range(4):
                            if line[m+n]!=colour:
                                win=0
                        if win==1:
                            if colour==3:
                                print('red win')
                                canvas.create_text(1000,100,text='red win')
                            elif colour==4:
                                print('green win')
                                canvas.create_text(1100,100,text='green win')
                            elif colour==5:
                                print('blue win')
                                canvas.create_text(1200,100,text='blue win')
def help():#帮助界面
    global helpon
    if helpon==0:
        helpon=1
        canvas.create_rectangle(0,0,1440,810,fill='#A0A0A0',tag='helpbg')
        canvas.create_rectangle(1350,700,1400,750,fill='red')
        canvas.create_text(1375,725,text='help')
        canvas.create_text(720,40,text='help',tag='head')
        canvas.create_text(700,100,text='this is the help page for this game, you can click anywhere to close it',tag='text1')
        canvas.create_text(700,120,text='FIR(five in a row) or gobang or 五子棋 is a simple chess game on the crossline chess board, it has a simple rule',tag='text2')
        canvas.create_text(700,140,text='each of the two players put their chess(usually black and white) in turn on the crossdot, if one of the colour successfully line up consequently in horizontal, verticle, diagnotical line with five of the chess, then that player wins',tag='text3')
        canvas.create_text(700,160,text='startpage',tag='text4')
        canvas.create_text(700,180,text='on the front page, you can choose the mode for the game, the system has initial settings (player vs computer level 10, player first, size 19x19) and you can click other blocks to change them',tag='text5')
        canvas.create_text(700,200,text='playpage',tag='text6')
        canvas.create_text(700,220,text='there is a board on the left and by clicking it you can put the chesses on it. in pvc or pvp mode, black always go first and in 3 people mode, the chess turn red-green-blue in turn and win when line up with 4',tag='text7')
        canvas.create_text(700,240,text='there are many functional icons at right, like show steps on the chess, regret and erase the newest step, replay the record of this game, save the coordinates of the game in the file in the same address of this game with name of time',tag='text8')
        canvas.create_text(700,260,text='you can restart this game with the same mode you chose or rechoose those mode, and you have already entered this page by clicking help buttom',tag='text9')
        canvas.create_text(700,280,text='when one of the player or computer wins, the judgement would automatically appears at right top. Even the game is finished, you can keep clicking the board for testing purpose',tag='text10')
        #canvas.create_text(700,300,text='',tag='text11')
        #canvas.create_text(700,320,text='',tag='text12')
    else:
        helpon=0
        
        canvas.delete('helpbg','head')
        for i in range(1,13):
            tag='text'+str(i)
            canvas.delete(tag)
'''
every level have a small random plus centric peak to make sure to put the chess approach the center randomly
lv0:totally randomly place on the board
lv1:base on the number of chess in surrounding 3x3 area
lv2:the 8 directions of 2 grids
lv3:the 3 grids but small difference in value
lv4:the 3 grids with large difference
lv5:the 4 grids
lv6:the 4 grids with relatively larger difference
lv7:the 5 grids with the ability to detect not linked conditions in one direction, decrease the value near the edge
lv8:the 5 grids with avoid diagonal start by 0.8 and prefer it after first step by factor 1.2
lv9:the 4 directions with 5 grid in a 4x11 2D array, divide into defense and attack, distinguish the edge in these conditions
lv10:know the conditions for unworthy point to attack or defense
'''
def click(coordinate):
    global x,y,reverse,step,page,num,l,board,black,white,red,green,blue,p,c,hardness,page,player,computer,pagechange,helpon,stepnum,replayon
    if replayon==0:
        x=coordinate.x
        y=coordinate.y
        if helpon==1 or 1350<x<1400 and 700<y<750:
            help()
        elif page==0:
            if 100<y<200:
                if 100<x<200:
                    num=11
                    canvas.delete('sizechoice')
                    canvas.create_rectangle(90,90,210,210,tag='sizechoice')
                elif 300<x<400:
                    num=13
                    canvas.delete('sizechoice')
                    canvas.create_rectangle(290,90,410,210,tag='sizechoice')
                elif 500<x<600:
                    num=15
                    canvas.delete('sizechoice')
                    canvas.create_rectangle(490,90,610,210,tag='sizechoice')
                elif 700<x<800:
                    num=17
                    canvas.delete('sizechoice')
                    canvas.create_rectangle(690,90,810,210,tag='sizechoice')
                elif 900<x<1000:
                    num=19
                    canvas.delete('sizechoice')
                    canvas.create_rectangle(890,90,1010,210,tag='sizechoice')
                elif 1100<x<1200:
                    num=21
                    canvas.delete('sizechoice')
                    canvas.create_rectangle(1090,90,1210,210,tag='sizechoice')
                    
            elif 250<y<300:
                if 75<x<125:
                    hardness=0
                    canvas.delete('levelchoice')
                    canvas.create_rectangle(65,240,135,310,tag='levelchoice')
                elif 175<x<225:
                    hardness=1
                    canvas.delete('levelchoice')
                    canvas.create_rectangle(165,240,235,310,tag='levelchoice')
                elif 275<x<325:
                    hardness=2
                    canvas.delete('levelchoice')
                    canvas.create_rectangle(265,240,335,310,tag='levelchoice')
                elif 375<x<425:
                    hardness=3
                    canvas.delete('levelchoice')
                    canvas.create_rectangle(365,240,435,310,tag='levelchoice')
                elif 475<x<525:
                    hardness=4
                    canvas.delete('levelchoice')
                    canvas.create_rectangle(465,240,535,310,tag='levelchoice')
                elif 575<x<625:
                    hardness=5
                    canvas.delete('levelchoice')
                    canvas.create_rectangle(565,240,635,310,tag='levelchoice')
                elif 675<x<725:
                    hardness=6
                    canvas.delete('levelchoice')
                    canvas.create_rectangle(665,240,735,310,tag='levelchoice')
                elif 775<x<825:
                    hardness=7
                    canvas.delete('levelchoice')
                    canvas.create_rectangle(765,240,835,310,tag='levelchoice')
                elif 875<x<925:
                    hardness=8
                    canvas.delete('levelchoice')
                    canvas.create_rectangle(865,240,935,310,tag='levelchoice')
                elif 975<x<1025:
                    hardness=9
                    canvas.delete('levelchoice')
                    canvas.create_rectangle(965,240,1035,310,tag='levelchoice')
                elif 1075<x<1125:
                    hardness=10
                    canvas.delete('levelchoice')
                    canvas.create_rectangle(1065,240,1135,310,tag='levelchoice')
                    
            elif 350<y<450:
                if 200<x<300:
                    player=1
                    computer=2
                    canvas.delete('first')
                    canvas.create_rectangle(190,340,310,460,tag='first')
                elif 400<x<500:
                    player=2
                    computer=1
                    canvas.delete('first')
                    canvas.create_rectangle(390,340,510,460,tag='first')
                    
            elif 500<y<600:
                if 200<x<300:
                    pagechange=1
                    canvas.delete('mode')
                    canvas.create_rectangle(190,490,310,610,tag='mode')
                elif 400<x<500:
                    pagechange=2
                    canvas.delete('mode')
                    canvas.create_rectangle(390,490,510,610,tag='mode')
                elif 600<x<700:
                    pagechange=3
                    canvas.delete('mode')
                    canvas.create_rectangle(590,490,710,610,tag='mode')
                elif 800<x<1000:
                    reload()
                
            elif 600<x<840 and 700<y<750:
                playpage()
                page=pagechange#三种模式
                if page==1:#人机
                    c=computer
                    p=player
                    canvas.create_text(975,300,text='level')
                    canvas.create_text(1000,300,text=hardness)
                    if c==1:
                        level()
        #功能
        elif 890<x<1090 and 700<y<750:
            startpage()
            
        elif 1100<x<1200 and 700<y<750:
            playpage()
            if page==1 and c==1:
                level()
        
        elif 900<x<1300 and 550<y<650:
            save()
    
        elif 950<x<1000 and 450<y<500:
            regret()
            
        elif 1100<x<1300 and 450<y<500:
            replay()
        
        elif 1140<x<1300 and 350<y<420:
            shownumber()
        
        elif l/2<x<(num+0.5)*l and l/2<y<(num+0.5)*l:
            x=round(x/l)-1
            y=round(y/l)-1
            if board[x][y]==0:
                if page==1:
                    chess(x,y,p)
                    level()
                elif page==2:
                    if step%2==0:
                        chess(x,y,1)
                    else:
                        chess(x,y,2)
                elif page==3:
                    if step%3==0:
                        chess(x,y,3)
                    elif step%3==1:
                        chess(x,y,4)
                    elif step%3==2:
                        chess(x,y,5)
    else:
        '''
        x=coordinate.x
        y=coordinate.y
        if 
        '''
        pass
    
def level():
    if hardness==0:
        lv0()
    elif hardness==1:
        lv1()
    elif hardness==2:
        lv2()
    elif hardness==3 or hardness==4:
        lv34()
    elif hardness==5 or hardness==6:
        lv56()
    elif hardness==7 or hardness==8:
        lv78()
    elif hardness==9 or hardness==10:
        lv910()
        
replayon=0
canvas.bind("<Button-1>",click)
def lv0():
    newboard=board
    value=grid(num)
    for i in range(num):
        for j in range(num):
            if newboard[i][j]==0:
                value[i][j]=round(random.random(),3)
    x,y=0,0
    for i in range(num):
        for j in range(num):
            if value[i][j]>value[x][y]:
                x,y=i,j
    chess(x,y,c)
def lv1():
    newboard=edge(board,num,1,0)
    value=grid(num)
    for i in range(1,num+1):
        for j in range(1,num+1):
            if newboard[i][j]==0:
                value[i-1][j-1]=round(((i+1)*(num-i)/num**2+(j+1)*(num-j)/num**2)*4+random.random(),3)
                for m in range(-1,2):
                    for n in range(-1,2):
                        if m!=0 or n!=0:
                            if newboard[i+m][j+n]==1 or newboard[i+m][j+n]==2:
                                value[i-1][j-1]+=1
    x,y=0,0
    for i in range(num):
        for j in range(num):
            if value[i][j]>value[x][y]:
                x,y=i,j
    chess(x,y,c)
def lv2():
    newboard=edge(board,num,2,0)
    value=grid(num)
    for i in range(2,num+2):
        for j in range(2,num+2):
            if newboard[i][j]==0:
                value[i-2][j-2]=round(((i-1)*(num-i)/num**2+(j-1)*(num-j)/num**2)*4+random.random(),3)
                for m in range(-1,2):
                    for n in range(-1,2):
                        if m!=0 or n!=0:
                            line=[0,0,0]
                            for k in range(1,3):
                                line[k]=newboard[i+k*m][j+k*n]
                            if hardness==2:
                                if line[1]==p and line[2]==p:
                                    value[i-2][j-2]+=10
                                elif line[1]==p and line[2]==c:
                                    value[i-2][j-2]+=1
                                elif line[1]==p:
                                    value[i-2][j-2]+=3
                                elif line[1]==0 and line[2]==p:
                                    value[i-2][j-2]+=1

                                if line[1]==c and line[2]==c:
                                    value[i-2][j-2]+=6
                                elif line[1]==c and line[2]==p:
                                    value[i-2][j-2]+=1
                                elif line[1]==c:
                                    value[i-2][j-2]+=2
                                elif line[1]==0 and line[2]==c:
                                    value[i-2][j-2]+=1                                
    x,y=0,0
    for i in range(num):
        for j in range(num):
            if value[i][j]>value[x][y]:
                x,y=i,j
    chess(x,y,c)
    
def lv34():
    newboard=edge(board,num,3,0)
    value=grid(num)
    for i in range(3,num+3):
        for j in range(3,num+3):
            if newboard[i][j]==0:
                value[i-3][j-3]=round(((i-2)*(num-i)/num**2+(j-2)*(num-j)/num**2)*4+random.random(),3)
                for m in range(-1,2):
                    for n in range(-1,2):
                        if m!=0 or n!=0:
                            line=[0,0,0,0]
                            for k in range(1,4):
                                line[k]=newboard[i+k*m][j+k*n]
                            if hardness==4:
                                if line[1]==p and line[2]==p and line[3]==p:
                                    value[i-3][j-3]+=3
                                elif line[1]==p and line[2]==p and line[3]==c:
                                    value[i-3][j-3]+=0.5
                                elif line[1]==p and line[2]==p:
                                    value[i-3][j-3]+=1
                                elif line[1]==p and line[2]==c:
                                    value[i-3][j-3]+=0.1
                                elif line[1]==p:
                                    value[i-3][j-3]+=0.3
                                    
                                if line[1]==c and line[2]==c and line[3]==c:
                                    value[i-3][j-3]+=3
                                elif line[1]==c and line[2]==c and line[3]==p:
                                    value[i-3][j-3]+=0.4
                                elif line[1]==c and line[2]==c:
                                    value[i-3][j-3]+=0.9
                                elif line[1]==c and line[2]==p:
                                    value[i-3][j-3]+=0.1
                                elif line[1]==c:
                                    value[i-3][j-3]+=0.2
                                    
                            if hardness==3:
                                if line[1]==p and line[2]==p and line[3]==p:
                                    value[i-3][j-3]+=4
                                elif line[1]==p and line[2]==p and line[3]==c:
                                    value[i-3][j-3]+=2
                                elif line[1]==p and line[2]==p:
                                    value[i-3][j-3]+=3
                                elif line[1]==p and line[2]==c:
                                    value[i-3][j-3]+=1
                                elif line[1]==p:
                                    value[i-3][j-3]+=2
                                    
                                if line[1]==c and line[2]==c and line[3]==c:
                                    value[i-3][j-3]+=4
                                elif line[1]==c and line[2]==c and line[3]==p:
                                    value[i-3][j-3]+=2
                                elif line[1]==c and line[2]==c:
                                    value[i-3][j-3]+=3
                                elif line[1]==c and line[2]==p:
                                    value[i-3][j-3]+=1
                                elif line[1]==c:
                                    value[i-3][j-3]+=2
    x,y=0,0
    for i in range(num):
        for j in range(num):
            if value[i][j]>value[x][y]:
                x,y=i,j
    chess(x,y,c)
    
def lv56():
    newboard=edge(board,num,4,0)
    value=grid(num)
    for i in range(4,num+4):
        for j in range(4,num+4):
            if newboard[i][j]==0:
                value[i-4][j-4]=round(((i-3)*(num-i)/num**2+(j-3)*(num-j)/num**2)*4+random.random(),3)
                for m in range(-1,2):
                    for n in range(-1,2):
                        if m!=0 or n!=0:
                            line=[0,0,0,0,0]
                            for k in range(1,5):
                                line[k]=newboard[i+k*m][j+k*n]
                            if hardness==5:
                                if line[1]==p and line[2]==p and line[3]==p and line[4]==p:
                                    value[i-4][j-4]+=300
                                elif line[1]==p and line[2]==p and line[3]==p and line[4]==c:
                                    value[i-4][j-4]+=50
                                elif line[1]==p and line[2]==p and line[3]==p:
                                    value[i-4][j-4]+=90
                                elif line[1]==p and line[2]==p and line[3]==c:
                                    value[i-4][j-4]+=8
                                elif line[1]==p and line[2]==p:
                                    value[i-4][j-4]+=15
                                elif line[1]==p and line[2]==c:
                                    value[i-4][j-4]+=2
                                elif line[1]==p:
                                    value[i-4][j-4]+=3
                                
                                if line[1]==c and line[2]==c and line[3]==c and line[4]==c:
                                    value[i-4][j-4]+=500
                                elif line[1]==c and line[2]==c and line[3]==c and line[4]==p:
                                    value[i-4][j-4]+=20
                                elif line[1]==c and line[2]==c and line[3]==c:
                                    value[i-4][j-4]+=50
                                elif line[1]==c and line[2]==c and line[3]==p:
                                    value[i-4][j-4]+=4
                                elif line[1]==c and line[2]==c:
                                    value[i-4][j-4]+=8
                                elif line[1]==c and line[2]==p:
                                    value[i-4][j-4]+=1
                                elif line[1]==c:
                                    value[i-4][j-4]+=2
                            
                            elif hardness==6:
                                if line[1]==p and line[2]==p and line[3]==p and line[4]==p:
                                    value[i-4][j-4]+=1200
                                elif line[1]==p and line[2]==p and line[3]==p and line[4]==c:
                                    value[i-4][j-4]+=100
                                elif line[1]==p and line[2]==p and line[3]==p:
                                    value[i-4][j-4]+=500
                                elif line[1]==p and line[2]==p and line[3]==c:
                                    value[i-4][j-4]+=10
                                elif line[1]==p and line[2]==p:
                                    value[i-4][j-4]+=20
                                elif line[1]==p and line[2]==c:
                                    value[i-4][j-4]+=2
                                elif line[1]==p:
                                    value[i-4][j-4]+=4
                            
                                if line[1]==c and line[2]==c and line[3]==c and line[4]==c:
                                    value[i-4][j-4]+=2000
                                elif line[1]==c and line[2]==c and line[3]==c and line[4]==p:
                                    value[i-4][j-4]+=200
                                elif line[1]==c and line[2]==c and line[3]==c:
                                    value[i-4][j-4]+=400
                                elif line[1]==c and line[2]==c and line[3]==p:
                                    value[i-4][j-4]+=5
                                elif line[1]==c and line[2]==c:
                                    value[i-4][j-4]+=10
                                elif line[1]==c and line[2]==p:
                                    value[i-4][j-4]+=1
                                elif line[1]==c:
                                    value[i-4][j-4]+=2                                
                            
    x,y=0,0
    for i in range(num):
        for j in range(num):
            if value[i][j]>value[x][y]:
                x,y=i,j
    chess(x,y,c)
    
def lv78():
    newboard=edge(board,num,5,3)
    value=grid(num)
    for i in range(5,num+5):
        for j in range(5,num+5):
            if newboard[i][j]==0:
                value[i-5][j-5]=round(((i-4)*(num-i)/num**2+(j-4)*(num-j)/num**2)*4+random.random(),3)
                for m in range(-1,2):
                    for n in range(-1,2):
                        if m!=0 or n!=0:
                            line=[0,0,0,0,0,0]
                            linevalue=0
                            for k in range(1,6):
                                line[k]=newboard[i+k*m][j+k*n]
                            if line[1]==p and line[2]==p and line[3]==p and line[4]==p:
                                linevalue+=1200
                            elif line[1]==0 and line[2]==p and line[3]==p and line[4]==p and (line[5]==c or line[5]==3):
                                linevalue+=99
                            elif line[1]==p and line[2]==p and line[3]==p and (line[4]==c or line[4]==3):
                                linevalue+=100
                            elif line[1]==p and line[2]==p and line[3]==p:
                                linevalue+=500
                            elif line[1]==p and line[2]==p and (line[3]==c or line[3]==3):
                                linevalue+=10
                            elif line[1]==p and line[2]==p:
                                linevalue+=20
                            elif line[1]==p and (line[2]==c or line[2]==3):
                                linevalue+=2
                            elif line[1]==p:
                                linevalue+=3
                            elif line[1]==0 and line[2]==p and line[3]==p and line[4]==0:
                                linevalue+=18
                            elif line[1]==0 and line[2]==p and line[3]==p and (line[4]==c or line[4]==3):
                                linevalue+=9
                            elif line[1]==0 and line[2]==p:
                                linevalue+=1
                                
                            if line[1]==c and line[2]==c and line[3]==c and line[4]==c:
                                linevalue+=2000
                            elif line[1]==0 and line[2]==c and line[3]==c and line[4]==c and (line[5]==p or line[5]==3):
                                linevalue+=199
                            elif line[1]==c and line[2]==c and line[3]==c and (line[4]==p or line[4]==3):
                                linevalue+=200
                            elif line[1]==c and line[2]==c and line[3]==c:
                                linevalue+=400
                            elif line[1]==c and line[2]==c and (line[3]==p or line[3]==3):
                                linevalue+=5
                            elif line[1]==c and line[2]==c:
                                linevalue+=10
                            elif line[1]==c and (line[2]==p or line[2]==3):
                                linevalue+=1
                            elif line[1]==c:
                                linevalue+=2
                            elif line[1]==0 and line[2]==c and line[3]==c and line[4]==0:
                                linevalue+=9
                            elif line[1]==0 and line[2]==c and line[3]==c and (line[4]==p or line[4]==3):
                                linevalue+=4
                            elif line[1]==0 and line[2]==c:
                                linevalue+=1
                                
                            if hardness==8:
                                if (m==1 or m==-1) and (n==1 or n==-1):
                                    if step<2:
                                        linevalue*=0.8
                                    else:
                                        linevalue*=1.2
                            value[i-5][j-5]+=linevalue
    x,y=0,0
    for i in range(num):
        for j in range(num):
            if value[i][j]>value[x][y]:
                x,y=i,j
    chess(x,y,c)
    
def lv910():
    defenseboard=edge(board,num,5,c)
    attackboard=edge(board,num,5,p)
    defensevalue=grid(num)
    attackvalue=grid(num)
    extravalue=grid(num)
    value=grid(num)
    '''
    得分数值
    value[][]>defensevalue[][]>gridvalue[]>v
               attackvalue[][]>
                extravalue[][]
    记录数值
    board>defenseboard>lines>line
          attackboard>
    三个分别算，优点：边缘可以任意调整为玩家或电脑
    '''
    #defense part
    for i in range(num):
        for j in range(num):
            if defenseboard[i+5][j+5]==0:
                lines=[[0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0]]
                gridvalue=[0,0,0,0]
                l=-1
                for m in range(-1,2):
                    for n in range(0,2):
                        if m==-1 or n==1:
                            l+=1
                            for k in range(-5,6):
                                lines[l][k+5]=defenseboard[i+5-k*m][j+5+k*n]
                                #存放单个点周围4个方向10个格子的状态
                for l in range(4):
                    line=lines[l]
                    v=0
                    #判断行分数
                    #已经输的情况，正式版本这里可以没有
                    if line[0]==p and line[1]==p and line[2]==p and line[3]==p and line[4]==p:#11111_
                        v+=5000
                    if line[6]==p and line[7]==p and line[8]==p and line[9]==p and line[10]==p:#_11111
                        v+=5000
                    
                    #直接会输的情况
                    if v==0:
                        if line[0]==0 and line[1]==p and line[2]==p and line[3]==p and line[4]==p:#01111_
                            v+=1600
                        if line[6]==p and line[7]==p and line[8]==p and line[9]==p and line[10]==0:#_11110
                            v+=1600
                        
                    #如果不下就输的情况，这两种都在100以上量级
                    #4个对手棋
                    if v==0:
                        if line[0]==c and line[1]==p and line[2]==p and line[3]==p and line[4]==p:#21111_
                            v+=1500
                        if line[2]==p and line[3]==p and line[4]==p and line[6]==p:#111_1
                            v+=1500
                        if line[3]==p and line[4]==p and line[6]==p and line[7]==p:#11_11
                            v+=1500
                        if line[4]==p and line[6]==p and line[7]==p and line[8]==p:#1_111
                            v+=1500
                        if line[6]==p and line[7]==p and line[8]==p and line[9]==p and line[10]==c:#_11112
                            v+=1500
                    
                        if line[2]==p and line[3]==0 and line[4]==p and line[6]==p and line[7]==0 and line[8]==p:#101_101
                            v+=1000
                            #子类，值减半
                        if line[4]==p and line[6]==0 and line[7]==p and line[8]==p and line[9]==0 and line[10]==p:#1_10101
                            v+=600
                        if line[0]==p and line[1]==0 and line[2]==p and line[3]==0 and line[4]==p and line[6]==p:#10101_1
                            v+=600
                        if line[3]==p and line[4]==0 and line[6]==p and line[7]==p and line[8]==0 and line[9]==p and line[10]==c:#10_11012
                            v+=1000
                        if line[0]==c and line[1]==p and line[2]==0 and line[3]==p and line[4]==p and line[6]==0 and line[7]==p:#21011_01
                            v+=1000
                    
                        #3个，因不确定数列外排列而值为90
                        if line[1]==0 and line[2]==p and line[3]==p and line[4]==p and line[6]==0:#0111_0
                            v+=900
                            if line[0]==2:
                                v+=200
                        if line[2]==0 and line[3]==p and line[4]==p and line[6]==p and line[7]==0:#011_10
                            v+=900
                        if line[3]==0 and line[4]==p and line[6]==p and line[7]==p and line[8]==0:#01_110
                            v+=900
                        if line[4]==0 and line[6]==p and line[7]==p and line[8]==p and line[9]==0:#0_1110
                            v+=900
                            if line[10]==2:
                                v+=200
                            #解法倾向于_11102
                        #子类，减半
                        if line[6]==p and line[7]==0 and line[8]==p and line[9]==p and line[10]==0:#_10110
                            v+=600
                        if line[0]==0 and line[1]==p and line[2]==p and line[3]==0 and line[4]==p:#01101_
                            v+=600
                        if line[6]==p and line[7]==p and line[8]==0 and line[9]==p and line[10]==0:#_11010
                            v+=600
                        if line[0]==0 and line[1]==p and line[2]==0 and line[3]==p and line[4]==p:#01011_
                            v+=600                        
                    
                    #对手走了两步内必胜情况,值定在5000左右。会有更多子类,重点考虑整个数列边缘部分
                    #每个大类互相独立，优先考虑上位
                    if v==0:
                        #1个2，3个1
                        if line[1]==c and line[2]==p and line[3]==p and line[4]==p or line[0]==c and line[1]==p and line[2]==p and line[3]==p and line[4]==0 or line[6]==p and line[7]==p and line[8]==p and line[9]==c or line[6]==0 and line[7]==p and line[8]==p and line[9]==p and line[10]==c:#2111_ _
                            v+=50
                        elif line[2]==c and line[3]==p and line[4]==p and line[6]==p or line[0]==c and line[1]==p and line[2]==p and line[3]==0 and line[4]==p or line[6]==p and line[7]==0 and line[8]==p and line[9]==p and line[10]==c or line[4]==p and line[6]==p and line[7]==p and line[8]==c:#211_1_
                            v+=50
                        elif line[3]==c and line[4]==p and line[6]==p and line[7]==p or line[0]==c and line[1]==p and line[2]==0 and line[3]==p and line[4]==p or line[3]==p and line[4]==p and line[6]==p and line[7]==c or line[6]==p and line[7]==p and line[8]==0 and line[9]==p and line[10]==c:#21_11_
                            v+=50
                        elif line[3]==c and line[4]==p and line[6]==p and line[7]==0 and line[8]==p or line[1]==c and line[2]==p and line[3]==0 and line[4]==p and line[6]==p or line[2]==p and line[3]==0 and line[4]==p and line[6]==p and line[7]==c or line[4]==p and line[6]==p and line[7]==0 and line[8]==p and line[9]==c:#21_1_1
                            v+=50
                        elif line[3]==p and line[4]==p and line[6]==0 and line[7]==p or line[2]==p and line[3]==p and line[4]==0 and line[6]==p or line[3]==p and line[4]==0 and line[6]==p and line[7]==p or line[4]==p and line[6]==0 and line[7]==p and line[8]==p:#11_ _1
                            v+=50
                        elif line[3]==p and line[4]==0 and line[6]==0 and line[7]==p and line[8]==0 and line[9]==p or line[1]==p and line[2]==0 and line[3]==p and line[4]==0 and line[6]==0 and line[7]==p:#10_0101
                            v+=50
                        
                        #2个1
                        elif line[3]==0 and line[4]==p and line[6]==p and line[7]==0:#01_10
                            v+=50
                        elif line[6]==p and line[7]==0 and line[8]==p and line[9]==0:#_1010
                            v+=45
                        elif line[1]==0 and line[2]==p and line[3]==0 and line[4]==p:#0101_
                            v+=45
                        elif line[6]==0 and line[7]==p and line[8]==p and line[9]==0:#_0110
                            v+=40
                        elif line[1]==0 and line[2]==p and line[3]==p and line[4]==0:#0110_
                            v+=40
                        elif line[4]==0 and line[6]==p and line[7]==p and line[8]==0:#0_110
                            v+=50
                        elif line[2]==0 and line[3]==p and line[4]==p and line[6]==0:#011_0
                            v+=50
                        elif line[3]==0 and line[4]==p and line[6]==0 and line[7]==p and line[8]==0:#01_010
                            v+=50
                        elif line[2]==0 and line[3]==p and line[4]==0 and line[6]==p and line[7]==0:#010_10
                            v+=50
                        
                    #其他情况，两步内不会输
                    if v==0:
                        if line[6]==p and line[7]==p and line[8]==c or line[4]==p and line[3]==p and line[2]==c:#_112
                            v+=8
                        elif line[6]==p and line[7]==0 and line[8]==c or line[4]==p and line[3]==0 and line[2]==c:#_102
                            v+=7
                        elif line[6]==p and line[7]==0 and line[8]==c or line[4]==p and line[3]==0 and line[2]==c:#_012
                            v+=4
                        elif line[6]==p and line[7]==c or line[4]==p and line[3]==c:#_12
                            v+=6
                        elif line[4]==p or line[6]==p:#_1
                            v+=10
                        elif line[3]==p and line[4]==0 or line[6]==0 and line[7]==p:#_01
                            v+=1
                        
                    #是否没必要
                    left=-1
                    right=12
                    for a in range(11):
                        if line[a]==c:
                            if a<5:
                                left=a
                            if a>5 and right>a:
                                right=a
                    dif=right-left
                    if dif<6 and hardness==10:
                        v=0
                    gridvalue[l]=v
                defensevalue[i][j]=sum(gridvalue)
    #attack part
    for i in range(num):
        for j in range(num):
            if attackboard[i+5][j+5]==0:
                lines=[[0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0]]
                gridvalue=[0,0,0,0]
                l=-1
                for m in range(-1,2):
                    for n in range(0,2):
                        if m==-1 or n==1:
                            l+=1
                            for k in range(-5,6):
                                lines[l][k+5]=attackboard[i+5-k*m][j+5+k*n]
                                #存放单个点周围4个方向10个格子的状态
                for l in range(4):
                    line=lines[l]
                    v=0
                    #判断行分数
                    #此行以下输为赢
                    #已经赢的情况，正式版本这里可以没有
                    if line[0]==c and line[1]==c and line[2]==c and line[3]==c and line[4]==c:#11111_
                        v+=4000
                    if line[6]==c and line[7]==c and line[8]==c and line[9]==c and line[10]==c:#_11111
                        v+=4000
                
                    #直接赢的情况
                    if v==0:
                        if line[1]==c and line[2]==c and line[3]==c and line[4]==c:#1111_
                            v+=3000
                        if line[6]==c and line[7]==c and line[8]==c and line[9]==c:#_1111
                            v+=3000
                
                    #如果下就赢的情况，这两种都在500以上量级
                    #4个棋
                    if v==0:
                        if line[2]==c and line[3]==c and line[4]==c and line[6]==c:#111_1
                            v+=2000
                        if line[3]==c and line[4]==c and line[6]==c and line[7]==c:#11_11
                            v+=2000
                        if line[4]==c and line[6]==c and line[7]==c and line[8]==c:#1_111
                            v+=2000
                        #要两步
                        if line[2]==c and line[3]==0 and line[4]==c and line[6]==c and line[7]==0 and line[8]==c:#101_101
                            v+=1200
                            #子类，值减半
                        if line[4]==c and line[6]==0 and line[7]==c and line[8]==c and line[9]==0 and line[10]==c:#1_10101
                            v+=600
                        if line[0]==c and line[1]==0 and line[2]==c and line[3]==0 and line[4]==c and line[6]==c:#10101_1
                            v+=600
                        if line[3]==c and line[4]==0 and line[6]==c and line[7]==c and line[8]==0 and line[9]==c and line[10]==p:#10_11012
                            v+=1200
                        if line[0]==p and line[1]==c and line[2]==0 and line[3]==c and line[4]==c and line[6]==0 and line[7]==c:#21011_01
                            v+=1200
                    
                        #3个
                        if line[1]==0 and line[2]==c and line[3]==c and line[4]==c and line[6]==0:#0111_0
                            v+=1200
                        if line[2]==0 and line[3]==c and line[4]==c and line[6]==c and line[7]==0:#011_10
                            v+=1200
                        if line[3]==0 and line[4]==c and line[6]==c and line[7]==c and line[8]==0:#01_110
                            v+=1200
                        if line[4]==0 and line[6]==c and line[7]==c and line[8]==c and line[9]==0:#0_1110
                            v+=1200
                    
                        #子类，减半
                        if line[6]==c and line[7]==0 and line[8]==c and line[9]==c and line[10]==0:#_10110
                            v+=600
                        if line[0]==0 and line[1]==c and line[2]==c and line[3]==0 and line[4]==c:#01101_
                            v+=600
                        if line[6]==c and line[7]==c and line[8]==0 and line[9]==c and line[10]==0:#_11010
                            v+=600
                        if line[0]==0 and line[1]==c and line[2]==0 and line[3]==c and line[4]==c:#01011_
                            v+=600                        
                
                    #两步内必胜情况,值定在50左右。会有更多子类,重点考虑整个数列边缘部分
                    #每个大类互相独立，优先考虑上位
                    if v==0:
                        #1个2，3个1
                        if line[1]==p and line[2]==c and line[3]==c and line[4]==c or line[0]==p and line[1]==c and line[2]==c and line[3]==c and line[4]==0 or line[6]==c and line[7]==c and line[8]==c and line[9]==p or line[6]==0 and line[7]==c and line[8]==c and line[9]==c and line[10]==p:#2111_ _
                            v+=50
                        elif line[2]==p and line[3]==c and line[4]==c and line[6]==c or line[0]==p and line[1]==c and line[2]==c and line[3]==0 and line[4]==c or line[6]==c and line[7]==0 and line[8]==c and line[9]==c and line[10]==p or line[4]==c and line[6]==c and line[7]==c and line[8]==p:#211_1_
                            v+=50
                        elif line[3]==p and line[4]==c and line[6]==c and line[7]==c or line[0]==p and line[1]==c and line[2]==0 and line[3]==c and line[4]==c or line[3]==c and line[4]==c and line[6]==c and line[7]==p or line[6]==c and line[7]==c and line[8]==0 and line[9]==c and line[10]==p:#21_11_
                            v+=50
                        elif line[3]==p and line[4]==c and line[6]==c and line[7]==0 and line[8]==c or line[1]==p and line[2]==c and line[3]==0 and line[4]==c and line[6]==c or line[2]==c and line[3]==0 and line[4]==c and line[6]==c and line[7]==p or line[4]==c and line[6]==c and line[7]==0 and line[8]==c and line[9]==p:#21_1_1
                            v+=50
                        elif line[3]==c and line[4]==c and line[6]==0 and line[7]==c or line[2]==c and line[3]==c and line[4]==0 and line[6]==c or line[3]==c and line[4]==0 and line[6]==c and line[7]==c or line[4]==c and line[6]==0 and line[7]==c and line[8]==c:#11_ _1
                            v+=50
                        elif line[3]==c and line[4]==0 and line[6]==0 and line[7]==c and line[8]==0 and line[9]==c or line[1]==c and line[2]==0 and line[3]==c and line[4]==0 and line[6]==0 and line[7]==c:#10_0101
                            v+=50
                
                        #2个1
                        elif line[3]==0 and line[4]==c and line[6]==c and line[7]==0:#01_10
                            v+=50
                        elif line[6]==c and line[7]==0 and line[8]==c and line[9]==0:#_1010
                            v+=45
                        elif line[1]==0 and line[2]==c and line[3]==0 and line[4]==c:#0101_
                            v+=45
                        elif line[6]==0 and line[7]==c and line[8]==c and line[9]==0:#_0110
                            v+=40
                        elif line[1]==0 and line[2]==c and line[3]==c and line[4]==0:#0110_
                            v+=40
                        elif line[4]==0 and line[6]==c and line[7]==c and line[8]==0:#0_110
                            v+=50
                        elif line[2]==0 and line[3]==c and line[4]==c and line[6]==0:#011_0
                            v+=50
                        elif line[3]==0 and line[4]==c and line[6]==0 and line[7]==c and line[8]==0:#01_010
                            v+=50
                        elif line[2]==0 and line[3]==c and line[4]==0 and line[6]==c and line[7]==0:#010_10
                            v+=50
                
                    #其他情况，两步内不会输
                    if v==0:
                        if line[6]==c and line[7]==c and line[8]==p or line[4]==c and line[3]==c and line[2]==p:#_112
                            v+=8
                        elif line[6]==c and line[7]==0 and line[8]==p or line[4]==c and line[3]==0 and line[2]==p:#_102
                            v+=7
                        elif line[6]==c and line[7]==0 and line[8]==p or line[4]==c and line[3]==0 and line[2]==p:#_012
                            v+=4
                        elif line[6]==c and line[7]==p or line[4]==c and line[3]==p:#_12
                            v+=6
                        elif line[4]==c or line[6]==c:#_1
                            v+=10
                        elif line[3]==c and line[4]==0 or line[6]==0 and line[7]==c:#_01
                            v+=1

                    #是否没必要
                    left=-1
                    right=12
                    for a in range(11):
                        if line[a]==p:
                            if a<5:
                                left=a
                            if a>5 and right>a:
                                right=a
                    dif=right-left
                    if dif<6 and hardness==10:
                        v=0
                    gridvalue[l]=v
                attackvalue[i][j]=sum(gridvalue)

    #extravalue:
    for i in range(num):
        for j in range(num):
            if board[i][j]==0:
                value[i][j]=defensevalue[i][j]+attackvalue[i][j]+extravalue[i][j]+round(((i+1)*(num-i)/num**2+(j+1)*(num-j)/num**2)*4+random.random(),3)
    x,y=0,0
    for i in range(num):
        for j in range(num):
            if value[i][j]>value[x][y]:
                x,y=i,j
    chess(x,y,c)

def save():
    canvas.create_text(1100,660,text='already saved with name',tag='saved1')
    canvas.create_text(1100,680,text=str(time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())),tag='saved2')
    canvas.update()
    name=str(time.strftime("%Y-%m-%d %H-%M-%S",time.localtime()))+'.txt'
    text=open(name,'a')
    text.write('mode:')
    if page==1:
        text.write('player vs computer, ')
        if c==1:
            text.write('computer is black, first 电脑先手执黑')
        else:
            text.write('player is black, first 玩家先手执黑')
        text.write('\n')
        text.write('computer level: ')
        text.write(str(hardness))
    elif page==2:
        text.write('player vs player')
    elif page==3:
        text.write('3 player')
    text.write('\n')
    if page==1 or page==2:
        text.write('step   black   white')
        text.write('\n')
        for i in range(math.floor((step)/2)):
            text.write(str(i+1))
            text.write('    ')
            text.write(str(black[i]))
            text.write('    ')
            text.write(str(white[i]))
            text.write('\n')
        if step%2==1:
            text.write(str(i+1))
            text.write('    ')
            text.write(str(black[i]))
    if page==3:
        text.write('step   red   green   blue')
        text.write('\n')
        for i in range(math.floor(step/3)):
            text.write(str(i+1))
            text.write('    ')
            text.write(str(red[i]))
            text.write('    ')
            text.write(str(green[i]))
            text.write('    ')
            text.write(str(blue[i]))
            text.write('\n')
        if step%3==1:
            text.write(str(red[i+1]))
            text.write('    ')
        elif step%3==2:
            text.write(str(red[i+1]))
            text.write('    ')            
            text.write(str(green[i+1]))
            text.write('    ')
    text.write('\n')
    text.write('\n')
    text.write('text below are for reload purpose')
    text.write('\n')
    text.write('page=')
    text.write(str(page))
    text.write(',')
    text.write('num=')
    text.write(str(num))
    text.write(',')
    text.write('stepnumber=')
    text.write(str(step))
    text.write(',')
    text.write('\n')
    if page==1:
        text.write('level=')
        text.write(str(hardness))
        text.write(',')
        text.write('player=')
        text.write(str(p))
        text.write(',')
    if page==1 or page==2:
        for i in range(math.floor((step)/2)):
            text.write('blackx')
            text.write(str(black[i][0]))
            text.write(',')
            text.write('blacky')
            text.write(str(black[i][1]))
            text.write(',')
            text.write('whitex')
            text.write(str(white[i][0]))
            text.write(',')
            text.write('whitey')
            text.write(str(white[i][1]))
            text.write(',')
        if step%2==1:
            text.write('blackx')
            text.write(str(black[i+1][0]))
            text.write(',')
            text.write('blacky')
            text.write(str(black[i+1][1]))
            text.write(',')
    if page==3:
        for i in range(math.floor((step)/3)):
            text.write('redx')
            text.write(str(red[i][0]))
            text.write(',')
            text.write('redy')
            text.write(str(red[i][1]))
            text.write(',')
            text.write('greenx')
            text.write(str(green[i][0]))
            text.write(',')
            text.write('greeny')
            text.write(str(green[i][1]))
            text.write(',')
            text.write('bluex')
            text.write(str(blue[i][0]))
            text.write(',')
            text.write('bluey')
            text.write(str(blue[i][1]))
            text.write(',')            
        if step%3==1:
            text.write('redx')
            text.write(str(red[i+1][0]))
            text.write(',')
            text.write('redy')
            text.write(str(red[i+1][1]))
            text.write(',')
        elif step%3==2:
            text.write('redx')
            text.write(str(red[i+1][0]))
            text.write(',')
            text.write('redy')
            text.write(str(red[i+1][1]))
            text.write(',')
            text.write('greenx')
            text.write(str(green[i+1][0]))
            text.write(',')
            text.write('greeny')
            text.write(str(green[i+1][1]))
            text.write(',')
    text.write('\n')
    text.write('hash value:')
    text.write('\n')
    text.close()
    text=open(name,'r')
    value=text.read()
    hashvalue=hashlib.sha3_256(value.encode('utf-8')).hexdigest()
    text.close()
    text=open(name,'a')
    text.write(str(hashvalue))
    text.close()
    time.sleep(5)
    canvas.delete('saved1')
    canvas.delete('saved2')
    canvas.update()
def regret():
    global black,white,red,green,blue,step,board,stepnum
    if page==1 or page==2:
        try:
            lastblack=black.pop()
            step-=1
            board[lastblack[0]][lastblack[1]]=0
            stepnum[lastblack[0]][lastblack[1]]=0
        except IndexError:
            pass
        try:
            lastwhite=white.pop()
            step-=1
            board[lastwhite[0]][lastwhite[1]]=0
            stepnum[lastwhite[0]][lastwhite[1]]=0
        except IndexError:
            pass
        create(num)
        for i in range(len(black)):
            put(black[i][0],black[i][1],1)
        for i in range(len(white)):
            put(white[i][0],white[i][1],2)
    elif page==3:
        try:
            lastred=red.pop()
            step-=1
            board[lastred[0]][lastred[1]]=0
            stepnum[lastred[0]][lastred[1]]=0
        except IndexError:
            pass
        try:
            lastgreen=green.pop()
            step-=1
            board[lastgreen[0]][lastgreen[1]]=0
            stepnum[lastgreen[0]][lastgreen[1]]=0
        except IndexError:
            pass
        try:
            lastblue=blue.pop()
            step-=1
            board[lastblue[0]][lastblue[1]]=0
            stepnum[lastblue[0]][lastblue[1]]=0
        except IndexError:
            pass
        create(num)
        for i in range(len(red)):
            put(red[i][0],red[i][1],3)
        for i in range(len(green)):
            put(green[i][0],green[i][1],4)
        for i in range(len(blue)):
            put(blue[i][0],blue[i][1],5)
def replay():
    global replayon
    canvas.create_text(1200,510,text='replaying...',tag='replaying1')
    canvas.create_text(1200,530,text='you shall not click anywhere',tag='replaying2')
    replayon=1
    create(num)
    canvas.update()
    time.sleep(1)
    if page==1 or page==2:
        for i in range(math.floor(step/2)):
            put(black[i][0],black[i][1],1)
            canvas.update()
            time.sleep(0.5)
            put(white[i][0],white[i][1],2)
            canvas.update()
            time.sleep(0.5)
        if step%2==1:
            put(black[i+1][0],black[i+1][1],1)
            canvas.update()
    elif page==3:
        for i in range(math.floor(step/3)):
            put(red[i][0],red[i][1],3)
            canvas.update()
            time.sleep(0.5)
            put(green[i][0],green[i][1],4)
            canvas.update()
            time.sleep(0.5)
            put(blue[i][0],blue[i][1],5)
            canvas.update()
            time.sleep(0.5)
        i+=1
        if step%3==1:
            put(red[i][0],red[i][1],3)
            canvas.update()
            time.sleep(0.5)
        elif step%3==2:
            put(red[i][0],red[i][1],3)
            canvas.update()
            time.sleep(0.5)
            put(green[i][0],green[i][1],4)
            canvas.update()
            time.sleep(0.5)
    replayon=0
    canvas.delete('replaying1','replaying2')
def shownumber():
    for i in range(num):
        for j in range(num):
            if stepnum[i][j]!=0:
                for k in range(3):
                    if board[i][j]==1:
                        canvas.create_text(l*(i+1),l*(j+1),text=stepnum[i][j],fill='#FFFFFF')
                    elif board[i][j]==2:
                        canvas.create_text(l*(i+1),l*(j+1),text=stepnum[i][j],fill='#000000')
                    elif board[i][j]==3:
                        canvas.create_text(l*(i+1),l*(j+1),text=stepnum[i][j],fill='#00FFFF')
                    elif board[i][j]==4:
                        canvas.create_text(l*(i+1),l*(j+1),text=stepnum[i][j],fill='#FF00FF')
                    elif board[i][j]==5:
                        canvas.create_text(l*(i+1),l*(j+1),text=stepnum[i][j],fill='#FFFF00')
def reload():
    global num,page,hardness,p,c,black,white,red,green,blue,step
    a=tkinter.filedialog.askopenfilename()
    file=open(a,'r')
    try:
        txt=file.read()
        hashvalue=txt[len(txt)-64:len(txt)]
        file.close()
        txt1=txt[0:len(txt)-64]
        realvalue=str(hashlib.sha3_256(txt1.encode('utf-8')).hexdigest())
        if hashvalue!=realvalue:
            canvas.create_text(900,625,text='the file has been modified or does not meet the requirement 文件已被修改或不符合')
        else:
            num=int(findnum(txt,'num='))
            playpage()
            page=int(findnum(txt,'page='))
            if page==1:
                hardness=int(findnum(txt,'level='))                
                p=int(findnum(txt,'player='))
                c=3-p
                canvas.create_text(975,300,text='level')
                canvas.create_text(1000,300,text=hardness)
            if page==1 or page==2:
                blackx=findallnumbetween(txt,'blackx',',')
                blacky=findallnumbetween(txt,'blacky',',')
                whitex=findallnumbetween(txt,'whitex',',')
                whitey=findallnumbetween(txt,'whitey',',')
                for i in range(len(whitex)):
                    chess(blackx[i],blacky[i],1)
                    chess(whitex[i],whitey[i],2)
                if int(findnum(txt,'stepnumber='))%2==1:
                    chess(blackx[i+1],blacky[i+1],1)
            elif page==3:
                redx=findallnumbetween(txt,'redx',',')
                redy=findallnumbetween(txt,'redy',',')
                greenx=findallnumbetween(txt,'greenx',',')
                greeny=findallnumbetween(txt,'greeny',',')
                bluex=findallnumbetween(txt,'bluex',',')
                bluey=findallnumbetween(txt,'bluey',',')
                for i in range(len(bluex)):
                    chess(redx[i],redy[i],3)
                    chess(greenx[i],greeny[i],4)
                    chess(bluex[i],bluey[i],5)
                if int(findnum(txt,'stepnumber='))%3==1:
                    chess(redx[i+1],redy[i+1],3)
                elif int(findnum(txt,'stepnumber='))%3==2:
                    chess(redx[i+1],redy[i+1],3)
                    chess(greenx[i+1],greeny[i+1],4)
                    
    except UnicodeDecodeError:
        canvas.create_text(900,650,text='file format error 文件格式错误')
        
canvas.pack()
window.mainloop()