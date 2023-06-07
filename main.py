import random
import string

def generowanie_imienia(dlugosc):
    samogloski = "aeiouyé"
    spolgloski = "bcdfgjklłmnprstwz"

    imie = random.choice(string.ascii_uppercase)

    for a in range(dlugosc - 1):
        if len(imie) % 2 == 0:
            imie +=random.choice(spolgloski)
        else:
            imie += random.choice(samogloski)

    return imie

def sklejanie_imienia(dlugosc, czyBaba=False, czyLiczebnik=False, czyTytul=False):
    imie=generowanie_imienia(dlugosc)

    if czyBaba:
        imie += 'a'

    if czyLiczebnik:
        liczebnik = random.randint(2, 16)
        imie += ' ' + na_rzymskie(liczebnik)

    if czyTytul:
        tytul = random.choice(['Odważny', 'Potężny', 'Zaciekły', 'Nieustraszony', "Niedźwiedzia Skóra", "Solban", "Laskonogi", "Krwawa Klinga", "Szybkopalcy", "Tchórzliwy", 'Potępiony', 'Chromy', 'Szarobrody', 'Miedzianobrody', 'Bezlitosny', 'Bandyta', 'Brzydki', 'Krwawa Siekiera', 'Czarny Książę', 'Groźny', 'Czarny Mag', 'Wędrowiec', 'Obieżyświat', "Pustynny", 'Dwa Miecze', 'Młotodzierżca'])
        imie += ' ' + tytul

    return imie


def na_rzymskie(liczebnik):
    konwersja = [(16, 'XVI'), (15, 'XV'), (14, 'XIV'), (13, 'XIII'), (12, 'XII'), (11, 'XI'), (10, 'X'), (9, 'IX'), (8, 'VIII'), (7, 'VII'), (6, 'VI'), (5, 'V'), (4, 'IV'), (3, 'III'), (2, 'II'), (1, 'I')]

    skonwersowane = ''
    while liczebnik > 0:
        for arab, rzym in konwersja:
            while liczebnik >= arab:
                skonwersowane += rzym
                liczebnik -= arab
    return skonwersowane


dlugosc_imienia = int(input("Podaj długość twojego imienia Wojownika: "))
czyBaba = input("Baba? (t/n):").lower() == "t"
czyLiczebnik = input("Czy chcesz liczebnik w imieniu? (t/n):").lower() == "t"
czyTytul = input("Czy chcesz przydomek do imienia? (t/n):").lower() == "t"

imie_wojownika=sklejanie_imienia(dlugosc_imienia, czyBaba, czyLiczebnik, czyTytul)
print("Imię twojego imienia Wojownika:", imie_wojownika)
