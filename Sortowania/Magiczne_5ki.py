#Magiczne 5ki - wybór k-tego elementu w czasie O(n) bez ryzyka ukwadratowienia

#A - tablica n liczb (szukamy liczby, która po posortowaniu byłaby pozycji k)

#1. Podziel A na (sufit z) n/5 grup po 5 elementów
#2. Rekurencyjnie znajduje x, mediane wśród median naszych piątek
#3. Wykonaj partition używając x jako pivot
#4. Jeśli x jest na pozycji k, to zwróć x
#   Jeśli x jest na pozycji dalszej niż k, to szukaj rekurencyjnie w lewej cześci tablicy, w przeciwnym razie w prawej
