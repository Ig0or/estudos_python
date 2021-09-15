# ATIVIDADE CONTÍNUA 05

# NOMES DOS ALUNOS: (MÁXIMO 6):
# ALUNO 1: Beatrici Ramos Feliciano
# ALUNO 2: Igor Guilherme da Paz Provensi
# ALUNO 3: Igor Ruiz de França
# ALUNO 4: Robson Ferreira Puert
# ALUNO 5: Yasmim Barbosa Vieira


import sqlalchemy

from sqlalchemy import Column, Integer, String, Float, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE
engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()
Base = declarative_base(engine)
session = Session()


class Filme(Base):
    # FAZER O MAPEAMENTO DA TABELA
    __tablename__ = "FILME"
    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    titulo = Column("TITULO", String(255), nullable=False)
    ano = Column("ANO", Integer, nullable=False)
    genero = Column("GENERO", String(255), nullable=False)
    duracao = Column("DURACAO", Integer, nullable=False)
    pais = Column("PAIS", String(255), nullable=False)
    diretor = Column("DIRETOR", String(255), nullable=False)
    elenco = Column("ELENCO", String(255), nullable=False)
    avaliacao = Column("AVALIACAO", Float, nullable=False)
    votos = Column("VOTOS", Integer, nullable=False)

    # Método construtor
    def __init__(
        self, titulo, ano, genero, duracao, pais, diretor, elenco, avaliacao, votos
    ):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.duracao = duracao
        self.pais = pais
        self.diretor = diretor
        self.elenco = elenco
        self.avaliacao = avaliacao
        self.votos = votos


# Classe para interação com o Banco de Dados
class BancoDeDados:
    def criar_tabela(self):
        # Cria a tabela FILME no banco de dados
        connection.execute(
            """CREATE TABLE IF NOT EXISTS FILME(
                              ID INTEGER PRIMARY KEY,
                              TITULO VARCHAR(255) NOT NULL,
                              ANO INT NOT NULL,
                              GENERO VARCHAR(255) NOT NULL,
                              DURACAO INT NOT NULL,
                              PAIS VARCHAR(255) NOT NULL,
                              DIRETOR VARCHAR(255) NOT NULL,
                              ELENCO VARCHAR(255) NOT NULL,
                              AVALIACAO FLOAT NOT NULL,
                              VOTOS INT NOT NULL)"""
        )

    def incluir(self, filme):
        """
        Recebe um objeto Filme e armazena esse
        objeto no banco de dados.
        """
        session.add(filme)
        session.commit()

    def incluir_lista(self, filmes):
        """
        Recebe uma lista de objetos Filme e armazena esses
        objetos no banco de dados.
        """
        session.add_all(filmes)
        session.commit()

    def alterar_avaliacao(self, id, avaliacao):
        """
        Recebe o id de um filme e altera sua avaliação de
        acordo com o valor do parâmetro avaliacao.
        """
        filme = session.query(Filme).filter(Filme.id == id).first()
        filme.avaliacao = avaliacao
        session.commit()

    def excluir(self, id):
        """
        Recebe o id de um filme e exclui o filme correspondente
        do banco de dados.
        """
        filme = session.query(Filme).filter(Filme.id == id).delete()
        session.commit()

    def buscar_por_id(self, id):
        """
        Realiza busca no banco de dados e retorna um
        objeto Filme de acordo com o seu id.
        """
        filme = session.query(Filme).filter(Filme.id == id)
        return filme

    def buscar_todos(self):
        """
        Realiza busca no banco de dados e retorna uma
        lista com todos os filmes cadastrados,
        ordenados pelo título de forma crescente.
        """
        filmes = session.query(Filme).order_by(Filme.titulo).all()
        return filmes

    def buscar_por_ano(self, ano):
        """
        Realiza busca no banco de dados e retorna uma
        lista com todos os filmes de determinado ano,
        ordenado pelo ID de forma crescente.
        """
        filmes = session.query(Filme).filter(Filme.ano == ano).order_by(Filme.id).all()
        return filmes

    def buscar_por_genero(self, genero):
        """
        Realiza busca no banco de dados e retorna uma
        lista com todos os filmes que pertencem a um determinado genêro,
        ordenados pelo titulo de forma crescente.
        """
        filmes = (
            session.query(Filme)
            .filter(Filme.genero.like("%" + genero + "%"))
            .order_by(Filme.titulo)
            .all()
        )
        return filmes

    def buscar_por_pais(self, pais):
        """
        Realiza busca no banco de dados e retorna uma
        lista com todos os filmes que pertencem a um determinado país,
        ordenados pelo ano de lançamento em ordem crescente.
        """
        filmes = (
            session.query(Filme).filter(Filme.pais == pais).order_by(Filme.ano).all()
        )
        return filmes

    def buscar_melhores_do_ano(self, ano):
        """
        Realiza busca no banco de dados e retorna uma lista com todos
        os filmes de um determinado ano, com avaliação maior ou igual a 75,
        ordenados pela avaliação de forma decrescente.
        DICA - utilize a função:
            .order_by(desc(Filme.avaliacao))
        """
        filmes = (
            session.query(Filme).filter(Filme.ano == ano).filter(Filme.avaliacao >= 75).order_by(desc(Filme.avaliacao)).all())
        return filmes

    def importar_filmes(self, nome_arquivo):
        """
        Recebe como parâmetro o nome de um arquivo de texto e importa os
        dados contidos no arquivo para o banco de dados.
        Considere que o arquivo contém uma listagem de filmes no formato:
        titulo;ano;genero;duracao;país;diretor;elenco;avaliacao;votos
        """
        arquivo = open(nome_arquivo, "r", encoding="UTF-8")
        filmes = []
        for linha in arquivo:
            filme = linha.split(";")
            dados_filme = Filme(
                filme[0],
                filme[1],
                filme[2],
                filme[3],
                filme[4],
                filme[5],
                filme[6],
                filme[7],
                filme[8],
            )
            filmes.append(dados_filme)
        session.add_all(filmes)
        session.commit()


# EXEMPLO DE PROGRAMA PRINCIPAL
banco = BancoDeDados()
banco.criar_tabela()


# Importa filmes do arquivo de texto e salva no banco de dados
banco.importar_filmes("movies.txt")


# Cria um novo Filme e insere no banco de dados
filme1 = Filme(
    "Parasite",
    2019,
    "Comedy, Drama, Thriller",
    132,
    "Korea",
    "Bong Joon Ho",
    "Song Kang-ho, Jang Hye-jin, Choi Woo-shik",
    92,
    40273,
)
banco.incluir(filme1)


# Cria uma lista com dois novos filmes e insere no banco de dados
filme2 = Filme(
    "Joker",
    2019,
    "Crime, Drama, Thriller",
    122,
    "USA",
    "Todd Phillips",
    "Joaquin Phoenix, Robert De Niro, Zazie Beetz",
    91,
    78481,
)
filme3 = Filme(
    "Avengers: Endgame",
    2019,
    "Drama, Thriller",
    181,
    "USA",
    "Anthony Russo, Joe Russo",
    "Robert Downey Jr., Chris Evans, Mark Ruffalo",
    93,
    715250,
)
lista_filmes = [filme2, filme3]
banco.incluir_lista(lista_filmes)


# Altera a avalação do filme de id 7 para 98
banco.alterar_avaliacao(7, 98)


# Exclui o filme de id 6
banco.excluir(6)


# Busca todos os filmes
lista = banco.buscar_todos()
print("-" * 60)
for f in lista:  # exibe lista de filmes
    print(f.id,f.titulo,f.ano,f.genero,f.duracao,f.pais,f.diretor,f.elenco,f.avaliacao,f.votos)


# Busca todos os filmes do ano de 2019
lista = banco.buscar_por_ano(2019)
print("-" * 60)
for f in lista:  # exibe lista de filmes
    print(f.id, f.titulo, f.ano)


# Busca todos os filmes do gênero 'Crime'
lista = banco.buscar_por_genero("Crime")
print("-" * 60)
for f in lista:  # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero)


# Busca todos os filmes do país 'Brazil'
lista = banco.buscar_por_pais("Brazil")
print("-" * 60)
for f in lista:  # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.pais)


# Busca os melhores filmes do ano de 2019
lista = banco.buscar_melhores_do_ano("2019")
print("-" * 60)
for f in lista:  # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.avaliacao)




