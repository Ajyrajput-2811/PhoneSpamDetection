from django.test import TestCase
from faker import Faker
from .models import User

class PopulateDatabaseTestCase(TestCase):
    def setUp(self):
        self.fake = Faker()

    def test_populate_database(self):
        num_records = 100  
        for _ in range(num_records):
            name = self.fake.name()
            phone_num = self.fake.phone_number()
            email = self.fake.email()
            password = self.fake.password()
            User.objects.create(name=name, phone_num=phone_num, email=email, password=password)
        total_users = User.objects.count()
        self.assertEqual(total_users, num_records)

