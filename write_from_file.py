import json

class write_from_file:
    data: list

    def __init__(self, path: str) -> None:
        self.data = json.load(open(path, encoding='utf-8'))

    def get_data(self) -> list:
        return self.data