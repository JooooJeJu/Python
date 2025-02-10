#wywołanie funkcji zmienić ✔️ , przekazywanie do tabeli też zmienić ✔️ 
'''
Program porównuje dwie metody przybliżania pierwiastka funkcji: Metoda biskecji oraz stycznych.
Metoda bisekcji została napisane przezemnie natomiast metoda stycznych została napisana przez inny zespół na zajeciach i została lekko zmodyfikowana.

Dla funkcji każdej metody tworzę nową tabela do której przypisuje następujące wartości: [Iteracja],[Przybliżenie Pierwiastka],[Błąd bezwzgledny],[Bład względny].
Wszystkie informacje są przechowywane w jednej tabeli, która na koniec funkcji jest zwracana.

Dodałem nową funkcję wypisz, która ma za zadanie wypisanie elementów w uporządkowany sposób.
Wypisywanie tabeli przebiega w następujący sposób: Wypisanie iteracji,przybliżenia pierwistka, błedu bezwzględnego i błędu względnego po czym zostają one oddzielone 
od siebie jedynie w celu lepszej widoczności danych 

Błędy są obliczane od drugiej iteracji, istnieje "problem" że błąd względny nie zostanie obliczony w niektórych przypadkach ponieważ przybliżeniem naszego  
miejsca zerowego może być 0.0, przez co będziemy próbować dzielić przez 0 dlatego wtedy pojawia się "-".

W 36 linijce należało by poprawić warunek aczkolwiek nie byłem w stanie dojść do prawidłowego rozwiązanie

Na końcu programu znajduję się wszystko związne z wyświetlaniem danych, dodałem zmienne które moim zdaniem są czytelniejsze oraz łatwiej jest modyfikować
argumenty funkcji dla niezaznajomionych biegle z kodem
'''
#✔️
def funkcja(x):
    return x-2
#✔️
def pochodna(x):
    return 1

#✔️
def bisekcja(f,a,b,e,wynik = []):

    numer = 1
    lewy = f(a)
    prawy = f(b)
    
    if lewy*prawy >=0:
        print('Nie ma miejsc zerowych w podanym przedziale') 
        #return # jeżeli damy równanie kwadratowe to musimy usunać returna 
    
    while (b-a)/2 > e:
        wynik.append(numer)
        
        srodekf = f((a+b)/2)
        srodek = (a+b)/2
        
        if lewy*srodekf <= 0:
            b = srodek
            prawy = f(b)
            numer += 1
            wynik.append(srodek)
        
        elif prawy*srodekf <= 0:
            a = srodek
            lewy = f(a)
            numer += 1
            wynik.append(srodek)
        
        if len(wynik) > 4:
            
            blad = abs(wynik[-1]-wynik[-5]) 
            wynik.append(blad)
            
            if wynik[-6] != 0:
                blad_wzgledny = (blad / abs(wynik[-6])) * 100  
                wynik.append(blad_wzgledny)
            
            else:
                wynik.append('-')  

        else:
            wynik.append('-')
            wynik.append('-')
    
    return wynik
#✔️
def newtons_method(f, df, x0, tolerance=1e-7, wynik = []):
    
    x = x0
    fx = f(x)
        
    iteration = 1
    
    while not abs(fx) < tolerance:
        wynik.append(iteration)
        
        fx = f(x)
        dfx = df(x)
        
        if dfx == 0:
            print("Pochodna jest równa zero. Metoda Newtona nie może kontynuować.") 
            return 
        
        x = x - fx / dfx
        
        iteration += 1
        
        wynik.append(x)
        
        if len(wynik) > 4:
            
            blad = abs(wynik[-1]-wynik[-5]) 
            wynik.append(blad)
            
            
            if wynik[-6] != 0:
                blad_wzgledny = (blad / abs(wynik[-6])) * 100  
                wynik.append(blad_wzgledny)
            
            
            else:
                wynik.append('-')  

        else:
            wynik.append('-')
            wynik.append('-')
    
    return wynik

#✔️
def wypisz(tabela):
    print('[Iteracja],[Przybliżenie Pierwiastka],[Błąd bezwzgledny],[Bład względny]')
    for i in range(0,len(tabela),4):
        print(tabela[i:i+4])
        print("--------------------------------")

#✔️
tolerancja = 0.1

#✔️
bi = []    
przedzial_lewy = -10
przedzial_prawy = 10
#✔️
bisekcja(funkcja,przedzial_lewy,przedzial_prawy,tolerancja,bi)
print("Metoda Bisekcji")
wypisz(bi)

#✔️
nm = []
miejsce_zerowe = 10
#✔️
newtons_method(funkcja,pochodna,miejsce_zerowe,tolerancja,nm)
print("Metoda Stycznych")
wypisz(nm)