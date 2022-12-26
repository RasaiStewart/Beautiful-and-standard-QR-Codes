import segno

wifi_settings = {
    "ssid": '(Wifi Name)',
    "password": '(Wifi Password)',
    "security": 'WPA',
}
wifi = segno.helpers.make_wifi(**wifi_settings)
wifi.save("Wifi.png", dark="yellow", light="#323524", scale=8)