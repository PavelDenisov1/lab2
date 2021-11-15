class entry:
    telephone: str
    weight: str
    inn: str
    passport_series: str
    occupation: str
    age: str
    academic_degree: str
    worldview: str
    address: str

    def __init__(self, dic: dict) -> None:
        self.telephone = dic['telephone']
        self.weight = dic['weight']
        self.inn = dic['inn']
        self.passport_series = dic['passport_series']
        self.occupation = dic['occupation']
        self.age = dic['age']
        self.academic_degree = dic['academic_degree']
        self.worldview = dic['worldview']
        self.address = dic['address']