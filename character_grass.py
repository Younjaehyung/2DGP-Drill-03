from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

#grass.draw_now(400,30)
#character.draw_now(400,90)

def draw_charcter(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.05)

def run_circle():
    print('circle')
    r=300
    cx=800//2
    cy=600//2
    for degree in range(0,360,3):
        theta=math.radians(degree)
        
        x=r*math.cos(theta)+cx
        y=r*math.sin(theta)+cy
        draw_charcter(x,y)
    pass

def run_top():
    for x in range(0,800,10):
        draw_charcter(x,550)
    print('top')
def run_right():
    for y in range(550,100,-10):
         draw_charcter(790,y)
    print('right')
def run_bottom():
    for x in range(790,0,-10):
         draw_charcter(x,90)
    print('bottom')
def run_left():
    for y in range(90,560,10):
         draw_charcter(0,y)
    print('left')
                


def run_rectangle():
    print('rectangle')
    run_top()
    run_right()
    run_bottom()
    run_left()
    pass


def run_rightdown():
    for x in range(0,410,10):
        y=600-x
        draw_charcter(x,y)
def run_rightup():
    for x in range(400,810,10):
        y=x-200
        draw_charcter(x,y)
def run_lefttop():
    for x in range(800,0,-10):
        draw_charcter(x,600)

        
def run_triangle():
    run_rightdown()
    run_rightup()
    run_lefttop()
    pass

while True:
    run_rectangle()
    run_circle()
    run_triangle()
    



close_canvas()
