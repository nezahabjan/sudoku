class Sudoku:
    def __init__(self):
        self.niz_podatkov = '030601080000820001820000000200400700004000900005002006000000028100067000090204030'
    def vrstica(self, indeks):
        vrstica = ''
        for i in range(1,10):
            vrstica += (self.niz_podatkov[(indeks - 1)*9 + i - 1])
        print(vrstica)
    def stolpec(self,indeks):
        stolpec = ''
        for i in range(0,9):
            stolpec += (self.niz_podatkov[indeks - 1 + i * 9])
        print(stolpec)
    def kvadratek(self, indeks):
        kvadratek = ''
        mesto = 0
        prvikvadratek = indeks//3*3*9 + (indeks - indeks//3*3)*3-2 - 1
        print(prvikvadratek)
        for j in range(0,3):
            for i in range(0,3):
                kvadratek += self.niz_podatkov[prvikvadratek + i + mesto]
                niz = '{0} {1} {2}'.format(i + mesto, prvikvadratek + i + mesto, self.niz_podatkov[prvikvadratek + i + mesto])
                print(niz)
            mesto += 9
        print(kvadratek)
        
primer = Sudoku()
primer.vrstica(2)
primer.stolpec(2)
primer.kvadratek(5)
