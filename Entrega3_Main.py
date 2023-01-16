from Entrega3_classes import *

class Sistema:
    def __init__(self):
        self.consultores = []
        self.gerentes = []
        self.projetos = []
        self.pendencias = []

    def menu(self):
        while True:
            print("\n")
            print("1 - Criar consultor")
            print("2 - Remover consultor")
            print("3 - Criar gerente")
            print("4 - Remover gerente")
            print("5 - Criar projeto")
            print("6 - Remover projeto")
            print("7 - Listar Gerentes/Consultores/Projetos")
            print("8 - Logar como consultor")
            print("9 - Logar como gerente")
            print("0 - Sair")
            opcao = input("Digite a opção desejada: ")
            print("\n")
        
            if opcao == "1":

                id = input("Digite o ID: ")
                usuario = input("Digite o usuário: ")
                senha = input("Digite a senha: ")
                nome = input("Digite o nome: ")
                area = input("Digite a area: ")

                self.criar_consultor(id, usuario, senha, nome, area)
                print(f'Consultor {nome} criado com sucesso.')

            elif opcao == "2":

                id = input("Digite o ID do consultor a ser removido: ")
                consultor = self.buscar_consultor(id)
                
                if consultor:
                    
                    self.remover_consultor(consultor)
                    
                    print(f'Consultor {consultor.nome} foi removido com sucesso.')

                else: print('Consultor não encontrado.')
    
            elif opcao == "3":

                id = input("Digite o ID: ")
                usuario = input("Digite o usuário: ")
                senha = input("Digite a senha: ")
                nome = input("Digite o nome: ")
                area = input("Digite a area: ")

                self.criar_gerente(id, usuario, senha, nome, area)
                print(f'Gerente {nome} criado com sucesso.')

            elif opcao == "4":

                id = input("Digite o ID do gerente a ser removido: ")
                gerente = self.buscar_gerente(id)
                
                if gerente:
                    self.remover_gerente(gerente)
                    print(f'Gerente {gerente.nome} foi removido com sucesso.')
                
                else:
                    print("Gerente não encontrado.")

            elif opcao == "5":

                nome = input("Digite o nome do projeto: ")
                area = input("Digite a área que aloca o projeto: ")
                id_gerente = input("Digite o ID do gerente responsável pelo projeto: ")
                gerente = self.buscar_gerente(id_gerente)

                if gerente:

                    ids_consultores = input("Digite os IDs dos consultores alocados no projeto separados por vírgula: ")
                    ids_consultores = ids_consultores.split(',')
                    consultores = [self.buscar_consultor(id) for id in ids_consultores]
                    
                    self.criar_projeto(nome, gerente, consultores,area)
                    print(f'Projeto {nome} criado com sucesso.')

                else: print("Gerente não encontrado.")

            elif opcao == "6":

                nome = input("Digite o nome do projeto a ser removido: ")
                projeto = self.buscar_projeto(nome)
                
                if projeto:
                    self.remover_projeto(projeto)
                    print(f'Projeto {projeto.nome} foi removido com sucesso.')
                
                else: print("Projeto não encontrado.")

            elif opcao == "7":
                self.listar()

            elif opcao == "8":
                id = input("Digite seu id: ")
                senha = input("Digite sua senha: ") 
                self.login_consultor(id,senha)

            elif opcao == "9":
                id = input("Digite seu id: ")
                senha = input("Digite sua senha: ") 
                self.login_gerente(id,senha)

            elif opcao == "0": break

            else: print("Opção inválida.")

    def login_consultor(self, id, senha):
        
        for consultor in self.consultores:

            if consultor.id == id and consultor.senha == senha:
                
                print(f"Bem vindo {consultor.nome} \n")

                while True:
                    print("\n")
                    print("1 - Ver meus dados")
                    print("2 - Modificar meus dados")
                    print("3 - Verificar Projetos onde estou alocado")
                    print("4 - Avançar com um projeto")
                    print("5 - Pedir retirada de um projeto")
                    print("6 - Sair")
                    opcao = input("Digite a opção desejada: ")
                    print("\n")

                    if opcao == "1":
                        consultor.ver_dados()

                    elif opcao == "2": 
                        consultor.modificar_dados() 

                    elif opcao == "3": 
                        consultor.verificar_projetos()

                    elif opcao == "4":
                        
                        resposta = input("Qual projeto gostaria de pedir aval para avançar: ")
                        projeto = self.buscar_projeto(resposta)
                        if projeto:

                            if consultor in projeto.consultores:
                                projeto.permissao_avancar_ou_entregar = True
                                print(f"Pedido feito, esperando permissão do gerente {projeto.gerente.nome} para avançar projeto")

                            else: print("Você não é consultor desse projeto")

                        else: print("Projeto não encontrado")

                    elif opcao == "5":
                        
                        resposta = input("Qual projeto gostaria de pedir aval para sair: ")
                        projeto = self.buscar_projeto(resposta)
                        if projeto:

                            if consultor in projeto.consultores:
                                self.pendencias.append([consultor,projeto])
                                print(f"Pedido feito, esperando permissão do gerente {projeto.gerente.nome} para sair do projeto {projeto.nome}")

                            else: print("Você não é consultor desse projeto")

                        else: print("Projeto não encontrado")

                    elif opcao == "6": break

                    else: print("Opção inválida")
    
    def login_gerente(self,id,senha):

        for gerente in self.gerentes:

            if gerente.id == id and gerente.senha == senha:
                
                print(f"Bem vindo {gerente.nome} \n")

                while True:
                    print("\n")
                    print("1 - Ver meus dados")
                    print("2 - Modificar meus dados")
                    print("3 - Verificar Projetos onde estou alocado")
                    print("4 - Avanço de projeto e entrega")
                    print("5 - Processos de retirada de projetos")
                    print("6 - Passar projeto para outro gerente")
                    print("7 - Sair")
                    opcao = input("Digite a opção desejada: ")
                    print("\n")

                    if opcao == "1": 
                        gerente.ver_dados()

                    elif opcao == "2": 
                        gerente.modificar_dados() 

                    elif opcao == "3": 
                        gerente.verificar_projetos()

                    elif opcao == "4":
                        print("Projetos disponíveis para aval:")
                        for projeto in self.projetos:
                            if id == projeto.gerente.id and projeto.permissao_avancar_ou_entregar == True:
                                print(projeto.nome)

                        resposta = input("Qual projeto gostaria de avançar: ")                          
                        projeto_para_aval = self.buscar_projeto(resposta)
                        
                        if projeto_para_aval:
                            gerente.avancar_e_entregar_projeto(projeto_para_aval)
                        
                        else: print("Projeto não encontrado na lista")
                    
                    elif opcao == "5":
                        print("Requisições de saída:")
                        for pedido in self.pendencias:
                            print([pedido[0].nome,pedido[1].nome])

                        resposta = input("Permitir qual saída(gerente,projeto): ")                          
                        aval = resposta.split(',')
                        
                        for pedido in self.pendencias:
                            if pedido[0].nome == aval[0] and pedido[1].nome == aval[1]:

                                if pedido[1].consultores != [pedido[0]]:
                                    pedido[0].projetos.remove(pedido[1])
                                    print("Aval concedido com sucesso")

                                else: print("Não foi possível devido a só existir esse consultor no projeto")

                    elif opcao == "6":
                        for projeto in self.projetos:
                            if projeto.gerente == gerente:
                                resposta = input(f"Deseja passar o projeto {projeto.nome} para outro gerente(sim/nao)")
                                projeto_a_passar = projeto

                                if resposta == 'sim':
                                    novo_gerente=input("Digite o ID do novo gerente: ")
                                    
                                    for n in self.gerentes:
                                        if n.id == novo_gerente: gerente.transferir_projeto(projeto_a_passar,n,sistema)


                    elif opcao == "7": break

                    else: print("Opção inválida")

    def criar_projeto(self, nome, gerente, consultores, area):
        
        projeto = Projeto(nome, gerente, consultores, area)
        gerente.projetos.append(projeto)
        
        for consultor in consultores:
            consultor.projetos.append(projeto)
        
        self.projetos.append(projeto)
        
    def remover_projeto(self, projeto):
        gerente = projeto.gerente
        consultores = projeto.consultores
        
        gerente.projetos.remove(projeto)
        for consultor in consultores:
            consultor.projetos.remove(projeto)
        
        self.projetos.remove(projeto)
    
    def criar_consultor(self, id, usuario, senha, nome, area):

        consultor = Consultor(id, usuario, senha, nome, area)
        self.consultores.append(consultor)
    
    def remover_consultor(self, consultor):
        projetos = consultor.projetos

        for projeto in projetos:
            
            if projeto.consultores == [consultor]:
                print(f"Não foi possível remover consultor, apenas ele está alocado no projeto {projeto.nome}")
                break

            else: projeto.remover_consultor(consultor)

        if consultor.projetos == []: self.consultores.remove(consultor)
    
    def criar_gerente(self, id, usuario, senha, nome, area):

        gerente = Gerente(id, usuario, senha, nome, area)
        self.gerentes.append(gerente)
        
    def remover_gerente(self, gerente):
        
        if gerente.projetos == []:
            self.gerentes.remove(gerente)

        else: print("Esse gerente possui projetos em andamento, não é possível removê-lo")

    def buscar_consultor(self, id):
        for consultor in self.consultores:
            if consultor.id == id:
                return consultor

    def buscar_gerente(self,id):
        for gerente in self.gerentes:
            if gerente.id == id:
                return gerente
    
    def buscar_projeto(self,nome):
        for projeto in self.projetos:
            if projeto.nome == nome:
                return projeto
     
    def listar(self):

        resposta=input("Deseja listar Projetos(sim/nao): ")
        if resposta == 'sim':
            print("\n")
            for projeto in self.projetos:
                print(projeto.nome)
            print("\n")
        
        resposta=input("Deseja listar Consultores(sim/nao): ")
        if resposta == 'sim':
            print("\n")
            for consultor in self.consultores:
                print(consultor.nome)
            print("\n")
        
        resposta=input("Deseja listar Gerentes(sim/nao): ")
        if resposta == 'sim':
            print("\n")
            for gerente in self.gerentes:
                print(gerente.nome)
            print("\n")

sistema=Sistema()
sistema.menu()