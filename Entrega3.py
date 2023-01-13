#Listas globais
lista_projetos=[]
lista_conslutores=[]
lista_gerentes=[]

class Consultor:

    def __init__(self,ID,usuario,senha) -> None:

        self.ID = ID
        self.usuario = usuario
        self.senha = __senha
        
class Gerente:

    def __init__(self,ID,usuario,senha) -> None:

        self.ID = ID
        self.usuario = usuario
        self.senha = __senha

class Projeto:

    def __init__(self,nome,area,cliente) -> None:

        self.nome = nome
        self.area = area
        self.cliente = cliente

    def set_nome(self,nome):
        self.nome = nome

    def set_area(self,area):
        self.area = area
    
    def set_cliente(self,cliente):
        self.cliente = cliente

class Sistema:

    def __init__(self,projetos,consultores,gerentes) -> None:
        
        self.projetos = projetos
        self.consultores = consultores
        self.gerentes = gerentes

    def ver_gerentes():
        return lista_gerentes

def Main():

    while True:
        print('1-Logar no sistema \n 2-Entrar sem logar \n 3-Sair')
        opcao = int(input('Digite a opção:'))

        if opcao == 1:
            pass
        if opcao == 2:
            Sem_logar()
        if opcao == 3:
            break

def Sem_logar():

    while True:

        print('1-Logar no sistema \n\
                2-Criar Projeto \n \
                3-Remover Projeto \n \
                4-Criar consultor \n \
                5-Remover consultor \n \
                6-Criar gerente\n \
                7-Remover gerente \n \
                8-Listagem \n \
                9-Sair')

        opcao = int(input('Digite a opção:'))

        if opcao == 1:
            pass
        if opcao == 2:
            criar_projetos()
        if opcao == 3:
            remover_projeto()
        if opcao == 4:
            pass
        if opcao == 5:
            pass
        if opcao == 6:
            pass
        if opcao == 7:
            pass
        if opcao == 8:
            pass
        if opcao == 9:
            break

def Logado_consultor():

    while True:
        print('1-Ver dados\n\
                2-Modificar dados \n \
                3-Verificar projetos alocados\n \
                4-Avançar projeto\n \
                5-Pedir retirada de um projeto \n \
                6-Sair')

        opcao = int(input('Digite a opção:'))

def Logado_gerente():
    
    while True:
        print('1-Ver dados\n\
                2-Modificar dados \n \
                3-Verificar projetos alocados\n \
                4-Avançar projeto\n \
                5-Dar aval sobre retirada de consultor \n \
                6-Repassar projeto\n \
                7-Entregar projeto \n \
                8-Sair')

        opcao = int(input('Digite a opção:'))

def remover_projeto():

        for proj in lista_projetos:
            print(proj.nome)
        
        nome_del = input('Qual projeto deseja deletar: ')

        for proj in lista_projetos:
            if proj.nome == nome_del: lista_projetos.remove(proj)

def criar_projetos():
        
        nome_proj=input('Nome do projeto: ')
        area_proj=input('Área do projeto: ')
        cliente_proj=input('Nome do cliente: ')

        projeto = Projeto(nome_proj,area_proj,cliente_proj)
        lista_projetos.append(projeto)

Main()