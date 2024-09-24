from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

#grass.draw_now(400,30)
#character.draw_now(400,90)


def run_circle():
    print('circle')
    
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(400,90)
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
