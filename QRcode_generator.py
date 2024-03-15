import pyqrcode
from pyqrcode import QRCode

s = "https://forms.gle/MPwC5q7NsV8q1pHt8"

url = pyqrcode.create(s)

url.svg("form.svg", scale=8)
