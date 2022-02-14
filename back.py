import sqlite3

db = sqlite3.connect('bling_simulator_database.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS dados_cadastrais(id INTEGER PRIMARY KEY, nome TEXT NOT NULL, tipo_de_pessoa TEXT NOT NULL, cep INTEGER NOT NULL, cidade TEXT NOT NULL, uf TEXT NOT NULL, endereco TEXT NOT NULL, numero INTEGER NOT NULL, bairro TEXT NOT NULL)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY, descricao TEXT NOT NULL, codigo TEXT, tipo TEXT, preco REAL NOT NULL, estoque INTEGER, check1 BLOB, check2 BLOB, check3 BLOB, minimo INTEGER, maximo INTEGER, origem TEXT, ncm REAL, imagem TEXT)''')
db.commit()

class Tabela:
    def __init__(self, nome_da_tabela):
        self.__nome_da_tabela = nome_da_tabela

    @property
    def get_table(self):
        cursor.execute(f'SELECT * FROM {self.__nome_da_tabela}')
        return [list(i) for i in cursor.fetchall()]

class Produto:
    # Conferir o que acontece quando se instancia uma classe sem todos os atributos necessários
    # def __init__(self, informacoes_do_produto=None):
    #     self.__descricao, self.__codigo, self.__tipo, self.__preco, self.__estoque, self.__check1, self.__check2, self.__check3, self.__minimo, self.__maximo, self.__origem, self.__ncm, self.__imagem = informacoes_do_produto

    def cadastrar_produto(self, informacoes_do_produto):
        cursor.execute('INSERT INTO produtos VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (informacoes_do_produto))
        db.commit()
        # except:
        #     raise('Houve um erro no cadastro do produto.')
        # else:
        #     db.commit()

    @property
    def get_produto(self, descricao):
        cursor.execute(f'SELECT * FROM produtos WHERE descricao = {descricao}')
        print(cursor.fetchall())

dados_cadastrais = Tabela('dados_cadastrais')
tabela_produtos = Tabela('produtos')