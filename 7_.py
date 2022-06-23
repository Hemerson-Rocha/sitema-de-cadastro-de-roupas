# sistema de cadastro (para as roupas, etc)
# salvar em arquivos texto

# tipo de peça(M/F) > categorias (blusa, calça, saia) > nome da peça > tamanho > preço
# infatil
# Acessorios(Bone, chapeu, lenço, carteira, bolsas, cinto)



# cada um vai ter o seu .txt

import re
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
        with open("roupa_masculina.txt", "a") as roup_masc:
            for infor in lista_infor:
                roup_masc.write(str(infor) + ":")
            roup_masc.write("\n")



class Roupa_Feminina(Roupa):
    def __init__(self, nome, preco, categoria, tamanho):
        super().__init__(nome, preco, categoria, tamanho)
        self.manda_para_o_arquivo()
    
    def manda_para_o_arquivo(self):
        lista_infor = [self.nome, self.preco, self.categoria, self.tamanho]
        with open("roupa_feminina.txt", "a") as roup_femi:
            for infor in lista_infor:
                roup_femi.write(str(infor) + ":")
            roup_femi.write("\n")



class Roupa_Infantil(Roupa):
    def __init__(self, nome, preco, categoria, tamanho):
        super().__init__(nome, preco, categoria, tamanho)
        self.manda_para_o_arquivo()

    def manda_para_o_arquivo(self):
        lista_infor = [self.nome, self.preco, self.categoria, self.tamanho]
        with open("roupa_infantil.txt", "a") as roup_infan:
            for infor in lista_infor:
                roup_infan.write(str(infor) + ":")
            roup_infan.write("\n")



class Acessorios(Roupa):
    def __init__(self, nome, preco, categoria, tamanho = None):
        super().__init__(nome, preco, categoria, tamanho)
        self.verifica_tamanho_ou_categoria()
        self.manda_para_o_arquivo()

    # @property
    # def categoria(self):
    #     return self._categoria.lower()

    def verifica_tamanho_ou_categoria(self):
        lista_categorias = ["bone", "chapeu", "lenço", "carteira", "bolsa", "cinto"]
        if not self.categoria in lista_categorias:
            raise ValueError("Categoria inválida")
    
    def manda_para_o_arquivo(self):
        lista_infor = [self.nome, self.preco, self.categoria]
        with open("acessorios.txt", "a") as acess:
            for infor in lista_infor:
                acess.write(str(infor) + ":")
            acess.write("\n")



nome = ""
preco = 0
categoria = ""
tamanho = ""
def registro_de_roupas():
    global nome, preco, categoria, tamanho
    nome = input("Digite o nome da peça: ")
    try:
        preco = float(input("Digite o preco da peça: "))
    except:
        raise ValueError("Preço inválido")
        
    categoria = input("Digite a categoria da peça: ")
    tamanho = input("Digite o tamanho da peça: ")

def registro_de_acessorios():
    global nome, preco, categoria
    nome = input("Digite o nome da peça: ")
    preco = float(input("Digite o preco da peça: "))
    categoria = input("Digite a categoria da peça: ")


while True:
    try:
        # os.system("cls")
        escolha = int(input("[1] - Registrar\n[2] - Excluir registro\n"))
    except:
        os.system("cls")
        print("[on red]Digite uma opção válida[/]")
        continue
    if escolha == 1:
        while True:

            try:
                # os.system("cls")
                print("Escolha a categoria")
                registrar = int(input("[1] - Roupa Masculina\n[2] - Roupa Feminina\n[3] - Roupa Infantil\n[4] - Acessorios\n[5] - Voltar\n"))
            except:
                os.system("cls")
                pass
            
            if registrar == 1:
                registro_de_roupas()
                nova_roup_masc = Roupa_Masculina(nome, preco, categoria, tamanho)
                # lista_infor = [nova_roup_masc.nome, nova_roup_masc.preco, nova_roup_masc.categoria, nova_roup_masc.tamanho]
                # print(lista_infor)
                # with open("roupa_masculina.txt", "a") as roup_masc:
                #     for infor in lista_infor:
                #         roup_masc.write(str(infor) + ":")
                #     roup_masc.write("\n")
            
            elif registrar == 2:
                registro_de_roupas()
                nova_roup_femin = Roupa_Feminina(nome, preco, categoria, tamanho)
                # print(f"{nova_roup_femin.nome}\n{nova_roup_femin.preco}\n{nova_roup_femin.categoria}\n{nova_roup_femin.tamanho}")
            
            elif registrar == 3:
                registro_de_roupas()
                nova_roup_infa = Roupa_Infantil(nome, preco, categoria, tamanho)
                # print(f"{nova_roup_infa.nome}\n{nova_roup_infa.preco}\n{nova_roup_infa.categoria}\n{nova_roup_infa.tamanho}")

            elif registrar == 4:
                registro_de_acessorios()
                novo_acess = Acessorios(nome, preco, categoria)
                # print(f"{novo_acess.nome}\n{novo_acess.preco}\n{novo_acess.categoria}")

            elif registrar == 5:
                break
            
            else:
                os.system("cls")
                print("[on red]Digite uma opção válida[/]")
    elif escolha == 2:
        # excluir
        pass
    else:
        os.system("cls")
        print("[on red]Digite uma opção válida[/]")
        continue

roup_mac = Roupa_Masculina("blusa Azul", 22.49, "BLuSa", "m")
print(f"{roup_mac.nome}\n{roup_mac.preco}\n{roup_mac.categoria}\n{roup_mac.tamanho}")

roup_femi = Roupa_Feminina("vestido rosa", 72.49, "VESTIDO", "m")
print(f"{roup_femi.nome}\n{roup_femi.preco}\n{roup_femi.categoria}\n{roup_femi.tamanho}")

roup_infa = Roupa_Infantil("Macacao roxo", 422.49, "macacão", "pp")
print(f"{roup_infa.nome}\n{roup_infa.preco}\n{roup_infa.categoria}\n{roup_infa.tamanho}")

ace = Acessorios("pulseira", 12.09, "pulseira")
print(f"{ace.nome}\n{ace.preco}\n{ace.categoria}")