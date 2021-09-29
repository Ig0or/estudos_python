from sqlalchemy import create_engine


class ItemNaoExisteException(Exception):
    pass


engine = create_engine("sqlite:///rpg.db")


def consultar_item(id_i):
    with engine.connect() as con:
        consulta = """ SELECT * FROM item WHERE id = :id_item"""
        bd = con.execute(consulta, id_item=id_i)
        item = bd.fetchone()
        if item:
            return item
        else:
            raise ItemNaoExisteException()

