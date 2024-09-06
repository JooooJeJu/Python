# -*- coding: utf-8 -*-
## Iciek Michał 25.06.2023

pathopen=str(input("Podaj scieżkę lub nazwę pliku z którego chcesz odczytać sekwencję aminokwasową: "))  ## do odczytu
pathsave=str(input("Podaj ścieżkę lub nazwę pliku do którego chcesz zapisać tą sekwencję: "))  ## do zapisu 
zliczanie = 0 ## zmienna pomocnicza/ bezszwowy plik 


while pathopen == pathsave:
    print("Scieżka odczytu nie może być taka sama jak ścieżka zapisu!")
    pathopen=str(input("Podaj scieżkę lub nazwę pliku z którego chcesz odczytać sekwencję aminokwasową: "))  ## do odczytu
    pathsave=str(input("Podaj ścieżkę lub nazwę pliku do którego chcesz zapisać tą sekwencję: "))  ## do zapisu
else:
    
    trojka_nukleotydy = ''
    akapit_nukleotydy = ''



    with open(pathopen, 'r') as odczyt, open(pathsave,'w') as zapis:
        zapis.write(odczyt.readline())  ## zapis pierwszego nagłówka 
        for linia in odczyt:
            if linia[0] == '>': ## czytanie i zapis nagłówka
                j=0
                while j <= len(akapit_nukleotydy)-1:
                    if j+1 and j+2 < len(akapit_nukleotydy)-1:
                        trojka_nukleotydy=akapit_nukleotydy[j]+akapit_nukleotydy[j+1]+akapit_nukleotydy[j+2]    ## przypisanie pierwszej trójki nukleotydów
                    else:
                        break
                    if trojka_nukleotydy == 'ATG':  ##szukanie startu jeżeli zostanie odnaleziony wchodzi w pętle gdzie są szukane i zapisywanie poszczególne trójki aminokwasowe
                        zapis.write('Start|')
                        trojka_nukleotydy=''
                        j=j+3
                        if j+1 >= len(akapit_nukleotydy)-1:
                                zapis.write("STOP|\n")
                                break
                        trojka_nukleotydy=akapit_nukleotydy[j]+akapit_nukleotydy[j+1]+akapit_nukleotydy[j+2]
                        k=j
                        while k <= len(akapit_nukleotydy)-1:   ##Szukanie i zapisywanie poszczególnych kodów do pliku
                            k=k+3
                            if k+1 >= len(akapit_nukleotydy)-1:
                                zapis.write("STOP|\n")
                                break
                            trojka_nukleotydy=akapit_nukleotydy[k]+akapit_nukleotydy[k+1]+akapit_nukleotydy[k+2]
                            if trojka_nukleotydy == 'GCA' or trojka_nukleotydy == 'GCG' or trojka_nukleotydy == 'GCT' or trojka_nukleotydy == 'GCC': 
                                zapis.write('Ala|')
                            elif trojka_nukleotydy == 'AGA' or trojka_nukleotydy == 'AGG' or trojka_nukleotydy == 'CGA' or trojka_nukleotydy == 'CGG' or trojka_nukleotydy == 'CGT' or trojka_nukleotydy == 'CGC':
                                zapis.write('Arg|')
                            elif trojka_nukleotydy == 'GAT' or trojka_nukleotydy == 'GAC':
                                zapis.write('Asp|')
                            elif trojka_nukleotydy == 'AAT' or trojka_nukleotydy == 'AAC':
                                zapis.write('Asn|')  
                            elif trojka_nukleotydy == 'TGT' or trojka_nukleotydy == 'TGC':
                                zapis.write('Cys|')
                            elif trojka_nukleotydy == 'GAA' or trojka_nukleotydy == 'GAG':
                                zapis.write('Glu|')
                            elif trojka_nukleotydy == 'CAA' or trojka_nukleotydy == 'CAG':
                                zapis.write('Gln|')
                            elif trojka_nukleotydy == 'GGA' or trojka_nukleotydy == 'GGG' or trojka_nukleotydy == 'GGT' or trojka_nukleotydy == 'GGC':
                                zapis.write('Gly|')
                            elif trojka_nukleotydy == 'CAT' or trojka_nukleotydy == 'CAC':
                                zapis.write('His|')
                            elif trojka_nukleotydy == 'ATA' or trojka_nukleotydy == 'ATT' or trojka_nukleotydy == 'ATC':
                                zapis.write('Ile|')
                            elif trojka_nukleotydy == 'TTA' or trojka_nukleotydy == 'TTG' or trojka_nukleotydy == 'CTA' or trojka_nukleotydy == 'CTG' or trojka_nukleotydy == 'CTT' or trojka_nukleotydy == 'CTC':
                                zapis.write('Leu|')
                            elif trojka_nukleotydy == 'AAA' or trojka_nukleotydy == 'AAG':
                                zapis.write('Lys|')
                            elif trojka_nukleotydy == 'TTT' or trojka_nukleotydy == 'TTC':
                                zapis.write('Phe|')
                            elif trojka_nukleotydy == 'CCA' or trojka_nukleotydy == 'CCG' or trojka_nukleotydy == 'CCT' or trojka_nukleotydy == 'CCC':
                                zapis.write('Pro|')
                            elif trojka_nukleotydy == 'AGT' or trojka_nukleotydy == 'AGC' or trojka_nukleotydy == 'TCA' or trojka_nukleotydy == 'TCG' or trojka_nukleotydy == 'TCT' or trojka_nukleotydy == 'TCC':
                                zapis.write('Ser|')
                            elif trojka_nukleotydy == 'ACA' or trojka_nukleotydy == 'ACG' or trojka_nukleotydy == 'ACT' or trojka_nukleotydy == 'ACC':
                                zapis.write('Thr|')
                            elif trojka_nukleotydy == 'TGG':
                                zapis.write('Trp|')
                            elif trojka_nukleotydy == 'TAT' or trojka_nukleotydy == 'TAC':
                                zapis.write('Tyr|')
                            elif trojka_nukleotydy == 'GTA' or trojka_nukleotydy == 'GTG' or trojka_nukleotydy == 'GTT' or trojka_nukleotydy == 'GTC':
                                zapis.write('Val|')
                            elif trojka_nukleotydy == 'ATG':                             
                                zapis.write('Met|')
                            elif trojka_nukleotydy == 'TAA' or trojka_nukleotydy == 'TAG' or trojka_nukleotydy == 'TGA':
                                zapis.write('STOP|\n')
                                k=k+3
                                j=k
                                break
                    else:
                        j=j+1
                akapit_nukleotydy='' ## wyzerowanie całego akapitu nukleotydów w celu zapisanie kolejnego 
                zapis.write(linia)
            else:
                zliczanie=0
                akapit_nukleotydy = akapit_nukleotydy.strip()
                akapit_nukleotydy=akapit_nukleotydy+linia
        j=0
        while j <= len(akapit_nukleotydy)-1:
            if j+1 and j+2 < len(akapit_nukleotydy)-1:
                trojka_nukleotydy=akapit_nukleotydy[j]+akapit_nukleotydy[j+1]+akapit_nukleotydy[j+2]    ## przypisanie pierwszej trójki nukleotydów
            if trojka_nukleotydy == 'ATG':  ##szukanie startu jeżeli zostanie odnaleziony wchodzi w pętle gdzie są szukane i zapisywanie poszczególne trójki aminokwasowe
                zapis.write('Start|')
                trojka_nukleotydy=''
                j=j+3
                trojka_nukleotydy=akapit_nukleotydy[j]+akapit_nukleotydy[j+1]+akapit_nukleotydy[j+2]
                k=j
                zliczanie=1
                while k <= len(akapit_nukleotydy)-1:   ##Szukanie i zapisywanie poszczególnych kodów do pliku
                    k=k+3
                    if k+1 >= len(akapit_nukleotydy)-1:
                        zapis.write("STOP|\n")
                        break
                    trojka_nukleotydy=akapit_nukleotydy[k]+akapit_nukleotydy[k+1]+akapit_nukleotydy[k+2]
                    if trojka_nukleotydy == 'GCA' or trojka_nukleotydy == 'GCG' or trojka_nukleotydy == 'GCT' or trojka_nukleotydy == 'GCC': 
                        zapis.write('Ala|')
                    elif trojka_nukleotydy == 'AGA' or trojka_nukleotydy == 'AGG' or trojka_nukleotydy == 'CGA' or trojka_nukleotydy == 'CGG' or trojka_nukleotydy == 'CGT' or trojka_nukleotydy == 'CGC':
                        zapis.write('Arg|')
                    elif trojka_nukleotydy == 'GAT' or trojka_nukleotydy == 'GAC':
                        zapis.write('Asp|')
                    elif trojka_nukleotydy == 'AAT' or trojka_nukleotydy == 'AAC':
                        zapis.write('Asn|')  
                    elif trojka_nukleotydy == 'TGT' or trojka_nukleotydy == 'TGC':
                        zapis.write('Cys|')
                    elif trojka_nukleotydy == 'GAA' or trojka_nukleotydy == 'GAG':
                        zapis.write('Glu|')
                    elif trojka_nukleotydy == 'CAA' or trojka_nukleotydy == 'CAG':
                        zapis.write('Gln|')
                    elif trojka_nukleotydy == 'GGA' or trojka_nukleotydy == 'GGG' or trojka_nukleotydy == 'GGT' or trojka_nukleotydy == 'GGC':
                        zapis.write('Gly|')
                    elif trojka_nukleotydy == 'CAT' or trojka_nukleotydy == 'CAC':
                        zapis.write('His|')
                    elif trojka_nukleotydy == 'ATA' or trojka_nukleotydy == 'ATT' or trojka_nukleotydy == 'ATC':
                        zapis.write('Ile|')
                    elif trojka_nukleotydy == 'TTA' or trojka_nukleotydy == 'TTG' or trojka_nukleotydy == 'CTA' or trojka_nukleotydy == 'CTG' or trojka_nukleotydy == 'CTT' or trojka_nukleotydy == 'CTC':
                        zapis.write('Leu|')
                    elif trojka_nukleotydy == 'AAA' or trojka_nukleotydy == 'AAG':
                        zapis.write('Lys|')
                    elif trojka_nukleotydy == 'TTT' or trojka_nukleotydy == 'TTC':
                        zapis.write('Phe|')
                    elif trojka_nukleotydy == 'CCA' or trojka_nukleotydy == 'CCG' or trojka_nukleotydy == 'CCT' or trojka_nukleotydy == 'CCC':
                        zapis.write('Pro|')
                    elif trojka_nukleotydy == 'AGT' or trojka_nukleotydy == 'AGC' or trojka_nukleotydy == 'TCA' or trojka_nukleotydy == 'TCG' or trojka_nukleotydy == 'TCT' or trojka_nukleotydy == 'TCC':
                        zapis.write('Ser|')
                    elif trojka_nukleotydy == 'ACA' or trojka_nukleotydy == 'ACG' or trojka_nukleotydy == 'ACT' or trojka_nukleotydy == 'ACC':
                        zapis.write('Thr|')
                    elif trojka_nukleotydy == 'TGG':
                        zapis.write('Trp|')
                    elif trojka_nukleotydy == 'TAT' or trojka_nukleotydy == 'TAC':
                        zapis.write('Tyr|')
                    elif trojka_nukleotydy == 'GTA' or trojka_nukleotydy == 'GTG' or trojka_nukleotydy == 'GTT' or trojka_nukleotydy == 'GTC':
                        zapis.write('Val|')
                    elif trojka_nukleotydy == 'ATG':                             
                        zapis.write('Met|')
                    elif trojka_nukleotydy == 'TAA' or trojka_nukleotydy == 'TAG' or trojka_nukleotydy == 'TGA':
                        zapis.write('STOP|\n')
                        k=k+3
                        j=k
                        break
            else:
                j=j+1