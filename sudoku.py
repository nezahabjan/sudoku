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
    def izpisi_sudoku(self):
        for i in range(0,9):
            niz = '{0}{1}{2} {3}{4}{5} {6}{7}{8}'.format(self.niz_podatkov[0+i*9],self.niz_podatkov[1+i*9],self.niz_podatkov[2+i*9],self.niz_podatkov[3+i*9],self.niz_podatkov[4+i*9],self.niz_podatkov[5+i*9],self.niz_podatkov[6+i*9],self.niz_podatkov[7+i*9],self.niz_podatkov[8+i*9]) 
            print(niz)
            if (i+1)%3 == 0 :
                print('')
                
primer = Sudoku()
primer.vrstica(2)
primer.stolpec(2)
primer.kvadratek(5)
primer.izpisi_sudoku()
