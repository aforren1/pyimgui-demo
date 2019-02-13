from psychopy import core, visual, event
import imgui
from pyglet_imgui_renderer import PygletRenderer


win = visual.Window(fullscr=True)

cir = visual.Circle(win, fillColor='red', radius=(0.2, 0.3))
#rad = visual.RadialStim(win, size=(0.2, 0.2))
#txt = visual.TextStim(win, text='foo', pos=(0, 0.3))
impl = PygletRenderer(win.backend.winHandle)
text_val = 'Write ID Here.'
dlg_width, dlg_height = 400, 150

win.flip()
while not event.getKeys(['escape']):
    imgui.new_frame()
    imgui.show_test_window()
    imgui.set_next_window_size(dlg_width, dlg_height)
    imgui.set_next_window_position(win.size[0]//2 - dlg_width//2,
                                   (win.size[1] * 3)//4 - dlg_height//2)
    imgui.begin("Custom window", False, flags=imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_COLLAPSE)
    imgui.text('ID:')
    imgui.same_line()
    changed, text_val = imgui.input_text('', text_val, 256)
    if imgui.button('OK'):
        print(text_val)
        core.quit()
    imgui.same_line()
    if imgui.button('Exit'):
        core.quit()
    imgui.end()
    cir.draw()
    # rad.draw()
    imgui.render()
    impl.render(imgui.get_draw_data())
    # txt.draw()
    win.flip()

impl.shutdown()
core.quit()
