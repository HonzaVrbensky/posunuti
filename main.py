x = 0
def posunuti_horizontal():
    global x
    for i in range(5):
       led.unplot(x, i)
    x = (x+1)%5
    for i in range(5):
        led.plot(x, i)

    pause(3000)

def on_button_pressed_a():
    basic.forever(posunuti_horizontal)
input.on_button_pressed(Button.A, on_button_pressed_a)

