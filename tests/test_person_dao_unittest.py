import unittest
from model.person import Person
from model.email import Email
from dao.person_dao import PersonDAO

class TestPersonDAO(unittest.TestCase):

    def setUp(self):
        self.dao = PersonDAO()

    def test_valid_person(self):
        person = Person(1, "John Doe", 30)
        person.add_email(Email(1, "john@example.com"))
        errors = self.dao.isValidToInclude(person)
        self.assertEqual(errors, [])

    def test_invalid_name(self):
        person = Person(1, "John123", 30)
        person.add_email(Email(1, "john@example.com"))
        errors = self.dao.isValidToInclude(person)
        self.assertIn("O nome deve ter pelo menos 2 partes e ser composto apenas de letras.", errors)

    def test_invalid_age(self):
        person = Person(1, "John Doe", 300)
        person.add_email(Email(1, "john@example.com"))
        errors = self.dao.isValidToInclude(person)
        self.assertIn("A idade deve estar no intervalo de 1 a 200.", errors)

    def test_no_email(self):
        person = Person(1, "John Doe", 30)
        errors = self.dao.isValidToInclude(person)
        self.assertIn("A pessoa deve ter pelo menos um email associado.", errors)

    def test_invalid_email_format(self):
        person = Person(1, "John Doe", 30)
        person.add_email(Email(1, "john.example.com"))
        errors = self.dao.isValidToInclude(person)
        self.assertIn("O email john.example.com não está no formato correto.", errors)

if __name__ == '__main__':
    unittest.main()