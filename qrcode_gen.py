import qrcode
from _datetime import datetime


class Qrcode_gen():
    
    def __init__(self, text):
        self.text = text
        self.img = None

    def qr_code_generation(self, img_stream):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )

        qr.add_data(self.text)
        self.img = qr.make_image(fill_color="black", back_color="white").save(img_stream, format="PNG")

