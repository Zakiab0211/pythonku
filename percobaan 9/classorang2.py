class Orang:
    
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

    def myfunc(self):
        print("Hello namaku " + self.nama)
        
p1 = Orang("John", 36)

p1.myfunc()
