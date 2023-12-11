# 4. feladat: Nyisd meg a KariVers.txt állományt és egészítsd ki a verset az utolsó versszakával a KariVers2.txt állományba.

def negyedik():

    beFajl = open("fajlok/KariVers.txt", "r", encoding="utf-8")
    versEleje = beFajl.read()
    beFajl.close()
    return versEleje

def hozzafuz():

    beleIr = open("fajlok/KariVers2.txt", "w", encoding="utf-8")
    versEleje = negyedik()
    print(versEleje)
    beleIr.write(versEleje)
    beleIr.write("\n\n„Tiszta öröm tüze átég a szemeken,\na harangjáték szól, \néjféli üzenet:\nKis Jézuska született!”")
    beleIr.close()



