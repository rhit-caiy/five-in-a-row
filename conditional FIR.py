#code=utf8
from tkinter import *
window=Tk()
canvas=Canvas(window,bg="#FFDD44",width=650,height=650)
window.title('五子棋')
for i in range(50,650,50):
    canvas.create_line(50,i,600,i)
    canvas.create_line(i,50,i,600)
chessboard=[[0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0]]
x=[0]
y=[0]
step=0
reverse=0
def b(x,y):
    if reverse==1:
        x,y=y-1,x+1    
    chessboard[x+6][6-y]=1
    canvas.create_oval(50*x+330,330-50*y,50*x+370,370-50*y,fill='black')
def w(x,y):
    chessboard[x+6][6-y]=2
    canvas.create_oval(50*x+330,330-50*y,50*x+370,370-50*y,fill='white')
def position(p):
    global x,y,step,reverse
    click_x=p.x
    click_y=p.y
    ax=round(click_x/50)
    ay=round(click_y/50)
    ax,ay=ax-7,7-ay
    if chessboard[ax+6][6-ay]==0:
        step+=1
        w(ax,ay)
        if step==1 and ay-ax>1:
            reverse=1
        if reverse==1:
            ax,ay=ay-1,ax+1
        x.append(ax)
        y.append(ay)
        black()
    else:
        pass
canvas.bind("<Button-1>",position)
b(0,0)
w(1,-1)
b(-1,1)
w(-2,2)
b(-1,0)
def black():
    #(1,2)
    if x[1]==1 and y[1]==2:
        b(1,0)
        if x[2]==2 and y[2]==0:
            b(-1,2)
            if x[3]==-1 and y[3]==3:
                b(-2,0)
                if x[4]==-3 and y[4]==0:
                    b(0,1)
                    if x[5]==2 and y[5]==-1 or x[5]==-2 and y[5]==3:
                        b(0,2)
                        if x[6]==0 and y[6]==3 or x[6]==0 and y[6]==-1 or x[6]==0 and y[6]==4:
                            b(1,3)
                            if x[7]==2 and y[7]==4:
                                b(-3,-1)#
                            else:
                                b(2,4)#
                        else:
                            b(0,3)
                            if x[7]==0 and y[7]==4:
                                b(0,-1)#
                            else:
                                b(0,4)#
                    elif x[5]==3 and y[5]==-2:
                        b(-2,3)
                        if x[6]==-3 and y[6]==4:
                            b(2,-1)#
                        else:
                            b(-3,4)#
                    else:
                        b(2,-1)
                        if x[6]==3 and y[6]==-2:
                            b(-2,3)#
                        else:
                            b(3,-2)#
                else:
                    b(-3,0)#
            elif x[3]==-1 and y[3]==-1:
                b(-3,0)
                if x[4]==-2 and y[4]==0:
                    b(-2,1)
                    if x[5]==1 and y[5]==4 or x[5]==0 and y[5]==3 or x[5]==-4 and y[5]==-1:
                        b(0,1)
                        if x[6]==2 and y[6]==-1 or x[6]==3 and y[6]==-2 or x[6]==-2 and y[6]==3:
                            b(1,1)
                            if x[7]==2 and y[7]==1:
                                b(-3,1)#
                            else:
                                b(2,1)#
                        else:
                            b(2,-1)
                            if x[7]==-2 and y[7]==3:
                                b(3,-2)#
                            else:
                                b(-2,3)#
                    else:
                        b(0,3)
                        if x[6]==-4 and y[6]==-1:
                            b(1,4)#
                        else:
                            b(-4,-1)#
                else:
                    b(-2,0)#
            elif x[3]==-1 and y[3]==-2:
                b(-1,3)
                if x[4]==-1 and y[4]==4:
                    b(-1,-1)#
                else:
                    b(-1,4)#
            else:
                b(-1,-1)
                if x[4]==-1 and y[4]==3:
                    b(-1,-2)#
                else:
                    b(-1,3)#
        elif x[2]==-2 and y[2]==0:
            b(-1,2)
            if x[3]==-1 and y[3]==3:
                b(-1,-2)
                if x[4]==-1 and y[4]==-1:
                    b(0,-1)
                    if x[5]==-2 and y[5]==-3 or x[5]==2 and y[5]==1 or x[5]==3 and y[5]==2:
                        b(0,1)
                        if x[6]==2 and y[6]==-1 or x[6]==-2 and y[6]==-3 or x[6]==-3 and y[6]==-4:
                            b(0,-2)
                            if x[7]==0 and y[7]==2:
                                b(0,-3)#
                            else:
                                b(0,2)#
                        else:
                            b(-2,3)
                            if x[7]==2 and y[7]==-1:
                                b(-3,4)#
                            else:
                                b(2,-1)#
                    else:
                        b(2,1)
                        if x[6]==3 and y[6]==2:
                            b(-2,-3)#
                        else:
                            b(3,2)#
                else:
                    b(-1,-1)#
            elif x[3]==-1 and y[3]==-1:
                b(2,0)
                if x[4]==3 and y[4]==0:
                    b(-1,3)
                    if x[5]==-1 and y[5]==4:
                        b(0,2)
                        if x[6]==1 and y[6]==1:
                            b(0,1)
                            if x[7]==2 and y[7]==-1 or x[7]==3 and y[7]==-2 or x[7]==-2 and y[7]==3:
                                b(0,-1)
                                if x[8]==0 and y[8]==-2:
                                    b(0,3)#
                                else:
                                    b(0,-2)#
                            else:
                                b(2,-1)
                                if x[8]==3 and y[8]==-2:
                                    b(-2,3)#
                                else:
                                    b(3,-2)#
                        elif x[6]==3 and y[6]==-1 or x[6]==-2 and y[6]==4:
                            b(1,1)
                            if x[7]==3 and y[7]==-1 or x[7]==-2 and y[7]==4:
                                b(0,1)
                                if x[8]==-2 and y[8]==3:
                                    b(-2,1)
                                    if x[9]==2 and y[9]==1:
                                        b(-3,1)#
                                    else:
                                        b(2,1)#
                                elif x[8]==-2 and y[8]==1:
                                    b(-2,3)
                                    if x[9]==2 and y[9]==-1:
                                        b(-3,4)#
                                    else:
                                        b(2,-1)#
                                elif x[8]==2 and y[8]==-1:
                                    b(0,-1)
                                    if x[9]==0 and y[9]==3:
                                        b(0,-2)#
                                    else:
                                        b(0,3)#
                                elif x[8]==0 and y[8]==-1:
                                    b(2,-1)
                                    if x[9]==-2 and y[9]==3:
                                        b(3,-2)#
                                    else:
                                        b(-2,3)#
                                elif x[8]==2 and y[8]==1:
                                    b(0,3)
                                    if x[9]==0 and y[9]==4:
                                        b(0,-1)#
                                    else:
                                        b(0,4)#
                                elif x[8]==0 and y[8]==3:
                                    b(2,1)
                                    if x[9]==3 and y[9]==1:
                                        b(-2,1)#
                                    else:
                                        b(3,1)#
                                elif x[8]==3 and y[8]==-2:
                                    b(2,1)
                                    if x[9]==3 and y[9]==1:
                                        b(-2,1)#
                                    else:
                                        b(3,1)#
                                else:
                                    b(2,-1)
                                    if x[9]==-2 and y[9]==3:
                                        b(3,-2)#
                                    else:
                                        b(-2,3)#
                            elif x[6]!=3:
                                b(3,-1)#
                            else:
                                b(-2,4)#
                        elif x[6]==2 and y[6]==1:
                            b(0,3)
                            if x[7]==4 and y[7]==-1:
                                b(5,-2)
                                if x[8]==1 and y[8]==1 or x[8]==-2 and y[8]==4 or x[8]==3 and y[8]==-1:
                                    b(0,1)
                                    if x[9]==0 and y[9]==-1:
                                        b(0,4)#
                                    else:
                                        b(0,-1)#
                                else:
                                    b(1,1)
                                    if x[9]==3 and y[9]==-1:
                                        b(-2,4)#
                                    else:
                                        b(3,-1)# 
                            elif x[7]==1 and y[7]==1 or x[7]==-2 and y[7]==4 or x[7]==3 and y[7]==-1:
                                b(0,1)
                                if x[8]==0 and y[8]==-1:
                                    b(0,4)#
                                else:
                                    b(0,-1)#
                            else:
                                b(1,1)
                                if x[8]==3 and y[8]==-1:
                                    b(-2,4)#
                                else:
                                    b(3,-1)#
                        elif x[6]==0 and y[6]==3:
                            b(2,1)
                            if x[7]==-2 and y[7]==5:
                                b(-3,6)
                                if x[8]==1 and y[8]==1:
                                    b(2,-1)
                                    if x[9]==-2 and y[9]==3 or x[9]==0 and y[9]==1 or x[9]==3 and y[9]==-2:
                                        b(2,2)
                                        if x[10]==2 and y[10]==-2:
                                            b(2,3)#
                                        else:
                                            b(2,-2)#
                                    else:
                                        b(0,1)
                                        if x[10]==3 and y[10]==-2:
                                            b(-2,3)#
                                        else:
                                            b(3,-2)#
                                elif x[8]==3 and y[8]==-1 or x[8]==-2 and y[8]==4:
                                    b(1,1)
                                    if x[9]==3 and y[9]==-1 or x[9]==-2 and y[9]==4:
                                        b(0,1)
                                        if x[10]==-2 and y[10]==1:
                                            b(3,1)#
                                        else:
                                            b(-2,1)#
                                    elif x[8]==3:
                                        b(-2,4)#
                                    else:
                                        b(3,-1)#
                                else:
                                    b(1,1)
                                    if x[9]==3 and y[9]==-1:
                                        b(-2,4)#
                                    else:
                                        b(3,-1)#
                            elif x[7]==1 and y[7]==1:
                                b(2,-1)
                                if x[8]==-2 and y[8]==5:
                                    b(-3,6)
                                    if x[9]==-2 and y[9]==3 or x[9]==0 and y[9]==1 or x[9]==3 and y[9]==-2:
                                        b(2,2)
                                        if x[10]==2 and y[10]==-2:
                                            b(2,3)#
                                        else:
                                            b(2,-2)#
                                    else:
                                        b(0,1)
                                        if x[10]==3 and y[10]==-2:
                                            b(-2,3)#
                                        else:
                                            b(3,-2)#
                                elif x[8]==-2 and y[8]==3 or x[8]==0 and y[8]==1 or x[8]==3 and y[8]==-2:
                                    b(2,2)
                                    if x[9]==2 and y[9]==-2:
                                        b(2,3)#
                                    else:
                                        b(2,-2)#
                                else:
                                    b(0,1)
                                    if x[9]==3 and y[9]==-2:
                                        b(-2,3)#
                                    else:
                                        b(3,-2)#
                            elif x[7]==3 and y[7]==-1 or x[7]==-2 and y[7]==4:
                                b(1,1)
                                if x[8]==3 and y[8]==-1 or x[8]==-2 and y[8]==4:
                                    b(0,1)
                                    if x[9]==-2 and y[8]==1:
                                        b(3,1)#
                                    else:
                                        b(-2,1)#
                                elif x[7]==3:
                                    b(-2,4)#
                                else:
                                    b(3,-1)#
                            else:
                                b(1,1)
                                if x[8]==3 and y[8]==-1:
                                    b(-2,4)#
                                else:
                                    b(3,-1)#
                        else:
                            b(1,1)
                            if x[7]==3 and y[7]==-1:
                                b(-2,4)#
                            else:
                                b(3,-1)#
                    else:
                        b(-1,4)#
                else:
                    b(3,0)#
            elif x[3]==-1 and y[3]==-2:
                b(-1,3)
                if x[4]==-1 and y[4]==4:
                    b(-1,-1)#
                else:
                    b(-1,4)#
            else:
                b(-1,-1)
                if x[4]==-1 and y[4]==-2:
                    b(-1,3)#
                else:
                    b(-1,-2)#
        elif x[2]==-3 and y[2]==0:
            b(2,0)
            if x[3]==3 and y[3]==0:
                b(-2,0)#
            else:
                b(3,0)#
        else:
            b(-2,0)
            if x[3]==2 and y[3]==0:
                b(-3,0)#
            else:
                b(2,0)#
    #(0,1)
    elif x[1]==0 and y[1]==1:
        b(-2,0)
        if x[2]==1 and y[2]==0:
            b(-1,2)
            if x[3]==-1 and y[3]==-1:
                b(-1,3)
                if x[4]==-1 and y[4]==4:
                    b(-3,0)
                    if x[5]==-4 and y[5]==0:
                        b(0,3)
                        if x[6]==1 and y[6]==4 or x[6]==-2 and y[6]==1 or x[6]==-4 and y[6]==-1:
                            b(1,3)
                            if x[7]==2 and y[7]==3 or x[7]==-2 and y[7]==3 or x[7]==3 and y[7]==3:
                                b(0,2)
                                if x[8]==2 and y[8]==4:
                                    b(-3,-1)#
                                else:
                                    b(2,4)#
                            else:
                                b(2,3)
                                if x[8]==3 and y[8]==3:
                                    b(-2,3)#
                                else:
                                    b(3,3)#
                        else:
                            b(-2,1)
                            if x[7]==1 and y[7]==4:
                                b(-4,-1)#
                            else:
                                b(1,4)#
                    else:
                        b(-4,0)#
                else:
                    b(-1,4)#
            elif x[3]==-1 and y[3]==3:
                b(-1,-1)
                if x[4]==-1 and y[4]==-2:
                    b(-3,0)
                    if x[5]==-4 and y[5]==0:
                        b(-3,1)
                        if x[6]==0 and y[6]==-2 or x[6]==-4 and y[6]==2:
                            b(-3,-1)
                            if x[7]==-3 and y[7]==3 or x[7]==-3 and y[7]==-2 or x[7]==-3 and y[7]==2:
                                b(0,2)
                                if x[8]==1 and y[8]==3:
                                    b(-4,-2)#
                                else:
                                    b(1,3)#
                            else:
                                b(-3,2)
                                if x[8]==-3 and y[8]==3:
                                    b(-3,-2)#
                                else:
                                    b(-3,3)#
                        elif x[6]==1 and y[6]==-3:
                            b(-4,2)
                            if x[7]==0 and y[7]==-2:
                                b(-5,3)#
                            else:
                                b(0,-2)#
                        else:
                            b(0,-2)
                            if x[7]==-4 and y[7]==2:
                                b(1,-3)#
                            else:
                                b(-4,2)#
                    else:
                        b(-4,0)#
                else:
                    b(-1,-2)#
            elif x[3]==-1 and y[3]==4:
                b(-1,-1)
                if x[4]==-1 and y[4]==3:
                    b(-1,-2)#
                else:
                    b(-1,3)#
            else:
                b(-1,3)
                if x[4]==-1 and y[4]==4:
                    b(-1,-1)#
                else:
                    b(-1,4)#
        elif x[2]==-3 and y[2]==0:
            b(-1,-1)
            if x[3]==-1 and y[3]==2:
                b(-1,-3)
                if x[4]==-1 and y[4]==-2:
                    b(-2,-2)
                    if x[5]==1 and y[5]==1 or x[5]==-3 and y[5]==-3:
                        b(-3,-1)
                        if x[6]==0 and y[6]==2 or x[6]==1 and y[6]==3 or x[6]==-4 and y[6]==-2:
                            b(-4,0)
                            if x[7]==-5 and y[7]==1:
                                b(0,-4)#
                            else:
                                b(-5,1)#
                        else:
                            b(0,2)
                            if x[7]==1 and y[7]==3:
                                b(-4,-2)#
                            else:
                                b(1,3)#
                    elif x[5]==2 and y[5]==2:
                        b(-3,-3)
                        if x[6]==1 and y[6]==1:
                            b(-4,-4)#
                        else:
                            b(1,1)#
                    else:
                        b(1,1)
                        if x[6]==2 and y[6]==2:
                            b(-3,-3)#
                        else:
                            b(2,2)#
                else:
                    b(-1,-2)#
            elif x[3]==-1 and y[3]==-2:
                b(1,1)
                if x[4]==2 and y[4]==2 or x[4]==-2 and y[4]==-2:
                    b(-1,3)
                    if x[5]==-1 and y[5]==2:
                        b(2,0)
                        if x[6]==1 and y[6]==0:
                            b(0,2)
                            if x[7]==3 and y[7]==-1:
                                b(-2,4)#
                            else:
                                b(3,-1)#
                        else:
                            b(1,0)#
                    else:
                        b(-1,2)#
                elif x[4]==3 and y[4]==3:
                    b(-2,-2)
                    if x[5]==2 and y[5]==2:
                        b(-3,-3)#
                    else:
                        b(2,2)#
                else:
                    b(2,2)
                    if x[5]==3 and y[5]==3:
                        b(-2,-2)#
                    else:
                        b(3,3)#
            elif x[3]==-1 and y[3]==-3:
                b(-1,2)
                if x[4]==-1 and y[4]==-2:
                    b(-1,3)#
                else:
                    b(-1,-2)#
            else:
                b(-1,-2)
                if x[4]==-1 and y[4]==-3:
                    b(-1,2)#
                else:
                    b(-1,-3)#
        elif x[2]==2 and y[2]==0:
            b(-3,0)
            if x[3]==1 and y[3]==0:
                b(-4,0)#
            else:
                b(1,0)#
        else:
            b(1,0)
            if x[3]==2 and y[3]==0:
                b(-3,0)#
            else:
                b(2,0)#
    #(1,1)
    if x[1]==1 and y[1]==1:
        b(-1,-2)
        if x[2]==-1 and y[2]==2 or x[2]==-1 and y[2]==-1:
            b(1,0)
            if x[3]==2 and y[3]==0 or x[3]==-2 and y[3]==0:
                b(0,-1)
                if x[4]==2 and y[4]==1 or x[4]==-2 and y[4]==-3:
                    b(0,-2)
                    if x[5]==0 and y[5]==1 or x[5]==0 and y[5]==-3:
                        b(1,-2)
                        if x[6]==2 and y[6]==-2 or x[6]==-2 and y[6]==-2 or x[6]==3 and y[6]==-2:
                            b(-2,1)
                            if x[7]==-3 and y[7]==2:
                                b(2,-3)#
                            else:
                                b(-3,2)#
                        elif x[6]==3 and y[6]==1:
                            b(4,1)
                            if x[7]==2 and y[7]==-2 or x[7]==-2 and y[7]==-2 or x[7]==3 and y[7]==-2:
                                b(-2,1)
                                if x[8]==-3 and y[8]==2:
                                    b(2,-3)#
                                else:
                                    b(-3,2)#
                            else:
                                b(2,-2)
                                if x[8]==3 and y[8]==-2:
                                    b(-2,-2)#
                                else:
                                    b(3,-2)#
                        elif x[6]==4 and y[6]==1:
                            b(3,1)
                            if x[7]==2 and y[7]==-2 or x[7]==-2 and y[7]==-2 or x[7]==3 and y[7]==-2:
                                b(-2,1)
                                if x[8]==-3 and y[8]==2:
                                    b(2,-3)#
                                else:
                                    b(-3,2)#
                            else:
                                b(2,-2)
                                if x[8]==3 and y[8]==-2:
                                    b(-2,-2)#
                                else:
                                    b(3,-2)#
                        else:
                            b(2,-2)
                            if x[7]==3 and y[7]==-2:
                                b(-2,-2)#
                            else:
                                b(3,-2)#
                    elif x[5]==0 and y[5]==2:
                        b(0,-3)
                        if x[6]==0 and y[6]==1:
                            b(0,-4)#
                        else:
                            b(0,1)#
                    else:
                        b(0,1)
                        if x[6]==0 and y[6]==2:
                            b(0,-3)#
                        else:
                            b(0,2)#
                elif x[4]==3 and y[4]==2:
                    b(-2,-3)
                    if x[5]==2 and y[5]==1:
                        b(-3,-4)#
                    else:
                        b(2,1)#
                else:
                    b(2,1)
                    if x[5]==3 and y[5]==2:
                        b(-2,-3)#
                    else:
                        b(3,2)#
            elif x[3]==3 and y[3]==0:
                b(-2,0)
                if x[4]==2 and y[4]==0:
                    b(-3,0)#
                else:
                    b(2,0)#
            else:
                b(2,0)
                if x[4]==3 and y[4]==0:
                    b(-2,0)#
                else:
                    b(3,0)#
        elif x[2]==-1 and y[2]==-3:
            b(0,-2)
            if x[3]==0 and y[3]==-1:
                b(-1,-1)
                if x[4]==-1 and y[4]==2:
                    b(-2,0)
                    if x[5]==2 and y[5]==0 or x[5]==1 and y[5]==0 or x[5]==-3 and y[5]==0:
                        b(-3,1)
                        if x[6]==-4 and y[6]==2:
                            b(1,-3)#
                        else:
                            b(-4,2)#
                    else:
                        b(1,0)
                        if x[6]==2 and y[6]==0:
                            b(-3,0)#
                        else:
                            b(2,0)#
                else:
                    b(-1,2)#
            elif x[3]==1 and y[3]==0:
                b(1,-2)
                if x[4]==1 and y[4]==2:
                    b(1,3)
                    if x[5]==2 and y[5]==-2 or x[5]==-2 and y[5]==-2:
                        b(0,-1)
                        if x[6]==-2 and y[6]==1 or x[6]==2 and y[6]==-3 or x[6]==-3 and y[6]==2:
                            b(0,-3)
                            if x[7]==0 and y[7]==1:
                                b(0,-4)#
                            else:
                                b(0,1)#
                        else:
                            b(-2,1)
                            if x[7]==-3 and y[7]==2:
                                b(2,-3)#
                            else:
                                b(-3,2)#
                    elif x[5]==3 and y[5]==-2:
                        b(-2,-2)
                        if x[6]==-3 and y[6]==-2:
                            b(2,-2)#
                        else:
                            b(-3,-2)#
                    else:
                        b(2,-2)
                        if x[6]==3 and y[6]==-2:
                            b(-2,-2)#
                        else:
                            b(3,-2)#
                elif x[4]==1 and y[4]==3:
                    b(1,2)
                    if x[5]==2 and y[5]==-2 or x[5]==-2 and y[5]==-2:
                        b(0,-1)
                        if x[6]==-2 and y[6]==1 or x[6]==2 and y[6]==-3 or x[6]==-3 and y[6]==2:
                            b(0,-3)
                            if x[7]==0 and y[7]==1:
                                b(0,-4)#
                            else:
                                b(0,1)#
                        else:
                            b(-2,1)
                            if x[7]==-3 and y[7]==2:
                                b(2,-3)#
                            else:
                                b(-3,2)#
                    elif x[5]==3 and y[5]==-2:
                        b(-2,-2)
                        if x[6]==-3 and y[6]==-2:
                            b(2,-2)#
                        else:
                            b(-3,-2)#
                    else:
                        b(2,-2)
                        if x[6]==3 and y[6]==-2:
                            b(-2,-2)#
                        else:
                            b(3,-2)#
                elif x[4]==2 and y[4]==-2 or x[4]==-2 and y[4]==-2:
                    b(0,-1)
                    if x[5]==1 and y[5]==2:
                        b(1,3)
                        if x[6]==-2 and y[6]==1 or x[6]==2 and y[6]==-3 or x[6]==-3 and y[6]==2:
                            b(0,-3)
                            if x[7]==0 and y[7]==1:
                                b(0,-4)#
                            else:
                                b(0,1)#
                        else:
                            b(-2,1)
                            if x[7]==-3 and y[7]==2:
                                b(2,-3)#
                            else:
                                b(-3,2)#
                    elif x[5]==1 and y[5]==3:
                        b(1,2)                    
                        if x[6]==-2 and y[6]==1 or x[6]==2 and y[6]==-3 or x[6]==-3 and y[6]==2:
                            b(0,-3)
                            if x[7]==0 and y[7]==1:
                                b(0,-4)#
                            else:
                                b(0,1)#
                        else:
                            b(-2,1)
                            if x[7]==-3 and y[7]==2:
                                b(2,-3)#
                            else:
                                b(-3,2)#
                    elif x[5]==-2 and y[5]==1 or x[5]==2 and y[5]==-3 or x[5]==-3 and y[5]==2:
                        b(0,-3)
                        if x[6]==0 and y[6]==1:
                            b(0,-4)#
                        else:
                            b(0,1)#
                    else:
                        b(-2,1)
                        if x[6]==-3 and y[6]==2:
                            b(2,-3)#
                        else:
                            b(-3,2)#
                elif x[4]==3 and y[4]==-2:
                    b(-2,-2)
                    if x[5]==-3 and y[5]==-2:
                        b(2,-2)#
                    else:
                        b(-3,-2)#
                else:
                    b(2,-2)
                    if x[5]==3 and y[5]==-2:
                        b(-2,-2)#
                    else:
                        b(3,-2)#
            elif x[3]==1 and y[3]==-2 or x[3]==1 and y[3]==2 or x[3]==1 and y[3]==3 or x[3]==1 and y[3]==-3 or x[3]==-1 and y[3]==2 or x[3]==-3 and y[3]==0 or x[3]==-4 and y[3]==0 or x[3]==-1 and y[3]==-1 or x[3]==-3 and y[3]==1 or x[3]==-4 and y[3]==2 or x[3]==1 and y[3]==-3:
                b(1,0)
                if x[4]==2 and y[4]==0 or x[4]==-2 and y[4]==0:
                    b(0,-1)
                    if x[5]==0 and y[5]==1 or x[5]==0 and y[5]==-3 or x[5]==0 and y[5]==2:
                        b(2,1)
                        if x[6]==3 and y[6]==2:
                            b(2,-3)#
                        else:
                            b(3,2)#
                    else:
                        b(0,1)
                        if x[6]==0 and y[6]==2:
                            b(0,-3)#
                        else:
                            b(0,2)#
                elif x[4]==3 and y[4]==0:
                    b(-2,0)
                    if x[5]==2 and y[5]==0:
                        b(-3,0)#
                    else:
                        b(2,0)#
                else:
                    b(2,0)
                    if x[5]==3 and y[5]==0:
                        b(-2,0)#
                    else:
                        b(3,0)#
            else:
                b(-2,0)
                if x[4]==1 and y[4]==0 or x[4]==-3 and y[4]==0 or x[4]==-4 and y[4]==0 and x[3]==2 and y[3]==0:
                    b(-1,-1)
                    if x[5]==-1 and y[5]==2:
                        b(-3,1)
                        if x[6]==-4 and y[6]==2:
                            b(1,-3)#
                        else:
                            b(-4,2)#
                    else:
                        b(-1,2)#
                elif x[4]==2 and y[4]==0:
                    b(-3,0)
                    if x[5]==1 and y[5]==0:
                        b(-4,0)#
                    else:
                        b(1,0)#
                else:
                    b(-3,0)
                    if x[5]==-4 and y[5]==0:
                        b(1,0)#
                    else:
                        b(-4,0)#
        else:
            b(-1,-1)
            if x[3]==-1 and y[3]==2:
                b(-1,-3)#
            else:
                b(-1,2)#
    #(1,0)
    if x[1]==1 and y[1]==0:
        b(-1,-1)
        if x[2]==-1 and y[2]==-2:
            b(-1,3)
            if x[3]==-1 and y[3]==2:
                b(1,1)
                if x[4]==2 and y[4]==2 or x[4]==-2 and y[4]==-2:
                    b(0,2)
                    if x[5]==2 and y[5]==0 or x[5]==-2 and y[5]==4:
                        b(0,1)
                        if x[6]==0 and y[6]==-1 or x[6]==0 and y[6]==3 or x[6]==0 and y[6]==4:
                            b(2,1)
                            if x[7]==3 and y[7]==1:
                                b(-2,1)#
                            else:
                                b(3,1)#
                        else:
                            b(0,3)
                            if x[7]==0 and y[7]==-1:
                                b(0,4)#
                            else:
                                b(0,-1)#
                    elif x[5]==3 and y[5]==-1:
                        b(-2,4)
                        if x[6]==-3 and y[6]==5:
                            b(2,0)#
                        else:
                            b(-3,5)#
                    else:
                        b(2,0)
                        if x[6]==3 and y[6]==-1:
                            b(-2,4)#
                        else:
                            b(3,-1)#
                elif x[4]==3 and y[4]==3:
                    b(-2,-2)
                    if x[5]==-3 and y[5]==-3:
                        b(2,2)#
                    else:
                        b(-3,-3)#
                else:
                    b(2,2)
                    if x[5]==3 and y[5]==3:
                        b(-2,-2)#
                    else:
                        b(3,3)#
            else:
                b(-1,2)#
        elif x[2]==-1 and y[2]==2:
            b(1,1)
            if x[3]==2 and y[3]==2:
                b(-2,-2)
                if x[4]==-3 and y[4]==-3:
                    b(0,1)
                    if x[5]==0 and y[5]==2:
                        b(1,2)
                        if x[6]==-3 and y[6]==2:
                            b(-4,2)
                            if y[7]==1:
                                b(-2,-1)
                                if x[8]==-3 and y[8]==-2:
                                    b(2,3)#
                                else:
                                    b(-3,-2)#
                            else:
                                b(-2,1)
                                if x[8]==-3 and y[8]==1:
                                    b(2,1)#
                                else:
                                    b(-3,1)#
                        elif x[6]==-4 and y[6]==2:
                            b(-3,2)
                            if y[7]==1:
                                b(-2,-1)
                                if x[8]==-3 and y[8]==-2:
                                    b(2,3)#
                                else:
                                    b(-3,-2)#
                            else:
                                b(-2,1)
                                if x[8]==-3 and y[8]==1:
                                    b(2,1)#
                                else:
                                    b(-3,1)#
                        elif y[6]==1:
                            b(-2,-1)
                            if x[7]==-3 and y[7]==-2:
                                b(2,3)#
                            else:
                                b(-3,-2)#
                        else:
                            b(-2,1)
                            if x[7]==-3 and y[7]==1:
                                b(2,1)#
                            else:
                                b(-3,1)#
                    elif x[5]==1 and y[5]==2:
                        b(0,2)
                        if y[6]==1:
                            b(0,3)
                            if x[7]==0 and y[7]==4:
                                b(0,-1)#
                            else:
                                b(0,4)#
                        else:
                            b(2,1)
                            if x[7]==3 and y[7]==1:
                                b(-2,1)#
                            else:
                                b(3,1)#
                    elif x[5]==2 and y[5]==1 or x[5]==-2 and y[5]==1:
                        b(-1,-2)
                        if x[6]==-1 and y[6]==-3:
                            b(0,-2)
                            if x[7]==0 and y[7]==2:
                                b(1,2)
                                if x[8]==-3 and y[8]==2:
                                    b(-4,2)
                                    if x[9]==2 and y[9]==3 or x[9]==-2 and y[9]==-1 or x[9]==3 and y[9]==4:
                                        b(-3,-2)
                                        if x[10]==-4 and y[10]==-2:
                                            b(1,-2)#
                                        else:
                                            b(-4,-2)#
                                    else:
                                        b(2,3)
                                        if x[10]==3 and y[10]==4:
                                            b(-2,-1)#
                                        else:
                                            b(3,4)#
                                elif x[8]==-4 and y[8]==2:
                                    b(-3,2)
                                    if x[9]==2 and y[9]==3 or x[9]==-2 and y[9]==-1 or x[9]==3 and y[9]==4:
                                        b(-3,-2)
                                        if x[10]==-4 and y[10]==-2:
                                            b(1,-2)#
                                        else:
                                            b(-4,-2)#
                                    else:
                                        b(2,3)
                                        if x[10]==3 and y[10]==4:
                                            b(-2,-1)#
                                        else:
                                            b(3,4)#
                                elif x[8]==2 and y[8]==3 or x[8]==-2 and y[8]==-1 or x[8]==3 and y[8]==4:
                                    b(-3,-2)
                                    if x[9]==-4 and y[9]==-2:
                                        b(1,-2)#
                                    else:
                                        b(-4,-2)#
                                else:
                                    b(2,3)
                                    if x[9]==3 and y[9]==4:
                                        b(-2,-1)#
                                    else:
                                        b(3,4)#
                            elif x[7]==1 and y[7]==2:
                                b(0,2)
                                if x[8]==0 and y[8]==-1:
                                    b(1,-2)
                                    if x[9]==2 and y[9]==-2:
                                        b(-3,-2)#
                                    else:
                                        b(2,-2)#
                                else:
                                    b(0,-1)#
                            elif x[7]==0:
                                b(1,-2)
                                if x[8]==2 and y[8]==-2:
                                    b(-3,-2)#
                                else:
                                    b(2,-2)#
                            else:
                                b(0,-1)
                                if x[8]==0 and y[8]==2:
                                    b(0,-3)#
                                else:
                                    b(0,2)#
                        else:
                            b(-1,-3)#
                    elif x[5]==3 and y[5]==1:
                        b(-2,1)
                        if x[6]==-3 and y[6]==1:
                            b(2,1)#
                        else:
                            b(-3,1)#
                    else:
                        b(2,1)
                        if x[6]==3 and y[6]==1:
                             b(-2,1)#
                        else:
                            b(3,1)#
                else:
                    b(-3,-3)#
            elif x[3]==-2 and y[3]==-2:
                b(2,2)
                if x[4]==3 and y[4]==3:
                    b(0,1)
                    if x[5]==2 and y[5]==1:
                        b(-2,1)
                        if x[6]==-3 and y[6]==1:
                            b(-2,-1)
                            if x[7]==1 and y[7]==2 or x[7]==-3 and y[7]==-2:
                                b(0,-1)
                                if x[8]==0 and y[8]==2 or x[8]==0 and y[8]==3 or x[8]==0 and y[8]==-2:
                                    b(-3,2)
                                    if x[9]==1 and y[9]==-2:
                                        b(-4,3)#
                                    else:
                                        b(1,-2)#
                                else:
                                    b(0,2)
                                    if x[9]==0 and y[9]==-2:
                                        b(0,3)#
                                    else:
                                        b(0,-2)#
                            elif x[7]==2 and y[7]==3:
                                b(-3,-2)
                                if x[8]==-4 and y[8]==-3:
                                    b(1,2)#
                                else:
                                    b(-4,-3)#
                            else:
                                b(1,2)
                                if x[8]==2 and y[8]==3:
                                    b(-3,-2)#
                                else:
                                    b(2,3)#
                        else:
                            b(-3,-1)#
                    elif x[5]==-2 and y[5]==1:
                        b(2,1)
                        if x[6]==3 and y[6]==1:
                            b(1,2)
                            if x[7]==-2 and y[7]==-1:
                                b(-2,0)
                                if x[8]>1:
                                    b(0,-2)
                                    if x[9]==0 and y[9]==2 or x[9]==0 and y[9]==-3 or x[9]==0 and y[9]==-1:
                                        b(-3,1)
                                        if x[10]==-4 and y[10]==2:
                                            b(1,-3)#
                                        else:
                                            b(-4,2)#
                                    else:
                                        b(0,-1)
                                        if x[10]==0 and y[10]==2:
                                            b(0,-3)#
                                        else:
                                            b(0,2)#
                                else:
                                    b(2,3)
                                    if x[9]==3 and y[9]==4:
                                        b(2,4)
                                        if x[10]==2 and y[10]==5:
                                            b(2,0)#
                                        else:
                                            b(2,5)#
                                    else:
                                        b(3,4)#
                            elif x[7]==-2 and y[7]==0:
                                b(-2,-1)
                                if x[8]==2 and y[8]==3:
                                    b(-3,-2)#
                                else:
                                    b(2,3)#
                            elif x[7]==2 and y[7]==3:
                                b(0,3)
                                if x[8]==-2 and y[8]==0:
                                    b(-2,-1)
                                    if x[9]==-3 and y[9]==-2:
                                        b(0,2)
                                        if x[10]==0 and y[10]==-1:
                                            b(0,4)#
                                        else:
                                            b(0,-1)#
                                    else:
                                        b(-3,-2)#
                                elif x[8]==-2 and y[8]==-1:
                                    b(-2,0)
                                    if x[9]==0 and y[9]==-1 or x[9]==0 and y[9]==2 or x[9]==0 and y[9]==4:
                                        b(3,0)
                                        if x[10]==-1 and y[10]==4:
                                            b(4,-1)#
                                        else:
                                            b(-1,4)#
                                    else:
                                        b(0,2)
                                        if x[10]==0 and y[10]==-1:
                                            b(0,4)#
                                        else:
                                            b(0,-1)#
                                elif x[8]==0 and y[8]==-1 or x[8]==0 and y[8]==2 or x[8]==0 and y[8]==4:
                                    b(3,0)
                                    if x[9]==-1 and y[9]==4:
                                        b(4,-1)#
                                    else:
                                        b(-1,4)#
                                else:
                                    b(0,2)
                                    if x[9]==0 and y[9]==-1:
                                        b(0,4)#
                                    else:
                                        b(0,-1)#
                            elif x[7]==3 and y[7]==4:
                                b(-2,-1)
                                if x[8]==-3 and y[8]==-2:
                                    b(2,3)#
                                else:
                                    b(-3,-2)#
                            else:
                                b(2,3)
                                if x[8]==3 and y[8]==4:
                                    b(-2,-1)#
                                else:
                                    b(3,4)#
                        else:
                            b(3,1)#
                    elif x[5]==3 and y[5]==1:
                        b(-2,1)
                        if x[6]==-3 and y[6]==1:
                            b(2,1)#
                        else:
                            b(-3,1)#
                    else:
                        b(2,1)
                        if x[6]==3 and y[6]==1:
                            b(-2,1)#
                        else:
                            b(3,1)#
                else:
                    b(3,3)#
            elif x[3]==3 and y[3]==3:
                b(-2,-2)
                if x[4]==-3 and y[4]==-3:
                    b(2,2)#
                else:
                    b(-3,-3)#
            else:
                b(2,2)
                if x[4]==3 and y[4]==3:
                    b(-2,-2)#
                else:
                    b(3,3)#
        elif x[2]==-1 and y[2]==3:
            b(-1,-2)
            if x[3]==-1 and y[3]==-3:
                b(-1,2)#
            else:
                b(-1,-3)#
        else:
            b(-1,2)
            if x[3]==-1 and y[3]==3:
                b(-1,-2)#
            else:
                b(-1,3)#
    #(0,-1)
    if x[1]==0 and y[1]==-1:
        b(-2,0)
        if x[2]==1 and y[2]==0:
            b(-4,0)
            if x[3]==-3 and y[3]==0:
                b(-3,-1)
                if x[4]==0 and y[4]==2 or x[4]==-4 and y[4]==-2:
                    b(-2,-2)
                    if x[5]==-5 and y[5]==1 or x[5]==-1 and y[5]==-3:
                        b(-1,-1)
                        if x[6]==-1 and y[6]==2 or x[6]==-1 and y[6]==3 or x[6]==-1 and y[6]==-2:
                            b(1,1)
                            if x[7]==2 and y[7]==2:
                                b(-3,-3)#
                            else:
                                b(2,2)#
                        else:
                            b(-1,2)
                            if x[7]==-1 and y[7]==3:
                                b(-1,-2)#
                            else:
                                b(-1,3)#
                    elif x[5]==0 and y[5]==-4:
                        b(-5,1)
                        if x[6]==-6 and y[6]==2:
                            b(-1,-3)#
                        else:
                            b(-6,2)#
                    else:
                        b(-1,-3)
                        if x[6]==0 and y[6]==-4:
                            b(-5,1)#
                        else:
                            b(0,-4)#
                elif x[4]==1 and y[4]==3:
                    b(-4,-2)
                    if x[5]==0 and y[5]==2:
                        b(-5,-3)#
                    else:
                        b(0,2)#
                else:
                    b(0,2)
                    if x[5]==1 and y[5]==3:
                        b(-4,-2)#
                    else:
                        b(1,3)#
            else:
                b(-3,0)#
        elif x[2]==-3 and y[2]==0:
            b(-1,-1)
            if x[3]==-1 and y[3]==2 or x[3]==-1 and y[3]==-2:
                b(0,2)
                if x[4]==1 and y[4]==3 or x[4]==-3 and y[4]==-1:
                    b(1,1)
                    if x[5]==2 and y[5]==2 or x[5]==-2 and y[5]==-2:
                        b(2,0)
                        if x[6]==1 and y[6]==0:
                            b(-1,3)
                            if x[7]==3 and y[7]==-1:
                                b(-1,2)#
                            else:
                                b(3,-1)
                        else:
                            b(1,0)#
                    elif x[5]==3 and y[5]==3:
                        b(-2,-2)
                        if x[6]==-3 and y[6]==-3:
                            b(2,2)#
                        else:
                            b(-3,-3)#
                    else:
                        b(2,2)
                        if x[6]==3 and y[6]==3:
                            b(-2,-2)#
                        else:
                            b(3,3)#
                elif x[4]==2 and y[4]==4:
                    b(-3,-1)
                    if x[5]==-4 and y[5]==-2:
                        b(1,3)#
                    else:
                        b(-4,-2)#
                else:
                    b(1,3)
                    if x[5]==2 and y[5]==4:
                        b(-3,-1)#
                    else:
                        b(2,4)#
            elif x[3]==-1 and y[3]==3:
                b(-1,-2)
                if x[4]==-1 and y[4]==-3:
                    b(-1,2)#
                else:
                    b(-1,-3)#
            else:
                b(-1,2)
                if x[4]==-1 and y[4]==3:
                    b(-1,-2)#
                else:
                    b(-1,3)#
        elif x[2]==-4 and y[2]==0:
            b(1,0)
            if x[3]==2 and y[3]==0:
                b(-3,0)#
            else:
                b(2,0)#
        else:
            b(-3,0)
            if x[3]==-4 and y[3]==0:
                b(1,0)#
            else:
                b(-4,0)#
    #(-1,-1)
    if x[1]==-1 and y[1]==-1:
        b(-2,0)
        if x[2]==-3 and y[2]==0:
            b(0,2)
            if x[3]==-3 and y[3]==-1:
                b(0,1)
                if x[4]==0 and y[4]==-1:
                    b(-2,-1)
                    if x[5]==-3 and y[5]==-2:
                        b(0,3)
                        if x[6]==0 and y[6]==4:
                            b(1,3)
                            if x[7]==2 and y[7]==4:
                                b(2,3)
                                if x[8]==1 and y[8]==2:
                                    b(3,3)
                                    if x[9]==4 and y[9]==3:
                                        b(-1,3)
                                    else:
                                        b(4,3)#
                                else:
                                    b(1,2)#
                            else:
                                b(2,4)#
                        else:
                            b(0,4)#
                    elif x[5]==1 and y[5]==2:
                        b(0,3)
                        if x[6]==0 and y[6]==4:
                            b(1,3)
                            if x[7]==2 and y[7]==4:
                                b(2,0)
                                if x[8]==1 and y[8]==0:
                                    b(1,1)
                                    if x[9]==3 and y[9]==-1:
                                        b(2,-1)
                                        if x[10]==2 and y[10]==1:
                                            b(-1,3)
                                            if x[11]==-2 and y[11]==4:
                                                b(-2,3)
                                                if x[12]==-3 and y[12]==3:
                                                    b(2,3)#
                                                else:
                                                    b(-3,3)#
                                            else:
                                                b(-2,4)#
                                        else:
                                            b(2,1)
                                            if x[10]==3 and y[10]==1 and x[11]==-2 and y[11]==1 or x[11]==3 and y[11]==1 and x[10]==-2 and y[10]==1:
                                                b(2,2)
                                                if x[12]==2 and y[12]==3:
                                                    b(2,-2)#
                                                else:
                                                    b(2,3)#
                                            elif x[10]==3 and y[10]==1 or x[11]==3 and y[11]==1:
                                                b(-2,1)#
                                            else:
                                                b(3,1)#
                                    elif x[9]==-1 and y[9]==3 or x[9]==4 and y[9]==-2:
                                        b(2,1)
                                        if x[10]==3 and y[10]==1:
                                            b(-2,1)#
                                        else:
                                            b(3,1)#
                                    else:
                                        b(3,-1)
                                        if x[10]==4 and y[10]==-2:
                                            b(-1,3)#
                                        else:
                                            b(4,-2)#
                                else:
                                    b(1,0)#
                            else:
                                b(2,4)#
                        else:
                            b(0,4)#
                    elif x[5]==2 and y[5]==-1:
                        b(3,-1)
                        if x[6]==1 and y[6]==2 or x[6]==-3 and y[6]==-2:
                            b(2,0)
                            if x[7]==1 and y[7]==0:
                                b(1,1)
                                if x[8]==-1 and y[8]==3:
                                    b(4,-2)#
                                else:
                                    b(-1,3)#
                            else:
                                b(1,0)#
                        elif x[6]==-4 and y[6]==-3:
                            b(1,2)
                            if x[7]==2 and y[7]==3:
                                b(-3,-2)#
                            else:
                                b(2,3)#
                        else:
                            b(-3,-2)
                            if x[7]==-4 and y[7]==-3:
                                b(1,2)#
                            else:
                                b(-4,-3)#
                    elif x[5]==3 and y[5]==-1:
                        b(2,-1)
                        if x[6]==1 and y[6]==2 or x[6]==-3 and y[6]==-2:
                            b(1,0)
                            if x[7]==2 and y[7]==0:
                                b(-1,2)
                                if x[8]==-2 and y[8]==3:
                                    b(3,-2)#
                                else:
                                    b(-2,3)#
                            else:
                                b(2,0)#
                        elif x[6]==-4 and y[6]==-3:
                            b(1,2)
                            if x[7]==2 and y[7]==3:
                                b(-3,-2)#
                            else:
                                b(2,3)#
                        else:
                            b(-3,-2)
                            if x[7]==-4 and y[7]==-3:
                                b(1,2)#
                            else:
                                b(-4,-3)#
                    elif x[5]==-4 and y[5]==-3:
                        b(1,2)
                        if x[6]==2 and y[6]==3:
                            b(-3,-2)#
                        else:
                            b(2,3)#
                    else:
                        b(-3,-2)
                        if x[6]==-4 and y[6]==-3:
                            b(1,2)#
                        else:
                            b(-4,-3)#
                elif x[4]==0 and y[4]==3:
                    b(0,-1)
                    if x[5]==0 and y[5]==-2:
                        b(2,0)
                        if x[6]==1 and y[6]==0:
                            b(1,1)
                            if y[7]==1:
                                b(-1,3)
                                if x[8]==-2 and y[8]==4:
                                    b(3,-1)#
                                else:
                                    b(-2,4)#
                            else:
                                b(2,1)
                                if x[8]==3 and y[8]==1:
                                    b(-2,1)#
                                else:
                                    b(3,1)#
                        else:
                            b(1,0)#
                    else:
                        b(0,-2)#
                elif x[4]==0 and y[4]==-2:
                    b(0,3)
                    if x[5]==0 and y[5]==4:
                        b(0,-1)#
                    else:
                        b(0,4)#
                else:
                    b(0,-1)
                    if x[5]==0 and y[5]==-2:
                        b(0,3)#
                    else:
                        b(0,-2)#
            elif x[3]==1 and y[3]==3:
                b(0,1)
                if x[4]==0 and y[4]==3:
                    b(2,0)
                    if x[5]==1 and y[5]==0:
                        b(1,1)
                        if y[6]==1:
                            b(-1,3)
                            if x[7]==3 and y[7]==-1:
                                b(-2,4)#
                            else:
                                b(3,-1)#
                        else:
                            b(2,1)
                            if x[7]==3 and y[7]==1:
                                b(-2,1)#
                            else:
                                b(3,1)#
                    else:
                        b(1,0)#
                elif x[4]==0 and y[4]==-1:
                    b(-2,-1)
                    if x[5]==-3 and y[5]==-2:
                        b(1,1)
                        if x[6]==2 and y[6]==1 or x[6]==-2 and y[6]==1:
                            b(2,0)
                            if x[7]==1 and y[7]==0:
                                b(-1,3)
                                if x[8]==-2 and y[8]==4:
                                    b(3,-1)#
                                else:
                                    b(-2,4)#
                            else:
                                b(1,0)#
                        elif x[6]==2 and y[6]==-1:
                            b(3,-1)
                            if y[7]==1:
                                b(2,0)
                                if x[8]==-1 and y[8]==3:
                                    b(4,-2)#
                                else:
                                    b(-1,3)#
                            else:
                                b(2,1)
                                if x[8]==3 and y[8]==1:
                                    b(-2,1)#
                                else:
                                    b(3,1)#
                        elif x[6]==3 and y[6]==-1:
                            b(2,-1)
                            if y[7]==1:
                                b(1,0)
                                if x[8]==2 and y[8]==0:
                                    b(-1,2)
                                    if x[9]==-2 and y[9]==-3:
                                        b(3,-2)#
                                    else:
                                        b(-2,-3)#
                                else:
                                    b(2,0)
                            else:
                                b(2,1)
                                if x[8]==3 and y[8]==1:
                                    b(-2,1)#
                                else:
                                    b(3,1)#
                        elif x[6]==2 and y[6]==3:
                            b(-3,-2)
                            if x[7]==-4 and y[7]==-3:
                                b(1,2)#
                            else:
                                b(-4,-3)#
                        else:
                            b(1,2)
                            if x[7]==2 and y[7]==3:
                                b(-3,-2)#
                            else:
                                b(2,3)#
                    elif x[5]==1 and y[5]==2:
                        b(-3,-2)
                        if x[6]==-4 and y[6]==-3:
                            b(-4,-2)
                            if x[7]==-3 and y[7]==-1:
                                b(-2,-2)
                                if x[8]==2 and y[8]==-1:
                                    b(3,-1)
                                    if x[9]==1 and y[9]==0:
                                        b(1,1)
                                        if y[10]==-2:
                                            b(-2,-3)
                                            if x[11]==-2 and y[11]==-4:
                                                b(-2,1)#
                                            else:
                                                b(-2,-4)#
                                        else:
                                            b(-1,-2)
                                            if x[11]==0 and y[11]==-2:
                                                b(-5,-2)#
                                            else:
                                                b(0,-2)#
                                    elif x[9]==1 and y[9]==1:
                                        b(1,0)
                                        if y[10]==-2:
                                            b(-2,-3)
                                            if x[11]==-2 and y[11]==-4:
                                                b(-2,1)#
                                            else:
                                                b(-2,-4)#
                                        else:
                                            b(-1,-2)
                                            if x[11]==0 and y[11]==-2:
                                                b(-5,-2)#
                                            else:
                                                b(0,-2)#
                                    elif y[9]==-2:
                                        b(-2,-3)
                                        if x[10]==-2 and y[10]==-4:
                                            b(-2,1)#
                                        else:
                                            b(-2,-4)#
                                    else:
                                        b(-1,-2)
                                        if x[10]==0 and y[10]==-2:
                                            b(-5,-2)#
                                        else:
                                            b(0,-2)#
                                elif x[8]==3 and y[8]==-1:
                                    b(2,-1)
                                    if x[9]==1 and y[9]==0:
                                        b(1,1)
                                        if y[10]==-2:
                                            b(-2,-3)
                                            if x[11]==-2 and y[11]==-4:
                                                b(-2,1)#
                                            else:
                                                b(-2,-4)#
                                        else:
                                            b(-1,-2)
                                            if x[11]==0 and y[11]==-2:
                                                b(-5,-2)#
                                            else:
                                                b(0,-2)#
                                    elif x[9]==1 and y[9]==1:
                                        b(1,0)
                                        if y[10]==-2:
                                            b(-2,-3)
                                            if x[11]==-2 and y[11]==-4:
                                                b(-2,1)#
                                            else:
                                                b(-2,-4)#
                                        else:
                                            b(-1,-2)
                                            if x[11]==0 and y[11]==-2:
                                                b(-5,-2)#
                                            else:
                                                b(0,-2)#
                                    elif y[9]==-2:
                                        b(-2,-3)
                                        if x[10]==-2 and y[10]==-4:
                                            b(-2,1)#
                                        else:
                                            b(-2,-4)#
                                    else:
                                        b(-1,-2)
                                        if x[10]==0 and y[10]==-2:
                                            b(-5,-2)#
                                        else:
                                            b(0,-2)#
                                elif x[8]==1 and y[8]==0:
                                    b(1,1)
                                    if x[9]==2 and y[9]==-1:
                                        b(3,-1)
                                        if y[10]==-2:
                                            b(-2,-3)
                                            if x[11]==-2 and y[11]==-4:
                                                b(-2,1)#
                                            else:
                                                b(-2,-4)#
                                        else:
                                            b(-1,-2)
                                            if x[11]==0 and y[11]==-2:
                                                b(-5,-2)#
                                            else:
                                                b(0,-2)#
                                    elif x[9]==3 and y[9]==-1:
                                        b(2,-1)
                                        if y[10]==-2:
                                            b(-2,-3)
                                            if x[11]==-2 and y[11]==-4:
                                                b(-2,1)#
                                            else:
                                                b(-2,-4)#
                                        else:
                                            b(-1,-2)
                                            if x[11]==0 and y[11]==-2:
                                                b(-5,-2)#
                                            else:
                                                b(0,-2)#
                                    elif y[9]==-2:
                                        b(-2,-3)
                                        if x[10]==-2 and y[10]==-4:
                                            b(-2,1)#
                                        else:
                                            b(-2,-4)#
                                    else:
                                        b(-1,-2)
                                        if x[10]==0 and y[10]==-2:
                                            b(-5,-2)#
                                        else:
                                            b(0,-2)#
                                elif x[8]==1 and y[8]==1:
                                    b(1,0)
                                    if x[9]==2 and y[9]==-1:
                                        b(3,-1)
                                        if y[10]==-2:
                                            b(-2,-3)
                                            if x[11]==-2 and y[11]==-4:
                                                b(-2,1)#
                                            else:
                                                b(-2,-4)#
                                        else:
                                            b(-1,-2)
                                            if x[11]==0 and y[11]==-2:
                                                b(-5,-2)#
                                            else:
                                                b(0,-2)#
                                    elif x[9]==3 and y[9]==-1:
                                        b(2,-1)
                                        if y[10]==-2:
                                            b(-2,-3)
                                            if x[11]==-2 and y[11]==-4:
                                                b(-2,1)#
                                            else:
                                                b(-2,-4)#
                                        else:
                                            b(-1,-2)
                                            if x[11]==0 and y[11]==-2:
                                                b(-5,-2)#
                                            else:
                                                b(0,-2)#
                                    elif y[9]==-2:
                                        b(-2,-3)
                                        if x[10]==-2 and y[10]==-4:
                                            b(-2,1)#
                                        else:
                                            b(-2,-4)#
                                    else:
                                        b(-1,-2)
                                        if x[10]==0 and y[10]==-2:
                                            b(-5,-2)#
                                        else:
                                            b(0,-2)#
                                elif y[8]==-2:
                                    b(-2,-3)
                                    if x[9]==-2 and y[9]==-4:
                                        b(-2,1)#
                                    else:
                                        b(-2,-4)#
                                else:
                                    b(-1,-2)
                                    if x[9]==0 and y[9]==-2:
                                        b(-5,-2)#
                                    else:
                                        b(0,-2)#
                            else:
                                b(-3,-1)#
                        else:
                            b(-4,-3)#
                    elif x[5]==2 and y[5]==-1:
                        b(3,-1)
                        if x[6]==1 and y[6]==2 or x[6]==-3 and y[6]==-2:
                            b(2,0)
                            if x[7]==1 and y[7]==0:
                                b(1,1)
                                if x[8]==-1 and y[8]==3:
                                    b(4,-2)#
                                else:
                                    b(-1,3)#
                            else:
                                b(1,0)#
                        elif x[6]==2 and y[6]==3:
                            b(-3,-2)
                            if x[7]==-4 and y[7]==-3:
                                b(1,2)#
                            else:
                                b(-4,-3)#
                        else:
                            b(1,2)
                            if x[7]==2 and y[7]==3:
                                b(-3,-2)#
                            else:
                                b(2,3)#
                    elif x[5]==3 and y[5]==-1:
                        b(2,-1)
                        if x[6]==1 and y[6]==2 or x[6]==-3 and y[6]==-2:
                            b(1,0)
                            if x[7]==2 and y[7]==0:
                                b(-1,2)
                                if x[8]==-2 and y[8]==3:
                                    b(3,-2)#
                                else:
                                    b(-2,-3)#
                            else:
                                b(2,0)#
                        elif x[6]==2 and y[6]==3:
                            b(-3,-2)
                            if x[7]==-4 and y[7]==-3:
                                b(1,2)#
                            else:
                                b(-4,-3)#
                        else:
                            b(1,2)
                            if x[7]==2 and y[7]==3:
                                b(-3,-2)#
                            else:
                                b(2,3)#
                    elif x[5]==2 and y[5]==3:
                        b(-3,-2)
                        if x[6]==-4 and y[6]==-3:
                            b(1,2)#
                        else:
                            b(-4,-3)#
                    else:
                        b(1,2)
                        if x[6]==2 and y[6]==3:
                            b(-3,-2)#
                        else:
                            b(2,3)#
                elif x[4]==0 and y[4]==4:
                    b(0,-1)
                    if x[5]==0 and y[5]==-2:
                        b(0,3)#
                    else:
                        b(0,-2)#
                else:
                    b(0,3)
                    if x[3]==0 and y[3]==4:
                        b(0,-1)#
                    else:
                        b(0,4)#
            elif x[3]==2 and y[3]==4:
                b(-3,-1)
                if x[4]==-4 and y[4]==-2:
                    b(1,3)#
                else:
                    b(-4,-2)#
            else:
                b(1,3)
                if x[4]==2 and y[4]==4:
                    b(-3,-1)#
                else:
                    b(2,4)#
        elif x[2]==1 and y[2]==0:
            b(-3,-1)
            if x[3]==0 and y[3]==2:
                b(-4,-2)
                if x[4]==-5 and y[4]==-3:
                    b(-4,0)
                    if x[5]==-3 and y[5]==0:
                        b(-2,-2)
                        if x[6]+y[6]==-4:
                            b(-3,-2)
                            if x[7]==-1 and y[7]==-2 or x[7]==-5 and y[7]==-2:
                                b(-2,-1)
                                if x[8]==-1 and y[8]==-4:
                                    b(-1,-5)
                                    if x[9]==-2:
                                        b(0,1)
                                        if x[10]==1 and y[10]==2:
                                            b(-4,-3)#
                                        else:
                                            b(1,2)#
                                    else:
                                        b(-2,-3)
                                        if x[10]==-2 and y[10]==-4:
                                            b(-2,1)#
                                        else:
                                            b(-2,-4)#
                                elif x[8]==-1 and y[8]==-5:
                                    b(-1,-4)
                                    if x[9]==-2:
                                        b(0,1)
                                        if x[10]==1 and y[10]==2:
                                            b(-4,-3)#
                                        else:
                                            b(1,2)#
                                    else:
                                        b(-2,-3)
                                        if x[10]==-2 and y[10]==-4:
                                            b(-2,1)#
                                        else:
                                            b(-2,-4)#
                                elif x[8]==-2:
                                    b(0,1)
                                    if x[9]==1 and y[9]==2:
                                        b(-4,-3)#
                                    else:
                                        b(1,2)#
                                else:
                                    b(-2,-3)
                                    if x[9]==-2 and y[9]==-4:
                                        b(-2,1)#
                                    else:
                                        b(-2,-4)#
                            elif x[7]==0 and y[7]==-2:
                                b(-5,-2)
                                if x[8]==-6 and y[8]==-2:
                                    b(-1,-2)#
                                else:
                                    b(-6,-2)#
                            else:
                                b(-1,-2)
                                if x[8]==0 and y[8]==-2:
                                    b(-5,-2)#
                                else:
                                    b(0,-2)#
                        else:
                            b(-1,-3)
                            if x[7]==0 and y[7]==-4:
                                b(-5,1)#
                            else:
                                b(0,-4)#
                    else:
                        b(-3,0)#
                else:
                    b(-5,-3)#
            elif x[3]==-4 and y[3]==-2:
                b(0,2)
                if x[4]==1 and y[4]==3:
                    b(-3,0)
                    if x[5]==-4 and y[5]==0:
                        b(0,1)
                        if x[6]==1 and y[6]==1:
                            b(1,2)
                            if x[7]==1 and y[7]==-2:
                                b(1,-3)
                                if x[8]==0 and y[8]==3 or x[8]==0 and y[8]==-1 or x[8]==0 and y[8]==4:
                                    b(-2,-1)
                                    if x[9]==-3 and y[9]==-2:
                                        b(2,3)#
                                    else:
                                        b(-3,-2)#
                                else:
                                    b(0,3)
                                    if x[9]==0 and y[9]==-1:
                                        b(0,4)#
                                    else:
                                        b(0,-1)#
                            elif x[7]==1 and y[7]==-3:
                                b(1,-2)
                                if x[8]==0 and y[8]==3 or x[8]==0 and y[8]==-1 or x[8]==0 and y[8]==4:
                                    b(-2,-1)
                                    if x[9]==-3 and y[9]==-2:
                                        b(2,3)#
                                    else:
                                        b(-3,-2)#
                                else:
                                    b(0,3)
                                    if x[9]==0 and y[9]==-1:
                                        b(0,4)#
                                    else:
                                        b(0,-1)#  
                            elif x[7]==0 and y[7]==3 or x[7]==0 and y[7]==-1 or x[7]==0 and y[7]==4:
                                b(-2,-1)
                                if x[8]==-3 and y[8]==-2:
                                    b(2,3)#
                                else:
                                    b(-3,-2)#
                            else:
                                b(0,3)
                                if x[8]==0 and y[8]==-1:
                                    b(0,4)#
                                else:
                                    b(0,-1)#
                        elif x[6]==1 and y[6]==2:
                            b(1,1)
                            if x[7]==0 and y[7]==-1 or x[7]==0 and y[7]==3 or x[7]==0 and y[7]==4:
                                b(-2,1)
                                if x[8]==-3 and y[8]==1:
                                    b(2,1)#
                                else:
                                    b(-3,1)#
                            else:
                                b(0,3)
                                if x[8]==0 and y[8]==-1:
                                    b(0,4)#
                                else:
                                    b(0,-1)#
                        elif x[6]==0 and y[6]==3:
                            b(-3,-2)
                            if x[7]==1 and y[7]==1:
                                b(1,2)
                                if x[8]==-2 and y[8]==-1:
                                    b(-3,1)
                                    if x[9]==-3 and y[9]==2:
                                        b(-3,-3)#
                                    else:
                                        b(-3,2)#
                                else:
                                    b(-2,-1)#
                            elif x[7]==1 and y[7]==2:
                                b(1,1)
                                if x[8]==-2 and y[8]==1 or x[8]==2 and y[8]==1 or x[8]==3 and y[8]==1:
                                    b(-3,1)
                                    if x[9]==-3 and y[9]==2:
                                        b(-3,-3)#
                                    else:
                                        b(-3,2)#
                                else:
                                    b(2,1)
                                    if x[9]==3 and y[9]==1:
                                        b(-2,1)#
                                    else:
                                        b(3,1)#
                            elif x[7]==-3 and y[7]==1 or x[7]==-3 and y[7]==2 or x[7]==-3 and y[7]==-3:
                                b(-2,-1)
                                if x[8]==1 and y[8]==2:
                                    b(-4,-3)#
                                else:
                                    b(1,2)#
                            else:
                                b(-3,1)
                                if x[8]==-3 and y[8]==2:
                                    b(-3,-3)#
                                else:
                                    b(-3,2)#
                        elif x[6]==0 and y[6]==-1:
                            b(-2,-1)
                            if x[7]==2 and y[7]==-1:
                                b(3,-1)
                                if x[8]==1 and y[8]==2:
                                    b(1,1)
                                    if x[9]==2 and y[9]==1 or x[9]==-2 and y[9]==1 or x[9]==3 and y[9]==1:
                                        b(-3,-2)
                                        if x[10]==-4 and y[10]==-3:
                                            b(-3,1)
                                            if x[11]==-3 and y[11]==2:
                                                b(-3,-3)#
                                            else:
                                                b(-3,2)#
                                        else:
                                            b(-4,-3)#
                                    else:
                                        b(2,1)
                                        if x[10]==3 and y[10]==1:
                                            b(-2,1)#
                                        else:
                                            b(3,1)#
                                elif x[8]==-3 and y[8]==-2:
                                    b(1,2)
                                    if x[9]==2 and y[9]==3:
                                        b(0,3)
                                        if x[10]==0 and y[10]==4:
                                            b(2,1)
                                            if y[11]==1:
                                                b(3,0)
                                                if x[12]==4 and y[12]==-1:
                                                    b(-1,4)#
                                                else:
                                                    b(4,-1)#
                                            else:
                                                b(1,1)
                                                if x[12]==3 and y[12]==1:
                                                    b(-2,1)#
                                                else:
                                                    b(3,1)#
                                        else:
                                            b(0,4)#
                                    else:
                                        b(2,3)#
                                elif x[8]==2 and y[8]==3:
                                    b(-3,-2)
                                    if x[9]==-4 and y[9]==-3:
                                        b(1,2)#
                                    else:
                                        b(-4,-3)#
                                else:
                                    b(1,2)
                                    if x[9]==2 and y[9]==3:
                                        b(-3,-2)#
                                    else:
                                        b(2,3)#
                            elif x[7]==3 and y[7]==-1:
                                b(2,-1)
                                if x[8]==1 and y[8]==2:
                                    b(1,1)
                                    if x[9]==2 and y[9]==1 or x[9]==-2 and y[9]==1 or x[9]==3 and y[9]==1:
                                        b(-3,-2)
                                        if x[10]==-4 and y[10]==-3:
                                            b(-3,1)
                                            if x[11]==-3 and y[11]==2:
                                                b(-3,-3)#
                                            else:
                                                b(-3,2)#
                                        else:
                                            b(-4,-3)#
                                    else:
                                        b(2,1)
                                        if x[10]==3 and y[10]==1:
                                            b(-2,1)#
                                        else:
                                            b(3,1)#
                                elif x[8]==-3 and y[8]==-2:
                                    b(1,2)
                                    if x[9]==2 and y[9]==3:
                                        b(0,3)
                                        if x[10]==0 and y[10]==4:
                                            b(2,1)
                                            if y[11]==1:
                                                b(3,0)
                                                if x[12]==4 and y[12]==-1:
                                                    b(-1,4)#
                                                else:
                                                    b(4,-1)#
                                            else:
                                                b(1,1)
                                                if x[12]==3 and y[12]==1:
                                                    b(-2,1)#
                                                else:
                                                    b(3,1)#
                                        else:
                                            b(0,4)#
                                    else:
                                        b(2,3)#
                                elif x[8]==2 and y[8]==3:
                                    b(-3,-2)
                                    if x[9]==-4 and y[9]==-3:
                                        b(1,2)#
                                    else:
                                        b(-4,-3)#
                                else:
                                    b(1,2)
                                    if x[9]==2 and y[9]==3:
                                        b(-3,-2)#
                                    else:
                                        b(2,3)#
                            elif x[7]==1 and y[7]==2:
                                b(1,1)
                                if x[8]==2 and y[8]==-1:
                                    b(3,-1)
                                    if x[9]==-2 and y[9]==1 or x[9]==2 and y[9]==1 or x[9]==3 and y[9]==1:
                                        b(-3,-2)
                                        if x[10]==-4 and y[10]==-3:
                                            b(-3,1)
                                            if x[11]==-3 and y[11]==2:
                                                b(-3,-3)#
                                            else:
                                                b(-3,2)#
                                        else:
                                            b(-4,-3)#
                                    else:
                                        b(2,1)
                                        if x[10]==3 and y[10]==1:
                                            b(-2,1)#
                                        else:
                                            b(3,1)#
                                elif x[8]==3 and y[8]==-1:
                                    b(2,-1)
                                    if x[9]==-2 and y[9]==1 or x[9]==2 and y[9]==1 or x[9]==3 and y[9]==1:
                                        b(-3,-2)
                                        if x[10]==-4 and y[10]==-3:
                                            b(-3,1)
                                            if x[11]==-3 and y[11]==2:
                                                b(-3,-3)#
                                            else:
                                                b(-3,2)#
                                        else:
                                            b(-4,-3)#
                                    else:
                                        b(2,1)
                                        if x[10]==3 and y[10]==1:
                                            b(-2,1)#
                                        else:
                                            b(3,1)#
                                elif x[8]==-2 and y[8]==1 or x[8]==2 and y[8]==1 or x[8]==3 and y[8]==1:
                                    b(-3,-2)
                                    if x[9]==-4 and y[9]==-3:
                                        b(-3,1)
                                        if x[10]==-3 and y[10]==2:
                                            b(-3,-3)#
                                        else:
                                            b(-3,2)#
                                    else:
                                        b(-4,-3)#
                                else:
                                    b(2,1)
                                    if x[9]==3 and y[9]==1:
                                            b(-2,1)#
                                    else:
                                        b(3,1)#
                            elif x[7]==-3 and y[7]==-2:
                                b(1,2)
                                if x[8]==2 and y[8]==3:
                                    b(0,3)
                                    if x[9]==0 and y[9]==4:
                                        b(2,1)
                                        if y[10]==1:
                                            b(3,0)
                                            if x[11]==4 and y[11]==-1:
                                                b(-1,4)#
                                            else:
                                                b(4,-1)#
                                        elif x[10]==2 and y[10]==-1:
                                            b(3,-1)
                                            if y[11]==1:
                                                b(3,0)
                                                if x[12]==4 and y[12]==-1:
                                                    b(-1,4)#
                                                else:
                                                    b(4,-1)#
                                            else:
                                                b(1,1)
                                                if x[12]==3 and y[12]==1:
                                                    b(-2,1)#
                                                else:
                                                    b(3,1)#
                                        elif x[10]==3 and y[10]==-1:
                                            b(2,-1)
                                            if y[11]==1:
                                                b(3,0)
                                                if x[12]==4 and y[12]==-1:
                                                    b(-1,4)#
                                                else:
                                                    b(4,-1)#
                                            else:
                                                b(1,1)
                                                if x[12]==3 and y[12]==1:
                                                    b(-2,1)#
                                                else:
                                                    b(3,1)#
                                        else:
                                            b(1,1)
                                            if x[11]==3 and y[11]==1:
                                                b(-2,1)#
                                            else:
                                                b(3,1)#
                                    else:
                                        b(0,4)#
                                else:
                                    b(2,3)#
                            elif x[7]==2 and y[7]==3:
                                b(-3,-2)
                                if x[8]==-4 and y[8]==-3:
                                    b(1,2)#
                                else:
                                    b(-4,-3)#
                            else:
                                b(1,2)
                                if x[8]==2 and y[8]==3:
                                    b(-3,-2)#
                                else:
                                    b(2,3)#
                        elif x[6]==0 and y[6]==4:
                            b(0,-1)
                            if x[7]==0 and y[4]==-2:
                                b(0,3)#
                            else:
                                b(0,-2)#
                        else:
                            b(0,3)
                            if x[7]==0 and y[7]==4:
                                b(0,-1)#
                            else:
                                b(0,4)#
                    else:
                        b(-4,0)#
                else:
                    b(1,3)#
            elif x[3]==1 and y[3]==3:
                b(-4,-2)
                if x[4]==-5 and y[4]==-3:
                    b(0,2)#
                else:
                    b(-5,-3)#
            else:
                b(0,2)
                if x[4]==1 and y[4]==3:
                    b(-4,-2)#
                else:
                    b(1,3)#
        elif x[2]==2 and y[2]==0:
            b(-3,0)
            if x[3]==-4 and y[3]==0:
                b(1,0)#
            else:
                b(-4,0)#
        else:
            b(1,0)
            if x[3]==2 and y[3]==0:
                b(-3,0)#
            else:
                b(2,0)#
    #(-2,-1)
    if x[1]==-2 and y[1]==-1:
        b(-1,-1)
        if x[2]==-1 and y[2]==2:
            b(-1,-2)
            if x[3]==-1 and y[3]==-3:
                b(-2,0)
                if x[4]==-3 and y[4]==0 or x[4]==1 and y[4]==0:
                    b(0,-2)
                    if x[5]==1 and y[5]==-3 or x[5]==-3 and y[5]==1:
                        b(1,-2)
                        if x[6]==2 and y[6]==-2 or x[6]==-2 and y[6]==-2:
                            b(0,-1)
                            if x[7]==0:
                                b(-2,1)
                                if x[8]==-3 and y[8]==2:
                                    b(2,-3)#
                                else:
                                    b(-3,2)#
                            else:
                                b(0,1)
                                if x[8]==0 and y[6]==2:
                                    b(0,-3)#
                                else:
                                    b(0,2)#
                        elif x[6]==3 and y[6]==-2:
                            b(-2,-2)
                            if x[7]==-3 and y[7]==-2:
                                b(2,-2)#
                            else:
                                b(-3,-2)#
                        else:
                            b(2,-2)
                            if x[7]==3 and y[7]==-2:
                                b(-2,-2)#
                            else:
                                b(3,-2)#
                    elif x[5]==2 and y[5]==-4:
                        b(-3,1)
                        if x[6]==-4 and y[6]==2:
                            b(1,-3)#
                        else:
                            b(-4,2)#
                    else:
                        b(1,-3)
                        if x[6]==2 and y[6]==-4:
                            b(-3,1)#
                        else:
                            b(2,-4)#
                elif x[4]==2 and y[4]==0:
                    b(-3,0)
                    if x[5]==-4 and y[5]==0:
                        b(1,0)#
                    else:
                        b(-4,0)#
                else:
                    b(1,0)
                    if x[5]==2 and y[5]==0:
                        b(-3,0)#
                    else:
                        b(2,0)#
            else:
                b(-1,-2)#
        elif x[2]==-1 and y[2]==-2:
            b(-1,2)
            if x[3]==-1 and y[3]==3:
                b(-3,0)
                if x[4]==-2 and y[4]==0 or x[4]==1 and y[4]==0:
                    b(-2,1)
                    if x[5]==0 and y[5]==3 or x[5]==-4 and y[5]==-1:
                        b(1,1)
                        if y[6]==1:
                            b(2,2)
                            if x[7]==3 and y[7]==3:
                                b(-2,-2)#
                            else:
                                b(3,3)#
                        else:
                            b(0,1)
                            if x[7]==2 and y[7]==1:
                                b(-3,1)#
                            else:
                                b(2,1)#
                    elif x[5]==1 and y[5]==4:
                        b(-4,-1)
                        if x[6]==-5 and y[6]==-2:
                            b(0,3)#
                        else:
                            b(-5,-2)#
                    else:
                        b(0,3)
                        if x[5]==-4 and y[5]==-1:
                            b(1,4)#
                        else:
                            b(-4,-1)#
                elif x[4]==-4 and y[4]==0:
                    b(-3,1)
                    if x[5]==-2 and y[5]==1:
                        b(-2,0)
                        if x[6]==1 and y[6]==0:
                            b(0,-2)
                            if x[7]==1 and y[7]==-3:
                                b(-4,2)#
                            else:
                                b(1,-3)#
                        else:
                            b(1,0)#
                    elif x[5]==0 and y[5]==3 or x[5]==-4 and y[5]==-1 or x[5]==0 and y[5]==1 or x[5]==-4 and y[5]==1 or x[5]==1 and y[5]==4 or x[5]==1 and y[5]==1:
                        b(-2,0)
                        if x[6]==1 and y[6]==0:
                            b(0,-2)
                            if x[7]==1 and y[7]==-3:
                                b(-4,2)#
                            else:
                                b(1,-3)#
                        else:
                            b(1,0)#
                    else:
                        b(-2,1)
                        if y[6]==1:
                            b(0,3)
                            if x[7]==1 and y[7]==4:
                                b(4,-1)#
                            else:
                                b(1,4)
                        else:
                            b(0,1)
                            if x[7]==1 and y[7]==1:
                                b(-4,1)#
                            else:
                                b(1,1)#
                else:
                    b(-2,0)
                    if x[5]==1 and y[5]==0:
                        b(-4,0)#
                    else:
                        b(1,0)#
            else:
                b(-1,3)#
        elif x[2]==-1 and y[2]==3:
            b(-1,-2)
            if x[3]==-1 and y[3]==-3:
                b(-1,2)#
            else:
                b(-1,-3)#
        else:
            b(-1,2)
            if x[3]==-1 and y[3]==3:
                b(-1,-2)#
            else:
                b(-1,3)#
#其他
    
canvas.pack()
window.mainloop()