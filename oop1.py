class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    def przedstaw_sie(self):
        print(f"Jestem {self.imie} {self.nazwisko}. Mam {self.wiek} lat.")
    def urodziny(self):
        wiek_przed = self.wiek
        self.wiek += 1
        return wiek_przed
    def podwyzka(self, procent):
        placa_przed = self.placa
        self.placa *= (1+procent/100)
        return placa_przed
class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, wiek, stanowisko, placa):       
            super().__init__(imie, nazwisko, wiek)
            self.stanowisko=stanowisko
            self.placa=placa
    def przedstaw_sie(self):
        print(f"Jestem {self.imie} {self.nazwisko}. Mam {self.wiek} lat. \nPracuje na staanowisku {self.stanowisko} i zarabiam {self.placa} zł.")
#def main():
# tworzymy dwa obiekty : pierwszy klasy Osoba a drugi klasy Pracownik
Jan = Osoba("Jan", "Nowak", 48)
Adam = Pracownik("Adam", "Mickiewicz", 220, "Wieszcz", 5_000)
    
# wywołujemy metodę przedstaw_sie() na każdym z nich
Jan.przedstaw_sie()
Adam.przedstaw_sie()
print("\nAdam miał urodziny")    
wiek_Adama_przed = Adam.urodziny()
Adam.przedstaw_sie()
print(f"Wiek Adama sprzed urodzin: {wiek_Adama_przed}")
    
print("\nAdam dostał podwyżkę 20%")
placa_Adama_przed = Adam.podwyzka(20)
    
Adam.przedstaw_sie()
print(f"Płaca Adama sprzed podwyżki: {placa_Adama_przed}zł")
#if __name__ == "__main__":
 #   main()