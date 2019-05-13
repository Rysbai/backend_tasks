import os


def work_on():
    patch = os.getcwd()
    print('Working on {}'.format(patch))
    return patch


def size_of():
    with open('text.txt') as f:
        contents = f.read()

    return len(contents)


class Helper:
    def __init__(self, path):
        self.path = path

    def get_path(self):
        base_dir = os.getcwd()
        return os.path.join(base_dir, self.path)


class Worker:

    def __init__(self):
        self.helper = Helper('db')

    def work(self):
        path = self.helper.get_path()
        print(f'Working on {path}')
        return path


class Pricer:
    DISCOUNT = 0.80

    def get_discounted_price(self, price):
        return price * self.DISCOUNT


class Field:
    def __init__(self, type, default, value=None):
        self.type = type
        self.default = default
        self._value = value

    @property
    def value(self):
        if self._value is None:
            return self.default
        else:
            return self._value


COUNTRIES = ('US', 'KG', 'RU', 'AU', 'DE')


class CountryPricer:
    DISCOUNT = 0.8
    country = Field(type="str", default=COUNTRIES[0])

    def get_discount_price(self, price, country):
        if country == self.country.value:
            return price * self.DISCOUNT
        else:
            return price
