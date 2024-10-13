class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)

    def get_emails(self):
        return self.emails
