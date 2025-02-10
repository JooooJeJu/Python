from collections import defaultdict, deque
from PIL import Image
import numpy as np
import random
import os 
from pathlib import Path



# Kierunki sąsiedztwa (8-kierunkowe)
kierunki = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]

def zbuduj_graf_sasiedztw(obraz):
    n = len(obraz)
    graf = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if obraz[i][j] == 1:  # Czarny piksel
                for dx, dy in kierunki:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < n and obraz[x][y] == 1:
                        graf[(i, j)].append((x, y))
    return graf

def rozlaczne_plamy(obraz):
    n = len(obraz)
    odwiedzone = [[False for _ in range(n)] for _ in range(n)]
    licznik = 0
    
    def bfs(start_i, start_j):
        kolejka = deque([(start_i, start_j)])
        odwiedzone[start_i][start_j] = True
        while kolejka:
            i, j = kolejka.popleft()
            for dx, dy in kierunki:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < n and obraz[x][y] == 1 and not odwiedzone[x][y]:
                    odwiedzone[x][y] = True
                    kolejka.append((x, y))
    
    for i in range(n):
        for j in range(n):
            if obraz[i][j] == 1 and not odwiedzone[i][j]:
                bfs(i, j)
                licznik += 1
    return licznik

def kolorowanie(obraz):
    n = len(obraz)
    #tworzenie macierzy z samych false i 0  n*n
    odwiedzone = [[False for _ in range(n)] for _ in range(n)]
    kolor = [[0 for _ in range(n)] for _ in range(n)]
    aktualny_kolor = 1
    
    def bfs(start_i, start_j, aktualny_kolor):
        kolejka = deque([(start_i, start_j)])
        odwiedzone[start_i][start_j] = True
        kolor[start_i][start_j] = aktualny_kolor
        while kolejka:
            i, j = kolejka.popleft()
            for dx, dy in kierunki:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < n and obraz[x][y] == 1 and not odwiedzone[x][y]:
                    odwiedzone[x][y] = True
                    kolor[x][y] = aktualny_kolor
                    kolejka.append((x, y))
    
    for i in range(n):
        for j in range(n):
            if obraz[i][j] == 1 and not odwiedzone[i][j]:
                aktualny_kolor += 1
                bfs(i, j, aktualny_kolor)
    return kolor

# Przykładowy obraz (1 - czarny piksel, 0 - biały piksel)
#obraz = [
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
#]

#pojawił się problem w którym mimo iż plik png znajduje się w tym samym folderze co skrypt 
#to i tak go nie widział dlatego biblioteka pathlib i "trywialne" rozwiązanie problemu 

#Określenie ścieżki do folderu, w którym znajduje się skrypt
sciezka_skrypt = Path(__file__).resolve().parent  # Ścieżka do katalogu skryptu

# Ścieżka do pliku w tym samym folderze
# ważne żeby obraz był N*N żeby wynik nie był zakłamany, względem tego co widzimy a jakie odpowiedzi daje program, 
# obraz 50*60 widzimy 6 plam aczkolwiek szósta plama znajduje się na pozycji >50, program zwróci żę znalazł 5 rozłącznych plam a nie 6 
# gdy nie jest N*N to program i tak zadziała ale "wytnie" tylko kwadrat którego n to krótszy bok obrazu np. 40x50 to obraz będzie 40x40
sciezka_obraz = sciezka_skrypt / "pixels.png"
sciezka_wyjscie = sciezka_skrypt / 'output_pixels.png'
#wczytanie obrazu z plik
img = Image.open(sciezka_obraz).convert("RGB")  # Wczytaj obraz


#przerobienie na macierz 
obraz = np.array(img)
obraz = np.all(obraz[:, :, :] == [0, 0, 0], axis=-1).astype(int)


# Zbuduj graf sąsiedztwa dla czarnych pikseli 
graf = zbuduj_graf_sasiedztw(obraz)
print("Graf sąsiedztwa:", graf)

# Znajdź liczbę rozłącznych czarnych plam na tym obrazie

liczba_plam = rozlaczne_plamy(obraz)
print("Liczba rozłącznych czarnych plam:", liczba_plam)

# Przypisz wszystkim czarnym pikselom atrybut koloru
kolory = np.array(kolorowanie(obraz))
print("Obraz z przypisanymi kolorami:")
for row in kolory:
    print(row)
    



# "zabawa" z biblioteką PIL, przy większych obrazach z danych tekstowych trudno jest cokolwiek wyczytać 
# więc graficzne przedstawienie rozłącznych plam jest przyjemniejsze dla oka


unikalne = np.unique(kolory)
unikalne = unikalne[unikalne > 0]

# Tworzenie mapy kolorów (losowe kolory dla każdej wartości)

mapa = {value: tuple(random.randint(0, 255) for _ in range(3)) for value in unikalne}
#mapa[0] = (255, 255, 255) #z powrotem białe tło ale na czarnym wyglada lepiej, lepszy kontrast

# Pobranie wymiarów obrazu
wysokosc, szerokosc = kolory.shape

# Tworzenie pustej macierzy obrazu w RGB
image_array = np.zeros((wysokosc, szerokosc, 3), dtype=np.uint8)

# Przypisywanie kolorów do obrazu
for wartosc, kolor in mapa.items():
    maska = kolory == wartosc  # Maska miejsc, gdzie występuje dany numer
    image_array[maska] = np.array(kolor, dtype=np.uint8)  # Przypisanie koloru

# Tworzenie obrazu i zapisanie go do pliku
img = Image.fromarray(image_array)
img.save(sciezka_wyjscie)
img.show()

    

    
    
'''
    Graf sąsiedztwa: Dla każdego czarnego piksela sprawdzamy jego 8 sąsiadów. Jeśli sąsiad jest czarny, dodajemy go do listy sąsiedztwa.

    Liczba rozłącznych czarnych plam: Używamy BFS (przeszukiwanie wszerz) do znalezienia wszystkich połączonych czarnych pikseli. Każde nowe wywołanie BFS oznacza nową plamę.

    Przypisanie kolorów: Każdej plamie przypisujemy unikalny kolor (liczbę), który jest używany do oznaczania wszystkich pikseli w tej plamie.
'''