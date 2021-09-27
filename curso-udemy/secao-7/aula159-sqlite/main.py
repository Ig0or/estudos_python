import sqlite3

# criando a base de dados e cursor
conexao = sqlite3.connect('base.db')
cursor = conexao.cursor()

# criar tabela
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

# inserir dados na tabela criada
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)',
               ('Maria', 50))

cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
               {'nome': 'João', 'peso': 49})

cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
               {'id': None, 'nome': 'Felipe', 'peso': 89})

# alterar dados da tabela
cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',
               {'nome': 'Joana', 'id': 2})

# excluir dados da tabela
cursor.execute('DELETE FROM clientes WHERE id=:id',
               {'id': 3})

# executar comando
conexao.commit()

# exibir dados
cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    print(linha)

cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 50')
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()
