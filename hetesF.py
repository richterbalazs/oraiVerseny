# 7. feladat:A feladathoz az adatokat a Mikulassszan.txt állományban találod. Ez egy rövid nyilvántartás, arról, hogy ki utazik a szánon.

def hetedik():

    beolvas = open("fajlok/Mikulasszan.txt", "r", encoding="utf-8")
    nev = beolvas.readline(1)
    magassag = beolvas.readline(2)
    print(nev, magassag)