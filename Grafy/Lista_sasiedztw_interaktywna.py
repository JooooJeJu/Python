"""
Program do zarządzania grafem nieskierowanym, umożliwiający wykonywanie różnych operacji na jego strukturze.
Program działa interaktywnie, udostępniając użytkownikowi menu do wyboru różnych operacji.
"""

import networkx as nx
import matplotlib.pyplot as plt

def dodaj_wierzcholek(slownik):
    a = input("Podaj etykiete wierzchołka: ")
    if a not in slownik:
        slownik[a] = []
    else:
        print("Klucz istnieje podaj inny!")
        dodaj_wierzcholek(slownik)

def usun_wierzcholek(slownik):
    a = input("Podaj etykietę wierzchołka do usunięcia: ")
    if a in slownik:
        del slownik[a]
        for v in slownik:
            if a in slownik[v]:  # Sprawdzenie, czy wierzchołek istnieje w liście sąsiadów
                slownik[v].remove(a)
        print(f"Wierzchołek {a} został usunięty.")
    else:
        print("Nie istnieje taki wierzchołek!")

"""
Stara funkcja która działała tylko na grafie o wierzchołkach liczbowych 

def usun_wierzcholek(slownik):
    a = input("Podaj etykietę wierzchołka do usunięcia: ")
    if a in slownik:
        del slownik[a]
        for v in slownik:
            slownik[v].remove(a)
    else:
        print("Nie istnieje taki wierzchołek!")
        usun_wierzcholek(slownik)
"""
def dodaj_krawedz(slownik):
    a = input("Podaj etykietę pierwszego wierzchołka: ")
    b = input("Podaj etykietę drugiego wierzchołka: ")
    if a in slownik and b in slownik:
        slownik[a].append(b)
        slownik[b].append(a)
    else:
        print("Krawędź juz istnieje!")
        dodaj_krawedz(slownik)
    

def usun_krawedz(slownik):
    a = input("Podaj etykietę pierwszego wierzchołka: ")
    b = input("Podaj etykietę drugiego wierzchołka: ")
    if a in slownik[b]:
        slownik[b].remove(a)
    if b in slownik[a]:
        slownik[a].remove(b)

def konwersja(slownik, wynik=[]):
    # Mapowanie wierzchołków na indeksy
    wierzcholki = list(slownik.keys())
    indeksy = {wierzcholek: i for i, wierzcholek in enumerate(wierzcholki)}
    
    wielkosc = len(wierzcholki)
    macierz = [[0 for _ in range(wielkosc)] for _ in range(wielkosc)]
    
    for key, val in slownik.items():
        for x in val:
            macierz[indeksy[key]][indeksy[x]] = 1
    
    wynik = macierz
    for i in range(len(macierz)):
        print(macierz[i])
    return wynik

"""
Stara konwersja z zajęć które działa tylko na wierzchołkach liczbowych
def konwersja(slownik,wynik=[]):
    wielkosc = len(slownik)
    macierz = [[0 for _ in range(wielkosc)] for _ in range(wielkosc)]
    for key,val in slownik.items():
        for x in val:
            macierz[key][x] = 1
    wynik = macierz
    for i in range(0,len(macierz)):
        print(macierz[i])
    return wynik
"""

def przeszukanie_dfs(graf, start, print_vertices=True):
    odwiedzone = set()
    glebokosci = {}
    def dfs(wierzcholek, glebokosc):
        odwiedzone.add(wierzcholek)
        glebokosci[wierzcholek] = glebokosc
        if print_vertices:
            print(f"{wierzcholek} (głębokość: {glebokosc})", end=' ')  
        
        for sasiad in graf[wierzcholek]:
            if sasiad not in odwiedzone:
                dfs(sasiad, glebokosc + 1)
    
    dfs(start, 0)
    return odwiedzone, glebokosci

def sprawdz_spojnosc(graf):
    if not graf:
        return True  

    start = next(iter(graf))
    odwiedzone,_ = przeszukanie_dfs(graf, start, print_vertices=False)

    return len(odwiedzone) == len(graf)

def znajdz_skladowe(slownik):
    #Zmodyfikowana funkcja DFS
    def dfs(wierzcholek, odwiedzone, skladowa):
        odwiedzone.add(wierzcholek)
        skladowa.append(wierzcholek)
        for sasiad in slownik.get(wierzcholek, []):
            if sasiad not in odwiedzone:
                dfs(sasiad, odwiedzone, skladowa)

    odwiedzone = set()
    spojne_skladowe = []

    for wierzcholek in slownik.keys():
        if wierzcholek not in odwiedzone:
            skladowa = []
            dfs(wierzcholek, odwiedzone, skladowa)
            spojne_skladowe.append(skladowa)

    return spojne_skladowe

def wyswietl_graf_plot(slownik):
    G = nx.Graph(slownik)
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500)
    plt.show()

def zapisz_graf(sciezka, slownik):
    """
    Zapisuje graf do pliku tekstowego w formacie:
    wierzchołek:sąsiad1,sąsiad2,...
    """
    try:
        with open(sciezka, 'w') as f:
            for wierzcholek, sasiedzi in slownik.items():
                linia = f"{wierzcholek}:{','.join(map(str, sasiedzi))}\n"
                f.write(linia)
        print(f"Graf został zapisany do pliku: {sciezka}")
    except Exception as e:
        print(f"Błąd podczas zapisywania grafu: {e}")

def wczytaj_graf(sciezka,slownik={}):
    f = open(sciezka,'r')
    for line in f:
        linijka = line
        linijka = linijka.strip()
        slownik[linijka[0]] = []
        for i in range(2,len(linijka)):
            if linijka[i] != ",":
                slownik[linijka[0]].append(linijka[i])
    f.close()
    return slownik  


    

def program(graf):
    while True:
        print("1. Dodaj wierzchołek")
        print("2. Usuń wierzchołek")
        print("3. Dodaj krawędź")
        print("4. Usuń krawędź")
        print("5. Wyświetl graf w formie tekstowej")
        print("6. Wyświetl graf w formie wykresu")
        print("7. Konwertuj na Macierz")
        print("8. Sprawdz spójność")
        print("9. Znajdz spójne składowe")
        print("10. Przeszukiwanie w głąb")
        print("11. Zapisz graf do pliku z którego został wczytany")
        print("12. Koniec")
        
        a = int(input("Podaj jaką operacje chcesz wykonać: "))
        
        if a == 1:
            dodaj_wierzcholek(graf)
            print("Wierzchołek dodany.")
        elif a == 2:
            usun_wierzcholek(graf)
            print("Wierzchołek usunięty.")
        elif a == 3:
            dodaj_krawedz(graf)
            print("Krawędź dodana.")
        elif a == 4:
            usun_krawedz(graf)
            print("Krawędź usunięta.")
        elif a == 5:
            print(graf)
        elif a == 6:
            wyswietl_graf_plot(graf)
        elif a == 7:
            konwersja(graf)
            print("Konwersja Udana")
        elif a == 8:
            if sprawdz_spojnosc(graf):
                print("\nGraf jest spójny.")
            else:
                print("\nGraf nie jest spójny.")
        elif a == 9:
            spojne_skladowe = znajdz_skladowe(graf)
            print("Spójne składowe grafu:")
            for skladowa in spojne_skladowe:
                print(skladowa)
        elif a == 10:
            a = input("Podaj etykiete wierzchołka od którego chcesz rozpocząć przeszukiwanie: ")
            odwiedzone, glebokosci = przeszukanie_dfs(graf, a)
            print("\nGłębokości wierzchołków:")
            for wierzcholek, glebokosc in glebokosci.items():
                print(f"{wierzcholek}: {glebokosc}")
        elif a == 11:
            zapisz_graf(sciezka, graf)
        elif a == 12:
            print("Koniec")
            break
        else:
            print("Nieprawidłowa operacja!")
        
sciezka = "C:\\Users\\mich4\\OneDrive\\Pulpit\\Algo\\Sprawozdanie_3_Grafy_Iciek_Michał\\Graf_1.txt"

graf = wczytaj_graf(sciezka)

program(graf)


