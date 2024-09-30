from pico2d import *

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running, dir_x, dir_y, facing

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                facing = 3  # 오른쪽
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                facing = 1  # 왼쪽
            elif event.key == SDLK_UP:
                dir_y += 1
                facing = 0  # 위쪽
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                facing = 2  # 아래쪽
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


running = True
x, y = 800 // 2, 600 // 2
frame = 0
dir_x, dir_y = 0, 0
facing = 2  # 초기 상태는 아래쪽을 바라보는 상태

while running:
    clear_canvas()
    grass.draw(400, 300, 800, 600)

    # 방향에 맞는 스프라이트를 그린다
    if dir_x != 0 or dir_y != 0:  # 이동 중일 때
        if facing == 3:  # 오른쪽
            character.clip_draw(frame * 100, 0, 100, 140, x, y)
        elif facing == 1:  # 왼쪽
            character.clip_draw(frame * 100, 150, 100, 140, x, y)
        elif facing == 0:  # 위쪽
            character.clip_draw(frame * 100, 300, 100, 140, x, y)
        elif facing == 2:  # 아래쪽
            character.clip_draw(frame * 100, 450, 100, 140, x, y)
    else:  # 정지 상태일 때
        if facing == 3:  # 오른쪽
            character.clip_draw(0, 0, 100, 140, x, y)
        elif facing == 1:  # 왼쪽
            character.clip_draw(0, 150, 100, 140, x, y)
        elif facing == 0:  # 위쪽
            character.clip_draw(0, 300, 100, 140, x, y)
        elif facing == 2:  # 아래쪽
            character.clip_draw(0, 450, 100, 140, x, y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 4
    x += dir_x * 5
    y += dir_y * 5
    delay(0.05)

close_canvas()
