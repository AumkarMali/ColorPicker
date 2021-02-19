from colorthief import ColorThief
color_thief = ColorThief('enter img name')
# get the dominant color
dominant_color = color_thief.get_color(quality=1) #RGB value

print(dominant_color)