import re
from model.person import Person

class PersonDAO:
    def save(self, person: Person):
        # Simulação de salvar a pessoa
        pass

    def isValidToInclude(self, person: Person):
        errors = []
        name_parts = person.name.split()
        if len(name_parts) < 2 or not all(part.isalpha() for part in name_parts):
            errors.append("O nome deve ter pelo menos 2 partes e ser composto apenas de letras.")

        if not (1 <= person.age <= 200):
            errors.append("A idade deve estar no intervalo de 1 a 200.")

        if len(person.get_emails()) == 0:
            errors.append("A pessoa deve ter pelo menos um email associado.")

        for email in person.get_emails():
            if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email.address):
                errors.append(f"O email {email.address} não está no formato correto.")

        return errors
