from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

#grass.draw_now(400,30)
#character.draw_now(400,90)


def run_circle():
    print('circle')
    r=300
    cx=800//2
    cy=600//2
    for degree in range(0,360,3):
        theta=math.radians(degree)
        
        x=r*math.cos(theta)+cx
        y=r*math.sin(theta)+cy
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.1)
    pass

def run_rectangle():
    print('rectangle')
    grass.draw_now(400,30)
    character.draw_now(400,90)

    pass

while True:
    run_rectangle()
    run_circle()
    break    



close_canvas()
