import json


class write_from_file:
    '''
      Объект класса write_from_file.

      Он нужен для того, чтобы считать данные из файла.

      Attributes
      ----------
        data: list
            Список, в котором хранятся данные.
    '''
    data: list

    def __init__(self, path: str) -> None:
        '''
            Инициализирует экземпляр класса write_from_file.

            Parameters
            ----------
              path: str
                Строковый параметр: путь, по которому находится файл.
        '''
        self.data = json.load(open(path, encoding='utf-8'))

    def get_data(self) -> list:
        '''
          Возвращает список словарей.

          Returns
          -------
            list:
              Список словарей.
        '''
        return self.data
