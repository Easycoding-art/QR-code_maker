import qrcode
import os

def create(data, file_name) :
    if not os.path.exists('QR-codes') :
        os.mkdir('QR-codes')
    img = qrcode.make(data)
    type(img)  # qrcode.image.pil.PilImage
    img.save('QR-codes/'+file_name+".png")