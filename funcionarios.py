class Funcionario:
    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

# A classe Junior não tem herança múltipla.
class Junior (Alura):
    pass

# A classe Pleno tem herança múltipla de Caelum e Alura.
class Pleno(Caelum, Alura): 
    # Se os métodos das superclasses forem iguais, 
    # prevalece o método da primeira superclasse.
    pass

jose = Junior()
jose.busca_perguntas_sem_resposta() 

# O código abaixo vai falhar, porque esse método não é da classe Alura.
# jose.busca_cursos_do_mes() 

jose.mostrar_tarefas()
# Mostra 'Fez muita coisa, Alurete!'

luan = Pleno()
luan.busca_perguntas_sem_resposta()

# O código abaixo vai funcionar, porque existe na classe Caelum.
luan.busca_cursos_do_mes()

luan.mostrar_tarefas() 
# Mostra 'Fez muita coisa, Caelumer'.