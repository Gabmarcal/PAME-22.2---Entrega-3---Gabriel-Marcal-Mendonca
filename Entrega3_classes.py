class Consultor:
    def __init__(self, id, usuario, senha, nome, area):
        self.id = id
        self.usuario = usuario
        self.senha = senha
        self.nome = nome
        self.area = area
        self.projetos = []

    def ver_dados(self):
        print(f'ID: {self.id}, Usuário: {self.usuario}, Nome: {self.nome}, area: {self.area}, senha: {self.senha}')

    def modificar_dados(self):
        
        resposta=input("Deseja mudar o usuário(sim/nao): ")
        if resposta == 'sim':
            novo_usuario=input("Novo usuário: ")
            self.usuario = novo_usuario

        resposta=input("Deseja mudar o nome(sim/nao): ")
        if resposta == 'sim':
            novo_nome=input("Novo nome: ")
            self.nome = novo_nome

        resposta=input("Deseja mudar a senha(sim/nao): ")
        if resposta == 'sim':
            nova_senha=input("Nova senha: ")
            self.senha = nova_senha

        resposta=input("Deseja mudar a area(sim/nao): ")
        if resposta == 'sim':
            nova_area=input("Nova area: ")
            self.area = nova_area

    def verificar_projetos(self):
        for projeto in self.projetos: print(projeto.nome)



class Gerente(Consultor):
    def __init__(self, id, usuario, senha, nome, area):
        super().__init__(id,usuario,senha,nome,area)

    def ver_dados(self):
        super().ver_dados()

    def modificar_dados(self):
        super().modificar_dados()

    def verificar_projetos(self):
        super().verificar_projetos()
    
    def avancar_e_entregar_projeto(self, projeto):
        
        if projeto.etapa < 4 and projeto.estado_do_projeto == 'Desenvolvimento':
            print(f'Projeto {projeto.nome} está na etapa {projeto.etapa} do Desenvolvimento.')
            resposta = input('Deseja avançar a etapa? (sim/nao)')
            
            if resposta == 'sim':
                projeto.etapa += 1
                projeto.permissao_avancar_ou_entregar = False
                print(f'Projeto {projeto.nome} avançou para {projeto.etapa} etapa do Desenvolvimento.')
            
            else: 
                projeto.permissao_avancar_ou_entregar = False
                print(f'Projeto {projeto.nome} permaneceu na {projeto.etapa} etapa do Desenvolvimento.')
        
        elif projeto.etapa == 4 and projeto.estado_do_projeto == 'Desenvolvimento':
            print(f'Projeto {projeto.nome} está na última etapa {projeto.etapa} do Desenvolvimento.')
            opcao = input('Deseja passar para a Concepção? (sim/nao)')
            
            if opcao == 'sim':
                projeto.etapa=1
                projeto.estado_do_projeto = 'Concepcao'
                print(f'Projeto {projeto.nome} passou para a Concepção.')
            
            else: 
                projeto.permissao_avancar_ou_entregar = False
                print(f'Projeto {projeto.nome} continua em Desenvolvimento.')

        elif projeto.etapa < 5 and projeto.estado_do_projeto == 'Concepcao' :
            print(f'Projeto {projeto.nome} está na etapa {projeto.etapa} da Concepção.')
            resposta = input('Deseja avançar a etapa? (sim/nao)')
            
            if resposta == 'sim':
                projeto.etapa += 1
                projeto.permissao_avancar_ou_entregar = False
                print(f'Projeto {projeto.nome} avançou para {projeto.etapa} etapa da Concepção.')
            
            else: 
                projeto.permissao_avancar_ou_entregar = False
                print(f'Projeto {projeto.nome} permaneceu na {projeto.etapa} etapa da Concepção.')

        elif projeto.etapa == 5 and projeto.estado_do_projeto == 'Concepcao':
            print(f'Projeto {projeto.nome} está na última etapa {projeto.etapa} da Concepção.')
            opcao = input('Deseja passar para a Identidade Visual? (sim/nao)')
            
            if opcao == 'sim':
                projeto.etapa=1
                projeto.estado_do_projeto = 'Identidade Visual'
                print(f'Projeto {projeto.nome} passou para a fase de Identidade Visual.')
            
            else: 
                projeto.permissao_avancar_ou_entregar = False
                print(f'Projeto {projeto.nome} continua na Concepção.')

        elif projeto.etapa < 6 and projeto.estado_do_projeto == 'Identidade Visual' :
            print(f'Projeto {projeto.nome} está na etapa {projeto.etapa} da Identidade Visual.')
            resposta = input('Deseja avançar a etapa? (sim/nao)')
            
            if resposta == 'sim':
                projeto.etapa += 1
                projeto.permissao_avancar_ou_entregar = False
                print(f'Projeto {projeto.nome} avançou para {projeto.etapa} etapa da Identidade Visual.')
            
            else: 
                projeto.permissao_avancar_ou_entregar = False
                print(f'Projeto {projeto.nome} permaneceu na {projeto.etapa} etapa da Identidade Visual.')

        elif projeto.etapa == 6 and projeto.estado_do_projeto == 'Identidade Visual':
            print(f'Projeto {projeto.nome} está na última etapa {projeto.etapa} da Identidade Visual.')
            opcao = input('Deseja entregar o projeto? (sim/nao)')
            
            if opcao == 'sim':
                sistema.remover_projeto(projeto)

                print(f'Projeto {projeto.nome} entregue.')
            
            else: 
                projeto.permissao_avancar_ou_entregar = False
                print(f'Projeto {projeto.nome} ainda não foi entregue.')
    
    def transferir_projeto(self, projeto, novo_gerente, sistema):
        
        if projeto in sistema.projetos:
            if projeto.gerente == self:
                if novo_gerente not in [p.gerente for p in sistema.projetos]:
                    
                    projeto.gerente = novo_gerente
                    print(f'Projeto {projeto.nome} foi transferido para o gerente {novo_gerente.nome}.')
                
                else:
                    print(f'O gerente {novo_gerente.nome} já está gerenciando outro projeto.')
            else:
                print(f'Você não é o gerente do projeto {projeto.nome}.')
        else:
            print(f'Projeto {projeto.nome} não encontrado.')



class Projeto:
    def __init__(self, nome, gerente, consultores, area):
        self.nome = nome
        self.gerente = gerente
        self.consultores = consultores
        self.area = area
        self.etapa = 1
        self.estado_do_projeto = 'Desenvolvimento'
        self.permissao_avancar_ou_entregar = False

    def adicionar_consultor(self, consultor):
        self.consultores.append(consultor)
        consultor.projetos.append(self)

    def remover_consultor(self, consultor):
        self.consultores.remove(consultor)
        consultor.projetos.remove(self)

    def ver_dados(self):
        return self.nome