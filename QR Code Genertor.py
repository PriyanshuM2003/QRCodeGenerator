import qrcode
import image

qr = qrcode.QRCode(
    version=15,
    box_size=72,
    border=5
)

data = "https://priyanshum2003.github.io/Portfolio/"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("QRCode.png")
