import time
import matplotlib.pyplot as plt
import random

# Funkcja do ładowania listy z pliku
def zaladuj_liste(sciezka):
    with open(sciezka, 'r') as f:
        return [int(line.strip()) for line in f]

# Pierwsza implementacja wyszukiwania binarnego
def binarne2(lista, cel):
    a = 0
    b = len(lista) - 1
    iteracje = 0
    while a < b:
        iteracje += 1
        srodek = (a + b) // 2
        if lista[srodek] < cel:
            a = srodek + 1
        else:
            b = srodek
    if a < len(lista) and lista[a] == cel:
        return a, iteracje
    return -1, iteracje

# Druga implementacja wyszukiwania binarnego
def binarne3(lista, cel):
    a = 0
    b = len(lista) - 1
    iteracje = 0
    while a <= b:
        iteracje += 1
        srodek = (a + b) // 2
        if lista[srodek] == cel:
            return srodek, iteracje
        elif lista[srodek] < cel:
            a = srodek + 1
        else:
            b = srodek - 1
    return -1, iteracje

# Funkcja do analizy i wizualizacji
def analiza(sciezki):
    plt.style.use('seaborn-v0_8-whitegrid')  # Ustawienie stylu

    rozmiary_list = []  # Lista rozmiarów list wczytywanych z plików
    czasy2_lista = []
    czasy3_lista = []
    iteracje2_lista = []
    iteracje3_lista = []

    etykiety_plikow = []  # Lista etykiet nazw plików

    # Przechodzenie przez pliki
    for idx, sciezka in enumerate(sciezki):
        lista = zaladuj_liste(sciezka)
        lista.sort()
        etykiety_plikow.append(sciezka.split('\\')[-1])  # Nazwa pliku jako etykieta
        rozmiary_list.extend([idx] * 100)  # Mniejsza liczba punktów (100 zamiast 250)

        cele = random.sample(range(min(lista), max(lista)), 100)  # 100 losowych wartości

        for cel in cele:
            # binarne2
            start = time.perf_counter()
            _, iteracje2 = binarne2(lista, cel)
            end = time.perf_counter()
            czasy2_lista.append((end - start) * 1000)  # Konwersja na milisekundy
            iteracje2_lista.append(iteracje2)

            # binarne3
            start = time.perf_counter()
            _, iteracje3 = binarne3(lista, cel)
            end = time.perf_counter()
            czasy3_lista.append((end - start) * 1000)  # Konwersja na milisekundy
            iteracje3_lista.append(iteracje3)
    # Tworzenie okna z czterema podwykresami (2x2)
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Porównanie dwóch implementacji wyszukiwania binarnego', fontsize=16)

    # Wykres czasu dla binarne2
    axes[0, 0].scatter(rozmiary_list, czasy2_lista, color='red', s=10, alpha=0.6, label='binarne2')
    axes[0, 0].set_xticks(range(len(sciezki)))
    axes[0, 0].set_xticklabels(etykiety_plikow, rotation=45)
    axes[0, 0].set_xlabel('Wielkość pliku')
    axes[0, 0].set_ylabel('Czas [ms]')
    axes[0, 0].set_title('Czas wyszukiwania (binarne2)')
    axes[0, 0].legend()

    # Wykres liczby iteracji dla binarne2
    axes[0, 1].scatter(rozmiary_list, iteracje2_lista, color='red', s=10, alpha=0.6, label='binarne2')
    axes[0, 1].set_xticks(range(len(sciezki)))
    axes[0, 1].set_xticklabels(etykiety_plikow, rotation=45)
    axes[0, 1].set_xlabel('Wielkość pliku')
    axes[0, 1].set_ylabel('Liczba iteracji')
    axes[0, 1].set_title('Liczba iteracji (binarne2)')
    axes[0, 1].legend()

    # Wykres czasu dla binarne3
    axes[1, 0].scatter(rozmiary_list, czasy3_lista, color='blue', s=10, alpha=0.6, label='binarne3')
    axes[1, 0].set_xticks(range(len(sciezki)))
    axes[1, 0].set_xticklabels(etykiety_plikow, rotation=45)
    axes[1, 0].set_xlabel('Wielkość pliku')
    axes[1, 0].set_ylabel('Czas [ms]')
    axes[1, 0].set_title('Czas wyszukiwania (binarne3)')
    axes[1, 0].legend()

    # Wykres liczby iteracji dla binarne3
    axes[1, 1].scatter(rozmiary_list, iteracje3_lista, color='blue', s=10, alpha=0.6, label='binarne3')
    axes[1, 1].set_xticks(range(len(sciezki)))
    axes[1, 1].set_xticklabels(etykiety_plikow, rotation=45)
    axes[1, 1].set_xlabel('Wielkość pliku')
    axes[1, 1].set_ylabel('Liczba iteracji')
    axes[1, 1].set_title('Liczba iteracji (binarne3)')
    axes[1, 1].legend()

    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Poprawienie odstępów
    plt.show()

    # Tworzenie nowego okna dla porównawczych wykresów
    plt.figure(figsize=(12, 6))
    plt.suptitle('Porównanie nałożonych danych', fontsize=16)

    # Wykres nałożonych czasów (binarne2 i binarne3)
    plt.subplot(1, 2, 1)
    plt.scatter(rozmiary_list, czasy2_lista, color='red', s=10, alpha=0.6, label='binarne2')
    plt.scatter(rozmiary_list, czasy3_lista, color='blue', s=10, alpha=0.6, label='binarne3')
    plt.xticks(range(len(sciezki)), etykiety_plikow, rotation=45)
    plt.xlabel('Wielkość pliku')
    plt.ylabel('Czas [ms]')
    plt.title('Porównanie czasu wyszukiwania')
    plt.legend()

    # Wykres nałożonych iteracji (binarne2 i binarne3)
    plt.subplot(1, 2, 2)
    plt.scatter(rozmiary_list, iteracje2_lista, color='red', s=10, alpha=0.6, label='binarne2')
    plt.scatter(rozmiary_list, iteracje3_lista, color='blue', s=10, alpha=0.6, label='binarne3')
    plt.xticks(range(len(sciezki)), etykiety_plikow, rotation=45)
    plt.xlabel('Wielkość pliku')
    plt.ylabel('Liczba iteracji')
    plt.title('Porównanie liczby iteracji')
    plt.legend()

    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Poprawienie odstępów
    plt.show()

# Ścieżki do plików
sciezki = [
    "C:\\Users\\mich4\\OneDrive\\Pulpit\\Algo\\Sprawozdanie_2_Wersja_2_wyszukiwanie_binarne_Iciek_Michal\\dane500.txt",
    "C:\\Users\\mich4\\OneDrive\\Pulpit\\Algo\\Sprawozdanie_2_Wersja_2_wyszukiwanie_binarne_Iciek_Michal\\dane1000.txt",
    "C:\\Users\\mich4\\OneDrive\\Pulpit\\Algo\\Sprawozdanie_2_Wersja_2_wyszukiwanie_binarne_Iciek_Michal\\dane10000.txt",
    "C:\\Users\\mich4\\OneDrive\\Pulpit\\Algo\\Sprawozdanie_2_Wersja_2_wyszukiwanie_binarne_Iciek_Michal\\dane100000.txt"
]

# Analiza danych
analiza(sciezki)
