"""W pliku tramwaje.json znajdują się dane z numerami aktualnie kursujących linii tramwajowych w Krakowie oraz przystanków, przez które przejeżdża dany tramwaj (stan na 5.11.2023). W języku Python, czytanie danych w formatach .json czy .csv jest wykonywane z pomocą modułów. W naszym przypadku:
import json
with open('tramwaje.json', "r", encoding='utf-8') as read_file:
data = json.load(read_file)
Wczytane dane (zróbmy print) są złożone z zagnieżdżonych typów: słownika, listy, słownika, listy: {'tramwaje': [{'linia': '1', 'przystanek': [{'nazwa': 'Wańkowicza 01'}, {'nazwa': 'Cienista 01'}, {'nazwa': 'Teatr Ludowy 01'}, …
Zatem, przykładowo, żeby odczytać pierwszy przystanek dla linii 1, trzeba wywołać w konsoli:
data['tramwaje'][0]['przystanek'][0]['nazwa'] żeby zobaczyć nazwę 'Wańkowicza 01'.
Należy przepisać dane do uproszczonego formatu typu słownik, którego kluczem będzie numer linii tramwajowej (zapisany jako int), a wartością krotka zawierająca wszystkie nazwy przystanków danej linii. Uwaga: technicznie przystanki oprócz nazw mają też numery, proszę uprościć dane, zapisując wyłącznie nazwy przystanków, bez końcowych numerów (01, 02…). Przykładowo, dla linii nr 1 spodziewany format danych wygląda następująco: {1: ('Wańkowicza', 'Cienista', 'Teatr Ludowy', 'Rondo Kocmyrzowskie im. Ks. Gorzelanego', 'Bieńczycka', 'Rondo Czyżyńskie', 'Centralna', 'Rondo 308. Dywizjonu', 'M1 al. Pokoju', 'TAURON Arena Kraków al. Pokoju', 'Dąbie', 'Ofiar Dąbia', 'Fabryczna', 'Francesco Nullo', 'Teatr Variété', 'Rondo Grzegórzeckie', 'Hala Targowa', 'Starowiślna', 'Poczta Główna', 'Plac Wszystkich Świętych', 'Filharmonia', 'UJ / AST', 'Muzeum Narodowe', 'Oleandry', 'Park Jordana', 'Reymana')}
Proszę wynik konwersji zapisać do pliku wyjściowego (również w formacie .json), np. w ten sposób:
with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
json.dump(trams, file, ensure_ascii=False)
W przykładzie założono, że słownik jest pod nazwą trams. Ponadto, proszę wypisać na ekranie następujące informacje: numer linii – liczba przystanków, posortowane po liczbie przystanków w kolejności malejącej. Na koniec wypisać również liczbę (nie nazwy) wszystkich przystanków obsługiwanych przez tramwaje (w tym celu należy znaleźć część wspólną krotek z nazwami przystanków, bo tramwaje często współdzielą ten sam przystanek). Uwaga: jako rozwiązanie proszę wysłać zarówno kod programu oraz wyjątkowo również otrzymany plik wynikowy."""

import json
from icecream import ic

with open("tramwaje.json", "r", encoding="utf-8") as read_file:
    data = json.load(read_file)
trams = dict()
for lines in data["tramwaje"]:
    trams[int(lines["linia"])] = tuple(
        przystanek["nazwa"][: len(przystanek["nazwa"]) - 3]
        for przystanek in lines["przystanek"]
    )
with open("tramwaje_out.json", "w", encoding="utf-8") as file:
    json.dump(trams, file, ensure_ascii=False)

tempTrams = trams
stops = {stop for stop in trams.values()}
stops = {i for stop in stops for i in stop}


for line in tempTrams.keys():
    tempTrams[line] = len(tempTrams[line])

sortedTrams = dict(sorted(tempTrams.items(), key=lambda x: x[1], reverse=True))

for t_key in sortedTrams.keys():
    print("Linia " + str(t_key) + " - " + str(sortedTrams[t_key]) + " przystanków")


print("\nLiczba wszystkich przystanków: " + str(len(stops)))
