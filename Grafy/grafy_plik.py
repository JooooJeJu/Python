sciezka = "C:\\Users\\mich4\\OneDrive\\Pulpit\\Algo\\Graf_1.txt"

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


graf = wczytaj_graf(sciezka)
odwiedzone, glebokosci = przeszukanie_dfs(graf, 'a')

print("\nGłębokości wierzchołków:")
for wierzcholek, glebokosc in glebokosci.items():
    print(f"{wierzcholek}: {glebokosc}")

if sprawdz_spojnosc(graf):
    print("\nGraf jest spójny.")
else:
    print("\nGraf nie jest spójny.")






'''
spójność #

składowe spójne 
odległości od wskazanego wierzchołka
czy jest drzewem(nieskierowany)
cykle
'''
