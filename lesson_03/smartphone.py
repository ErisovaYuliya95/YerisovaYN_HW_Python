class Smartphone:

    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        if number[:3] == '+79':
            self.number = number
        else:
            raise ValueError("Неверный формат номера телефона")
