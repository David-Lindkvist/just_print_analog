basic.forever(function on_forever() {
    basic.pause(2000)
    let signal = pins.analogReadPin(AnalogPin.P2)
    basic.showNumber(signal)
})
