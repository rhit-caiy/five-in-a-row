#coding=utf8
def grid(a):
    b=[[0 for i in range(a)] for i in range(a)]
    return b
def edge(a,b,c,d):#a数组是bxb格子周围多c格填充d
    grid=[[d for i in range(b+2*c)] for i in range(b+2*c)]
    for i in range(c,b+c):
        for j in range(c,b+c):
            grid[i][j]=a[i-c][j-c]
    return grid

from tkinter import *
import random
import time
window=Tk()
canvas=Canvas(window,bg="#FFDD44",width=1100,height=1100)
window.title('五子棋')

num=39
l=20
#num=21
#l=35
num=25
l=30

board=grid(num)
for i in range(l,(num+1)*l,l):
    canvas.create_line(l,i,num*l,i)
    canvas.create_line(i,l,i,num*l)
def chess(x,y,colour):
    board[x][y]=colour
    if colour==1:
        canvas.create_oval(l*x+0.6*l,l*y+0.6*l,l*x+1.4*l,l*y+1.4*l,fill='black')
        #black.append([x,y])
    elif colour==2:
        canvas.create_oval(l*x+0.6*l,l*y+0.6*l,l*x+1.4*l,l*y+1.4*l,fill='white')
        #white.append([x,y])
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
                        if colour==1:
                            print('black win')
                        elif colour==2:
                            print('white win')

def level(hardness,c,p):
    if hardness==0:
        lv0(hardness,c,p)
    elif hardness==1:
        lv1(hardness,c,p)
    elif hardness==2:
        lv2(hardness,c,p)
    elif hardness==3 or hardness==4:
        lv34(hardness,c,p)
    elif hardness==5 or hardness==6:
        lv56(hardness,c,p)
    elif hardness==7 or hardness==8:
        lv78(hardness,c,p)
    elif hardness==9 or hardness==10:
        lv910(hardness,c,p)

def lv0(hardness,c,p):
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
def lv1(hardness,c,p):
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
def lv2(hardness,c,p):
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
    
def lv34(hardness,c,p):
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
                            if hardness==3:
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
                                    
                            if hardness==4:
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
    
def lv56(hardness,c,p):
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
    
def lv78(hardness,c,p):
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
    
def lv910(hardness,c,p):
    newboard=edge(board,num,5,3)
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
                        v+=2000
                    if line[6]==p and line[7]==p and line[8]==p and line[9]==p and line[10]==p:#_11111
                        v+=2000
                    
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
                        v+=1000
                    if line[6]==c and line[7]==c and line[8]==c and line[9]==c and line[10]==c:#_11111
                        v+=1000
                
                    #直接赢的情况
                    if v==0:
                        if line[1]==c and line[2]==c and line[3]==c and line[4]==c:#1111_
                            v+=2000
                        if line[6]==c and line[7]==c and line[8]==c and line[9]==c:#_1111
                            v+=2000
                
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
                
                    #两步内必胜情况,值定在5000左右。会有更多子类,重点考虑整个数列边缘部分
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

computer1=1
computer2=2
hardness1=10
hardness2=10

def start(self):
    global step
    for step in range(1,201):
        if step%2==1:
            level(hardness1,computer1,computer2)
        elif step%2==0:
            level(hardness2,computer2,computer1)
        window.update()
canvas.bind("<Button-1>",start)
canvas.pack()
window.mainloop()