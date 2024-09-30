import pico2d

pico2d.open_canvas()
while(True):
    character = pico2d.load_image("character.png")
    character.draw(400, 300)
    pico2d.update_canvas()
    pico2d.clear_canvas()
    pico2d.update_canvas()