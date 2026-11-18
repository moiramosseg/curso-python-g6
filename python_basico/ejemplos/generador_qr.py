import qrcode

import qrcode

# 1. Define los datos o el enlace que contendrá el QR
data = "https://google.com"

# 2. Genera el código QR
img = qrcode.make(data)

# 3. Guarda la imagen en un archivo
img.save("./python_basico/codigo_qr.png")
