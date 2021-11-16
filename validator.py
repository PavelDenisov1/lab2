import re
import time
import entry
from tqdm import tqdm


class validator:
    entries: list[entry]
    valid_entries: list[entry]
    invalid_entries: list[entry]
    error_types: entry

    def __init__(self, entries: list) -> None:
        self.entries = []
        for entry in entries:
            self.entries.append(entry)
        self.valid_entries = []
        self.invalid_entries = []
        self.error_types = {
            "telephone": 0,
            "weight": 0,
            "inn": 0,
            "passport_series": 0,
            "occupation": 0,
            "age": 0,
            "academic_degree": 0,
            "worldview": 0,
            "address": 0
        }

    def get_data(self) -> list:
        return self.valid_entries

    def get_count_valid_entries(self) -> int:
        return len(self.valid_entries)

    def get_count_invalid_entries(self) -> int:
        return len(self.invalid_entries)

    def get_error_types(self) -> dict:
        return self.error_types

    def parse(self) -> None:
        for entry in self.entries and tqdm(self.entries):
            key_list = self.parse_entry(entry)
            if not key_list:
                self.valid_entries.append(entry)
            else:
                self.invalid_entries.append(entry)
                for key in key_list:
                    self.error_types[key] += 1

    def parse_entry(self, entry: dict) -> list[str]:
        keys = []
        for key in entry.keys():
            if not self.check(key, entry[key]):
                keys.append(key)
        return keys

    def check(self, key: str, value: str) -> bool:
        pattern = ''
        if key == 'telephone':
            pattern = '\\+[0-9]-\\([0-9]{3}\\)\\-[0-9]{3}\\-[0-9]{2}\\-[0-9]{2}'
        elif key == 'weight':
            try:
                float_weight = float(value)
                return 200 > float_weight > 40
            except ValueError:
                return False
        elif key == 'inn':
            pattern = '^\\d{12}$'
        elif key == 'passport_series':
            return len(str(value)) == 5
        elif key == 'occupation':
            pattern = '[а-яА-Я]+'
        elif key == 'age':
            try:
                int_age = int(value)
                return int_age >= 18 and int_age < 120
            except ValueError:
                return False
        elif key == 'academic_degree' or key == 'worldview':
            pattern = '[a-zA-Zа-яА-Я]+'
        elif key == 'address':
            pattern = '.+[0-9]+'
        if re.match(pattern, value):
            return True
        return False