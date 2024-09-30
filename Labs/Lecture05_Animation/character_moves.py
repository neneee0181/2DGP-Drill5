from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 여기를 채우세요.

for x in range(0,800,5):
    clear_canvas()
    grass.draw(400,30)
    character.draw(x,90)
    update_canvas()
    delay(0.01)

close_canvas()

