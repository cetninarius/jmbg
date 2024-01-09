# JMBG Package

A python package for validating and processing JMBG numbers (Eng: UMCN).

>(Kliknite [ovde](README.sr.md) za verziju na Srpskom)

## What is a JMBG

Unique Master Citizen Number (Cr/Ba/Srb: Jedinstveni matični broj građana, JMBG)
is an identification number that is assigned to every citizen of former Yugoslav republics of the SFR Yugoslavia.
This function can be used to efficiently verify a JMBG number, and to simply access all data contained inside.

Check [wiki](https://en.wikipedia.org/wiki/Unique_Master_Citizen_Number) for more information.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install JMBG.

```bash
pip install jmbg
```

## Usage

```python
from jmbg import jmbg

# initializes a JMBG object
x = jmbg('0404003710088')
```

### Validation
```python
x.is_valid()
# returns: True
```
Checks if the JMBG number is valid according to the official format 'abcdefghijklm', using the control digit and the formula:
> m = 11 − (( 7×(a + g) + 6×(b + h) + 5×(c + i) + 4×(d + j) + 3×(e + k) + 2×(f + l) ) mod 11)


### Date of birth
```python
x.date()
# returns: datetime.date(2003, 4, 4)
```

### Political region of birth
```python
x.political_region()
# returns: 'Beograd'
```
Gets the name of the political region where the person was born (containing č,ć,š...), or the string
'Foreigner' when the person was not born in one of the political regions, or the string 'Temporary residence'
when a person is a temporary resident.

### Ordinal code
```python
x.ordinal()
# returns: '008'
```
Gets the unique ordinal number of the particular RR (represents a person within the DDMMYYYRR section in the
particular political region).

000–499 codes are used for male gender, while 500–999 codes are used for female gender.

### Gender
```python
x.gender()
# returns: 'Male'
```

### Control digit
```python
x.control_digit()
# returns: '8'
```
Gets the control digit (last digit)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please contact me for any requests and suggestions.

Mail: [Radomir Perišić](mailto:radomirraca2003@gmail.com)

## License
[MIT](https://choosealicense.com/licenses/mit/)