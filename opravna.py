import difflib
vocabulary_path = '/Users/tomasjelinek/PycharmProjects/opravatextu/syn2015_word_utf8.tsv'
path = '/Users/tomasjelinek/PycharmProjects/opravatextu/voda_errors.txt'
cesta='/Users/tomasjelinek/PycharmProjects/opravatextu/vysledek.txt'
special_characters = '.,"„“()[]\''
vysledek=[]
slovnik=[]
seznamtext=[]
slovicka=[]
rozdily=[]
fajne=[]
chybky=[]


slovnikload=open(vocabulary_path, 'r')
for line in slovnikload:
    fields = line.split('\t')
    slovnik.append(fields[1])

def korekce(slovo, znak1, znak2):
    global fajne
    global chybky
    zaklad=slovo
    slovo=slovo
    cislo1=0
    cislo2=len(slovo)
    if znak1!='':
        cislo1=1
    if znak2!='':
        cislo2=-1

    slovo=slovo[cislo1:cislo2]

    shoda = difflib.get_close_matches(slovo, slovnik, 1, cutoff=0.85)
    if shoda == []:
        return zaklad
    if shoda != []:
        if znak1+shoda[0]+znak2!=zaklad:
            print(zaklad, znak1+shoda[0]+znak2)
            rozdily.append([zaklad,znak1+shoda[0]+znak2])
            chybky.append(zaklad)
            fajne.append(znak1+shoda[0]+znak2)
        return znak1+shoda[0]+znak2



input_data = open(path,'r')
output_data = open(cesta,'w')
uspech=0
for line in input_data:
    words = line.split(" ")
    print(words)
    for slovo in words:

        spznakkonec = ""
        spznakzacatek = ""
        zirafa = True
        for char in slovo:
            if char in special_characters:
                if zirafa == True:
                    spznakzacatek = char
                elif zirafa == False:
                    spznakkonec = char

            zirafa = False

        output_data.write(korekce(slovo, spznakzacatek, spznakkonec))
        if "\n" not in slovo:
            output_data.write(' ')
input_data.close()
output_data.close()