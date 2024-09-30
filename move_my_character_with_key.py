from pico2d import *

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running, dir_x, dir_y, facing, idle

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x = 1
                facing = 0  # 오른쪽
                idle = False
            elif event.key == SDLK_LEFT:
                dir_x = -1
                facing = 1  # 왼쪽
                idle = False
            elif event.key == SDLK_UP:
                dir_y = 1
                facing = 2  # 위쪽
                idle = False
            elif event.key == SDLK_DOWN:
                dir_y = -1
                facing = 3  # 아래쪽
                idle = False
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key in (SDLK_RIGHT, SDLK_LEFT):
                dir_x = 0
            elif event.key in (SDLK_UP, SDLK_DOWN):
                dir_y = 0
            if dir_x == 0 and dir_y == 0:
                idle = True


def draw_character(frame, facing, x, y, idle):
    if idle:
        if frame % 2 == 0:
            character.clip_draw(0, 450, 100, 140, x, y)
        else:
            character.clip_draw(200, 450, 100, 140, x, y)
    else:
        character.clip_draw(frame * 100, facing * 150, 100, 140, x, y)


running = True
x, y = 800 // 2, 600 // 2
frame = 0
dir_x, dir_y = 0, 0
facing = 2
idle = True

while running:
    clear_canvas()
    grass.draw(400, 300, 800, 600)

    draw_character(frame if not idle else (frame % 2), facing, x, y, idle)

    update_canvas()
    handle_events()

    if dir_x != 0 or dir_y != 0:
        frame = (frame + 1) % 4
        idle = False
    else:
        frame = (frame + 1) % 2

    x += dir_x * 5
    y += dir_y * 5
    delay(0.05)

close_canvas()
