
#Blok o największej sumie 

'''
def suma(ciag,zapis_ciagu = [],zapis_sumy = []):
    for i in range(0,len(ciag)):
        zapis_ciagu.append(ciag[i])
        zapis_sumy.append(ciag[i])
        for j in range(i+1,len(ciag)):
            zapis_ciagu.append(str(zapis_ciagu[-1])+","+str(ciag[j]))
            zapis_sumy.append(zapis_sumy[-1]+ciag[j])
    
    print(max(zapis_sumy))
    print(zapis_ciagu[zapis_sumy.index(max(zapis_sumy))])
    
    return zapis_sumy,zapis_ciagu

'''
'''
def suma(ciag):
    max_suma = float('-inf') 
    aktualna_suma = 0
    start = 0
    koniec = 0
    temp_start = 0

    for i in range(len(ciag)):
        aktualna_suma += ciag[i]
        
        if aktualna_suma > max_suma:
            max_suma = aktualna_suma
            start = temp_start
            koniec = i
        
        if aktualna_suma < 0:
            aktualna_suma = 0
            temp_start = i + 1

    print(f"Maksymalna suma: {max_suma}")
    print(f"Podciąg o maksymalnej sumie: {ciag[start:koniec+1]}")
    return max_suma, ciag[start:koniec+1]
'''


#podciąg o największej sumie Algorytm Kadane
def suma(ciag):
     
    max_suma = aktualna_suma = ciag[0]
     
    for i in range(1, len(ciag)):
        aktualna_suma = max(ciag[i], aktualna_suma + ciag[i])
        max_suma = max(max_suma, aktualna_suma)
        
    return max_suma
    
    
blok = [-4,3,-1,2]

print(suma(blok))
