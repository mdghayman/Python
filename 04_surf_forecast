#Decision tool to determine whether it's worth getting out of bed for a surf

wind_speed = int(input("What's the wind speed, in kilometres per hour?"))

wind_point = str(input("Where is the wind coming from?\n"
                       "Enter 'off' for offshore / 'on' for onshore:"))

swell_size = int(input("What's the swell size, in feet?"))

#swell_time = int(input("How much time between swells, in seconds?"))

if swell_size>3 and (wind_point=='off' or wind_speed < 10):
    print("Gnarly! Go surfing!")
else:
    print("Maybe you should sleep in!")
