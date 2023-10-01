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
save_pointX = []
save_pointY = []
def canvas():
    clear_canvas()
    ground.draw(TUK_X,TUK_Y)

def make_arrow():
    global  save_pointX, save_pointY
    canvas()
    for i in range(len(save_pointX)):
        arrow.clip_draw(0, 0, 50, 52, save_pointX[i], save_pointY[i])
   # update_canvas()
def character_move():
    global character_x, character_y, frame
    global  save_pointX, save_pointY
    make_arrow()
    frame = (frame + 1) % 5
    if (character_x > save_pointX[0]):
        ground.draw(TUK_X // 2, TUK_Y // 2)
        character.clip_draw(frame * 100, 10, 100, 80, character_x, character_y)  # left
        update_canvas()
    elif (character_x == save_pointX[0]):
        ground.draw(TUK_X // 2, TUK_Y // 2)
        character.clip_draw(frame * 100, 310, 100, 80, character_x, character_y)  # left_stop
        del save_pointX[0]
        del save_pointY[0]
        update_canvas()
    elif (character_x < save_pointX[0]):
        ground.draw(TUK_X // 2, TUK_Y // 2)
        arrow.clip_draw(0, 0, 50, 52, point_x, point_y)
        character.clip_draw(frame * 100, 110, 100, 80, character_x, character_y)  # right
        update_canvas()
        if (character_x == save_pointX[0]):
            ground.draw(TUK_X // 2, TUK_Y // 2)
            character.clip_draw(frame * 100, 410, 100, 80, character_x, character_y)  # right_stop
            del save_pointX[0]
            del save_pointY[0]
            update_canvas()



def handle_events():
    global  running
    global  point_x, point_y, save_pointX, save_pointY
    global  character_x, character_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            save_pointX.append(event.x)
            save_pointY.append(event.y)
            make_arrow()
            for i in range(0, 100 + 1, 4):
                t = i / 100
                character_x = (1 - t) * character_x + t * point_x
                character_y = (1 - t) * character_y + t * point_y
                character_move()
                delay(0.2)

while running:
    clear_canvas()
    ground.draw(TUK_X // 2, TUK_Y // 2)
    handle_events()
    update_canvas()
