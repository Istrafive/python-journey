import qrcode

# This function is used to generate the qr code based on the user inputs
def generate_qr_code(data:str, filename:str, color:str, bgcolor:str) -> None:
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill=color, back_color=bgcolor)
    img.save(filename)
    print(f"{colors['green']}QR Code successfully generated and saved as {filename}{colors['end']}")

# This conditional checks if the file is being imported on another or if it is being ran in it's main file
# Essentially if the name of the file in which the code is being ran is the main file (this one)
# it will do all of the instructions after, if not it won't
if __name__=='__main__':
    # ANSI escape code for the different colors
    colors = {
        'red': '\033[91m',
        'end': '\033[0m',
        'green': '\033[92m'
        }
    # acceptable colors that can be used to generate the qr code
    color_list = [
            'white', 'black', 'yellow', 'blue', 'orange', 'purple', 'pink', 'green', 'red', 'violet'
            ]
    
    # This loop ensures that if the user's inputs are invalid, the user can change them
    while True:
        print() # prints an empty line to avoid jumbling up lines
        link = input("Enter the link: ")
        filename = input("Enter the name of the file you wish to store the qr code in (enter as .png): ")

        # This conditional checks if the file is indeed a png
        if filename[-4:]!='.png':
            print(f"{colors['red']}This filename is not valid, try again{colors['end']}")
            continue

        # Asks the user to input a color and if the color is invalid, uses the default
        color = input("Enter the main color of the qr code (default is black): ").lower()
        if color not in color_list:
            color = 'black'

        # Asks the user to input the background color and if it is invalid, uses the default
        bgcolor = input("Enter the background color of the qr code (default is white): ").lower()
        print() # prints an empty line to avoid jumbling up lines
        if bgcolor not in color_list:
            bgcolor = 'white'

        # This conditional ensures that both colors are not the same
        if color!=bgcolor:
            generate_qr_code(link, filename, color, bgcolor)
            break

        else:
            print(
                f"""{colors['red']}
                Your color and background color can't be the same, try again
                {colors['end']}"""
                )