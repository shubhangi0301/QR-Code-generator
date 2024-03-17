#importing pyqrcode
import pyqrcode

class Generate:
    def __init__(self, data, size, error):
        self.data = data
        self.size = size
        self.error = error
    
    def generate_qr(self, filename):
        qr = pyqrcode.create(self.data, error=self.error, version=self.size, mode='binary')
        qr.svg('Output/' + filename + '.svg')
