const readmeContent = `
# Person and Email Validator

Este projeto implementa um sistema de validação para objetos `Person` e `Email`, garantindo que os dados atendam a certos critérios de integridade. O sistema valida nomes, idades e formatos de email.

## Estrutura do Projeto

```
/validador_pessoa_TDD
│
├── /model
│   ├── person.py         
│   └── email.py          
│
├── /dao
│   └── person_dao.py     
│
├── /tests
│   ├── test_person_dao_unittest.py  
│   └── test_person_dao_pytest.py    
│
└── requirements.txt       
```

## Pré-requisitos

Antes de executar o projeto, você deve ter o Python 3.x e o `pip` instalados no seu sistema. 

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/Desduh/validador_pessoa_TDD
   cd validador_pessoa_TDD
   ```

3. Instale as dependências:
   Este projeto utiliza apenas as bibliotecas padrão do Python, então não há necessidade de instalar pacotes externos.

## Execução de Testes

### Usando unittest

Para executar os testes com o framework `unittest`, utilize o seguinte comando:

```bash
python -m unittest discover -s tests
```

## Estrutura de Dados

### Classe `Person`

- `id` (int): Identificador único da pessoa.
- `name` (str): Nome da pessoa, deve ter pelo menos duas partes e ser composto apenas por letras.
- `age` (int): Idade da pessoa, deve estar no intervalo [1, 200].
- `emails` (list): Lista de objetos `Email` associados à pessoa.

### Classe `Email`

- \`id\` (int): Identificador único do email.
- \`address\` (str): Endereço de email, deve estar no formato "_____@____._____".
