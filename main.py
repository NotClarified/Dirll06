from pico2d import *

TUK_X, TUK_Y = 1280, 1024
open_canvas(TUK_X, TUK_Y)

ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

frame = 0
running = True

point_x, point_y = 0, 0
character_x, character_y = 0, 0
arrows = []

def handle_events():
    global running, arrows
    global point_x, point_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            point_x, point_y = event.x, TUK_Y - 1 - event.y
            arrow.clip_draw(0, 0, 50, 52, point_x, point_y)
            for ax, ay in arrows:
                arrow.clip_draw(0, 0, 50, 52, ax, ay)
            update_canvas()


def mouse_events():
    global running
    global point_x, point_y
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            point_x, point_y = event.x, TUK_Y - 1 - event.y
            arrows.append((point_x, point_y))

def character_move():
    global  point_x, point_y
    global character_x, character_y, frame
    global running, arrows

    if len(arrows) > 0:
        target_x, target_y = arrows[0]
        for i in range(0, 100 + 1, 4):
            frame = (frame + 1) % 8
            t = i / 100
            if i == 0:
                character_x, character_y = 0, 0
            character_x = (1 - t) * character_x + t * target_x
            character_y = (1 - t) * character_y + t * target_y
            ground.draw(TUK_X // 2, TUK_Y // 2)
            if character_x > target_x:
                ground.draw(TUK_X // 2, TUK_Y // 2)
                character.clip_draw(frame * 100, 10, 100, 80, character_x, character_y)  # left
            elif character_x == target_x:
                ground.draw(TUK_X // 2, TUK_Y // 2)
                character.clip_draw(frame * 100, 310, 100, 80, character_x, character_y)  # left_stop
                character_x, character_y = target_x, target_y
                arrows.pop(0)
            elif character_x < target_x:
                ground.draw(TUK_X // 2, TUK_Y // 2)
                character.clip_draw(frame * 100, 110, 100, 80, character_x, character_y)  # right
        for ax, ay in arrows:
            arrow.clip_draw(0, 0, 50, 52, ax, ay)  # 클릭한 손가락
        arrow.clip_draw(0, 0, 50, 52, point_x, point_y)  # 움직이는 손가락
        update_canvas()
        delay(0.2)



while running:
    ground.draw(TUK_X // 2, TUK_Y // 2)
    mouse_events()
    character_move()
    handle_events()  # 핸들 이벤트를 여기서
