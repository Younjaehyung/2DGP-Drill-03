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
    delay(0.1)

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
    for y in range(600,0,-10):
    print('right')
def runt_bottom():
    print('bottom)
def runt_left():
    print('left')
                


def run_rectangle():
    print('rectangle')
    run_top()
    run_right()
    runt_bottom()
    runt_left()
    pass

while True:
    run_rectangle()
    #run_circle()
    break    



close_canvas()
