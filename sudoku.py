class Sudoku:
    def __init__(self):
        self.niz_podatkov = ''
    def spremeni_niz(self, niz):
        self.niz_podatkov = niz
        print('Niz vnešen')
    def vrstica(self, indeks):
        vrstica = ''
        for i in range(1,10):
            vrstica += (self.niz_podatkov[(indeks - 1)*9 + i - 1])
        print(vrstica)
        return vrstica
    def stolpec(self,indeks):
        stolpec = ''
        for i in range(0,9):
            stolpec += (self.niz_podatkov[indeks - 1 + i * 9])
        print(stolpec)
        return stolpec
    def kvadratek(self, indeks):
        kvadratek = ''
        mesto = 0
        prvikvadratek = indeks//3*3*9 + (indeks - indeks//3*3)*3-2 + 2
        for j in range(0,3):
            for i in range(0,3):
                kvadratek += self.niz_podatkov[prvikvadratek + i + mesto]
            mesto += 9
        print(kvadratek)
        return(kvadratek)
    def izpisi_sudoku(self):
        for i in range(0,9):
            niz = '{0}{1}{2} {3}{4}{5} {6}{7}{8}'.format(self.niz_podatkov[0+i*9],self.niz_podatkov[1+i*9],self.niz_podatkov[2+i*9],self.niz_podatkov[3+i*9],self.niz_podatkov[4+i*9],self.niz_podatkov[5+i*9],self.niz_podatkov[6+i*9],self.niz_podatkov[7+i*9],self.niz_podatkov[8+i*9]) 
            print(niz)
            if (i+1)%3 == 0 :
                print('')
    def pravilna_vrstica(self, indeks):
        vrsta = ''
        vrsta = self.vrstica(indeks)
        brez_ponovitev = set()
        napaka = False
        for i in vrsta:
            if i == '0':
                print('Do konca izpolni sudoku!')
                napaka = True
                return False
                break
            elif i in brez_ponovitev:
                print('Napaka - število se ponovi')
                napaka = True
                return False
                break
            else:
                brez_ponovitev.add(i)
        if napaka == False:
            print('Vrstica je pravilno izpoljena')
            return True
                
    def pravilen_kvadratek(self, indeks):
        vrsta = ''
        vrsta = self.kvadratek(indeks)
        brez_ponovitev = set()
        napaka = False
        for i in vrsta:
            if i == '0':
                print('Do konca izpolni sudoku!')
                napaka = True
                return False
                break
            
            elif i in brez_ponovitev:
                print('Napaka - število v kvadratku se ponovi')
                napaka = True
                return False
                break
            else:
                brez_ponovitev.add(i)
        if napaka == False:
            print('Kvadratek je pravilno izpolnjen')
            return True
    
    def pravilen_stolpec(self, indeks):
        vrsta = ''
        vrsta = self.stolpec(indeks)
        brez_ponovitev = set()
        napaka = False
        for i in vrsta:
            if i == '0':
                print('Do konca izpolni sudoku!')
                napaka = True
                return False
                break
            elif i in brez_ponovitev:
                print('Napaka - število se ponovi')
                napaka = True
                return False
                break
            else:
                brez_ponovitev.add(i)
        if napaka == False:
            print('Stolpec je pravilno izpoljena')
            return True
    def pravilen_sudoku(self):
        napaka = False
        prazna_vrstica = False
        for i in self.niz_podatkov:
            if i == '0':
                prazna_vrstica = True
                print('Najprej do konca izpolni sudoku!')
                
        for i in range(0,9):
            if self.pravilna_vrstica(i) == False or self.pravilen_stolpec(i) == False or self.pravilen_kvadratek(i) == False:
                napaka = True
        if prazna_vrstica == True:
             print('Najprej do konca izpolni sudoku!')
        elif napaka == False:
            print('Sudoku je pravilno izpolnjen')
        else:
            print('Sudoku ni pravilno izpolnjen')

primer = Sudoku()
#print('Vpiši svoj sudoku niz za preverbo:')
niz = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'
#niz = input()
primer.spremeni_niz(niz)
#primer.vrstica(2)
#primer.stolpec(2)
#primer.kvadratek(5)
#primer.izpisi_sudoku()
#primer.pravilna_vrstica(1)
#primer.pravilen_kvadratek(i)
primer.pravilen_sudoku()
