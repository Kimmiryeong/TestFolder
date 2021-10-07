from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character=load_image('character.png')


while True:

# 사각 운동


    x=0
    y=40
    while x < 780:
    
        # 게임 루프
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
    
        # 게임 로직: 게임 내에 있는 캐릭터의 상태를 바꿔주는 것
        x+=2
        delay(0.01)

    while y < 580:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(780,y)
        y+=2
        delay(0.01)

    while x > 20:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,580)
        x-=2
        delay(0.01)

    while y > 90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(20,y)
        y-=2
        delay(0.01)

    clear_canvas()



    # 원 그리기
    for degree in range (0, 360+1):
        x = 400
        y = 325
        r = 200
        pi      = (3.141592 /180)*degree
        iX=x+r*math.cos(pi)
        iY=y+r*math.sin(pi)
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(iX,iY)
        delay(0.01)
    
    
    
