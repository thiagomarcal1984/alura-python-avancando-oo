class Pessoa:
    tamanho_cpf = 11

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def valida_cpf(self):
        return True if len(self.cpf) == __class__.tamanho_cpf else False

pe = Pessoa('00000000001', 'Ruby')
print(pe.valida_cpf())

pe = Pessoa('0000000000', 'Cristal')
print(pe.valida_cpf())

# Redefinição da classe Pessoa:
class Pessoa:
    tamanho_cpf = 11

p = Pessoa()

print(f'Tamanho CPF na instância: {p.tamanho_cpf}')
print(f'Mudando o tamanho do CPF no objeto para 12...')

p.tamanho_cpf = 12

print(f'Tamanho CPF na instância: {p.tamanho_cpf}')

print(f'Tamanho CPF na classe: {Pessoa.tamanho_cpf}')
print(f'Tamanho CPF na classe: {p.__class__.tamanho_cpf}')
