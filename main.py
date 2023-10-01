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
    global running
    global point_x, point_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            point_x, point_y = event.x, TUK_Y - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            point_x, point_y = event.x, TUK_Y - 1 - event.y
            arrows.append((point_x, point_y))
            character_move()

def character_move():
    global  point_x, point_y
    global character_x, character_y, frame
    frame = (frame + 1) % 8
    clear_canvas()
    ground.draw(TUK_X // 2, TUK_Y // 2)
    for i in range(0, 100 + 1, 4):
        t = i / 100
        for ax, ay in arrows:
            arrow.clip_draw(0, 0, 50, 52, ax, ay)
        character_x = (1 - t) * character_x + t * point_x
        character_y = (1 - t) * character_y + t * point_y
        if character_x > point_x:
            character.clip_draw(frame * 100, 10, 100, 80, character_x, character_y)  # left
        elif character_x == point_x:
            character.clip_draw(frame * 100, 310, 100, 80, character_x, character_y)  # left_stop
            del arrows[0]
        elif character_x < point_x:
            character.clip_draw(frame * 100, 110, 100, 80, character_x, character_y)  # right
        update_canvas()
        delay(0.05)


while running:
    clear_canvas()
    ground.draw(TUK_X // 2, TUK_Y // 2)
    update_canvas()
    handle_events()
