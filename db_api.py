import sqlite3

conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()
# --> posso colocar o row aqui para tranformar tudo em dicionario

def criar_tabela(cursor):
    cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')
    

def inserir_registro(nome, email):
    dados = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
    conexao.commit()
    print('Dados inseridos com sucesso!')


def atualizar_registro(nome, email, id):
    dados = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?", dados)
    conexao.commit()
    print('Dados atualizados com sucesso!')


def deletar_registro(id):
    dados = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?", dados)
    conexao.commit()
    print('Dados deletados com sucesso!')


def inserir_muitos(dados):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?,?)', dados)
    conexao.commit()
    print('Dados atualizados com sucesso!')
    

# dados = [
#         ('Diego', 'diego@outlook.com'),
#         ('Gustavo', 'gustavo@yahoo.com')
#     ]
# inserir_muitos(dados)

def recuperar_cliente(id):
    cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
    return cursor.fetchone()

# Outra forma de mostrar clientes em dicionário par chave e valor
def recuperar_cliente_row(id):
    cursor.row_factory = sqlite3.Row
    cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
    return cursor.fetchone()
    

def listar_clientes(cursor):
    return cursor.execute('SELECT * FROM clientes ORDER BY nome')


# Chamando as funçoes
cliente = recuperar_cliente(5)
print(cliente)

clientes = listar_clientes(cursor)
for client in clientes:
    print(client)

cliente = recuperar_cliente_row(3)
print(dict(cliente))