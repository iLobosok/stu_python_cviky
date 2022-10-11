def minimalne_cislo(a, b, c):
    a = int(input('input a : '))
    b = int(input('input b : '))
    c = int(input('input c : '))

    minimalne_cislo = 0

    if a < b and a < c :
        minimalne_cislo = a
    if b < a and b < c :
        minimalne_cislo = b
    if c < a and c < b :
        minimalne_cislo = c

    print(minimalne_cislo, "je minimalne cislo")
minimalne_cislo(input, input, input)