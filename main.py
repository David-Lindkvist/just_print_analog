def on_forever():
    basic.pause(2000)
    signal = pins.analog_read_pin(AnalogPin.P2)
    basic.show_number(signal)
basic.forever(on_forever)
