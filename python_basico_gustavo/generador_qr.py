import  qrcode
from PIL import Image

data = "https://github.com"

img = qrcode.make(data)
qr = qrcode.QRCode(
    version=1,  # tamaño del QR (1 a 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # nivel de corrección de errores
    box_size=10,  # tamaño de cada cuadro
    border=4,     # grosor del borde
)

# Añadir datos
qr.add_data(data)
qr.make(fit=True)

# Generar imagen
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")
print("Código QR generado y guardado como 'qr_code.png'")