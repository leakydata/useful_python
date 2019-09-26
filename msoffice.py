# Color converting fuctions; convert from BGR decimal colors in Office object model to rgb, hex
def int_color_to_hex(long_color):
    red = int(long_color%256) # red
    green = int((long_color/256)%256)
    blue = int((long_color/65536)%256)
    #print(hex(red),hex(green),hex(blue))
    return '%02x%02x%02x' % (red,green,blue)

def int_color_to_rgb(long_color):
    red = int(long_color%256) # red
    green = int((long_color/256)%256)
    blue = int((long_color/65536)%256)
    return (red,green,blue)

def rgb_color_to_int(rgb):
    bgr = (rgb[2], rgb[1], rgb[0])
    strValue = '%02x%02x%02x' % bgr
    iValue = int(strValue, 16)
    return iValue

def hex_color_to_int(hex_color):
    #Split the hex by the nth character i.e. 2 and convert the hex to decimal
    rgb = [int(hex_color[i:i+2],16) for i in range(0, len(hex_color), 2)]
    bgr = (rgb[2], rgb[1], rgb[0])
    strValue = '%02x%02x%02x' % bgr
    iValue = int(strValue, 16)
    return iValue

def hex_color_to_rgb(hex_color):
    #Split the hex by the nth character i.e. 2 and convert the hex to decimal
    r,g,b = [int(hex_color[i:i+2],16) for i in range(0, len(hex_color), 2)]
    return (r,g,b)
