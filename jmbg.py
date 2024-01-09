import datetime

_political_region_codes = {'00': 'Foreigner', '01': 'Foreigner', '02': 'Foreigner', '03': 'Foreigner',
                           '04': 'Foreigner',
                           '05': 'Foreigner', '06': 'Foreigner', '07': 'Foreigner', '08': 'Foreigner',
                           '09': 'Foreigner',
                           '10': 'Banja Luka', '11': 'Bihać', '12': 'Doboj', '13': 'Goražde', '14': 'Livno',
                           '15': 'Mostar', '16': 'Prijedor', '17': 'Sarajevo', '18': 'Tuzla', '19': 'Zenica',
                           '20': 'Crna gora', '21': 'Podgorica', '22': 'Crna gora', '23': 'Crna gora',
                           '24': 'Crna gora',
                           '25': 'Crna gora', '26': 'Nikšić', '27': 'Crna gora', '28': 'Crna gora', '29': 'Pljevlja',
                           '30': 'Osijek', '31': 'Bjelovar', '32': 'Varaždin', '33': 'Zagreb', '34': 'Karlovac',
                           '35': 'Gospić', '36': 'Rijeka', '37': 'Sisak', '38': 'Split', '39': 'Hrvatska',
                           '40': '----', '41': 'Bitolj', '42': 'Kumanovo', '43': 'Ohrid', '44': 'Prilep',
                           '45': 'Skoplje', '46': 'Strumica', '47': 'Tetovo', '48': 'Veles', '49': 'Štip',
                           '50': 'Slovenija',
                           '60': 'Temporary residence', '61': 'Temporary residence', '62': 'Temporary residence',
                           '63': 'Temporary residence', '64': 'Temporary residence',
                           '65': 'Temporary residence', '66': 'Temporary residence', '67': 'Temporary residence',
                           '68': 'Temporary residence', '69': 'Temporary residence',
                           '70': 'Serbia', '71': 'Beograd', '72': 'Šumadija', '73': 'Niš', '74': 'J. Morava',
                           '75': 'Zaječar', '76': 'Podunavlje', '77': 'Podrinje', '78': 'Kraljevo', '79': 'Užice',
                           '80': 'Novi Sad', '81': 'Sombor', '82': 'Subotica', '83': 'Vojvodina', '84': 'Vojvodina',
                           '85': 'Zrenjanin', '86': 'Pančevo', '87': 'Kikinda', '88': 'Ruma', '89': 'S. Mitrovica',
                           '90': 'KiM', '91': 'Priština', '92': 'K. Mitrovica', '93': 'Peć', '94': 'Đakovica',
                           '95': 'Prizren', '96': 'KiM', '97': 'KiM', '98': 'KiM', '99': 'KiM',
                           }


class jmbg:
    """A class used to represent a JMBG number (Eng: UMCN)

    Unique Master Citizen Number (Cr/Ba/Srb: Jedinstveni matični broj građana, JMBG)
    is an identification number that is assigned to every citizen of former Yugoslav republics of the SFR Yugoslavia.
    This function can be used to efficiently verify a JMBG number, and to simply access all data contained inside.

    Attributes
    ----------
    _array : list
        JMBG number split in a list of 13 characters
    """

    def __init__(self, jmbg_number: str):
        """
        Parameters
        ----------
        jmbg_number : str
            The JMBG number (Eng: UMCN) - exactly 13 characters
        """
        if len(jmbg_number) != 13:
            raise ValueError('Incorrect length of the JMBG number - must be 13 characters long')

        self._array = list(jmbg_number)

    def __str__(self):
        return "".join(self._array)

    def _first_digit_year(self):
        """Calculates the first digit of year of birth based on the current date

        Returns
        -------
        y : str
            first digit of year of birth
        """

        current_year = datetime.date.today().year.__str__()  # for calculating breakpoints between 1999 and 2000 etc...
        if int(self._array[4]) < 5 + int(current_year[1]):
            y = current_year[0]
        else:
            y = int(current_year[0]) - 1
        return str(y)

    def date(self) -> datetime.date:
        """Gets complete date of birth

        Returns
        -------
        date
            date of birth, or -1 when date is not valid
        """

        d = self._array[0] + self._array[1]
        m = self._array[2] + self._array[3]
        y = self._first_digit_year() + self._array[4] + self._array[5] + self._array[6]

        valid_date = None
        try:
            new_date = datetime.date.fromisoformat(f"{y}-{m}-{d}")
            valid_date = True
        except ValueError:
            valid_date = False

        return datetime.date.fromisoformat(f"{y}-{m}-{d}") if valid_date else -1

    def political_region_code(self) -> str:
        """Gets a two-digit code of a political region

        Use method self.political_region to get the name of the political region

        Returns
        -------
        political_region_code
            two-digit code of a political region
        """

        return self._array[7] + self._array[8]

    def political_region(self) -> str:
        """Gets the name of the political region where the person was born (containing č,ć,š...), or the string
        'Foreigner' when the person was not born in one of the political regions, or the string 'Temporary residence'
        for such cases

        Returns
        -------
        political_region
            name of the political region or strins 'Foreigner' and 'Temporary residence'
        """

        return _political_region_codes[self.political_region_code()]

    def ordinal(self) -> str:
        """Gets the unique ordinal number of the particular RR (represents a person within the DDMMYYYRR section in the
        particular political region)

        000–499: male, 500–999: female

        Returns
        -------
        ordinal
            three-digit code
        """

        return self._array[9] + self._array[10] + self._array[11]

    def gender(self) -> str:
        """Gets the persons' gender

        Returns
        -------
        gender
            'Male' or 'Female'
        """

        return 'Male' if int(self.ordinal()) < 500 else 'Female'

    def control_digit(self) -> str:
        """Gets the control digit (last digit)

        Returns
        -------
        control_digit
            control digit
        """

        return self._array[12]

    def is_valid(self) -> bool:
        """Validates the JMBG number

        Checks if the JMBG number is valid according to the official format 'abcdefghijklm', using the control digit
        and the formula: m = 11 − (( 7×(a + g) + 6×(b + h) + 5×(c + i) + 4×(d + j) + 3×(e + k) + 2×(f + l) ) mod 11)

        Returns
        -------
        valid
            True if the JMBG is valid, or False if there's an error
        """

        valid_date = None
        if self.date() != -1:
            valid_date = True
        else:
            return False

        formula = 7 * (int(self._array[0]) + int(self._array[6])) + \
                  6 * (int(self._array[1]) + int(self._array[7])) + \
                  5 * (int(self._array[2]) + int(self._array[8])) + \
                  4 * (int(self._array[3]) + int(self._array[9])) + \
                  3 * (int(self._array[4]) + int(self._array[10])) + \
                  2 * (int(self._array[5]) + int(self._array[11]))

        control = 11 - (int(formula) % 11)

        valid_control_digit = True if str(control) == self.control_digit() else False

        return valid_control_digit and valid_date

