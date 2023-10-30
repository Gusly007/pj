from __future__ import division

import turtle
import colorsys
import math

turtle.setup()
turtle.hideturtle()
turtle.title("Tower of Hanoi ")
turtle.speed(0)
turtle.tracer(0,0)

n = 5
peg_height = 300
ring_height_max = 10
ring_width_max = 150
ring_width_min = 20
ring_delta = 15
ring_delta_max = 30
ring_height = 20
animation_step = 10

A = [] # List of rings in Peg A
B = []
C = []

T = [] # list of turtles

def draw_line(x,y,heading,length,pensize,color):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(heading)
    turtle.down()
    turtle.color(color)
    turtle.pensize(pensize)
    turtle.fd(length)

def draw_scene():
    turtle.bgcolor('light blue')
    draw_line(-600,-100,0,1200,10,'brown')
    for i in range(-250,251,250):
        draw_line(i,-93,90,peg_height,5,'black')

def initialize():
    global ring_width_max,ring_width_min,ring_ratio,ring_delta
    for i in range(n):
        A.append(i)
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        t.pencolor('red')
        t.fillcolor('light green')
        T.append(t)
    ring_delta = min(135/(n-1),ring_delta_max)

def draw_single_ring(r, x, k, extra=0):
    global ring_delta

    w = ring_width_max - ring_delta*(r-1)
    T[r].up()
    T[r].goto(x-w/2,-95+ring_height*k + extra)
    T[r].down()
    T[r].seth(0)
    T[r].begin_fill()
    for i in range(2):
        T[r].fd(w)
        T[r].left(90)
        T[r].fd(ring_height)
        T[r].left(90)
    T[r].end_fill()

def draw_rings():
    for i in range(len(A)):
        draw_single_ring(A[i],-250,i)
    for i in range(len(B)):
        draw_single_ring(B[i],0,i)
    for i in range(len(C)):
        draw_single_ring(C[i],250,i)

def move_ring(PP,QQ):
    if PP == "A":
        x = -250
        P = A
    elif PP == "B":
        x = 0
        P = B
    else:
        x = 250
        P = C

    if QQ =="A":
        x2 = -250
        Q = A
    elif QQ == "B":
        x2 = 0
        Q = B
    else:
        x2 = 250
        Q = C

    for extra in range(1,250-(-95+ring_height*(len(P)-1)),animation_step):
        T[P[len(P)-1]].clear()
        draw_single_ring(P[len(P)-1],x,len(P)-1,extra)
        turtle.update()

    T[P[len(P)-1]].clear()
    draw_single_ring(P[len(P)-1],x,len(P)-1,extra)
    turtle.update()
    tp = x
    if x2 > x:
        step = animation_step
    else:
        step = -animation_step
    for tp in range(x,x2,step):
        T[P[len(P)-1]].clear()
        draw_single_ring(P[len(P)-1],tp,len(P)-1,extra)
        turtle.update()
    T[P[len(P)-1]].clear()
    draw_single_ring(P[len(P)-1],x2,len(P)-1,extra)
    turtle.update()
    Q.append(P[len(P)-1])
    del P[-1]
    for extra in range(250-(-95+ring_height*(len(Q)-1)),0,-animation_step):
        T[Q[len(Q)-1]].clear()
        draw_single_ring(Q[len(Q)-1],x2,len(Q)-1,extra)
        turtle.update()
    T[Q[len(Q)-1]].clear()
    draw_single_ring(Q[len(Q)-1],x2,len(Q)-1)
    turtle.update()
    return


#compar
def filter_string(str__a,str__b):
    if len(str__a) != len(str__b):
        return
    for idx in range(0,len(str__b)):
        if str__a[idx] != str__b[idx]:
            return len(str__a)-idx
    pass

def dec2gray(num):
    """retourne le code gray correspondant au nombre entier 'num' """
    return (num>>1)^num

# dec2bin améliore l'affichage binaire des nombres en ajoutant si nécessaire des zéros à gauche
dec2bin = lambda x, n=8: bin(x)[2:].zfill(n)
#first try move rings in x to z
# fgray = dec2bin(dec2gray(3),4)
#  sgray = dec2bin(dec2gray(4),4)
#  idx = filter_string(fgray,sgray)
def tower_of_hanoi(x,y,z,n):
    dictionary = {}
    dictionary["1"] = 1
    list1 = []
    for init in range(0,n):
        list1.insert(init,init+1)
    print(list1)
    print(list1[0])
    list2 = []
    list3 = []
    for index in range(2,n+1):
        dictionary[str(index)]=1
    print(dictionary)
    for nb in range(0,pow(2,n)-1):
            fgray = dec2bin(dec2gray(nb),n)
            sgray = dec2bin(dec2gray(nb+1),n)
            idx = filter_string(str(fgray),str(sgray))
            print(fgray)
            print(sgray)
            print(idx)
            if idx > 1:
                if dictionary[str(idx)] == 1:
                    if  list2 == [] or list2[0]>idx :
                            move_ring(x,y)
                            dictionary[str(idx)] = 2
                            del list1[0]
                            list2.insert(0,idx)
                    else:
                        move_ring(x,z)
                        dictionary[str(idx)] = 3
                        del list1[0]
                        list3.insert(0,idx)
                else:
                    if dictionary[str(idx)] == 2:
                        if  list1 == [] or list1[0]>idx:
                            move_ring(y,x)
                            dictionary[str(idx)] = 1
                            del list2[0]
                            list1.insert(0,idx)
                        else:
                            move_ring(y,z)
                            dictionary[str(idx)] = 3
                            del list2[0]
                            list3.insert(0,idx)

                    else:
                        if dictionary[str(idx)] == 3:
                            if  list1 == [] or list1[0]>idx:
                                move_ring(z,x)
                                dictionary[str(idx)] = 1
                                del list3[0]
                                list1.insert(0,idx)

                            else:
                                move_ring(z,y)
                                dictionary[str(idx)] = 2
                                del list3[0]
                                list2.insert(0,idx)


            elif idx == 1:
                if n%2 == 0:
                    if dictionary['1'] == 1 :
                        move_ring(x,y)
                        dictionary[str(idx)] = 2
                        del list1[0]
                        list2.insert(0,idx)
                    elif dictionary['1'] == 2:
                        move_ring(y,z)
                        dictionary[str(idx)] = 3
                        del list2[0]
                        list3.insert(0,idx)
                    elif dictionary['1'] == 3:
                        move_ring(z,x)
                        dictionary[str(idx)] = 1
                        del list3[0]
                        list1.insert(0,idx)
                else:
                    if dictionary['1'] == 1 :
                        move_ring(x,z)
                        dictionary[str(idx)] = 3
                        del list1[0]
                        list3.insert(0,idx)
                    elif dictionary['1'] == 2:
                        move_ring(y,x)
                        dictionary[str(idx)] = 1
                        del list2[0]
                        list1.insert(0,idx)
                    elif dictionary['1'] == 3:
                        move_ring(z,y)
                        dictionary[str(idx)] = 2
                        del list3[0]
                        list2.insert(0,idx)
            print(dictionary)

draw_scene()
turtle.update()
n = int(turtle.numinput('Number of Rings','Please enter number of rings:',5,2,10))
initialize()
draw_rings()
tower_of_hanoi("A","B","C",n)
turtle.update()