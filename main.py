moisture = 0

def on_log_full():
    radio.set_group(77)
    radio.set_transmit_serial_number(True)
    radio.send_string("" + control.device_name() + "\"LOG FULL\"")
    power.low_power_request()
datalogger.on_log_full(on_log_full)

def on_button_pressed_a():
    basic.show_string("A:" + ("" + str(moisture)))
    basic.clear_screen()
    power.low_power_request()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    power.low_power_enable(LowPowerEnable.PREVENT)
    basic.show_string("LOG RESET!")
    datalogger.delete_log(datalogger.DeleteType.FULL)
    control.reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("L:" + ("" + str(input.light_level())))
    basic.show_string("T:" + ("" + str(input.temperature())))
    basic.clear_screen()
    power.low_power_request()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.show_string(control.device_name())
    basic.clear_screen()
    power.low_power_request()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_full_power_every():
    global moisture
    if input.light_level() > 50:
        radio.set_group(77)
        radio.set_transmit_serial_number(True)
        led.set_brightness(99)
        datalogger.include_timestamp(FlashLogTimeStampFormat.MILLISECONDS)
        datalogger.set_column_titles("temp", "lum", "h2o")
        moisture = pins.analog_read_pin(AnalogPin.P1)
        if True:
            radio.send_value(control.device_name(), input.temperature())
            radio.send_value(control.device_name(), input.light_level())
        if moisture <= 400:
            radio.send_value(control.device_name(), moisture)
            basic.show_icon(IconNames.SAD)
            basic.pause(500)
            basic.clear_screen()
            music.play(music.builtin_playable_sound_effect(soundExpression.yawn),
                music.PlaybackMode.IN_BACKGROUND)
        else:
            radio.send_value(control.device_name(), moisture)
        datalogger.log(datalogger.create_cv("temp", input.temperature()),
            datalogger.create_cv("lum", input.light_level()),
            datalogger.create_cv("h2o", moisture))
    power.low_power_request()
power.full_power_every(60000, on_full_power_every)
