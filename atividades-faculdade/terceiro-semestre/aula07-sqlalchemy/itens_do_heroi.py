from sqlalchemy import create_engine
from herois import consultar_heroi, consultar_heroi_por_nome


class ItemNaoExisteException(Exception):
    pass


engine = create_engine("sqlite:///rpg.db")


def heroi_tem_item(id_h):
    heroi = consultar_heroi(id_h)
    with engine.connect() as con:
        # consulta =
        bd = con.execute("""SELECT * FROM ItemDoHeroi""")
        for item in bd.fetchall():
            if item['idHeroi'] == id_h:
                return True
        return False


def heroi_quantos_itens(id_h):
    heroi = consultar_heroi(id_h)
    with engine.connect() as con:
        # consulta =
        bd = con.execute("""SELECT * FROM ItemDoHeroi""")
        qtd_itens = 0
        for item in bd.fetchall():
            if item['idHeroi'] == id_h:
                qtd_itens += 1
        return qtd_itens


def itens_do_heroi(id_h):
    heroi = consultar_heroi(id_h)
    with engine.connect() as con:
        bd = con.execute("""SELECT * FROM ItemDoHeroi 
        JOIN item ON ItemDoHeroi.idItem = item.id""")
        lista_itens = []
        for item in bd.fetchall():
            if item["idHeroi"] == id_h:
                lista_itens.append(dict(item))
        return lista_itens


def itens_em_uso_por_nome_do_heroi(nome):
    heroi = consultar_heroi_por_nome(nome)
    with engine.connect() as con:
        bd = con.execute("""
        SELECT *, heroi.nome AS nomeHeroi FROM ItemDoHeroi
        JOIN heroi ON ItemDoHeroi.idHeroi = heroi.id
        JOIN item ON ItemDoHeroi.idItem = item.id 
        """)
        lista_itens = []
        for item in bd.fetchall():
            if item['nomeHeroi'] == nome and item["emUso"] == 1:
                lista_itens.append(dict(item))
        return lista_itens
