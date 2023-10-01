from pico2d import *

TUK_X, TUK_Y = 1280, 1024
open_canvas(TUK_X, TUK_Y)

ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

frame = 0
running = True

character_x, character_y = 0, 0
point_x, point_y = 0, 0
save_point = []
def make_arrow():
    pass
def character_move():
    pass

def handle_events():
    global  running
    global  point_x, point_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSE_TOUCHID:
            save_point.append(event.x, event.y)
            make_arrow()
            character_move()


while running:
    clear_canvas()
    ground.draw(TUK_X // 2, TUK_Y // 2)

    character_move()
