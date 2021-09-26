input.onButtonPressed(Button.A, function () {
    dimm = dimm + 10
})
input.onButtonPressed(Button.B, function () {
    dimm = dimm - 10
})
let dimm = 0
dimm = 0
basic.forever(function () {
    if (dimm < 0) {
        dimm = 0
    } else if (dimm > 255) {
        dimm = 255
    }
    led.setBrightness(dimm)
    basic.setLedColor(basic.rgbw(
    0,
    dimm,
    0,
    0
    ))
    basic.showIcon(IconNames.Heart)
})
