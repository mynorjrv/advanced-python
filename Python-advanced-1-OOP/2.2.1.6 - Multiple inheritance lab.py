class Scanner:
    def scan(self):
        print('scan() method from Scanner class')
        
class Printer:
    def print(self):
        print('print() method from Printer class')
        
class Fax:
    def send(self):
        print('send() method from Fax class')
    
    def print(self):
        print('print() method from Fax class')
        


class MFD_SPF(Scanner, Printer, Fax):
    pass

class MFD_SFP(Scanner, Fax, Printer):
    pass

spf = MFD_SPF()
spf.scan()
spf.print()
spf.send()

sfp = MFD_SFP()
sfp.scan()
sfp.print()
sfp.send()