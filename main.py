def on_button_pressed_a():
    global dimm
    dimm = dimm + 10
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global dimm
    dimm = dimm - 10
input.on_button_pressed(Button.B, on_button_pressed_b)

dimm = 0
dimm = 0

def on_forever():
    global dimm
    if dimm < 0:
        dimm = 0
    elif dimm > 255:
        dimm = 255
    led.set_brightness(dimm)
    basic.set_led_color(basic.rgbw(0, dimm, 0, 0))
    basic.show_icon(IconNames.HEART)
basic.forever(on_forever)
