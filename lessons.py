LESSONS = [
    {
        "id": 1,
        "title": "Bioinformatyka od podstaw: Wyświetlanie",
        "description": "Zanim przeanalizujemy nasze dane biologiczne, musimy nauczyć się 'rozmawiać' z komputerem. Podstawową komendą w Pythonie jest `print()`, która po prostu bierze to, co włożysz w nawiasy i wyświetla to na ekranie.\n\nJeśli chcemy wyświetlić tekst (czyli po prostu zbiór znaków), musimy otoczyć go cudzysłowami lub apostrofami, o tak: `print('ATGC')`.\n\nTwoje zadanie:\nUżyj funkcji `print()`, aby wyświetlić sekwencję 'GATTACA'.",
        "expected_output": "GATTACA\n",
        "initial_code": "# Użyj funkcji print(), nie zapomnij o cudzysłowach wokół tekstu!\n"
    },
    {
        "id": 2,
        "title": "Zmienne: Zapisywanie sekwencji startowej",
        "description": "W bioinformatyce sekwencje mają miliony liter. Zamiast przepisywać je za każdym razem, przechowujemy je w tak zwanych 'zmiennych'. Zmienna to po prostu naklejka na pudełko, do którego coś wkładamy.\n\nAby stworzyć zmienną, podajemy jej nazwę, znak równości `=` (co oznacza 'przypisz wartość'), a potem samą wartość, np.: `gen = 'ATGC'`.\n\nGdy chcesz wyświetlić zawartość zmiennej, przekazujesz jej nazwę (już bez cudzysłowów!) do funkcji print: `print(gen)`.\n\nTwoje zadanie:\nStwórz zmienną o nazwie `sekwencja`, wpisz do niej tekst 'ATGC', a w następnej linijce wyświetl ją używając `print()`.",
        "expected_output": "ATGC\n",
        "initial_code": "sekwencja = 'ATGC'\n# Napisz kod, który poniżej wyświetli zawartość zmiennej sekwencja:\n"
    },
    {
        "id": 3,
        "title": "Analiza: Długość odczytu DNA i zagnieżdżanie funkcji",
        "description": "Często musimy wiedzieć, jak długa jest sekwencja. Służy do tego wbudowana funkcja `len()` (od słowa *length* - długość). Robi to tak: `len('ATGC')` zwraca 4.\n\n**Ważny koncept: Zagnieżdżanie funkcji!**\nSamo obliczenie długości nic nie pokaże na ekranie. Komputer policzy i zachowa to w pamięci. Jeśli chcesz zobaczyć wynik, musisz włożyć wynik jednej funkcji w drugą! Jak rosyjskie matrioszki.\n\nSpójrz: `print( len(zmienna) )` - najpierw komputer uruchomi środek (policzy), a potem przekaże wynik do zewnętrznej funkcji (wypisze).\n\nTwoje zadanie:\nMasz zmienną `dna`. Od razu wypisz jej długość na ekran, zagnieżdżając odpowiednie funkcje tak jak w przykładzie wyżej.",
        "expected_output": "18\n",
        "initial_code": "dna = 'ATGCGTACGTTAGCTAGC'\n# Użyj print(...) łącząc to z len(...)\n"
    },
    {
        "id": 4,
        "title": "Łączenie łańcuchów (Konkatenacja znaków)",
        "description": "Czasami w laboratorium otrzymujemy pofragmentowane odczyty DNA (tzw. reads) i musimy je połączyć w jedną ciągłą nić. W Pythonie, jeśli masz dwa teksty (tzw. stringi), możesz je po prostu do siebie dodać zwykłym plusem `+`!\n\nPrzykład:\n`print('AT' + 'GC')` wypisze `ATGC`.\nMożesz też dodawać do siebie całe zmienne: `nowa_sekwencja = pierwsza + druga`.\n\nTwoje zadanie:\nMasz dwie zmienne `odczyt1` i `odczyt2`. Dodaj je do siebie, opcjonalnie dając wynikowi nową zmienną (np. `calosc`), a w kolejnej linijce wyświetl wyraz używając `print()`.",
        "expected_output": "ATGCTAGCATGC\n",
        "initial_code": "odczyt1 = 'ATGCTA'\nodczyt2 = 'GCATGC'\n\n# Połącz je i wydrukuj:\n"
    },
    {
        "id": 5,
        "title": "Metody obiektu: Zamiana na wielkie litery",
        "description": "Zdarza się, że pobierasz dane z bazy, gdzie sekwencja jest zapisana małymi literami ('atgc'). Bioinformatycy wolą wielkie litery.\nZamiast pisać złożony kod do podmiany każdej litery, możemy użyć 'metod'.\n\nMetody to specjalne funkcje 'przyklejone' do konkretnego typu danych (w naszym przypadku - do tekstu). Wywołujemy je po kropce: `zmienna.metoda()`.\nDo zamiany tekstu na wielkie litery służy metoda `.upper()`.\n\nPrzykład:\n`ladne_dna = brzydkie_dna.upper()`\n`print(ladne_dna)`\n\nTwoje zadanie:\nWydrukuj zawartość zmiennej `moje_dna` tak, aby była w stu procentach napisana wielkimi literami (pamiętaj o metodzie `.upper()`).",
        "expected_output": "GATTACA\n",
        "initial_code": "moje_dna = 'gattaca'\n\n# Zmień na wielkie litery i wydrukuj wynik:\n"
    },
    {
        "id": 6,
        "title": "Liczymy nukleotydy! (Metoda count)",
        "description": "Kolejną potężną metodą przyklejoną do tekstu jest `.count()`. Służy ona do zliczania, ile razy konkretny znak lub fragment występuje w tekście. Jej obsługa jest prosta - wystarczy napisać, czego szukamy.\n\nPrzykład:\n`wynik = nazwa_zmiennej.count('A')` - zwróci liczbę 'A' w tekście.\n\nJest to niesamowicie przydatne przy obliczaniu częstotliwości występowania poszczególnych nukleotydów - na tym opiera się na przykład kluczowy pomiar zawartości par GC (tzw. GC Content) z całych genomów!\n\nTwoje zadanie:\nUżyj metody `.count()`, aby policzyć, ile razy litera 'G' (Guanina) występuje w zmiennej `sekwencja` i wydrukuj wynik swojego wyszukiwania używając `print(...)`.",
        "expected_output": "4\n",
        "initial_code": "sekwencja = 'GATACGATGCGTAC'\n\n# Sprawdź ile 'G' jest w sekwencji i wydrukuj odpowiedź:\n"
    },
    {
        "id": 7,
        "title": "Matematyka i operatory. (Liczymy zawartość GC!)",
        "description": "Zawartość par G-C (GC-content) w genomie jest użyteczną daną ewolucyjną, i termodynamiczną: wyższa zawartość G-C (od Guaniny 'G' i Cytozyny 'C') często oznacza, że helisa pęka w wyższych temperaturach.\n\nPython radzi sobie ze standardową matematyką używając takich znaków jak:\nDodawanie: `+`\nMnożenie: `*` (gwiazdka)\nDzielenie: `/` (ukośnik)\nNawiasy działają według znanej z matematyki kolejności wykonywania działań: `(a + b) / c`.\n\nWiesz już jak policzyć długość `len()` (nasza podstawa), oraz ilość poszczególnych nukleotydów `.count('G')` i `.count('C')`.\n\nTwoje zadanie:\nWydrukuj policzoną ilość `G` plus ilość `C`. Muszą znajdować się one wewnątrz print, np. `print( ilosc_G + ilosc_C )`.",
        "expected_output": "6\n",
        "initial_code": "dna = 'CGCATACGATTGCCGTAC'\n\n# Krok 1: Policz w kodzie C oraz G łącząc w jedną sumę, następnie wydrukuj!\n"
    },
    {
        "id": 8,
        "title": "Podstawy Analizy GC Content",
        "description": "Kontynuujemy nasze obliczenia dla zawartości Guaniny 'G' i Cytozyny 'C'. \nAby uzyskać wartość procentową, musimy zsumować ilość 'G' i 'C', wynik dzielimy przez całkowitą długość nici ( len(...) ) a następnie całość mnożymy `* 100`.\n\nŻeby nasz program był przejrzysty (to super ważne dla bioinformatyków!), podzielmy matematykę na etapy i osobne zmienne!\n\nProsta ściąga:\n`dlugosc = len(...)`\n`sukcesy = ... countG ... + ... countC ...`\n`wynik_procent = ( ... ) * 100`\n\nTwoje zadanie:\nOblicz ile dokładnie procent całego odczytu `dna` to zawartość par G i C. Wydrukuj swój procent na samym końcu.",
        "expected_output": "33.33333333333333\n",
        "initial_code": "dna = 'CGCATACGATTGCCGTAC'\n\n# Krok 1 - zmierz zmienne:\n\n# Krok 2 - zrób obliczenia dla (%):\n\n# Krok 3 - wydrukuj samo (%):\n"
    },
    {
        "id": 9,
        "title": "Wyciąganie części sekwencji - Slicing (Część 1)",
        "description": "Czasami chcesz zbadać tylko konkretny kawałek długiego łańcucha genetycznego - np. usunąć sztuczne tagi/start kodony. \nW Pythonie pozycja znaków (liter) liczona jest od... zera! Pierwsza litera łańcucha to litera na tak zwanym 'indeksie [0]'. Ostatnia, jeśli słowo ma 4 litery to indeks [3].\n\nAby wybrać literę, wrzucamy jej indeks w nawiasy kwadratowe OBOK zmiennej, tak: `dna[0]`. Komenda `print( dna[2] )` wydrukuje... trzecią literkę od lewej (np. dla 'ATGC' było by to G)!\n\nTwoje zadanie:\nSekwencja ma dużo liter. Dostałeś polecenie z bazy, aby odczytać wyłącznie czwartą nukleotydę (czyli na indeksie ... no zgadnij?).\nZrób to używając zapisu nawiasów kwadratowych!",
        "expected_output": "A\n",
        "initial_code": "kod_z_bazy = 'GCGACGTCA'\n\n# Wydrukuj czwarty nukleotyd:\n"
    },
    {
        "id": 10,
        "title": "Wycinanie fragmentów sekwencji - Slicing (Część 2)",
        "description": "Z nawiasów kwadratowych wyciągniesz najwięcej mocy, jeśli zastosujesz składnię `[od:do]` (podajemy indeksy startowy i końcowy oddzielone dwukropkiem).\n\nPrzykład: `sekwencja[0:3]` pobierze dokładnie litery spod indeksów z miejsc zerowego, pierwszego oraz drugiego i na końcu przerwie. Pokaże więc PIERWSZE 3 LITERY. Python wycina litery włączając indeks startowy, ale ZATRZYMUJĄC się 'przed' indeksem końcowym.\n\nJeśli utniesz np. trzon 'ATA' i 'C' zostanie - to wygenerowałeś mutację sekwencji!\n\nTwoje zadanie:\nWytnij startowy kodon `ATG` leżący dokładnie na samym początku sekwencji poniżej, zapisz go nowej zmiennej o nazwie `kodon`, i wydrukuj go.",
        "expected_output": "ATG\n",
        "initial_code": "genom = 'ATGGTCTAAGTC'\n\n# Wyciągnij kodon z użyciem [x:y]\n"
    },
    {
        "id": 11,
        "title": "Decyzje w kodzie: if i else",
        "description": "Bioinformatyk często podejmuje decyzję na podstawie progu, np. czy sekwencja ma wysokie GC-content. Do takich decyzji służy `if` i `else`.\n\nSchemat jest prosty:\n- `if` sprawdza warunek\n- jeśli warunek jest prawdziwy, wykona się blok pod `if`\n- jeśli nie, wykona się blok pod `else`\n\nW tym zadaniu masz już policzoną wartość `gc`. Twoja rola to podjąć decyzję i wypisać odpowiedni komunikat.\n\nTwoje zadanie:\nJeśli `gc` jest większe lub równe 50, wypisz `wysokie GC`. W przeciwnym razie wypisz `niskie GC`.",
        "expected_output": "wysokie GC\n",
        "initial_code": "dna = 'GCGCGCATAT'\ngc = (dna.count('G') + dna.count('C')) / len(dna) * 100\n\n# Dodaj if/else i wypisz odpowiedni komunikat:\n"
    },
    {
        "id": 12,
        "title": "Wiecej progow: elif",
        "description": "Czasem dwa przypadki to za malo. Np. jakosc odczytu moze byc slaba, srednia lub wysoka. Do wielu progow sluzy `elif` (czyli 'else if').\n\nKolejnosc sprawdzania ma znaczenie:\n- najpierw `if`\n- potem kolejne `elif`\n- na koncu `else` jako domyslna opcja\n\nTwoje zadanie:\nDla zmiennej `quality` wypisz:\n- `slaba jakosc`, gdy wartosc jest mniejsza niz 20\n- `srednia jakosc`, gdy wartosc jest mniejsza niz 30\n- `wysoka jakosc` w pozostalych przypadkach.",
        "expected_output": "srednia jakosc\n",
        "initial_code": "quality = 27\n\n# Zbuduj if/elif/else i wydrukuj odpowiedni poziom jakosci:\n"
    },
    {
        "id": 13,
        "title": "Laczenie warunkow: and, or, not",
        "description": "W prawdziwej analizie rzadko wystarcza jeden warunek. Czesto trzeba polaczyc kilka kryteriow naraz.\n\nOperatory logiczne:\n- `and`: oba warunki musza byc prawdziwe\n- `or`: wystarczy, ze jeden warunek jest prawdziwy\n- `not`: odwraca warunek\n\nTwoje zadanie:\nMasz zmienne `length` i `gc`. Wypisz `kandydat OK` tylko wtedy, gdy dlugosc jest co najmniej 100 i jednoczesnie `gc` jest co najmniej 50. W przeciwnym razie wypisz `kandydat ODRZUC`.",
        "expected_output": "kandydat OK\n",
        "initial_code": "length = 130\ngc = 56\n\n# Uzyj if z operatorem and i wypisz decyzje:\n"
    },
    {
        "id": 14,
        "title": "Powtarzanie operacji: petla while",
        "description": "Petla `while` wykonuje kod tak dlugo, jak dlugo warunek jest prawdziwy. To dobre narzedzie, gdy liczba powtorzen zalezy od stanu zmiennej.\n\nW tym cwiczeniu symulujemy przetwarzanie kilku probek jedna po drugiej.\n\nTwoje zadanie:\nDopoki `pozostale_probki` jest wieksze od zera, wypisuj `analizuje probke`, a potem zmniejszaj licznik o 1.\n\nWskazowka:\nBez zmniejszania licznika petla nigdy sie nie skonczy.",
        "expected_output": "analizuje probke\nanalizuje probke\nanalizuje probke\n",
        "initial_code": "pozostale_probki = 3\n\n# Napisz petle while, ktora wykona sie 3 razy:\n"
    },
    {
        "id": 15,
        "title": "Przeglad sekwencji znak po znaku: petla for",
        "description": "Petla `for` jest idealna do przechodzenia po sekwencji znak po znaku. W bioinformatyce to podstawa wielu prostych analiz.\n\nW tym zadaniu policzysz liczbe nukleotydow `G` recznie, bez uzywania `.count()`.\n\nPlan:\n- utworz licznik startujacy od 0\n- przejdz petla `for` po kazdym znaku w `dna`\n- gdy znak to `G`, zwieksz licznik\n- na koncu wypisz licznik\n\nTwoje zadanie:\nWydrukuj liczbe wystapien `G` w zmiennej `dna`.",
        "expected_output": "4\n",
        "initial_code": "dna = 'GATGCGGA'\n\n# Policz recznie ile razy wystepuje 'G' i wydrukuj wynik:\n"
    },
    {
        "id": 16,
        "title": "Listy: wiele sekwencji naraz",
        "description": "Do tej pory pracowales na jednej sekwencji. W praktyce masz wiele odczytow i dobrze trzymac je razem. Do tego sluzy lista, czyli kolekcja elementow w nawiasach kwadratowych.\n\nPrzyklad listy: `['ATGC', 'GATTACA', 'TTAA']`\n\nFunkcja `len()` dziala tez na liscie i zwraca liczbe elementow, a nie liczbe znakow jednego napisu.\n\nTwoje zadanie:\nDla listy `odczyty` wypisz, ile sekwencji sie w niej znajduje.",
        "expected_output": "4\n",
        "initial_code": "odczyty = ['ATGC', 'GATTACA', 'CGTA', 'TTTT']\n\n# Wypisz liczbe elementow listy odczyty:\n"
    },
    {
        "id": 17,
        "title": "Petla for po liscie: suma dlugosci odczytow",
        "description": "Teraz laczymy dwie umiejetnosci: liste i petle `for`.\n\nCel biologiczny: policzyc laczna liczbe nukleotydow we wszystkich odczytach.\n\nPlan:\n- utworz zmienna `suma = 0`\n- przejdz petla po kazdej sekwencji z listy\n- do `suma` dodawaj dlugosc aktualnej sekwencji\n- na koncu wypisz `suma`\n\nTwoje zadanie:\nWydrukuj laczna dlugosc wszystkich sekwencji z listy `odczyty`.",
        "expected_output": "15\n",
        "initial_code": "odczyty = ['ATGC', 'GATTAC', 'CGTAA']\n\n# Policz laczna dlugosc wszystkich odczytow i wypisz wynik:\n"
    },
    {
        "id": 18,
        "title": "Srednia dlugosc odczytu",
        "description": "Sama suma to czesto za malo. W raportach bardzo czesto podaje sie srednia dlugosc odczytu.\n\nWzor:\n- suma_dlugosci / liczba_odczytow\n\nW tym zadaniu masz juz liste sekwencji. Uzyj petli do policzenia sumy i na koncu oblicz srednia.\n\nTwoje zadanie:\nWydrukuj srednia dlugosc sekwencji z listy `odczyty`.",
        "expected_output": "5.0\n",
        "initial_code": "odczyty = ['ATGC', 'GATTAC', 'CGTAA']\n\n# Krok 1: policz sume dlugosci\n# Krok 2: podziel przez liczbe elementow listy\n# Krok 3: wypisz srednia\n"
    },
    {
        "id": 19,
        "title": "Slownik jako licznik nukleotydow",
        "description": "Slownik (dict) pozwala powiazac klucz z wartoscia, np. litere nukleotydu z liczba wystapien.\n\nPrzygotowalismy pusty licznik dla `A`, `C`, `G`, `T`.\nTwoim zadaniem jest przejsc po sekwencji i zwiekszac odpowiedni licznik.\n\nWskazowka:\nDla aktualnego znaku `n` mozesz zwiekszyc licznik tak: `licznik[n] = licznik[n] + 1`.\n\nTwoje zadanie:\nPo policzeniu wszystkiego wypisz tylko liczbe `G`.",
        "expected_output": "2\n",
        "initial_code": "dna = 'ATGCGAT'\nlicznik = {'A': 0, 'C': 0, 'G': 0, 'T': 0}\n\n# Przejdz po dna i uzupelnij licznik:\n\n# Na koncu wypisz licznik dla G:\n"
    },
    {
        "id": 20,
        "title": "Sortowanie dlugosci odczytow",
        "description": "Sortowanie przydaje sie np. przy szybkim znalezieniu najkrotszych lub najdluzszych odczytow.\n\nMozesz posortowac liste rosnaco i wtedy najmniejszy element bedzie na poczatku.\n\nTwoje zadanie:\nPosortuj liste `dlugosci` rosnaco i wypisz pierwszy element (czyli najkrotsza dlugosc).",
        "expected_output": "5\n",
        "initial_code": "dlugosci = [12, 5, 9, 7]\n\n# Posortuj liste i wypisz najkrotsza dlugosc:\n"
    },
    {
        "id": 21,
        "title": "Set: unikalne identyfikatory probek",
        "description": "W danych laboratoryjnych czesto pojawiaja sie duplikaty ID. Zbior `set` przechowuje tylko unikalne wartosci.\n\nPrzyklad:\nJesli zrobisz set z `['S1', 'S2', 'S1']`, to zostana tylko dwa elementy: `S1` i `S2`.\n\nTwoje zadanie:\nZ listy `ids` utworz zbior unikalnych ID i wypisz, ile unikalnych probek masz lacznie.",
        "expected_output": "4\n",
        "initial_code": "ids = ['S1', 'S2', 'S1', 'S3', 'S2', 'S4']\n\n# Utworz zbior unikalnych ID i wypisz jego dlugosc:\n"
    },
    {
        "id": 22,
        "title": "Pierwsza funkcja def",
        "description": "Funkcje pozwalaja zapakowac powtarzalny fragment kodu pod jedna nazwa. To bardzo wazne, gdy projekt zaczyna rosnac.\n\nW tym zadaniu tworzysz funkcje, ktora przyjmuje jedna sekwencje i zwraca jej dlugosc.\n\nTwoje zadanie:\nUzupelnij funkcje `dlugosc_sekwencji`, aby zwracala poprawny wynik, a potem wypisz wynik dla `GATTACA`.",
        "expected_output": "7\n",
        "initial_code": "def dlugosc_sekwencji(seq):\n    # Zamiast pass zwroc dlugosc przekazanej sekwencji\n    pass\n\n# Wywolaj funkcje dla 'GATTACA' i wypisz wynik:\n"
    },
    {
        "id": 23,
        "title": "Funkcja z return: procent GC",
        "description": "Teraz tworzysz funkcje bardziej bioinformatyczna: liczenie procentu GC.\n\nPlan:\n- policz ile jest `G` i `C`\n- podziel przez dlugosc sekwencji\n- pomnoz przez 100\n- zwroc wynik przez `return`\n\nTwoje zadanie:\nUzupelnij funkcje `gc_percent`, a nastepnie wypisz wynik dla sekwencji `ATGC`.",
        "expected_output": "50.0\n",
        "initial_code": "def gc_percent(seq):\n    # Policz procent GC i zwroc wartosc\n    pass\n\n# Wypisz wynik dla 'ATGC':\n"
    },
    {
        "id": 24,
        "title": "Reverse complement (wersja podstawowa)",
        "description": "Reverse complement to kluczowa operacja biologiczna: najpierw odwracasz sekwencje, a potem zamieniasz kazda litere na komplementarna.\n\nMapowanie komplementow:\n- A <-> T\n- C <-> G\n\nTwoje zadanie:\nDla zmiennej `dna` stworz reverse complement i wypisz wynik.\n\nWskazowka:\n- najpierw zrob odwrocona kolejnosc znakow\n- potem petla `for` i doklejanie komplementow do nowego napisu",
        "expected_output": "GCAT\n",
        "initial_code": "dna = 'ATGC'\nkomplement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}\nwynik = ''\n\n# Krok 1: odwroc sekwencje\n# Krok 2: przejdz petla i buduj reverse complement\n# Krok 3: wypisz wynik\n"
    },
    {
        "id": 25,
        "title": "Mini pipeline: filtr kandydatow",
        "description": "Laczymy wszystko w mini pipeline. Masz liste sekwencji i chcesz policzyc, ile z nich ma GC co najmniej 50 procent.\n\nPlan:\n- ustaw licznik kandydatow na 0\n- przejdz petla po sekwencjach\n- dla kazdej policz GC\n- jesli warunek GC >= 50 jest spelniony, zwieksz licznik\n- na koncu wypisz licznik\n\nTwoje zadanie:\nWydrukuj liczbe sekwencji spelniajacych warunek GC >= 50.",
        "expected_output": "2\n",
        "initial_code": "sekwencje = ['ATGC', 'GGGG', 'ATAT']\n\n# Policz ile sekwencji ma GC >= 50 i wypisz wynik:\n"
    },
    {
        "id": 26,
        "title": "Pliki: pierwszy odczyt z open",
        "description": "W praktyce dane rzadko sa wpisywane recznie w kodzie. Najczesciej czytasz je z plikow.\n\nW tym zadaniu masz juz przygotowany maly plik tekstowy. Twoim celem jest otworzyc go do odczytu i pobrac pierwsza linie.\n\nWskazowki:\n- uzyj `open(..., 'r')`\n- pierwsza linie pobierzesz przez `readline()`\n- zbedny znak nowej linii usuniesz przez `strip()`\n\nTwoje zadanie:\nWypisz pierwsza linie z pliku `prosty_odczyt.txt`.",
        "expected_output": "ATGC\n",
        "initial_code": "sciezka = 'prosty_odczyt.txt'\nwith open(sciezka, 'w') as f:\n    f.write('ATGC\\nGATTACA\\n')\n\n# Otworz plik do odczytu i wypisz pierwsza linie bez koncowego znaku nowej linii:\n"
    },
    {
        "id": 27,
        "title": "FASTA: ile rekordow w pliku",
        "description": "Format FASTA zapisuje sekwencje jako rekordy. Kazdy rekord zaczyna sie linia naglowkowa z symbolem `>`.\n\nW tym zadaniu policzysz liczbe rekordow FASTA, czyli liczbe linii zaczynajacych sie od `>`.\n\nPlan:\n- otworz plik\n- przejdz petla po liniach\n- gdy linia zaczyna sie od `>`, zwieksz licznik\n- wypisz licznik\n\nTwoje zadanie:\nWydrukuj liczbe rekordow w `mini.fasta`.",
        "expected_output": "3\n",
        "initial_code": "fasta_path = 'mini.fasta'\nwith open(fasta_path, 'w') as f:\n    f.write('>seq1\\nATGC\\n>seq2\\nGGTTAA\\n>seq3\\nTTA\\n')\n\n# Policz ile linii zaczyna sie od '>' i wypisz wynik:\n"
    },
    {
        "id": 28,
        "title": "FASTA: suma nukleotydow",
        "description": "Sekwencja FASTA moze byc podzielona na wiele linii. W analizie czesto potrzebujesz lacznej dlugosci wszystkich sekwencji, ale bez naglowkow.\n\nW tym zadaniu:\n- pomijasz linie zaczynajace sie od `>`\n- pomijasz puste linie\n- dla pozostalych linii dodajesz ich dlugosc\n\nTwoje zadanie:\nWydrukuj laczna liczbe nukleotydow z pliku `multi_line.fasta`.",
        "expected_output": "10\n",
        "initial_code": "fasta_path = 'multi_line.fasta'\nwith open(fasta_path, 'w') as f:\n    f.write('>a\\nATG\\nCGA\\n>b\\nTT\\nAA\\n')\n\n# Policz laczna dlugosc wszystkich linii sekwencji (bez naglowkow) i wypisz wynik:\n"
    },
    {
        "id": 29,
        "title": "Raport TSV: zapis i odczyt",
        "description": "Po analizie trzeba zapisac wynik do czytelnego raportu. Popularny format to TSV, gdzie kolumny sa oddzielone tabulatorem `\\t`.\n\nW tym zadaniu stworzysz plik `raport.tsv` z naglowkiem i jedna linia danych.\n\nPlan:\n- otworz plik do zapisu\n- zapisz linie naglowka: `id` i `gc`\n- zapisz linie danych z `seq_id` i `gc`\n- otworz plik ponownie i wypisz druga linie\n\nTwoje zadanie:\nWypisz linie danych z pliku raportu.",
        "expected_output": "seq1\t50.0\n",
        "initial_code": "seq_id = 'seq1'\ngc = 50.0\nout_path = 'raport.tsv'\n\n# Zapisz raport TSV (naglowek + jedna linia danych), a potem wypisz druga linie:\n"
    },
    {
        "id": 30,
        "title": "Mini projekt: podsumowanie FASTA",
        "description": "Final tego modułu: prosty analizator FASTA.\n\nMasz plik z trzema rekordami. Twoim celem jest policzyc:\n- ile rekordow jest w pliku\n- jaka jest maksymalna dlugosc sekwencji\n\nNa koncu wypisz oba wyniki w jednej linii, oddzielone spacja.\n\nWskazowka:\nNajpierw zbierz dlugosci do listy, potem uzyj `len(...)` i `max(...)`.",
        "expected_output": "3 6\n",
        "initial_code": "fasta_path = 'projekt.fasta'\nwith open(fasta_path, 'w') as f:\n    f.write('>s1\\nATGC\\n>s2\\nGGTTAA\\n>s3\\nATATA\\n')\n\n# Wypisz: liczba_rekordow max_dlugosc\n"
    },
    {
        "id": 31,
        "title": "Try/except: bezpieczna konwersja",
        "description": "W danych laboratoryjnych czasem trafia sie literowka i liczba przychodzi jako niepoprawny tekst. Program nie powinien sie wtedy wywalic, tylko elegancko obsluzyc blad.\n\nDo tego sluzy `try/except`.\n\nTwoje zadanie:\nSprobuj zamienic `quality_text` na liczbe `int(...)` i wypisac wynik. Jesli pojawi sie blad konwersji (`ValueError`), wypisz komunikat `blad konwersji`.",
        "expected_output": "blad konwersji\n",
        "initial_code": "quality_text = '27X'\n\n# Uzyj try/except: sprobuj int(...), a przy ValueError wypisz 'blad konwersji':\n"
    },
    {
        "id": 32,
        "title": "Czyszczenie sekwencji: replace i upper",
        "description": "Surowe dane moga zawierac spacje, znaki nowej linii i male litery. Przed analiza warto je ujednolicic.\n\nW tym zadaniu:\n- usun spacje\n- usun znaki nowej linii\n- zamien litery na wielkie\n\nTwoje zadanie:\nWypisz oczyszczona sekwencje z `raw`.",
        "expected_output": "ATGCTA\n",
        "initial_code": "raw = ' atg c\\nta '\n\n# Oczysc dane i wypisz wynik:\n"
    },
    {
        "id": 33,
        "title": "TSV: split na kolumny",
        "description": "Wyniki analiz czesto sa zapisane w liniach TSV (kolumny rozdzielone tabulatorem `\\t`).\n\nMozesz podzielic taka linie metoda `split('\\t')`, a potem odczytac wybrana kolumne po indeksie.\n\nTwoje zadanie:\nPodziel zmienna `line` i wypisz kolumne z sekwencja.",
        "expected_output": "ATGC\n",
        "initial_code": "line = 'seq1\\tATGC\\t4'\n\n# Podziel linie po tabulatorze i wypisz druga kolumne (sekwencje):\n"
    },
    {
        "id": 34,
        "title": "CSV: suma dlugosci z pliku",
        "description": "W tej lekcji czytasz prosty plik CSV z kolumnami `id,length`. Pierwsza linia to naglowek, ktory trzeba pominac.\n\nTwoje zadanie:\nWczytaj plik `odczyty.csv`, pomin naglowek i policz sume wartosci z kolumny `length`. Na koncu wypisz sume.",
        "expected_output": "15\n",
        "initial_code": "path = 'odczyty.csv'\nwith open(path, 'w') as f:\n    f.write('id,length\\ns1,4\\ns2,6\\ns3,5\\n')\n\n# Odczytaj CSV, pomin pierwsza linie i policz sume dlugosci:\n"
    },
    {
        "id": 35,
        "title": "List comprehension: filtr dluzszych sekwencji",
        "description": "List comprehension to krotki i czytelny sposob tworzenia nowej listy na podstawie starej.\n\nWzor:\n`[element for element in lista if warunek]`\n\nTwoje zadanie:\nZ listy `sekwencje` utworz nowa liste zawierajaca tylko sekwencje o dlugosci co najmniej 5 i wypisz liczbe takich sekwencji.",
        "expected_output": "2\n",
        "initial_code": "sekwencje = ['ATGC', 'GATTACA', 'TTAA', 'CCCCCC']\n\n# Uzyj list comprehension, a potem wypisz liczbe sekwencji o dlugosci >= 5:\n"
    },
    {
        "id": 36,
        "title": "Statystyki: min i max dlugosci",
        "description": "Szybkie podsumowanie zbioru danych to czesto minimum i maksimum.\n\nW tym zadaniu masz liste sekwencji. Najpierw zamien je na liste dlugosci, a potem znajdz najmniejsza i najwieksza wartosc.\n\nTwoje zadanie:\nWypisz `min` i `max` dlugosci w jednej linii, oddzielone spacja.",
        "expected_output": "4 7\n",
        "initial_code": "sekwencje = ['ATGC', 'GATTACA', 'TTAA']\n\n# Policz min i max dlugosci i wypisz je w formacie: min max\n"
    },
    {
        "id": 37,
        "title": "Sredni GC dla wielu sekwencji",
        "description": "W praktyce czesto porownujesz cala paczke sekwencji, a nie pojedynczy odczyt.\n\nTwoje zadanie:\nPolicz GC procent dla kazdej sekwencji z listy `sekwencje`, a potem wypisz srednia wartosc GC dla calej listy.",
        "expected_output": "50.0\n",
        "initial_code": "sekwencje = ['ATGC', 'GGGG', 'ATAT']\n\n# Krok 1: dla kazdej sekwencji policz procent GC\n# Krok 2: policz srednia z tych procentow\n# Krok 3: wypisz srednia\n"
    },
    {
        "id": 38,
        "title": "FASTA do slownika: id -> sekwencja",
        "description": "Po wczytaniu FASTA czesto wygodnie trzymac dane w slowniku: klucz to ID rekordu, wartosc to sekwencja.\n\nW tym zadaniu rekordy sa jedno-liniowe (kazda sekwencja zajmuje jedna linie).\n\nTwoje zadanie:\nWczytaj `parse.fasta` do slownika i wypisz sekwencje o ID `s2`.",
        "expected_output": "GGTTAA\n",
        "initial_code": "fasta_path = 'parse.fasta'\nwith open(fasta_path, 'w') as f:\n    f.write('>s1\\nATGC\\n>s2\\nGGTTAA\\n')\n\n# Wczytaj FASTA do slownika i wypisz rekord s2:\n"
    },
    {
        "id": 39,
        "title": "Raport wielu rekordow: zapis sortowany",
        "description": "Aby raport byl przewidywalny, warto zapisywac rekordy w stalej kolejnosci.\n\nW tym zadaniu:\n- zapisz plik TSV z naglowkiem\n- wpisz dane z `gc_map` posortowane rosnaco po ID\n- odczytaj plik i wypisz ostatnia linie\n\nTwoje zadanie:\nWypisz ostatnia linie raportu po zapisie.",
        "expected_output": "s2\t66.7\n",
        "initial_code": "gc_map = {'s2': 66.7, 's1': 50.0}\nout_path = 'multi_raport.tsv'\n\n# Zapisz TSV z danymi posortowanymi po ID i wypisz ostatnia linie pliku:\n"
    },
    {
        "id": 40,
        "title": "Mini projekt: filtr dlugosci i srednia",
        "description": "Ostatnie zadanie tego etapu laczy kilka krokow analizy na danych FASTA.\n\nMasz plik z trzema sekwencjami. Twoim celem jest policzyc:\n- ile sekwencji ma dlugosc co najmniej 5\n- jaka jest srednia dlugosc wszystkich sekwencji\n\nNa koncu wypisz oba wyniki w jednej linii, oddzielone spacja.",
        "expected_output": "2 5.0\n",
        "initial_code": "fasta_path = 'filtrowanie.fasta'\nwith open(fasta_path, 'w') as f:\n    f.write('>a\\nATGC\\n>b\\nGGTTAA\\n>c\\nTTTTT\\n')\n\n# Wypisz: liczba_sekwencji_o_dlugosci>=5 srednia_dlugosc\n"
    },
    {
        "id": 41,
        "title": "Blok 1: Jak Python wykonuje kod",
        "description": "Python wykonuje kod linia po linii, od gory do dolu. To nie jest czarna magia: kazda instrukcja uruchamia sie w kolejnosci.\n\nKomentarze (`#`) sa tylko dla czlowieka i nie sa wykonywane przez Python.\n\nTwoje zadanie:\nUstaw dwie zmienne i wypisz je w kolejnosci, aby zobaczyc jak kod wykonuje sie krok po kroku.",
        "expected_output": "Python\n1991\n",
        "initial_code": "# 1) Ustaw nazwa_narzedzia na 'Python'\n# 2) Ustaw rok_powstania na 1991\n# 3) Wypisz obie zmienne w dwoch liniach\n"
    },
    {
        "id": 42,
        "title": "Blok 1: Typy danych w praktyce",
        "description": "W Pythonie kazda wartosc ma typ. Najczestsze na starcie:\n- `str` (tekst)\n- `int` (liczba calkowita)\n- `float` (liczba zmiennoprzecinkowa)\n- `bool` (prawda/falsz)\n\nTwoje zadanie:\nWypisz nazwy typow dla podanych zmiennych, po jednej na linie.",
        "expected_output": "str\nint\nfloat\nbool\n",
        "initial_code": "seq = 'ATGC'\nreads = 42\ngc = 52.5\nis_clean = True\n\n# Wypisz kolejno: typ seq, typ reads, typ gc, typ is_clean\n# Wskazowka: type(x).__name__\n"
    },
    {
        "id": 43,
        "title": "Blok 1: print i proste wykonanie",
        "description": "Instrukcja `print()` pokazuje wynik na ekranie. To najprostszy sposob, by podejrzec co dzieje sie w kodzie.\n\nTwoje zadanie:\nPolicz i wypisz kolejno:\n- sume `a + b`\n- iloraz `a / b`\n- wynik porownania `a > b`.",
        "expected_output": "7\n2.5\nTrue\n",
        "initial_code": "a = 5\nb = 2\n\n# Wypisz trzy wyniki w opisanej kolejnosci:\n"
    },
    {
        "id": 44,
        "title": "Blok 2: String jako sekwencja DNA",
        "description": "W bioinformatyce sekwencja DNA to po prostu string. Mozesz odczytywac konkretne pozycje przez indeksy.\n\nPamietaj:\n- pierwszy znak ma indeks 0\n- ostatni mozna pobrac przez indeks ujemny `-1`\n\nTwoje zadanie:\nWypisz pierwszy i ostatni nukleotyd sekwencji `seq`.",
        "expected_output": "A\nT\n",
        "initial_code": "seq = 'ATGCGT'\n\n# Wypisz pierwszy nukleotyd\n# Wypisz ostatni nukleotyd\n"
    },
    {
        "id": 45,
        "title": "Blok 2: Wycinanie fragmentu seq[start:end]",
        "description": "Wycinanie fragmentow sekwencji to jedna z najczestszych operacji.\n\nSkladnia `seq[start:end]` bierze znak od `start` (wlacznie) do `end` (bez tego indeksu).\n\nTwoje zadanie:\nWytnij z `seq` fragment od indeksu 3 do 8 i wypisz go.",
        "expected_output": "TGCCC\n",
        "initial_code": "seq = 'AAATGCCCTT'\n\n# Wypisz fragment seq[3:8]\n"
    },
    {
        "id": 46,
        "title": "Blok 2: upper, len i count('GC')",
        "description": "Przed analiza warto ujednolicic litery do wielkich (`upper()`). Potem latwo policzyc dlugosc (`len`) i liczbe motywow (`count`).\n\nTwoje zadanie:\n1) Zamien sekwencje na wielkie litery\n2) Wypisz jej dlugosc\n3) Wypisz ile razy wystepuje motyw `GC`.",
        "expected_output": "10\n4\n",
        "initial_code": "seq = 'gcATGCGcgc'\n\n# Oczysc litery do upper i wypisz: dlugosc oraz count('GC')\n"
    },
    {
        "id": 47,
        "title": "Blok 3: Lista probek i petla for",
        "description": "Lista pozwala trzymac wiele sekwencji naraz, a petla `for` przejsc po kazdej z nich.\n\nTwoje zadanie:\nDla kazdej sekwencji z listy `proby` wypisz jej dlugosc (kazda dlugosc w nowej linii).",
        "expected_output": "4\n7\n3\n",
        "initial_code": "proby = ['ATGC', 'GATTACA', 'TTA']\n\n# Przejdz petla for po probach i wypisz dlugosc kazdej sekwencji\n"
    },
    {
        "id": 48,
        "title": "Blok 3: List comprehension i %GC",
        "description": "Klasyczny wzorzec w bioinformatyce: policzyc metryke dla kazdej sekwencji.\n\nList comprehension robi to zgrabnie w jednej konstrukcji.\n\nTwoje zadanie:\nUtworz liste procentow GC dla sekwencji z `proby` i wypisz cala liste.",
        "expected_output": "[50.0, 100.0, 0.0]\n",
        "initial_code": "proby = ['ATGC', 'GGGG', 'ATAT']\n\n# Zbuduj liste gc_values z procentem GC dla kazdej sekwencji i wypisz gc_values\n"
    },
    {
        "id": 49,
        "title": "Blok 4: Slownik i kod genetyczny",
        "description": "Slownik (`dict`) mapuje klucz na wartosc. To naturalny model dla kodu genetycznego: kodon -> aminokwas.\n\nTwoje zadanie:\n1) Wypisz aminokwas dla pojedynczego kodonu `ATG`\n2) Dla sekwencji `dna` skladajacej sie z dwoch kodonow wypisz translacje w formacie `Aminokwas1-Aminokwas2`.",
        "expected_output": "Met\nMet-Phe\n",
        "initial_code": "kod_genetyczny = {'ATG': 'Met', 'TTT': 'Phe', 'TAA': 'Stop'}\nkodon = 'ATG'\ndna = 'ATGTTT'\n\n# Krok 1: wypisz tlumaczenie pojedynczego kodonu\n# Krok 2: podziel dna na dwa kodony i wypisz translacje w formacie Aminokwas1-Aminokwas2\n"
    },
    {
        "id": 50,
        "title": "Blok 5: Funkcje gc_content i reverse_complement",
        "description": "Funkcje sprawiaja, ze kod jest czytelny i wielokrotnego uzytku.\n\nTwoje zadanie:\n1) Uzupelnij funkcje `gc_content(seq)`\n2) Uzupelnij funkcje `reverse_complement(seq)`\n3) Wypisz wynik `gc_content('ATGC')` oraz `reverse_complement('ATGC')`.",
        "expected_output": "50.0\nGCAT\n",
        "initial_code": "def gc_content(seq):\n    # Zwracaj procent GC jako float\n    pass\n\ndef reverse_complement(seq):\n    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}\n    # Zwracaj reverse complement dla podanej sekwencji\n    pass\n\n# Wypisz gc_content('ATGC')\n# Wypisz reverse_complement('ATGC')\n"
    },
    {
        "id": 51,
        "title": "Blok 6: if/else gdy sekwencja ma N",
        "description": "Warunki `if/else` pomagaja zdecydowac co zrobic z danymi o roznej jakosci.\n\nW tym zadaniu sprawdzisz, czy sekwencja zawiera znak `N` (nieznany nukleotyd).\n\nTwoje zadanie:\nJesli `N` jest w sekwencji, wypisz `zawiera N`, w przeciwnym razie wypisz `czysta`.",
        "expected_output": "zawiera N\n",
        "initial_code": "seq = 'ATNGC'\n\n# Uzyj if/else i wypisz odpowiedni komunikat\n"
    },
    {
        "id": 52,
        "title": "Blok 6: try/except gdy plik jest pusty",
        "description": "`try/except` pozwala obsluzyc sytuacje awaryjne bez wywrotki programu.\n\nW tym zadaniu plik istnieje, ale jest pusty.\n\nTwoje zadanie:\nSprobuj wczytac pierwsza linie. Jesli jest pusta, rzuć `ValueError`, a w `except` wypisz `plik pusty`.",
        "expected_output": "plik pusty\n",
        "initial_code": "path = 'pusty.txt'\nwith open(path, 'w') as f:\n    pass\n\n# Uzyj try/except z ValueError i wypisz 'plik pusty' dla pustego pliku\n"
    },
    {
        "id": 53,
        "title": "Blok 7: FASTA recznie - liczba rekordow",
        "description": "Zanim siegniesz po biblioteki, warto umiec recznie rozumiec FASTA.\n\nKazdy rekord FASTA zaczyna sie linia z `>`.\n\nTwoje zadanie:\nWczytaj plik i policz, ile jest rekordow FASTA.",
        "expected_output": "2\n",
        "initial_code": "path = 'manual.fasta'\nwith open(path, 'w') as f:\n    f.write('>r1\\nATGC\\n>r2\\nGGTTAA\\n')\n\n# Policz liczbe rekordow FASTA i wypisz wynik\n"
    },
    {
        "id": 54,
        "title": "Blok 7: FASTA recznie - pobierz sekwencje s2",
        "description": "Drugi krok recznego parsera FASTA: znalezc sekwencje dla konkretnego ID.\n\nZakladamy prosty format: naglowek i jedna linia sekwencji.\n\nTwoje zadanie:\nWczytaj plik i wypisz sekwencje rekordu `s2`.",
        "expected_output": "GGTTAA\n",
        "initial_code": "path = 'manual2.fasta'\nwith open(path, 'w') as f:\n    f.write('>s1\\nATGC\\n>s2\\nGGTTAA\\n')\n\n# Znajdz rekord s2 i wypisz jego sekwencje\n"
    },
    {
        "id": 55,
        "title": "Blok 7: TSV recznie - policz case",
        "description": "TSV to czesty format metadanych w pipeline.\n\nTwoje zadanie:\nWczytaj plik `meta.tsv`, pomin naglowek, a potem policz ile probek ma wartosc `case` w kolumnie `group`.",
        "expected_output": "2\n",
        "initial_code": "path = 'meta.tsv'\nwith open(path, 'w') as f:\n    f.write('sample\\tgroup\\nA\\tcase\\nB\\tcontrol\\nC\\tcase\\n')\n\n# Policz ile wierszy ma group == 'case' i wypisz wynik\n"
    },
    {
        "id": 56,
        "title": "Sprawdzian 1: typy i string DNA",
        "description": "Krotki test laczacy Blok 1 i Blok 2.\n\nMasz tekstowa sekwencje i liczbe jako tekst. Twoim celem jest:\n- ujednolicic sekwencje do wielkich liter\n- policzyc jej dlugosc\n- policzyc motyw `GC`\n- zamienic liczbe z tekstu na int\n\nTwoje zadanie:\nWypisz cztery linie: sekwencja_upper, dlugosc, count('GC'), quality_int.",
        "expected_output": "ATGCGC\n6\n2\n42\n",
        "initial_code": "seq = 'atgcgc'\nquality_text = '42'\n\n# Wypisz: sekwencja upper, jej dlugosc, count('GC'), quality jako int\n"
    },
    {
        "id": 57,
        "title": "Lekcja teoretyczna: jak czytac FASTA",
        "description": "Checkpoint teorii miedzy zadaniami praktycznymi.\n\nCo warto zapamietac:\n- naglowek FASTA zawsze zaczyna sie od `>`\n- identyfikator rekordu jest w naglowku\n- sekwencja moze byc podzielona na wiele linii\n\nTwoje zadanie:\nWypisz dwie linie podsumowania: `header: >id` oraz `sequence: linie DNA`.",
        "expected_output": "header: >id\nsequence: linie DNA\n",
        "initial_code": "# Wypisz dwie linie teorii o FASTA:\n# 1) header: >id\n# 2) sequence: linie DNA\n"
    },
    {
        "id": 58,
        "title": "Sprawdzian 2: listy, funkcje i warunki",
        "description": "Sprawdzian laczacy Blok 3, 5 i 6.\n\nMasz liste sekwencji.\nTwoje kroki:\n- napisz funkcje `gc_content(seq)`\n- przejdz po liscie\n- policz ile sekwencji ma GC >= 50\n\nTwoje zadanie:\nWypisz liczbe sekwencji spelniajacych warunek GC >= 50.",
        "expected_output": "2\n",
        "initial_code": "sekwencje = ['ATGC', 'GGGG', 'ATAT']\n\ndef gc_content(seq):\n    # Zwracaj procent GC\n    pass\n\n# Policz ile sekwencji ma GC >= 50 i wypisz wynik\n"
    },
    {
        "id": 59,
        "title": "Blok 4: translacja trzech kodonow",
        "description": "Rozszerzamy prace ze slownikiem kodu genetycznego.\n\nTwoje zadanie:\nPodziel sekwencje DNA na kodony po 3 znaki i przetlumacz trzy kolejne kodony przez slownik.\nWypisz wynik jako `Aminokwas1-Aminokwas2-Aminokwas3`.",
        "expected_output": "Met-Phe-Stop\n",
        "initial_code": "kod_genetyczny = {'ATG': 'Met', 'TTT': 'Phe', 'TAA': 'Stop'}\ndna = 'ATGTTTTAA'\n\n# Przetlumacz trzy kodony i wypisz wynik z myslnikami\n"
    },
    {
        "id": 60,
        "title": "Sprawdzian 3: reverse complement + GC",
        "description": "Sprawdzian laczacy dwie kluczowe operacje bioinformatyczne.\n\nTwoje zadanie:\n1) Oblicz reverse complement sekwencji `seq`\n2) Wypisz reverse complement\n3) Wypisz procent GC dla reverse complement\n\nWskazowka:\nGC dla sekwencji i jej reverse complement jest taki sam.",
        "expected_output": "GCAT\n50.0\n",
        "initial_code": "seq = 'ATGC'\ncomp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}\n\n# Krok 1: policz reverse complement\n# Krok 2: wypisz reverse complement\n# Krok 3: wypisz procent GC tej sekwencji\n"
    },
    {
        "id": 61,
        "title": "Lekcja teoretyczna: parser reczny vs biblioteka",
        "description": "To lekcja koncepcyjna. W bioinformatyce dobrze znac oba podejscia:\n- parser reczny: daje zrozumienie formatu i latwiejszy debug\n- biblioteka (np. Biopython): szybciej i bezpieczniej w codziennej pracy\n\nTwoje zadanie:\nWypisz dwie linie: `reczny: rozumiem format` oraz `biopython: szybka praktyka`.",
        "expected_output": "reczny: rozumiem format\nbiopython: szybka praktyka\n",
        "initial_code": "# Wypisz dwie linie teorii o podejsciu recznym i bibliotecznym\n"
    },
    {
        "id": 62,
        "title": "Blok 7: raport GC do TSV",
        "description": "Budujemy praktyczny etap pipeline: z FASTA do raportu tabelarycznego.\n\nTwoje zadanie:\nDla dwoch rekordow oblicz procent GC, zapisz raport TSV i wypisz ostatnia linie pliku.",
        "expected_output": "s2\t100.0\n",
        "initial_code": "records = [('s1', 'ATGC'), ('s2', 'GGGG')]\nout_path = 'gc_report.tsv'\n\n# Zapisz TSV: id\tgc\n# Potem wypisz ostatnia linie pliku\n"
    },
    {
        "id": 63,
        "title": "Sprawdzian 4: FASTA -> statystyki",
        "description": "Sprawdzian przekrojowy z pracy na plikach i petlach.\n\nMasz plik FASTA.\nTwoje zadanie:\n- policz liczbe rekordow\n- policz srednia dlugosc sekwencji\n\nWypisz oba wyniki w jednej linii, oddzielone spacja.",
        "expected_output": "3 5.0\n",
        "initial_code": "path = 'stats.fasta'\nwith open(path, 'w') as f:\n    f.write('>x\\nATGC\\n>y\\nGGTTAA\\n>z\\nTTTTT\\n')\n\n# Wypisz: liczba_rekordow srednia_dlugosc\n"
    },
    {
        "id": 64,
        "title": "Lekcja teoretyczna: jak myslec o tabeli",
        "description": "Krotki checkpoint przed pandas.\n\nNajwazniejsze pojecia:\n- wiersz = jedna probka (rekord)\n- kolumna = jedna cecha (np. wiek, grupa)\n\nTwoje zadanie:\nWypisz dwie linie: `wiersz=probka` i `kolumna=cecha`.",
        "expected_output": "wiersz=probka\nkolumna=cecha\n",
        "initial_code": "# Wypisz dwie linie teorii o danych tabelarycznych\n"
    },
    {
        "id": 65,
        "title": "Blok 8 prep: filtrowanie i grupowanie recznie",
        "description": "Dwie bardzo czeste operacje na metadanych to filtrowanie i grupowanie.\n\nTwoje zadanie:\nDla listy slownikow policz, ile probek jest w kazdej tkance (`tissue`) i wypisz:\n- najpierw liczbe dla `brain`\n- potem liczbe dla `liver`.",
        "expected_output": "2\n1\n",
        "initial_code": "meta = [\n    {'sample': 'A', 'tissue': 'brain'},\n    {'sample': 'B', 'tissue': 'liver'},\n    {'sample': 'C', 'tissue': 'brain'},\n]\n\n# Policz probki per tissue i wypisz: brain, potem liver\n"
    },
    {
        "id": 66,
        "title": "Sprawdzian 5: laczenie metadanych i wynikow GC",
        "description": "Sprawdzian laczacy slowniki, petle i warunki.\n\nMasz metadane i osobno mape GC.\nTwoje zadanie:\nWypisz ID probek, ktore sa w grupie `case` i maja GC >= 50 (kazde ID w nowej linii).",
        "expected_output": "A\nC\n",
        "initial_code": "meta = [\n    {'sample': 'A', 'group': 'case'},\n    {'sample': 'B', 'group': 'control'},\n    {'sample': 'C', 'group': 'case'},\n]\ngc_map = {'A': 52.0, 'B': 40.0, 'C': 60.0}\n\n# Wypisz sample dla case z GC >= 50\n"
    },
    {
        "id": 67,
        "title": "Lekcja teoretyczna: mean i std",
        "description": "Checkpoint teorii statystycznej.\n\nInterpretacja:\n- `mean` mowi o poziomie centralnym\n- `std` mowi o rozrzucie wokol sredniej\n\nTo podstawa przed PCA i analiza odleglosci.\n\nTwoje zadanie:\nWypisz dwie linie: `mean=srodek` i `std=rozrzut`.",
        "expected_output": "mean=srodek\nstd=rozrzut\n",
        "initial_code": "# Wypisz dwie linie teorii o mean i std\n"
    },
    {
        "id": 68,
        "title": "Sprawdzian 6: macierz odleglosci",
        "description": "W filogenetyce czesto pracujesz na macierzy odleglosci.\n\nTwoje zadanie:\nZ podanej macierzy 3x3 wez elementy nad przekatna (0,1), (0,2), (1,2).\nWypisz srednia i maksimum tych odleglosci w jednej linii.",
        "expected_output": "4.0 6\n",
        "initial_code": "M = [\n    [0, 2, 4],\n    [2, 0, 6],\n    [4, 6, 0],\n]\n\n# Oblicz srednia i max z elementow nad przekatna i wypisz: srednia max\n"
    },
    {
        "id": 69,
        "title": "Lekcja teoretyczna: po co subprocess",
        "description": "W bioinformatyce Python czesto nie liczy wszystkiego sam.\n\nTypowy podzial roli:\n- Python: przygotowuje dane i steruje krokiem pipeline\n- narzedzie zewnetrzne (np. MAFFT/IQ-TREE): wykonuje ciezkie obliczenia\n\nTwoje zadanie:\nWypisz dwie linie: `python steruje narzedziem` i `narzedzie robi obliczenia`.",
        "expected_output": "python steruje narzedziem\nnarzedzie robi obliczenia\n",
        "initial_code": "# Wypisz dwie linie teorii o roli subprocess\n"
    },
    {
        "id": 70,
        "title": "Sprawdzian 7: mini orchestracja pipeline",
        "description": "Final tego pakietu: polacz logike biologiczna z prostym krokiem narzedziowym.\n\nTwoje zadanie:\n1) Dla listy sekwencji policz ile ma GC >= 50 i wypisz te liczbe\n2) Uruchom `echo PIPELINE_OK` przez subprocess i wypisz wynik\n\nTo odzwierciedla typowy schemat: analiza + wywolanie narzedzia.",
        "expected_output": "2\nPIPELINE_OK\n",
        "initial_code": "import subprocess\nsekwencje = ['ATGC', 'GGGG', 'ATAT']\n\n# Krok 1: policz ile sekwencji ma GC >= 50 i wypisz liczbe\n# Krok 2: subprocess echo PIPELINE_OK i wypisz wynik\n"
    },
    {
        "id": 71,
        "title": "Blok 7+: FASTA wieloliniowe do slownika",
        "description": "Rozszerzamy parser FASTA: rekord moze miec sekwencje w wielu liniach.\n\nTwoje zadanie:\nWczytaj plik FASTA, zloz linie sekwencji dla kazdego ID i zapisz do slownika `id -> sekwencja`.\nNa koncu wypisz sekwencje rekordu `s1`.",
        "expected_output": "ATGCC\n",
        "initial_code": "path = 'multi_parse.fasta'\nwith open(path, 'w') as f:\n    f.write('>s1\\nATG\\nCC\\n>s2\\nTTAA\\n')\n\n# Wczytaj FASTA wieloliniowe do slownika i wypisz rekord s1\n"
    },
    {
        "id": 72,
        "title": "Filtrowanie sekwencji: brak N i minimalna dlugosc",
        "description": "Typowy krok quality control: odrzuc sekwencje z `N` i zbyt krotkie odczyty.\n\nTwoje zadanie:\nZ listy `seqs` wybierz sekwencje bez `N` i o dlugosci co najmniej 5, a potem wypisz liczbe tych sekwencji.",
        "expected_output": "2\n",
        "initial_code": "seqs = ['ATGCN', 'GGGGG', 'ATATA', 'NNNNN']\n\n# Przefiltruj sekwencje i wypisz liczbe poprawnych rekordow\n"
    },
    {
        "id": 73,
        "title": "Lekcja teoretyczna: co znaczy O(n)",
        "description": "Checkpoint teorii algorytmicznej.\n\nW bioinformatyce czesto przechodzisz po sekwencji znak po znaku.\nTaki algorytm ma zwykle zlozonosc liniowa O(n).\n\nTwoje zadanie:\nWypisz dwie linie: `O(n)=jedno przejscie` oraz `O(n*m)=dwie petle`.",
        "expected_output": "O(n)=jedno przejscie\nO(n*m)=dwie petle\n",
        "initial_code": "# Wypisz dwie linie teorii o zlozonosci\n"
    },
    {
        "id": 74,
        "title": "Sortowanie rekordow po GC malejaco",
        "description": "Czesto chcesz zobaczyc najpierw sekwencje o najwyzszym GC.\n\nTwoje zadanie:\nDla listy rekordow `(id, seq)` policz GC i posortuj rekordy malejaco po GC.\nWypisz ID rekordu z najwyzszym GC.",
        "expected_output": "s2\n",
        "initial_code": "records = [('s1', 'ATGC'), ('s2', 'GGGG'), ('s3', 'ATAT')]\n\n# Posortuj rekordy po GC malejaco i wypisz ID pierwszego rekordu\n"
    },
    {
        "id": 75,
        "title": "TSV: sredni GC dla grupy",
        "description": "W metadanych czesto porownujesz srednie miedzy grupami.\n\nTwoje zadanie:\nWczytaj TSV, wybierz wiersze z grupa `case`, policz sredni GC i wypisz wynik.",
        "expected_output": "55.0\n",
        "initial_code": "path = 'group_gc.tsv'\nwith open(path, 'w') as f:\n    f.write('sample\\tgroup\\tgc\\nA\\tcase\\t50\\nB\\tcontrol\\t40\\nC\\tcase\\t60\\n')\n\n# Policz sredni GC tylko dla group == 'case' i wypisz wynik\n"
    },
    {
        "id": 76,
        "title": "Sprawdzian 8: FASTA + filtr + statystyka",
        "description": "Sprawdzian laczacy parser FASTA, warunki i liczenie metryk.\n\nTwoje zadanie:\nWczytaj FASTA i policz, ile rekordow ma jednoczesnie: dlugosc >= 5 oraz GC >= 50.\nWypisz tylko liczbe rekordow spelniajacych oba warunki.",
        "expected_output": "1\n",
        "initial_code": "path = 'mix8.fasta'\nwith open(path, 'w') as f:\n    f.write('>a\\nATGC\\n>b\\nGGGGG\\n>c\\nATATA\\n')\n\n# Wypisz liczbe rekordow z dlugoscia >= 5 i GC >= 50\n"
    },
    {
        "id": 77,
        "title": "VCF podstawy: policz SNP",
        "description": "VCF zawiera warianty genomowe. SNP to przypadek, gdy REF i ALT maja po jednym nukleotydzie.\n\nTwoje zadanie:\nWczytaj prosty VCF i policz liczbe SNP (pomijaj linie naglowka zaczynajace sie od `#`).",
        "expected_output": "2\n",
        "initial_code": "path = 'mini.vcf'\nwith open(path, 'w') as f:\n    f.write('##fileformat=VCFv4.2\\n')\n    f.write('#CHROM\\tPOS\\tID\\tREF\\tALT\\tQUAL\\n')\n    f.write('1\\t10\\t.\\tA\\tG\\t35\\n')\n    f.write('1\\t20\\t.\\tAT\\tA\\t50\\n')\n    f.write('1\\t30\\t.\\tC\\tT\\t99\\n')\n\n# Policz SNP i wypisz wynik\n"
    },
    {
        "id": 78,
        "title": "VCF: filtr po QUAL",
        "description": "Warianty czesto filtruje sie po jakosci (`QUAL`).\n\nTwoje zadanie:\nPolicz ile rekordow VCF ma QUAL >= 30 i wypisz wynik.",
        "expected_output": "2\n",
        "initial_code": "path = 'qual.vcf'\nwith open(path, 'w') as f:\n    f.write('#CHROM\\tPOS\\tID\\tREF\\tALT\\tQUAL\\n')\n    f.write('1\\t10\\t.\\tA\\tG\\t10\\n')\n    f.write('1\\t20\\t.\\tC\\tT\\t30\\n')\n    f.write('1\\t30\\t.\\tG\\tA\\t60\\n')\n\n# Policz rekordy z QUAL >= 30\n"
    },
    {
        "id": 79,
        "title": "Lekcja teoretyczna: REF, ALT i QUAL",
        "description": "Checkpoint teorii VCF.\n\n- REF: baza referencyjna\n- ALT: baza alternatywna\n- QUAL: jakosc wywolania wariantu\n\nTwoje zadanie:\nWypisz trzy linie: `REF=baza referencyjna`, `ALT=wariant`, `QUAL=jakosc`.",
        "expected_output": "REF=baza referencyjna\nALT=wariant\nQUAL=jakosc\n",
        "initial_code": "# Wypisz 3 linie teorii o polach VCF\n"
    },
    {
        "id": 80,
        "title": "Slownik: czestosc kodonow",
        "description": "Przechodzac po sekwencji co 3 znaki, mozna policzyc czestosc kodonow.\n\nTwoje zadanie:\nDla sekwencji `dna` policz wystapienia kodonow i wypisz:\n- liczbe `ATG`\n- liczbe `TTT`.",
        "expected_output": "2\n1\n",
        "initial_code": "dna = 'ATGTTTATG'\n\n# Policza czestosc kodonow w ramce od 0 i wypisz: ATG, potem TTT\n"
    },
    {
        "id": 81,
        "title": "Funkcja translate_do_stop",
        "description": "Budujemy uzyteczna funkcje translacji: idziesz kodon po kodonie i zatrzymujesz sie na `Stop`.\n\nTwoje zadanie:\nUzupelnij funkcje `translate_do_stop` i wypisz wynik dla `ATGTTTTAA`.",
        "expected_output": "Met-Phe\n",
        "initial_code": "kod = {'ATG': 'Met', 'TTT': 'Phe', 'TAA': 'Stop'}\n\ndef translate_do_stop(seq):\n    # Tlumacz kodony po 3 i przerwij, gdy trafisz na Stop\n    pass\n\n# Wypisz wynik translate_do_stop('ATGTTTTAA')\n"
    },
    {
        "id": 82,
        "title": "Sprawdzian 9: translacja + GC",
        "description": "Sprawdzian laczacy slownik kodu genetycznego i liczenie GC.\n\nTwoje zadanie:\n1) Przetlumacz dwa kodony z sekwencji `dna`\n2) Wypisz translacje\n3) Wypisz GC procent dla calej sekwencji.",
        "expected_output": "Met-Ala\n50.0\n",
        "initial_code": "kod = {'ATG': 'Met', 'GCC': 'Ala'}\ndna = 'ATGGCCAT'\n\n# Wypisz translacje pierwszych dwoch kodonow\n# Potem wypisz GC procent dla calej sekwencji\n"
    },
    {
        "id": 83,
        "title": "Okna przesuwne: max GC window",
        "description": "Sliding window to bardzo czesty wzorzec.\n\nTwoje zadanie:\nDla sekwencji `seq` i okna o rozmiarze 4 policz maksymalny procent GC wsrod wszystkich okien i wypisz wynik.",
        "expected_output": "100.0\n",
        "initial_code": "seq = 'ATGCGCGT'\nwindow = 4\n\n# Przesun okno po sekwencji, policz GC procent dla kazdego i wypisz maksimum\n"
    },
    {
        "id": 84,
        "title": "Motyw w sekwencji: pozycje wystapien",
        "description": "Szukamy wszystkich wystapien motywu, np. miejsca startu kodonu.\n\nTwoje zadanie:\nZnajdz wszystkie pozycje motywu `ATG` w sekwencji `seq` i wypisz je w jednej linii, oddzielone spacja.",
        "expected_output": "0 3\n",
        "initial_code": "seq = 'ATGATGAT'\nmotif = 'ATG'\n\n# Znajdz wszystkie pozycje motif i wypisz je jako: 0 3 ...\n"
    },
    {
        "id": 85,
        "title": "Lekcja teoretyczna: po co sliding window",
        "description": "Checkpoint koncepcyjny.\n\nOkna przesuwne pomagaja wykrywac lokalne sygnaly, np. regiony o podwyzszonym GC lub motywy regulatorowe.\n\nTwoje zadanie:\nWypisz dwie linie: `okno=lokalny sygnal` i `motyw=konkretna sekwencja`.",
        "expected_output": "okno=lokalny sygnal\nmotyw=konkretna sekwencja\n",
        "initial_code": "# Wypisz dwie linie teorii o oknach i motywach\n"
    },
    {
        "id": 86,
        "title": "Odleglosc Hamminga",
        "description": "Odleglosc Hamminga to liczba pozycji, na ktorych dwa napisy tej samej dlugosci sie roznia.\n\nTwoje zadanie:\nPolicz odleglosc Hamminga dla `s1` i `s2` i wypisz wynik.",
        "expected_output": "2\n",
        "initial_code": "s1 = 'GATTACA'\ns2 = 'GACTATA'\n\n# Policz liczbe roznych pozycji i wypisz wynik\n"
    },
    {
        "id": 87,
        "title": "Suma odleglosci par w macierzy",
        "description": "Dla 3 sekwencji masz 3 pary odleglosci nad przekatna.\n\nTwoje zadanie:\nZ podanej macierzy odleglosci wypisz sume elementow nad przekatna.",
        "expected_output": "4\n",
        "initial_code": "M = [\n    [0, 1, 2],\n    [1, 0, 1],\n    [2, 1, 0],\n]\n\n# Wypisz sume elementow nad przekatna\n"
    },
    {
        "id": 88,
        "title": "Sprawdzian 10: FASTA + Hamming",
        "description": "Sprawdzian laczacy parser FASTA i odleglosc Hamminga.\n\nTwoje zadanie:\nWczytaj dwie sekwencje z FASTA i wypisz ich odleglosc Hamminga.",
        "expected_output": "1\n",
        "initial_code": "path = 'ham.fasta'\nwith open(path, 'w') as f:\n    f.write('>a\\nATGC\\n>b\\nATGT\\n')\n\n# Wczytaj dwie sekwencje i wypisz ich odleglosc Hamminga\n"
    },
    {
        "id": 89,
        "title": "Subprocess: uruchomienie komendy z argumentem",
        "description": "Praktyka subprocess: przekazujesz komende jako liste argumentow.\n\nTwoje zadanie:\nUruchom `echo IQTREE_OK` przez subprocess i wypisz stdout po `strip()`.",
        "expected_output": "IQTREE_OK\n",
        "initial_code": "import subprocess\n\n# Uruchom echo IQTREE_OK i wypisz wynik\n"
    },
    {
        "id": 90,
        "title": "Subprocess: kod wyjscia",
        "description": "Kazdy proces zwraca kod wyjscia. 0 oznacza sukces.\n\nTwoje zadanie:\nUruchom `python3 -c \"print(123)\"` przez subprocess i wypisz jego `returncode`.",
        "expected_output": "0\n",
        "initial_code": "import subprocess\n\n# Uruchom python3 -c 'print(123)' i wypisz returncode\n"
    },
    {
        "id": 91,
        "title": "Lekcja teoretyczna: reprodukowalnosc pipeline",
        "description": "Checkpoint praktyki projektowej.\n\nReprodukowalnosc oznacza, ze ten sam kod na tych samych danych daje ten sam wynik.\n\nTwoje zadanie:\nWypisz dwie linie: `loguj parametry` i `zapisuj wersje narzedzi`.",
        "expected_output": "loguj parametry\nzapisuj wersje narzedzi\n",
        "initial_code": "# Wypisz dwie linie o reprodukowalnosci\n"
    },
    {
        "id": 92,
        "title": "JSON config: odczyt progu",
        "description": "Parametry pipeline warto trzymac w configu JSON.\n\nTwoje zadanie:\nWczytaj plik `config.json` i wypisz wartosc pola `min_len`.",
        "expected_output": "5\n",
        "initial_code": "import json\n\npath = 'config.json'\nwith open(path, 'w') as f:\n    json.dump({'min_len': 5, 'min_gc': 50}, f)\n\n# Wczytaj config i wypisz min_len\n"
    },
    {
        "id": 93,
        "title": "JSON config: zastosuj progi",
        "description": "Po wczytaniu configu zastosuj progi do filtrowania sekwencji.\n\nTwoje zadanie:\nPolicz ile sekwencji spelnia jednoczesnie warunki `len >= min_len` oraz `GC >= min_gc` i wypisz wynik.",
        "expected_output": "2\n",
        "initial_code": "config = {'min_len': 4, 'min_gc': 50}\nseqs = ['ATGC', 'GGGG', 'ATAT']\n\n# Zastosuj progi z config i wypisz liczbe pasujacych sekwencji\n"
    },
    {
        "id": 94,
        "title": "Sprawdzian 11: FASTA + config + filtr",
        "description": "Sprawdzian laczacy parser FASTA i parametry z configu.\n\nTwoje zadanie:\nWczytaj FASTA, zastosuj progi `min_len` i `min_gc`, a potem wypisz liczbe sekwencji, ktore przeszly filtr.",
        "expected_output": "1\n",
        "initial_code": "config = {'min_len': 5, 'min_gc': 50}\npath = 'cfg_filter.fasta'\nwith open(path, 'w') as f:\n    f.write('>a\\nATGC\\n>b\\nGGGGG\\n>c\\nATATA\\n')\n\n# Wypisz liczbe sekwencji, ktore przechodza filtry config\n"
    },
    {
        "id": 95,
        "title": "Lekcja teoretyczna: debugowanie krok po kroku",
        "description": "Checkpoint teorii debugowania.\n\nSprawdzaj pipeline warstwowo:\n1) wejscie\n2) stan posredni\n3) wynik koncowy\n\nTwoje zadanie:\nWypisz trzy linie: `1 wejscie`, `2 posrednie`, `3 wynik`.",
        "expected_output": "1 wejscie\n2 posrednie\n3 wynik\n",
        "initial_code": "# Wypisz trzy kroki debugowania pipeline\n"
    },
    {
        "id": 96,
        "title": "Mini pipeline z funkcji etapowych",
        "description": "Laczymy etapy w funkcje: czyszczenie sekwencji i liczenie GC.\n\nTwoje zadanie:\nNapisz funkcje `clean_seq` i `gc_content`, uruchom je dla `raw`, a potem wypisz:\n- oczyszczona sekwencje\n- GC procent.",
        "expected_output": "ATGC\n50.0\n",
        "initial_code": "raw = 'atn gc'\n\ndef clean_seq(s):\n    # usun spacje, usun N i zamien na upper\n    pass\n\ndef gc_content(s):\n    # zwroc procent GC\n    pass\n\n# Uruchom oba etapy i wypisz wynik\n"
    },
    {
        "id": 97,
        "title": "Obsluga KeyError przy translacji",
        "description": "Czasem kodon nie istnieje w slowniku. Program powinien obsluzyc to bez awarii.\n\nTwoje zadanie:\nSprobuj przetlumaczyc kodon i w razie `KeyError` wypisz `brak kodonu`.",
        "expected_output": "brak kodonu\n",
        "initial_code": "kod = {'ATG': 'Met'}\nkodon = 'AAA'\n\n# Uzyj try/except KeyError i wypisz wynik\n"
    },
    {
        "id": 98,
        "title": "Enumerate: znajdz indeks nukleotydu",
        "description": "`enumerate` daje jednoczesnie indeks i wartosc.\n\nTwoje zadanie:\nZnajdz pierwsze wystapienie `G` w sekwencji i wypisz: indeks oraz litere.",
        "expected_output": "2 G\n",
        "initial_code": "seq = 'ATGC'\n\n# Uzyj enumerate, znajdz pierwsze G i wypisz: indeks litera\n"
    },
    {
        "id": 99,
        "title": "Sprawdzian 12: przekroj przed finalem",
        "description": "Przekroj umiejetnosci: czyszczenie, filtr i statystyka.\n\nTwoje zadanie:\nDla listy sekwencji:\n- pomin sekwencje z `N`\n- policz ile zostalo poprawnych\n- policz sredni GC dla poprawnych\n\nWypisz liczbe poprawnych i sredni GC (w osobnych liniach).",
        "expected_output": "3\n50.0\n",
        "initial_code": "seqs = ['ATGC', 'GGGG', 'ATAT', 'ATNG']\n\n# Wypisz liczbe poprawnych sekwencji (bez N)\n# Wypisz sredni GC poprawnych sekwencji\n"
    },
    {
        "id": 100,
        "title": "Final 100: raport koncowy mini pipeline",
        "description": "Lekcja jubileuszowa: laczysz kilka krokow i robisz finalny mini raport.\n\nTwoje zadanie:\nDla listy rekordow policz:\n- liczbe rekordow\n- liczbe rekordow z GC >= 50\n\nWypisz obie wartosci jako dwie linie raportu: `rekordy=...` i `high_gc=...`.",
        "expected_output": "rekordy=3\nhigh_gc=2\n",
        "initial_code": "records = [('a', 'ATGC'), ('b', 'GGGG'), ('c', 'ATAT')]\n\n# Wypisz raport koncowy: rekordy=<liczba>, high_gc=<liczba>\n"
    },
    {
        "id": 101,
        "title": "Wiz 1: histogram GC biny",
        "description": "Budujemy podstawe pod histogram.\n\nTwoje zadanie:\nPolicz ile wartosci z listy `gc` wpada do trzech binow:\n- mniejsze niz 50\n- od 50 do 69\n- co najmniej 70\n\nWypisz wynik jako: `b1 b2 b3`.",
        "expected_output": "2 2 1\n",
        "initial_code": "gc = [42, 55, 68, 71, 30]\n\n# Policz biny i wypisz: b1 b2 b3\n"
    },
    {
        "id": 102,
        "title": "Lekcja teoretyczna: jak czytac histogram",
        "description": "Checkpoint teorii wizualizacji.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `x=zakres wartosci`\n- `y=liczebnosc`.",
        "expected_output": "x=zakres wartosci\ny=liczebnosc\n",
        "initial_code": "# Wypisz 2 linie teorii o histogramie\n"
    },
    {
        "id": 103,
        "title": "Wiz 2: normalizacja min-max",
        "description": "Przed wykresami czesto normalizujemy dane.\n\nTwoje zadanie:\nPolicz znormalizowana wartosc `x=20` dla listy `[10, 20, 30]` wzorem min-max i wypisz wynik.",
        "expected_output": "0.5\n",
        "initial_code": "values = [10, 20, 30]\nx = 20\n\n# Uzyj wzoru: (x - min) / (max - min)\n"
    },
    {
        "id": 104,
        "title": "Wiz 3: punkty scatter",
        "description": "Przygotowujemy dane do scatter plotu.\n\nTwoje zadanie:\nZbuduj liste par `(length, gc)` tylko dla rekordow z GC >= 50 i wypisz cala liste.",
        "expected_output": "[(150, 60), (90, 55)]\n",
        "initial_code": "records = [('s1', 100, 40), ('s2', 150, 60), ('s3', 90, 55)]\n\n# Zbuduj liste par (length, gc) dla gc >= 50 i wypisz ja\n"
    },
    {
        "id": 105,
        "title": "Sprawdzian 13: wizualizacja i statystyka",
        "description": "Sprawdzian laczacy srednia i prosty filtr.\n\nTwoje zadanie:\nDla listy `data` wypisz:\n1) srednia\n2) ile wartosci jest >= 50.",
        "expected_output": "55.0\n3\n",
        "initial_code": "data = [40, 50, 60, 70]\n\n# Wypisz srednia i liczbe elementow >= 50\n"
    },
    {
        "id": 106,
        "title": "Lekcja teoretyczna: skale osi",
        "description": "Checkpoint teorii wykresow.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `zla_skala=zly_wniosek`\n- `opisuj_osie_i_jednostki`.",
        "expected_output": "zla_skala=zly_wniosek\nopisuj_osie_i_jednostki\n",
        "initial_code": "# Wypisz 2 linie teorii o skali osi\n"
    },
    {
        "id": 107,
        "title": "Wiz 4: ascii bar",
        "description": "Szybka wizualizacja tekstowa tez sie przydaje w debugowaniu.\n\nTwoje zadanie:\nDla listy `values` znajdz maksimum i wypisz pasek `#` o tej dlugosci.",
        "expected_output": "####\n",
        "initial_code": "values = [3, 1, 4]\n\n# Wypisz '#' * max(values)\n"
    },
    {
        "id": 108,
        "title": "Wiz 5: pseudo-heatmapa",
        "description": "Mapujemy wartosci macierzy na symbole:\n- `H` dla wartosci >= 5\n- `L` dla wartosci < 5\n\nTwoje zadanie:\nDla kazdego wiersza wypisz linie symboli.",
        "expected_output": "LH\nHL\n",
        "initial_code": "M = [[1, 5], [7, 2]]\n\n# Wypisz 2 linie pseudo-heatmapy\n"
    },
    {
        "id": 109,
        "title": "Wiz 6: srednia odleglosc nad przekatna",
        "description": "Dla macierzy odleglosci liczymy elementy nad przekatna.\n\nTwoje zadanie:\nPolicz srednia wartosc elementow nad przekatna i wypisz wynik.",
        "expected_output": "4.0\n",
        "initial_code": "M = [[0, 2, 4], [2, 0, 6], [4, 6, 0]]\n\n# Policz srednia z elementow nad przekatna\n"
    },
    {
        "id": 110,
        "title": "Sprawdzian 14: wybierz typ wykresu",
        "description": "Sprawdzian decyzji analitycznej.\n\nTwoje zadanie:\nJesli listy `lengths` i `gc` maja ten sam rozmiar > 1, wypisz `scatter`, inaczej `blad`.",
        "expected_output": "scatter\n",
        "initial_code": "lengths = [100, 200, 150]\ngc = [40, 60, 55]\n\n# Wypisz odpowiedni typ wykresu\n"
    },
    {
        "id": 111,
        "title": "Lekcja teoretyczna: supervised vs unsupervised",
        "description": "Checkpoint teorii ML.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `supervised=etykiety`\n- `unsupervised=bez_etykiet`.",
        "expected_output": "supervised=etykiety\nunsupervised=bez_etykiet\n",
        "initial_code": "# Wypisz 2 linie teorii o supervised i unsupervised\n"
    },
    {
        "id": 112,
        "title": "ML 1: train/test split",
        "description": "Podzial danych to podstawa uczciwej oceny modelu.\n\nTwoje zadanie:\nDla `n=10` i `train_frac=0.8` policz liczbe probek train i test, a potem wypisz `train test`.",
        "expected_output": "8 2\n",
        "initial_code": "n = 10\ntrain_frac = 0.8\n\n# Policz train_n=int(n*train_frac), test_n=n-train_n i wypisz: train_n test_n\n"
    },
    {
        "id": 113,
        "title": "ML 2: klasyfikator progowy",
        "description": "Najprostszy model: predykcja 1, gdy score >= threshold.\n\nTwoje zadanie:\nDla listy score'ow i progu zbuduj liste predykcji i wypisz ja.",
        "expected_output": "[0, 1, 1]\n",
        "initial_code": "scores = [0.2, 0.8, 0.6]\nthreshold = 0.5\n\n# Zbuduj liste predykcji 0/1 i wypisz ja\n"
    },
    {
        "id": 114,
        "title": "ML 3: confusion matrix",
        "description": "Liczymy TP, FP, FN, TN.\n\nTwoje zadanie:\nDla `y_true` i `y_pred` wypisz: `TP FP FN TN`.",
        "expected_output": "1 0 1 2\n",
        "initial_code": "y_true = [1, 0, 1, 0]\ny_pred = [1, 0, 0, 0]\n\n# Policz TP FP FN TN i wypisz je w tej kolejnosci\n"
    },
    {
        "id": 115,
        "title": "Sprawdzian 15: precision recall f1",
        "description": "Sprawdzian metryk klasyfikacji.\n\nTwoje zadanie:\nDla TP=4, FP=1, FN=3 policz:\n- precision\n- recall\n- f1\n\nPrecision wypisz bez zaokraglania, recall i f1 zaokraglij do 2 miejsc.",
        "expected_output": "0.8\n0.57\n0.67\n",
        "initial_code": "tp, fp, fn = 4, 1, 3\n\n# Policz precision, recall, f1 i wypisz w 3 liniach\n"
    },
    {
        "id": 116,
        "title": "Lekcja teoretyczna: data leakage",
        "description": "Checkpoint krytyczny dla ML.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `leakage=dane_z_przyszlosci`\n- `split_przed_feature_engineering`.",
        "expected_output": "leakage=dane_z_przyszlosci\nsplit_przed_feature_engineering\n",
        "initial_code": "# Wypisz 2 linie teorii o data leakage\n"
    },
    {
        "id": 117,
        "title": "ML 4: standaryzacja z-score",
        "description": "Liczymy standaryzacje z-score wzorem `(x-mean)/std`.\n\nTwoje zadanie:\nDla podanych wartosci policz z-score i wypisz wynik.",
        "expected_output": "1.0\n",
        "initial_code": "x, mean, std = 7, 5, 2\n\n# Policz z-score i wypisz\n"
    },
    {
        "id": 118,
        "title": "ML 5: nearest centroid",
        "description": "Wybieramy klase centroidu o mniejszym dystansie.\n\nTwoje zadanie:\nPolicz dystans punktu `p` do `c1` i `c2`, a potem wypisz `c1` albo `c2`.",
        "expected_output": "c2\n",
        "initial_code": "p = (4, 4)\nc1 = (1, 1)\nc2 = (6, 6)\n\n# Porownaj dystanse euklidesowe i wypisz blizszy centroid\n"
    },
    {
        "id": 119,
        "title": "ML 6: najlepszy prog",
        "description": "Szukamy progu z najwyzsza accuracy.\n\nTwoje zadanie:\nSprawdz progi 0.5 i 0.7 dla danych `scores` i `y_true`, a potem wypisz lepszy prog.",
        "expected_output": "0.5\n",
        "initial_code": "scores = [0.1, 0.4, 0.6, 0.9]\ny_true = [0, 0, 1, 1]\n\n# Policz accuracy dla 0.5 i 0.7, wypisz lepszy prog\n"
    },
    {
        "id": 120,
        "title": "Sprawdzian 16: porownanie modeli",
        "description": "Sprawdzian wyboru modelu po F1.\n\nTwoje zadanie:\nPolicz F1 dla modelu A (p=0.8, r=0.5) i B (p=0.7, r=0.7).\nWypisz `A` albo `B` dla lepszego modelu.",
        "expected_output": "B\n",
        "initial_code": "pA, rA = 0.8, 0.5\npB, rB = 0.7, 0.7\n\n# Policz F1 dla obu modeli i wypisz nazwe lepszego\n"
    },
    {
        "id": 121,
        "title": "Instalacje 1: komenda pip",
        "description": "W praktyce musisz umiec zlozyc polecenie instalacji pakietow.\n\nTwoje zadanie:\nZ listy `packages` zbuduj i wypisz komende: `python -m pip install ...`.",
        "expected_output": "python -m pip install pandas numpy scikit-learn\n",
        "initial_code": "packages = ['pandas', 'numpy', 'scikit-learn']\n\n# Zbuduj komende pip install i wypisz\n"
    },
    {
        "id": 122,
        "title": "Instalacje 2: requirements parser",
        "description": "Plik requirements moze miec puste linie i komentarze.\n\nTwoje zadanie:\nPolicz aktywne wpisy pakietow i wypisz ich liczbe.",
        "expected_output": "3\n",
        "initial_code": "req_text = 'numpy==2.0.0\\n# komentarz\\npandas>=2.2\\n\\nscikit-learn\\n'\n\n# Policz linie niepuste i niekomentarzowe\n"
    },
    {
        "id": 123,
        "title": "Lekcja teoretyczna: pip vs conda",
        "description": "Checkpoint narzedziowy.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `pip=pakiety_python`\n- `conda=srodowisko_i_pakiety`.",
        "expected_output": "pip=pakiety_python\nconda=srodowisko_i_pakiety\n",
        "initial_code": "# Wypisz 2 linie teorii o pip i conda\n"
    },
    {
        "id": 124,
        "title": "Instalacje 3: sprawdz modul",
        "description": "Mozesz sprawdzic dostepnosc modulu bez importowania go na sile.\n\nTwoje zadanie:\nUzyj `importlib.util.find_spec` dla modulu `json` i wypisz `json_ok`, jesli modul istnieje.",
        "expected_output": "json_ok\n",
        "initial_code": "import importlib.util\n\n# Sprawdz czy modul json istnieje i wypisz json_ok\n"
    },
    {
        "id": 125,
        "title": "Sprawdzian 17: brakujacy pakiet",
        "description": "Sprawdzian instalacyjny.\n\nTwoje zadanie:\nJesli modul `___nie_istnieje___` nie istnieje, wypisz `zainstaluj`.",
        "expected_output": "zainstaluj\n",
        "initial_code": "import importlib.util\nname = '___nie_istnieje___'\n\n# Sprawdz modul i wypisz komunikat\n"
    },
    {
        "id": 126,
        "title": "Subprocess 1: uruchom echo",
        "description": "Podstawowe uruchomienie komendy zewnetrznej.\n\nTwoje zadanie:\nUruchom `echo TOOL_OK` i wypisz stdout po `strip()`.",
        "expected_output": "TOOL_OK\n",
        "initial_code": "import subprocess\n\n# Uruchom echo TOOL_OK i wypisz wynik\n"
    },
    {
        "id": 127,
        "title": "Subprocess 2: obsluga kodu bledu",
        "description": "Proces moze zakonczyc sie kodem bledu.\n\nTwoje zadanie:\nUruchom proces, ktory konczy sie kodem 3, i wypisz `returncode`.",
        "expected_output": "3\n",
        "initial_code": "import subprocess\n\n# Uruchom python3 -c 'import sys; sys.exit(3)' i wypisz returncode\n"
    },
    {
        "id": 128,
        "title": "Lekcja teoretyczna: bezpieczny subprocess",
        "description": "Checkpoint bezpieczenstwa.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `shell_false=bezpieczniej`\n- `lista_argumentow=brak_problemu_quoting`.",
        "expected_output": "shell_false=bezpieczniej\nlista_argumentow=brak_problemu_quoting\n",
        "initial_code": "# Wypisz 2 linie teorii o subprocess\n"
    },
    {
        "id": 129,
        "title": "Subprocess 3: budowa komendy MAFFT",
        "description": "Budujemy komende uruchomienia narzedzia bioinformatycznego.\n\nTwoje zadanie:\nDla pliku `in.fasta` zbuduj komende MAFFT zapisujaca wynik do `out.fasta` i wypisz ja.",
        "expected_output": "mafft --auto in.fasta > out.fasta\n",
        "initial_code": "inp = 'in.fasta'\nout = 'out.fasta'\n\n# Zbuduj i wypisz komende MAFFT\n"
    },
    {
        "id": 130,
        "title": "Sprawdzian 18: MAFFT + IQ-TREE komendy",
        "description": "Sprawdzian laczenia dwoch narzedzi.\n\nTwoje zadanie:\nWypisz dwie linie:\n1) komenda MAFFT tworzaca `aln.fasta`\n2) komenda IQ-TREE dla `aln.fasta`.",
        "expected_output": "mafft --auto in.fasta > aln.fasta\niqtree2 -s aln.fasta -m MFP -B 1000\n",
        "initial_code": "# Wypisz 2 komendy: MAFFT i IQ-TREE\n"
    },
    {
        "id": 131,
        "title": "Pipeline 1: odczyt watkow z configu",
        "description": "Config steruje parametrami uruchomienia.\n\nTwoje zadanie:\nWczytaj liczbe watkow z configu i wypisz ja.",
        "expected_output": "4\n",
        "initial_code": "config = {'threads': 4}\n\n# Wypisz wartosc threads\n"
    },
    {
        "id": 132,
        "title": "Pipeline 2: komenda IQ-TREE z watkami",
        "description": "Laczymy config z budowa komendy.\n\nTwoje zadanie:\nZbuduj komende IQ-TREE z parametrem `-T` pobranym z configu i wypisz ja.",
        "expected_output": "iqtree2 -s aln.fasta -T 4\n",
        "initial_code": "config = {'threads': 4}\n\n# Zbuduj komende iqtree2 -s aln.fasta -T <threads> i wypisz\n"
    },
    {
        "id": 133,
        "title": "Lekcja teoretyczna: reprodukowalnosc 2.0",
        "description": "Checkpoint praktyki zespolowej.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `zapisz_seed`\n- `zapisz_wersje`.",
        "expected_output": "zapisz_seed\nzapisz_wersje\n",
        "initial_code": "# Wypisz 2 linie o reprodukowalnosci\n"
    },
    {
        "id": 134,
        "title": "Pipeline 3: analiza logu",
        "description": "W diagnostyce pipeline liczba bledow jest kluczowa.\n\nTwoje zadanie:\nPolicz ile razy w logu pojawia sie `ERROR` i wypisz liczbe.",
        "expected_output": "2\n",
        "initial_code": "log = 'INFO start\\nERROR brak_pliku\\nWARN retry\\nERROR timeout\\n'\n\n# Policz liczbe wystapien ERROR\n"
    },
    {
        "id": 135,
        "title": "Sprawdzian 19: status uruchomienia",
        "description": "Sprawdzian logiki wykonania narzedzia.\n\nTwoje zadanie:\nJesli `returncode == 0` i `errors == 0`, wypisz `OK`, inaczej `FAIL`.",
        "expected_output": "FAIL\n",
        "initial_code": "returncode = 1\nerrors = 0\n\n# Wypisz status uruchomienia\n"
    },
    {
        "id": 136,
        "title": "VCF feature 1: transitions",
        "description": "Transitions to zmiany A<->G albo C<->T.\n\nTwoje zadanie:\nDla listy wariantow policz liczbe transitions i wypisz wynik.",
        "expected_output": "2\n",
        "initial_code": "variants = [('A', 'G'), ('C', 'T'), ('A', 'T')]\n\n# Policz transitions i wypisz liczbe\n"
    },
    {
        "id": 137,
        "title": "Lekcja teoretyczna: feature engineering",
        "description": "Checkpoint ML praktyczny.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `cechy=informacja_numeryczna`\n- `dobre_cechy=lepszy_model`.",
        "expected_output": "cechy=informacja_numeryczna\ndobre_cechy=lepszy_model\n",
        "initial_code": "# Wypisz 2 linie teorii o cechach\n"
    },
    {
        "id": 138,
        "title": "Feature 2: AT-skew",
        "description": "AT-skew liczony jest jako `(A-T)/(A+T)`.\n\nTwoje zadanie:\nPolicz AT-skew dla sekwencji i wypisz wynik.",
        "expected_output": "-0.2\n",
        "initial_code": "seq = 'AATTTG'\n\n# Policz AT-skew i wypisz wynik\n"
    },
    {
        "id": 139,
        "title": "Feature 3: tabela cech z sekwencji",
        "description": "Tworzymy prosty wektor cech: dlugosc i GC.\n\nTwoje zadanie:\nDla kazdej sekwencji z listy zbuduj tuple `(len, gc_percent)` i wypisz liste tych tuple.",
        "expected_output": "[(4, 50.0), (4, 100.0)]\n",
        "initial_code": "seqs = ['ATGC', 'GGGG']\n\n# Zbuduj liste cech (len, gc_percent) i wypisz\n"
    },
    {
        "id": 140,
        "title": "Sprawdzian 20: etykietowanie po cechach",
        "description": "Sprawdzian laczacy warunki i cechy.\n\nTwoje zadanie:\nDla listy `(length, gc)` nadaj etykiete 1 gdy `length >= 5` i `gc >= 50`, inaczej 0.\nWypisz liste etykiet.",
        "expected_output": "[0, 0, 1]\n",
        "initial_code": "features = [(4, 50.0), (6, 40.0), (7, 60.0)]\n\n# Wypisz liste etykiet 0/1\n"
    },
    {
        "id": 141,
        "title": "Integracja 1: kolejnosc etapow",
        "description": "Pipeline ma konkretna kolejnosc etapow.\n\nTwoje zadanie:\nWypisz etapy polaczone strzalkami `->`.",
        "expected_output": "load->clean->features->model->report\n",
        "initial_code": "stages = ['load', 'clean', 'features', 'model', 'report']\n\n# Wypisz etapy polaczone przez ->\n"
    },
    {
        "id": 142,
        "title": "Integracja 2: raport txt",
        "description": "Raport koncowy to czesto zwykly plik tekstowy.\n\nTwoje zadanie:\nZapisz 3 linie raportu i wypisz ostatnia linie.",
        "expected_output": "f1=0.70\n",
        "initial_code": "path = 'summary.txt'\nlines = ['samples=20', 'accuracy=0.80', 'f1=0.70']\n\n# Zapisz linie do pliku i wypisz ostatnia\n"
    },
    {
        "id": 143,
        "title": "Lekcja teoretyczna: DAG i zaleznosci",
        "description": "Checkpoint architektury pipeline.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `DAG=brak_cykli`\n- `zaleznosci=kolejnosc_uruchomienia`.",
        "expected_output": "DAG=brak_cykli\nzaleznosci=kolejnosc_uruchomienia\n",
        "initial_code": "# Wypisz 2 linie teorii o DAG\n"
    },
    {
        "id": 144,
        "title": "Integracja 3: poprawna kolejnosc zaleznosci",
        "description": "Masz etapy i ich zaleznosci.\n\nTwoje zadanie:\nWypisz jedna poprawna kolejnosc wykonania etapow.",
        "expected_output": "load clean features model report\n",
        "initial_code": "deps = {'features': ['clean'], 'clean': ['load'], 'model': ['features'], 'report': ['model'], 'load': []}\n\n# Wypisz poprawna kolejnosc uruchomienia\n"
    },
    {
        "id": 145,
        "title": "Sprawdzian 21: FASTA + komenda",
        "description": "Sprawdzian laczacy parser i budowe komendy narzedzia.\n\nTwoje zadanie:\nWczytaj FASTA, policz liczbe rekordow i wypisz:\n1) liczbe rekordow\n2) komende MAFFT dla pliku `two.fasta` do `two_aln.fasta`.",
        "expected_output": "2\nmafft --auto two.fasta > two_aln.fasta\n",
        "initial_code": "path = 'two.fasta'\nwith open(path, 'w') as f:\n    f.write('>a\\nATGC\\n>b\\nGGGG\\n')\n\n# Wypisz liczbe rekordow i komende MAFFT\n"
    },
    {
        "id": 146,
        "title": "Lekcja teoretyczna: must-know instalacji",
        "description": "Checklist rzeczy obowiazkowych.\n\nTwoje zadanie:\nWypisz trzy linie:\n- `venv_lub_conda`\n- `requirements_txt`\n- `pip_install_r`.",
        "expected_output": "venv_lub_conda\nrequirements_txt\npip_install_r\n",
        "initial_code": "# Wypisz 3 linie checklisty instalacji\n"
    },
    {
        "id": 147,
        "title": "Instalacje 4: unikalne requirements",
        "description": "Przed zapisem requirements warto usunac duplikaty i uporzadkowac liste.\n\nTwoje zadanie:\nDla listy pakietow wypisz unikalne nazwy posortowane alfabetycznie, polaczone przecinkami.",
        "expected_output": "numpy,pandas,scikit-learn\n",
        "initial_code": "reqs = ['numpy', 'pandas', 'numpy', 'scikit-learn']\n\n# Wypisz unikalne posortowane pakiety jako jeden tekst z przecinkami\n"
    },
    {
        "id": 148,
        "title": "Sprawdzian 22: plan instalacja + test narzedzia",
        "description": "Sprawdzian praktyki wdrozeniowej.\n\nTwoje zadanie:\nWypisz dwie linie:\n1) komenda instalacji `biopython`\n2) komenda testowa dla `iqtree2`.",
        "expected_output": "python -m pip install biopython\niqtree2 -h\n",
        "initial_code": "# Wypisz 2 komendy: instalacja i szybki test narzedzia\n"
    },
    {
        "id": 149,
        "title": "Lekcja teoretyczna: kiedy nie potrzebujesz ML",
        "description": "Nie kazdy problem wymaga modelu uczenia.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `malo_danych=proste_reguly`\n- `najpierw_baseline_potem_ml`.",
        "expected_output": "malo_danych=proste_reguly\nnajpierw_baseline_potem_ml\n",
        "initial_code": "# Wypisz 2 linie teorii o decyzji: reguly czy ML\n"
    },
    {
        "id": 150,
        "title": "Final 150: pelna mini orchestracja",
        "description": "Final etapu 150: laczysz filtry biologiczne, plan instalacji i komende uruchomienia narzedzia.\n\nTwoje zadanie:\nDla listy rekordow policz ile ma GC >= 50 i wypisz raport jako 3 linie:\n- `high_gc=...`\n- `install=...`\n- `run=...`.",
        "expected_output": "high_gc=2\ninstall=python -m pip install biopython\nrun=iqtree2 -s aln.fasta -T 2\n",
        "initial_code": "records = [('a', 'ATGC'), ('b', 'GGGG'), ('c', 'ATAT')]\nthreads = 2\n\n# Wypisz 3 linie raportu koncowego\n"
    },
    {
        "id": 151,
        "title": "Instalacje 8: utworzenie venv",
        "description": "Pierwszy krok bezpiecznego projektu to izolowane srodowisko.\n\nTwoje zadanie:\nWypisz komende tworzenia srodowiska `.venv`.",
        "expected_output": "python -m venv .venv\n",
        "initial_code": "# Wypisz komende tworzenia venv\n"
    },
    {
        "id": 152,
        "title": "Instalacje 9: aktywacja venv",
        "description": "Po utworzeniu srodowiska trzeba je aktywowac.\n\nTwoje zadanie:\nWypisz komende aktywacji dla macOS/Linux.",
        "expected_output": "source .venv/bin/activate\n",
        "initial_code": "# Wypisz komende aktywacji srodowiska\n"
    },
    {
        "id": 153,
        "title": "Lekcja teoretyczna: po co izolacja srodowiska",
        "description": "Checkpoint teorii instalacji.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `izolacja=brak_konfliktow`\n- `powtarzalnosc=te_same_wersje`.",
        "expected_output": "izolacja=brak_konfliktow\npowtarzalnosc=te_same_wersje\n",
        "initial_code": "# Wypisz 2 linie teorii o izolacji srodowiska\n"
    },
    {
        "id": 154,
        "title": "Instalacje 10: komenda pip install z listy",
        "description": "Budujemy komende instalacji z wielu pakietow.\n\nTwoje zadanie:\nZ listy `pkgs` zloz i wypisz jedna komende `python -m pip install ...`.",
        "expected_output": "python -m pip install numpy pandas matplotlib\n",
        "initial_code": "pkgs = ['numpy', 'pandas', 'matplotlib']\n\n# Wypisz komende instalacji\n"
    },
    {
        "id": 155,
        "title": "Instalacje 11: sprawdzanie modulu",
        "description": "Sprawdzamy, czy modul jest dostepny.\n\nTwoje zadanie:\nDla `json` i `___nope___` wypisz `1 0` (1=modul istnieje, 0=brak).",
        "expected_output": "1 0\n",
        "initial_code": "import importlib.util\n\n# Sprawdz dwa moduly i wypisz: 1 0\n"
    },
    {
        "id": 156,
        "title": "Sprawdzian 23: setup projektu",
        "description": "Sprawdzian setupu od zera.\n\nTwoje zadanie:\nWypisz trzy linie: tworzenie venv, aktywacja, instalacja z requirements.",
        "expected_output": "python -m venv .venv\nsource .venv/bin/activate\npython -m pip install -r requirements.txt\n",
        "initial_code": "# Wypisz 3 linie setupu projektu\n"
    },
    {
        "id": 157,
        "title": "Lekcja teoretyczna: pinowanie wersji",
        "description": "Checkpoint teorii dependencies.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `pin=stabilny_build`\n- `brak_pin=ryzyko_regresji`.",
        "expected_output": "pin=stabilny_build\nbrak_pin=ryzyko_regresji\n",
        "initial_code": "# Wypisz 2 linie teorii o pinowaniu\n"
    },
    {
        "id": 158,
        "title": "Instalacje 12: parser requirements",
        "description": "Liczymy aktywne wpisy requirements (bez pustych i bez komentarzy).\n\nTwoje zadanie:\nWypisz liczbe aktywnych linii.",
        "expected_output": "3\n",
        "initial_code": "text = 'numpy==2.0.0\\n# komentarz\\n\\npandas>=2.2\\nscikit-learn\\n'\n\n# Policz aktywne wpisy\n"
    },
    {
        "id": 159,
        "title": "Instalacje 13: komenda z requirements",
        "description": "Drugi standard setupu to instalacja z pliku.\n\nTwoje zadanie:\nWypisz komende instalacji z `requirements.txt`.",
        "expected_output": "python -m pip install -r requirements.txt\n",
        "initial_code": "# Wypisz komende\n"
    },
    {
        "id": 160,
        "title": "Sprawdzian 24: instaluj i sprawdz",
        "description": "Sprawdzian laczacy instalacje i weryfikacje.\n\nTwoje zadanie:\nWypisz dwie linie: komenda instalacji `biopython`, a potem komenda testu importu.",
        "expected_output": "python -m pip install biopython\npython -c \"import Bio; print('OK')\"\n",
        "initial_code": "# Wypisz 2 linie komend\n"
    },
    {
        "id": 161,
        "title": "Lekcja teoretyczna: seed i losowosc",
        "description": "Checkpoint teorii ML.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `seed=powtarzalny_los`\n- `bez_seed=inne_wyniki`.",
        "expected_output": "seed=powtarzalny_los\nbez_seed=inne_wyniki\n",
        "initial_code": "# Wypisz 2 linie teorii o seed\n"
    },
    {
        "id": 162,
        "title": "ML 7: srednie kolumn cech",
        "description": "Mamy macierz cech i liczymy srednia dla kazdej kolumny.\n\nTwoje zadanie:\nDla `X` wypisz srednie kolumn jako `m1 m2`.",
        "expected_output": "3.0 4.0\n",
        "initial_code": "X = [[1, 2], [3, 4], [5, 6]]\n\n# Policz srednie kolumn i wypisz\n"
    },
    {
        "id": 163,
        "title": "ML 8: standaryzacja pojedynczej wartosci",
        "description": "Liczymy z-score dla jednego punktu.\n\nTwoje zadanie:\nPolicz z-score dla `x=14`, `mean=10`, `std=2`.",
        "expected_output": "2.0\n",
        "initial_code": "x, mean, std = 14, 10, 2\n\n# Wypisz z-score\n"
    },
    {
        "id": 164,
        "title": "Wiz 7: etykiety binow",
        "description": "Przygotowujemy etykiete histogramu.\n\nTwoje zadanie:\nDla wartosci `x=67` wypisz etykiete `mid`, gdzie:\n- low < 50\n- mid 50-69\n- high >= 70.",
        "expected_output": "mid\n",
        "initial_code": "x = 67\n\n# Wypisz etykiete binu\n"
    },
    {
        "id": 165,
        "title": "Sprawdzian 25: cechy i filtr",
        "description": "Sprawdzian laczacy cechy i logike warunkowa.\n\nTwoje zadanie:\nDla listy `(len, gc)` wypisz liczbe rekordow, ktore maja `len >= 5` i `gc >= 50`.",
        "expected_output": "2\n",
        "initial_code": "features = [(4, 45), (5, 50), (7, 60)]\n\n# Wypisz liczbe pasujacych rekordow\n"
    },
    {
        "id": 166,
        "title": "Lekcja teoretyczna: niezbalansowane klasy",
        "description": "Checkpoint krytyczny dla klasyfikacji.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `accuracy_moze_oszukac`\n- `patrz_precision_recall`.",
        "expected_output": "accuracy_moze_oszukac\npatrz_precision_recall\n",
        "initial_code": "# Wypisz 2 linie teorii o klasach niezbalansowanych\n"
    },
    {
        "id": 167,
        "title": "ML 9: balanced accuracy",
        "description": "Liczymy balanced accuracy jako srednia TPR i TNR.\n\nTwoje zadanie:\nDla podanych wartosci wypisz balanced accuracy.",
        "expected_output": "0.85\n",
        "initial_code": "tp, fn, tn, fp = 8, 2, 18, 2\n\n# Policz TPR, TNR i balanced accuracy\n"
    },
    {
        "id": 168,
        "title": "ML 10: TPR i FPR",
        "description": "Dla punktu na ROC liczymy TPR i FPR.\n\nTwoje zadanie:\nWypisz `TPR FPR`.",
        "expected_output": "0.8 0.1\n",
        "initial_code": "tp, fn, fp, tn = 8, 2, 1, 9\n\n# Wypisz TPR i FPR\n"
    },
    {
        "id": 169,
        "title": "ML 11: wybor progu po F1",
        "description": "Porownujemy dwa progi i wybieramy lepszy po F1.\n\nTwoje zadanie:\nDla progow 0.4 i 0.6 wypisz lepszy prog.",
        "expected_output": "0.4\n",
        "initial_code": "scores = [0.2, 0.5, 0.8, 0.9]\ny_true = [0, 1, 1, 0]\n\n# Porownaj progi 0.4 i 0.6 po F1 i wypisz lepszy\n"
    },
    {
        "id": 170,
        "title": "Sprawdzian 26: mini raport metryk",
        "description": "Sprawdzian laczacy confusion matrix i metryki.\n\nTwoje zadanie:\nDla TP=3, FP=1, FN=2 wypisz precision i recall (w dwoch liniach).",
        "expected_output": "0.75\n0.6\n",
        "initial_code": "tp, fp, fn = 3, 1, 2\n\n# Wypisz precision i recall\n"
    },
    {
        "id": 171,
        "title": "Lekcja teoretyczna: hiperparametry",
        "description": "Checkpoint teorii modelowania.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `hiperparametr=ustawiasz_przed_treningiem`\n- `parametr=model_uczy_z_danych`.",
        "expected_output": "hiperparametr=ustawiasz_przed_treningiem\nparametr=model_uczy_z_danych\n",
        "initial_code": "# Wypisz 2 linie teorii o hiperparametrach\n"
    },
    {
        "id": 172,
        "title": "ML 12: liczba kombinacji grid search",
        "description": "Grid search testuje wszystkie kombinacje.\n\nTwoje zadanie:\nDla list o rozmiarach 3 i 4 policz liczbe kombinacji.",
        "expected_output": "12\n",
        "initial_code": "a = [1, 2, 3]\nb = ['l1', 'l2', 'l3', 'l4']\n\n# Wypisz liczbe kombinacji\n"
    },
    {
        "id": 173,
        "title": "ML 13: rozmiary foldow",
        "description": "Dla k-fold sprawdzamy rozmiar kazdego folda.\n\nTwoje zadanie:\nDla `n=10`, `k=5` wypisz rozmiary foldow jako jedna linie.",
        "expected_output": "2 2 2 2 2\n",
        "initial_code": "n, k = 10, 5\n\n# Wypisz rozmiary foldow\n"
    },
    {
        "id": 174,
        "title": "ML 14: mean i std cv",
        "description": "Podsumowanie cross-validation to zwykle mean i std.\n\nTwoje zadanie:\nDla listy score'ow wypisz mean i std (std zaokraglij do 2 miejsc).",
        "expected_output": "0.8\n0.08\n",
        "initial_code": "scores = [0.7, 0.8, 0.9]\n\n# Wypisz mean i std\n"
    },
    {
        "id": 175,
        "title": "Sprawdzian 27: wybierz stabilniejszy model",
        "description": "Sprawdzian wyboru modelu po srednim score i stabilnosci.\n\nTwoje zadanie:\nPorownaj modele A i B. Wypisz model o wyzszym mean, a przy remisie wybierz mniejszy std.",
        "expected_output": "B\n",
        "initial_code": "A = [0.80, 0.82, 0.78]\nB = [0.81, 0.81, 0.81]\n\n# Wypisz lepszy model\n"
    },
    {
        "id": 176,
        "title": "Lekcja teoretyczna: po co skalowanie",
        "description": "Checkpoint preprocessingu.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `skalowanie=porownywalne_cechy`\n- `bez_skalowania=dominacja_duzej_skali`.",
        "expected_output": "skalowanie=porownywalne_cechy\nbez_skalowania=dominacja_duzej_skali\n",
        "initial_code": "# Wypisz 2 linie teorii o skalowaniu\n"
    },
    {
        "id": 177,
        "title": "ML 15: min-max lista",
        "description": "Skalujemy cala liste do zakresu [0,1].\n\nTwoje zadanie:\nDla listy `vals` wypisz liste po min-max scaling.",
        "expected_output": "[0.0, 0.5, 1.0]\n",
        "initial_code": "vals = [10, 20, 30]\n\n# Wypisz znormalizowana liste\n"
    },
    {
        "id": 178,
        "title": "ML 16: z-score lista",
        "description": "Liczymy z-score dla calej listy.\n\nTwoje zadanie:\nDla `vals=[2,4,6]` wypisz liste z-score.",
        "expected_output": "[-1.0, 0.0, 1.0]\n",
        "initial_code": "vals = [2, 4, 6]\n\n# Wypisz liste z-score\n"
    },
    {
        "id": 179,
        "title": "Integracja 4: pipeline cech",
        "description": "Opisujemy etapy przetwarzania cech.\n\nTwoje zadanie:\nWypisz etapy `clean`, `scale`, `model` polaczone strzalkami.",
        "expected_output": "clean->scale->model\n",
        "initial_code": "steps = ['clean', 'scale', 'model']\n\n# Wypisz lacuch etapow\n"
    },
    {
        "id": 180,
        "title": "Sprawdzian 28: preprocess + decyzja",
        "description": "Sprawdzian laczacy warunki i cechy po preprocessingu.\n\nTwoje zadanie:\nDla listy `(len, gc)` wypisz ile rekordow spelnia `len >= 6` i `gc >= 50`.",
        "expected_output": "2\n",
        "initial_code": "features = [(4, 40), (6, 55), (7, 49), (8, 80)]\n\n# Wypisz liczbe pasujacych rekordow\n"
    },
    {
        "id": 181,
        "title": "Lekcja teoretyczna: overfitting",
        "description": "Checkpoint generalizacji.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `train_duzo_test_malo=overfit`\n- `male_rozjazdy=lepiej`.",
        "expected_output": "train_duzo_test_malo=overfit\nmale_rozjazdy=lepiej\n",
        "initial_code": "# Wypisz 2 linie teorii o overfittingu\n"
    },
    {
        "id": 182,
        "title": "ML 17: train-test gap",
        "description": "Liczymy roznice train-test i oceniamy ryzyko overfitu.\n\nTwoje zadanie:\nJesli gap > 0.2 wypisz `overfit`, inaczej `ok`.",
        "expected_output": "overfit\n",
        "initial_code": "train = 0.95\ntest = 0.70\n\n# Wypisz ocene\n"
    },
    {
        "id": 183,
        "title": "ML 18: wybor lambda",
        "description": "Wybieramy lambda z najwyzszym score walidacyjnym.\n\nTwoje zadanie:\nWypisz najlepsza wartosc lambda.",
        "expected_output": "0.1\n",
        "initial_code": "val_scores = {0.01: 0.78, 0.1: 0.82, 1.0: 0.80}\n\n# Wypisz najlepsza lambda\n"
    },
    {
        "id": 184,
        "title": "ML 19: early stopping",
        "description": "Wstrzymujemy trening po `patience` epokach bez poprawy.\n\nTwoje zadanie:\nDla podanych strat wypisz numer epoki, na ktorej nastapi stop (1-indexed).",
        "expected_output": "5\n",
        "initial_code": "loss = [0.50, 0.45, 0.44, 0.44, 0.45]\npatience = 2\n\n# Wypisz epoke stopu\n"
    },
    {
        "id": 185,
        "title": "Sprawdzian 29: decyzja o generalizacji",
        "description": "Sprawdzian koncowy sekcji generalizacji.\n\nTwoje zadanie:\nDla train, val, test wypisz `OK`, jesli roznice miedzy nimi nie przekraczaja 0.1, inaczej `FAIL`.",
        "expected_output": "OK\n",
        "initial_code": "train, val, test = 0.90, 0.88, 0.86\n\n# Wypisz status\n"
    },
    {
        "id": 186,
        "title": "Lekcja teoretyczna: rola programow zewnetrznych",
        "description": "Checkpoint integracji bioinformatycznej.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `python=orchestracja`\n- `narzedzia=obliczenia_specjalistyczne`.",
        "expected_output": "python=orchestracja\nnarzedzia=obliczenia_specjalistyczne\n",
        "initial_code": "# Wypisz 2 linie teorii o integracji narzedzi\n"
    },
    {
        "id": 187,
        "title": "Integracja 5: para komend MAFFT i IQ-TREE",
        "description": "Budujemy dwa kolejne kroki analizy filogenetycznej.\n\nTwoje zadanie:\nWypisz dwie linie: komenda MAFFT, potem komenda IQ-TREE (T=4).",
        "expected_output": "mafft --auto in.fasta > aln.fasta\niqtree2 -s aln.fasta -m MFP -T 4\n",
        "initial_code": "# Wypisz dwie komendy w poprawnej kolejnosci\n"
    },
    {
        "id": 188,
        "title": "Integracja 6: parser logu runtime",
        "description": "Wyciagamy liczbe sekund z logu.\n\nTwoje zadanie:\nZ linii `Runtime: 123 sec` wypisz samo `123`.",
        "expected_output": "123\n",
        "initial_code": "line = 'Runtime: 123 sec'\n\n# Wypisz liczbe sekund\n"
    },
    {
        "id": 189,
        "title": "Integracja 7: komenda Dsuite",
        "description": "Budujemy komende dla testow introgresji.\n\nTwoje zadanie:\nDla podanych nazw plikow wypisz komende Dsuite Dtrios.",
        "expected_output": "Dsuite Dtrios tree.nwk vars.vcf sets.txt\n",
        "initial_code": "tree = 'tree.nwk'\nvcf = 'vars.vcf'\nsets = 'sets.txt'\n\n# Wypisz komende Dsuite Dtrios\n"
    },
    {
        "id": 190,
        "title": "Sprawdzian 30: plan uruchomienia narzedzi",
        "description": "Sprawdzian laczacy instalacje i dwa kroki narzedziowe.\n\nTwoje zadanie:\nWypisz trzy linie: install, align, tree.",
        "expected_output": "python -m pip install biopython\nmafft --auto in.fasta > aln.fasta\niqtree2 -s aln.fasta -T 4\n",
        "initial_code": "# Wypisz 3 linie planu uruchomienia\n"
    },
    {
        "id": 191,
        "title": "Lekcja teoretyczna: workflow manager",
        "description": "Checkpoint architektury workflow.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `workflow=automatyzacja_krokow`\n- `zaleznosci=kontrola_kolejnosci`.",
        "expected_output": "workflow=automatyzacja_krokow\nzaleznosci=kontrola_kolejnosci\n",
        "initial_code": "# Wypisz 2 linie teorii o workflow managerze\n"
    },
    {
        "id": 192,
        "title": "Workflow 1: co mozna uruchomic teraz",
        "description": "Krok jest runnable, gdy wszystkie zaleznosci sa juz done.\n\nTwoje zadanie:\nDla podanych deps i done wypisz nazwe kroku, ktory mozna uruchomic teraz.",
        "expected_output": "clean\n",
        "initial_code": "deps = {'clean': ['load'], 'features': ['clean']}\ndone = {'load'}\n\n# Wypisz krok runnable\n"
    },
    {
        "id": 193,
        "title": "Workflow 2: poprawna kolejnosc",
        "description": "Wyznaczamy logiczna kolejnosc etapow.\n\nTwoje zadanie:\nWypisz kolejnosc: load clean features model.",
        "expected_output": "load clean features model\n",
        "initial_code": "# Wypisz poprawna kolejnosc etapow\n"
    },
    {
        "id": 194,
        "title": "Workflow 3: brakujace pliki",
        "description": "Przed uruchomieniem kroku trzeba sprawdzic wejscia.\n\nTwoje zadanie:\nPolicz ile plikow z `required` nie ma w `existing` i wypisz liczbe.",
        "expected_output": "1\n",
        "initial_code": "required = ['a.fasta', 'b.tsv', 'c.vcf']\nexisting = {'a.fasta', 'c.vcf'}\n\n# Wypisz liczbe brakujacych plikow\n"
    },
    {
        "id": 195,
        "title": "Sprawdzian 31: RUN czy STOP",
        "description": "Sprawdzian logiki workflow.\n\nTwoje zadanie:\nJesli `missing > 0` wypisz `STOP`, w przeciwnym razie `RUN`.",
        "expected_output": "STOP\n",
        "initial_code": "missing = 1\n\n# Wypisz decyzje\n"
    },
    {
        "id": 196,
        "title": "Lekcja teoretyczna: dokumentacja projektu",
        "description": "Checkpoint praktyki zespolowej.\n\nTwoje zadanie:\nWypisz dwie linie:\n- `README=jak_uruchomic`\n- `CHANGELOG=co_sie_zmienilo`.",
        "expected_output": "README=jak_uruchomic\nCHANGELOG=co_sie_zmienilo\n",
        "initial_code": "# Wypisz 2 linie teorii o dokumentacji\n"
    },
    {
        "id": 197,
        "title": "Release 1: sekcje README",
        "description": "Tworzymy checkliste sekcji README.\n\nTwoje zadanie:\nPolicz liczbe sekcji w liscie `sections` i wypisz wynik.",
        "expected_output": "5\n",
        "initial_code": "sections = ['Opis', 'Instalacja', 'Dane', 'Uruchomienie', 'Wyniki']\n\n# Wypisz liczbe sekcji\n"
    },
    {
        "id": 198,
        "title": "Release 2: manifest wersji",
        "description": "Wypisujemy manifest wersji narzedzi w stalej kolejnosci.\n\nTwoje zadanie:\nDla slownika `versions` wypisz jedna linie `key=value` oddzielona srednikami i posortowana po kluczu.",
        "expected_output": "iqtree=2.3;mafft=7.5;python=3.12\n",
        "initial_code": "versions = {'python': '3.12', 'mafft': '7.5', 'iqtree': '2.3'}\n\n# Wypisz manifest w stalej kolejnosci\n"
    },
    {
        "id": 199,
        "title": "Sprawdzian 32: release gate",
        "description": "Finalny test gotowosci wydania.\n\nTwoje zadanie:\nJesli wszystkie checki sa True wypisz `PASS`, inaczej `FAIL`.",
        "expected_output": "FAIL\n",
        "initial_code": "checks = [True, True, False]\n\n# Wypisz PASS albo FAIL\n"
    },
    {
        "id": 200,
        "title": "Final 200: pelny raport gotowosci pipeline",
        "description": "Final etapu 200: laczysz metryki biologiczne, instalacje i kroki narzedziowe.\n\nTwoje zadanie:\nDla listy rekordow wypisz piec linii raportu:\n- `samples=...`\n- `high_gc=...`\n- `install=...`\n- `align=...`\n- `tree=...`.",
        "expected_output": "samples=3\nhigh_gc=2\ninstall=python -m pip install -r requirements.txt\nalign=mafft --auto in.fasta > aln.fasta\ntree=iqtree2 -s aln.fasta -T 4\n",
        "initial_code": "records = [('a', 'ATGC'), ('b', 'GGGG'), ('c', 'ATAT')]\n\n# Wypisz 5 linii raportu koncowego\n"
    }
]