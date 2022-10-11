def pocet_parnych(n):
    for i in range(n):
        vstup = input()
        cislo = int(vstup)
        if cislo % 2 == 0:
            print("parna")
        elif cislo % 2 == 1: 
            print("neparna")
pocet_parnych(5)