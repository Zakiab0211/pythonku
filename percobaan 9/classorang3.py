class Orang:
    def __init__(mysillyobject, nama, usia):
        mysillyobject.nama = nama
        mysillyobject.usia = usia
        
    def myfunc(abc):
        print("Hello namaku " + abc.nama)
        
p1 = Orang("John", 36)

p1.myfunc()
