#### Comandos úteis em Python
#


#### Console
# dir()  -->  Mostra os comandos possíveis de uma variável
# help()  --> Ajuda

print('Hello World')
from faker import Faker
fake = Faker('pt-Br')
print(f'Novo email: {fake.email()}')