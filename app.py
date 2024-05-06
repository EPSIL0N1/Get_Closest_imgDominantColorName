from colorthief import ColorThief
import matplotlib.pyplot as plt
import webcolors

ct = ColorThief("ColorName_Detection/blood2.jpeg")
dominant_color = ct.get_color(quality=1)

def closest_color(rgb):
    differences = {}
    for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = webcolors.hex_to_rgb(color_hex)
        differences[sum([(r - rgb[0]) ** 2,
                        (g - rgb[1]) ** 2,
                        (b - rgb[2]) ** 2])] = color_name
        
    return differences[min(differences.keys())]
    
print(closest_color(dominant_color))