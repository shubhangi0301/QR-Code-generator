import pyqrcode
from pyqrcode import QRCode

# String which represents the QR code
s = "https://forms.gle/MPwC5q7NsV8q1pHt8"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the SVG file
url.svg("form.svg", scale=8)
