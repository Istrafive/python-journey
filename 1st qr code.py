import qrcode

def generate_qr_code(data, filename='yourqrcode.png'):
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR Code successfully generated and saved as {filename}")


if __name__=='__main__':
    link = input("Enter the link: ")
    generate_qr_code(link)