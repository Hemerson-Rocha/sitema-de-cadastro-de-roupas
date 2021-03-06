import os
from rich import print

class Roupa:
    def __init__(self, nome, preco, categoria, tamanho):
        self._nome = nome
        self.preco = preco
        self._categoria = categoria
        self._tamanho = tamanho
        self.verifica_tamanho_ou_categoria()


    @property
    def nome(self):
        return self._nome.title()

    @property
    def categoria(self):
        return self._categoria.lower()

    @property
    def tamanho(self):
        return self._tamanho.upper()

    def verifica_tamanho_ou_categoria(self):
        lista_tamanhos = ["PP", "P", "M", "G", "GG"]
        if not self.tamanho in lista_tamanhos:
            raise ValueError("Tamanho inválido :/")
    


class Roupa_Masculina(Roupa):
    def __init__(self, nome, preco, categoria, tamanho):
        super().__init__(nome, preco, categoria, tamanho)
        self.manda_para_o_arquivo()


    def manda_para_o_arquivo(self):
        lista_infor = [self.nome, self.preco, self.categoria, self.tamanho]
        with open("roupa_masculina.txt", "a", encoding="utf-8") as roup_masc:
            for infor in lista_infor:
                roup_masc.write(str(infor) + ":")
            roup_masc.write("\n")



class Roupa_Feminina(Roupa):
    def __init__(self, nome, preco, categoria, tamanho):
        super().__init__(nome, preco, categoria, tamanho)
        self.manda_para_o_arquivo()


    def manda_para_o_arquivo(self):
        lista_infor = [self.nome, self.preco, self.categoria, self.tamanho]
        with open("roupa_feminina.txt", "a", encoding="utf-8") as roup_femi:
            for infor in lista_infor:
                roup_femi.write(str(infor) + ":")
            roup_femi.write("\n")



class Roupa_Infantil(Roupa):
    def __init__(self, nome, preco, categoria, tamanho):
        super().__init__(nome, preco, categoria, tamanho)
        self.manda_para_o_arquivo()


    def manda_para_o_arquivo(self):
        lista_infor = [self.nome, self.preco, self.categoria, self.tamanho]
        with open("roupa_infantil.txt", "a", encoding="utf-8") as roup_infan:
            for infor in lista_infor:
                roup_infan.write(str(infor) + ":")
            roup_infan.write("\n")



class Acessorios(Roupa):
    def __init__(self, nome, preco, categoria, tamanho = None):
        super().__init__(nome, preco, categoria, tamanho)
        self.verifica_tamanho_ou_categoria()
        self.manda_para_o_arquivo()


    def verifica_tamanho_ou_categoria(self):
        lista_categorias = ["bone", "chapeu", "lenço", "carteira", "bolsa", "cinto"]
        if not self.categoria in lista_categorias:
            raise ValueError("Categoria inválida")
    
    def manda_para_o_arquivo(self):
        lista_infor = [self.nome, self.preco, self.categoria]
        with open("acessorios.txt", "a", encoding="utf-8") as acess:
            for infor in lista_infor:
                acess.write(str(infor) + ":")
            acess.write("\n")



nome = ""
preco = 0
categoria = ""
tamanho = ""
def registro_de_roupas():
    while True:
        global nome, preco, categoria, tamanho
        nome = input("Digite o nome da peça: ")
        try:
            preco = float(input("Digite o preco da peça: "))
        except:
            print("[on red]Preço inválido[/]")
            continue
        categoria = input("Digite a categoria da peça: ")
        tamanho = input("Digite o tamanho da peça: ")

        print("*"*20 + "\nAs informações foram digitadas corretamente?")
        try:
            digit_corretamente = int(input("[1] - Sim\n[2] - Não\n"))
        except:
            print("[on red]Digite uma opção válida[/]")
            continue
        if digit_corretamente == 1:
            break
        elif digit_corretamente == 2:
            continue
        else:
            print("[on red]Digite uma opção válida[/]")
            continue

def registro_de_acessorios():
    while True:
        global nome, preco, categoria
        nome = input("Digite o nome da peça: ")
        preco = float(input("Digite o preco da peça: "))
        categoria = input("Digite a categoria da peça: ")

        print("*"*20 + "\nAs informações foram digitadas corretamente?")
        try:
            digit_corretamente = int(input("[1] - Sim\n[2] - Não\n"))
        except:
            print("[on red]Digite uma opção válida[/]")
            continue
        if digit_corretamente == 1:
            break
        elif digit_corretamente == 2:
            continue
        else:
            print("[on red]Digite uma opção válida[/]")
            continue

def excluir_item(arquivo):
    with open(arquivo,"r") as roup_teste:
        i = 0
        lista = []
        lista_com_id = []
        for infor in roup_teste:
            print(f"ID - {i} - {infor}")
            lista.append(infor)
            lista_com_id.append(str(i)+":"+str([infor]))
            i += 1

    try:
        id_excluir = int(input("Digite o ID do item que você quer excluir\n"))
    except:
        raise ValueError("Não digite letras")

    if len(lista_com_id) - 1 >= id_excluir:
        lista_com_id.pop(id_excluir)
        lista.pop(id_excluir)
    else:
        print("O ID não está no arquivo")

    with open(arquivo,"w") as roup_teste:
        for linha in lista:
            roup_teste.write(str(linha))


while True:
    try:
        os.system("cls")
        escolha = int(input("[1] - Registrar\n[2] - Excluir registro\n"))
    except:
        os.system("cls")
        print("[on red]Digite uma opção válida[/]")
        continue
    if escolha == 1:
        while True:

            try:
                print("\nEscolha a categoria")
                registrar = int(input("[1] - Roupa Masculina\n[2] - Roupa Feminina\n[3] - Roupa Infantil\n[4] - Acessorios\n[5] - Voltar\n"))
            except:
                os.system("cls")
                pass
            
            if registrar == 1:
                registro_de_roupas()
                nova_roup_masc = Roupa_Masculina(nome, preco, categoria, tamanho)
            
            elif registrar == 2:
                registro_de_roupas()
                nova_roup_femin = Roupa_Feminina(nome, preco, categoria, tamanho)
            
            elif registrar == 3:
                registro_de_roupas()
                nova_roup_infa = Roupa_Infantil(nome, preco, categoria, tamanho)

            elif registrar == 4:
                registro_de_acessorios()
                novo_acess = Acessorios(nome, preco, categoria)

            elif registrar == 5:
                break
            
            else:
                os.system("cls")
                print("[on red]Digite uma opção válida[/]")
    elif escolha == 2:
        while True:
            try:
                print("\nEscolha a categoria")
                categoria_excluir = int(input("[1] - Roupa Masculina\n[2] - Roupa Feminina\n[3] - Roupa Infantil\n[4] - Acessorios\n[5] - Voltar\n"))
            except:
                os.system("cls")
                pass
            if categoria_excluir == 1:
                excluir_item("roupa_masculina.txt")
            elif categoria_excluir == 2:
                excluir_item("roupa_feminina.txt")
            elif categoria_excluir == 3:
                excluir_item("roupa_infantil.txt")
            elif categoria_excluir == 4:
                excluir_item("acessorios.txt")
            elif categoria_excluir == 5:
                    break
            else:
                os.system("cls")
                print("[on red]Digite uma opção válida[/]")
                continue
            
            break
    else:
        os.system("cls")
        print("[on red]Digite uma opção válida[/]")
        continue
