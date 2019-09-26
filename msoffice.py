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


# Detect the closest color in a dictionary of potential colors to a test color

# Calculates the euclidian distance of the RGB(x,y,z) color treated as a vector
def distance(c1, c2):
    (r1,g1,b1) = c1
    (r2,g2,b2) = c2
    return math.sqrt((r1 - r2)**2 + (g1 - g2) ** 2 + (b1 - b2) **2) #Euclidean Distance between RGB values

# Dictionary of potential colors (can have as many or as few colors as you like
rgb_code_dictionary = {
    (255, 255, 255): 'Whitish', #WHITE
    (255, 0, 0): 'Reddish', #RED
    #(255, 102, 0):'Orangelike', #ORANGE
    (255, 255, 0): 'Yellowy', #YELLOW
    #(139,69,19): 'Brownish',
    (0, 255, 0): 'Greenish', #GREEN
    (0, 0, 255): 'Blueish', #BLUE
    #(102, 0, 255):'Purplish', #PURPLE
    (0, 64, 80):'Grey Blue', #Grey Blue
    (0, 0, 0): 'Blackish' #BLACK
    }

# Returns the closest color in the color code dictionary based on euclidean distance in vector space
def rgb_closest_color(test_color):
    colors = list(rgb_code_dictionary.keys())
    closest_colors = sorted(colors, key=lambda color: distance(color, test_color))
    closest_color = closest_colors[0]
    return rgb_code_dictionary[closest_color]

