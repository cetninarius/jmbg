# JMBG Paket

Python paket za validaciju i rad sa Jedinstvenim matičnim brojevima građana (JMBG). 

>(Click [here](README.md) for English version)

## Šta je JMBG

Jedinstveni matični broj građana (skraćeno JMBG) je identifikacioni broj dat svim novorođenim građanima SFRJ
(Socijalističke Federativne Republike Jugoslavije) od 1976. godine.

Svi građani rođeni pre 1976. godine su dobili broj zavisno od regiona u kojem su tada živjeli. 
Broj je još uviek u upotrebi u državama novonastalim od bivših republika SFRJ.

Pogledajte [Wikipediju](https://sh.wikipedia.org/wiki/Jedinstveni_mati%C4%8Dni_broj_gra%C4%91ana) za više informacija.

## Installacija

Za instalaciju paketa koristite paket-menadžer [pip](https://pip.pypa.io/en/stable/).

```bash
pip install jmbg
```

## Upotreba

```python
from jmbg import jmbg

# inicijalizacija JMBG objekta
x = jmbg('0404003710088')
```

### Validacija
```python
x.is_valid()
# vraća: True
```
Proverava da li je JMBG validan po zvaničnom formatu 'abcdefghijklm', koristeći kontrolnu cifru i formulu::
> m = 11 − (( 7×(a + g) + 6×(b + h) + 5×(c + i) + 4×(d + j) + 3×(e + k) + 2×(f + l) ) mod 11)


### Datum rođenja
```python
x.date()
# vraća: datetime.date(2003, 4, 4)
```

### Region (grad) rođenja
```python
x.political_region()
# vraća: 'Beograd'
```
Vraća naziv grada (političkog regiona) gde je osoba rođena, ili string 'Foreigner' 
za strance, i 'Temporary residence' za osobe sa privremenim boravkom.

### Redni broj
```python
x.ordinal()
# vraća: '008'
```
Vraća redni broj rođenja osobe tog dana na tom političkom regionu

000–499 za muškarce, i 500–999 za žene.

### Pol
```python
x.gender()
# vraća: 'Male'
```

### Controlna cifra
```python
x.control_digit()
# vraća: '8'
```
Vraća kontrolnu cifru JMBG-a (poslednju cifru)

## Saradnja
Pull request-ovi su dobrodošli. Za veće izmene, prvo otvorite 'issue' na Github-u kako bismo mogli da diskutujemo.

Kontaktirajte me za sve zahteve i sugestije.

Mejl: [Radomir Perišić](mailto:radomirraca2003@gmail.com)

## License
[MIT](https://choosealicense.com/licenses/mit/)