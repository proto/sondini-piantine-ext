let sonda = ""
let moisture = 0
let h2o = ""
let temp = ""
let lum = ""
power.fullPowerEvery(3600000, function () {
    radio.setTransmitPower(7)
    radio.setGroup(97)
    radio.setTransmitSerialNumber(true)
    led.setBrightness(100)
    sonda = "potus"
    moisture = pins.analogReadPin(AnalogPin.P1)
    h2o = "h2o"
    temp = "temp"
    lum = "lum"
    if (true) {
        radio.sendString(sonda)
        radio.sendValue(h2o, moisture)
        radio.sendValue(temp, input.temperature())
        radio.sendValue(lum, input.lightLevel())
    }
    if (moisture <= 400) {
        basic.showIcon(IconNames.Sad)
        basic.pause(1000)
        basic.clearScreen()
    }
    power.lowPowerRequest()
})
