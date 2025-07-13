from smartphone import Smartphone

catalog = [
    Smartphone('Xiaomi', 'Redmi 9', '+7922 1112233'),
    Smartphone('Realme', '13 Pro', '+7912 2562233'),
    Smartphone('Samsung', 'X10', '+7922 2582211'),
    Smartphone('Xiaomi', 'Mi 5', '+7937 1112233'),
    Smartphone('Samsung', 'X12', '+7912 1112288')
]

for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model}. {smartphone.number}')
