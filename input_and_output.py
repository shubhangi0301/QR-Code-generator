#importing pyqrcode
class Input:
    def  __init__(self, name, dic):
        self.name = name
        self.dic = dic
    def return_name(self):
        return self.name
    def return_directory(self):
        return self.dic
    
class Output:
    def  __init__(self,name, qr):
        self.qr = qr
        self.name = name
    def savefile(self, type):
        filenames = self.name.split('/')
        if type == 1 :
            filename = 'Output/' + filenames[len(filenames) - 1] + '.png'
            self.qr.save(filename)
            print("File Succesfully Saved as PNG")
        if type == 2:
            filename = 'Output/' + filenames[len(filenames) - 1] + '.svg'
            self.qr.svg(filename)
            print("File Succesfully Saved as SVG")
        