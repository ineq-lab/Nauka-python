# zad 1.
sentence = 'Kurs Pythona jest prosty i przyjemny.'
print('Liczba znaków to:', len(sentence))
print('Tylko słowo:', sentence.replace('Kurs Pythona jest prosty i przyjemny.', '"prosty"'))
print('Znaki o indeksie\n''7 to:', sentence[7],
      '\n''12 to:', sentence[12], '\n''-4 to:',
      sentence[-4], '\n''36 to:', sentence[36])
sentence = sentence.replace('rz', 'sz')
sentence = sentence.replace('u', 'ó')
print('2 błędy ortograficzne:', sentence)
# zad 2.
imie = input('imie:')
nazwisko = input('nazwisko:')
nr_tel = input('numer telefonu:')


print('Czy imie składa sie wyłącznie z liter?', imie.isalpha())
print('Czy nazwisko składa sie wyłącznie z liter?', nazwisko.isalpha())
print('Czy numer telefonu składa sie wyłącznie z cyfr?', nr_tel.isdigit())

imie = imie.capitalize()
nazwisko = nazwisko.capitalize()
print(imie, nazwisko)

nr_tel = nr_tel.replace('-', '').replace(' ', '')
print(nr_tel)

print('Użytkownik to kobieta?', imie.endswith('a'))
personal = imie + " " + nazwisko + " " + nr_tel
print(personal)
print('Liczba znaków to:', len(personal))
print("Liczba liter to:", len(personal) - personal.count(' ') - 9)
print(len(imie+nazwisko))
# zad 3
DNA = 'ACTGTGCTGACTCCCGGTGCTGCCGCTGCCATAGCTAAAGCCCGGGTCCTGGTAGGCAGGCGGGAAGCAG \
GGTGGGGGTCCCGGGTACTGGTAGGGGTAGCCCTGACCCAGAGGCGGGGGGGCAGCCGGGTGGGGCAGCG \
GGGCCAGCGTGTCCTGAA-CGAAGTCCCACTGGAGCCACTGTTGAGGTTCAGGGTGGCGAGATCTGGCGG \
NNNAGGGTAGGTGAGGGCCGCGGAGGGGCCTCCGGCGTTCCCCTCCCCCCCGCCCTGAAACCCGAAGCCC \
CCACTCACTGCTGCAGAGATCCCCTGAAAACGTAGTAGCACTGCTCgagacAGGTGATCTGTTGACCTGA \
AACCGCAGGAAGCCGTGCTTCAGCAAGCTGCTGGCGTACTTCCGGGCCT---GCCGCTCCTTGAAGCCCT \
CCACGTGTGTGTACAGCCAGTCCACCACGTCCGCCCCTGGCCGGCACCAGCGGTCAGCCCGCAGCCTCGA \
GGCAAGCAGCCCTGCCNNTGGCACTATCCGC-CGCGGGGACGGCCACTCACCGATGACGGCATNNGCGAT \
GGTGATCTTGAGCCACATGCGGTCGCGGATCTCCAGTCCCGAG---GGCAGCTGCATGACCCGGACGACG \
GCGCTCATGTCACtcaccgtcagcggcgcctcttccagCCAGCTCTGCAAAGCACAGACAGCCCCGCTTC \
GCCCCAGCATCTGAAAGCGGGGGACTCggcAcgCTGCACCCCCAGGGGAGCCTCTGGGCAGAGCCTGCGC \
CAGGGCGCAAGCTGGACGGTGCGTGACAGCAGGGCCCCGGCCCACTGCAGGATGCACCCCCGTGAGGCTG \
GGGCGTGAGCAGGGGGGTTGGACAtttAGTCTCCCACTTCTACAGACACTTTTCATCAGGATCCTAGGCA \
CAAACTGGGCTGAAACCCCACCCTGCAGACCAGGAAGTAATGAGAACAGGGCAGGCCCCTTCCCCTCNNC \
GCATGCC-CACCCGAGAGCGCAGGCTGTTAGTCGTGTTAATGGCAGGAAGCAGAATGGAGACCTGGCCCC \
TGCCTCTGAA-CCGTGGGTGCTCaactggctaGCCCTACGTACATCCCCTGTTCcggCCAACACACAGAC \
ATGAGCAGGATGGGCTGCACAAGGTGGGCACGGGTGCCTGTGCACACGTCTGTGCAGGGAGTTGGGGACA \
GGCAACACACACGTGTCACAGCCCCATGACGGggcaattgcGCCATGCTGGCTGAATGGCAGAGACGCCC \
CTCCAAGCCTCGGTTTCTGCTGGGGCCCTCAGGAGCTGCCACTTACGTGGAGCACCAGGCACGGAGCTGG \
TTAGTGAGGAGGAGCTGGTGCGCGTGACGGCGCTGGAGCAGGGACTCGTACCGTAGCGGGGCAGGGCNNN \
TGTCAGTGCCGCCGTGTGGtcagcggcgatCGGCG-GGTCGATGGGCCGCACCGGGTCAGCTGGGTGNAG \
ACACGTGGCGATGACAGGCGGACAGATGGACAGGGTGGGAGGGCAGGGTGCAGGGCACAGAGGAGAGAGG \
CCTTCAGGCTAGGTAGGCGCCCCCTCCCCATCCCGccccGTGTGCCCCGAGGGCCACTCACCCCGTGGGA \
CGGTGAAGTAGCTTCG-GGCGTTGGGTCCAGCACTTGGCCACAGTGAGGCTGNAAATGGCTGCAGGAACG \
GTGGTCCCCCCGCAAGGCCCCCATGGTCCCACCTCCCTGCCTGGCCCCTCCCGCTCCAGCGCCNCCAGCC'

zasada_azotowa = DNA.count('ACGT')
DNA = DNA.upper()
DNA = DNA.replace(' ', '')
print('Nić DNA po obróbce:', DNA)
A = DNA.count('A')
C = DNA.count('C')
G = DNA.count('G')
T = DNA.count('T')
print('W kodzie DNA występuje:\n{} adenin\n{} cytozyn\n{} guanin\n{} tymin'.format(A, C, G, T))
print("Liczba zasad azotowych:", zasada_azotowa, 'nr indeksu:', DNA.find('ACGT'),
      DNA.find('ACGT', 310, 1471), DNA.rfind('ACGT'))
print('Liczba wystąpień GAGA:', DNA.count('GAGA'))
print('Długość nici DNA', len(DNA))
print('7 Guanin z rzędu nr:', DNA.find('GGGGGGG'), 'indeksu')
print('6 cytozyn z rzędu od końca nici nr:', DNA.rfind('CCCCCC'), 'indeksu')
CTGAAA = DNA.count('CTGAAA')
CTGAA_ = DNA.count('CTGAA-')
print('Liczba wystąpień CTGAAA:', CTGAAA)
print('Liczba wystąpień CTGAA- wątpliwej ostatniej adeniny:', CTGAA_)
print('Liczba obydwu sekwencji CTGAAA i CTGAA-:', CTGAA_+CTGAAA)
DNA = DNA.replace('-', '').replace('N', '')
DNA = DNA.replace('GAGA', 'AGAG')
print('DNA', DNA)
RNA = DNA.replace('T', 'U')
print('RNA', RNA)
# Końcowa obróbka nici DNA z: '-','N' z zamianą 'GAGA','AGAG'
lDNA = len(DNA)
print('Długość nici DNA i RNA:{}' .format(lDNA))
