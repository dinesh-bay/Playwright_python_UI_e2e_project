from faker import Faker
import random
import string


class RandomDataUtil:
    def __init__(self):
        self.faker = Faker()

    def get_first_name(self) -> str:
        return self.faker.first_name()

    def get_last_name(self) -> str:
        return self.faker.last_name()

    def get_full_name(self) -> str:
        return self.faker.name()

    def get_email(self) -> str:
        return self.faker.email()

    def get_phone_number(self) -> str:
        return self.faker.phone_number()

    def get_username(self) -> str:
        return self.faker.user_name()

    def get_password(self, length: int = 10) -> str:
        return self.faker.password(length=length)

    def get_random_country(self) -> str:
        return self.faker.country()

    def get_random_state(self) -> str:
        return self.faker.state()

    def get_random_city(self) -> str:
        return self.faker.city()

    def get_random_pin(self) -> str:
        return self.faker.postcode()

    def get_random_address(self) -> str:
        return self.faker.street_address()

    def get_random_alphanumeric(self, length: int) -> str:
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def get_random_numeric(self, length: int) -> str:
        return ''.join(random.choice(string.digits) for _ in range(length))

    def get_random_uuid(self) -> str:
        return str(self.faker.uuid4())
