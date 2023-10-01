from pico2d import *

TUK_X, TUK_Y = 1280, 1024
open_canvas(TUK_X, TUK_Y)

ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

frame = 0
running = True

point_x, point_y = 0, 0
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

def character_move():
    global frame
while running:
    clear_canvas()
    ground.draw(TUK_X // 2, TUK_Y // 2)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)