import psutil

battery = psutil.sensors_battery()

if battery.power_plugged:
    print("Charging", battery.percent, "%")

elif not battery.power_plugged:
    print("Not charging", battery.percent, "%")
    print("Discharge time", int(battery.secsleft), "sec left")

if int(battery.percent == 10) or int(battery.percent < 10):
    if bool(battery.power_plugged == False):
        print("battery is low!", battery.percent, "%)
        if int(battery.percent == 7) or int(battery.percent < 7):
            print("**Warning**", battery.percent, "battery is very low!", "%")
            quit()
    elif bool(battery.power_plugged == True):
        print("Continue charging")
