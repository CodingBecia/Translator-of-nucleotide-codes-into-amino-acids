#Kusztelak Paulina, Okołowicz Bernadeta, data: 25.06, wersja: 3

'''definiujemy funkcja o nazwie nukleotydy, 
w której znajduje się tabela kodu geneytcznego (sekwencji trójek nukleotydowych, które będą transkrybowane z podanej nici DNA). 
Jeśli trójka nie znajduje się w tabeli,
to w jej miejsce wpisuje się ?
'''

def nukleotydy(kodon):

    kod_genetyczny = {
        'TTT': 'Lys', 'TAA': 'Ile', 'CAT': 'Val', 'TCA': 'Ser', 'TGA': 'Thr', 'CGT': 'Ala',
        'TTC': 'Lys', 'TAG': 'Ile', 'CAC': 'Val', 'TCG': 'Ser', 'TGG': 'Thr', 'CGC': 'Ala',
        'AAA': 'Phe', 'TAT': 'Ile', 'AGA': 'Ser', 'GGA': 'Pro', 'TGT': 'Thr', 'ATA': 'Tyr',
        'AAG': 'Phe', 'TAC': 'Met', 'AGG': 'Ser', 'GGG': 'Pro', 'TGC': 'Thr', 'ATG': 'Tyr',
        'AAT': 'Leu', 'CAA': 'Val', 'AGT': 'Ser', 'GGT': 'Pro', 'CGA': 'Ala', 'GTA': 'His',
        'AAC': 'Leu', 'CAG': 'Val', 'AGC': 'Ser', 'Pro': 'GGC', 'CGG': 'Ala', 'GTG': 'His',
        'CTT': 'Gln', 'TTA': 'Asn', 'CTA': 'Asp', 'CTT': 'Glu', 'ACA': 'Cys', 'ACC': 'Trp',
        'GTC': 'Gln', 'TTG': 'Asn', 'CTG': 'Asp', 'CTC': 'Glu', 'ACG': 'Cys', 'GCA': 'Arg',
        'GCG': 'Arg', 'GCT': 'Arg', 'GCC': 'Arg', 'TCT': 'Arg', 'TCC': 'Arg', 'CCA': 'Gly',
        'CCG': 'Gly', 'CCT': 'Gly', 'CCC': 'Gly', 'ATT': 'STOP', 'ATC': 'STOP', 'ACT': 'STOP',
    }
    return kod_genetyczny.get(kodon, '?')

'''funkcja plik_fasta otwiera dwa pilki w formacie FASTA, wejściowy i wyjściowy, 
plik wejściowy odczytuje sekwencje nukleotydów, a zapisuje ją w pliku wyjściowym
jako sekwencje aminkowasową.
W celu transkrypcji sekwencji nukleotydów, stosujemy warunek if, 
który do zmiennej kodony przypisauje listę złożoną z wycinków sekwencji - sekwencja, zaczynający się od indeksu i i kończący na indeksie i+3.
W pętli range, 3 argument oznacza, że i ma się zwiększać o krok równy 3.
Jeśli sekwencja rozpoczyna się od kodonu START (TAC - Met), to rozpoczynamy pętlę for.
W pętli sprawdzamy wszystkie następujące sekwencje, jeśli zgadzają się z tabelą kodu genetycznego, przypisujemy je do zmiennej - białko.
Jeśli kodon oznacza sekwencję STOP, przerywamy pracę pętli.
Następnie do plików wyjściowego i wejściowego przypisaujemy odpowiednie nagłówki.
 '''
def plik_fasta(sciezka_wejsciowa, sciezka_wyjsciowa):
    with open(sciezka_wejsciowa, 'r') as plik_wejsciowy, open(sciezka_wyjsciowa, 'w') as plik_wyjsciowy:
        sekwencja = ''
        for line in plik_wejsciowy:
            if line.startswith('>'):
                naglowek = line.strip()
                if sekwencja:
                    transkrypcja = ''
                    kodony = []
                    for i in range(0, len(sekwencja), 3):
                        kodon = sekwencja[i:i+3]
                        kodony.append(kodon)
                    if kodony[0] == 'TAC':
                        for kodon in kodony:
                            bialko = nukleotydy(kodon)
                            transkrypcja += bialko

                            if bialko == 'STOP':
                                break

                        plik_wyjsciowy.write(naglowek + ' (Po transkrypcji)\n')
                        plik_wyjsciowy.write(transkrypcja + '\n')
                    else:
                        plik_wyjsciowy.write(naglowek + ' (Brak kodonu start)\n')
                sekwencja = ''
            else:
                sekwencja += line.strip()



sciezka_wejsciowa= input('Podaj ścieżkę do pliku FASTA wejściowego: ')

sciezka_wyjsciowa = input('Podaj ścieżkę do pliku FASTA wyjściowego: ')

plik_fasta(sciezka_wejsciowa, sciezka_wyjsciowa)

print('Brawo! Transkrypcja się udała! Swój wynik możesz zobaczyć w pliku:', sciezka_wyjsciowa)
