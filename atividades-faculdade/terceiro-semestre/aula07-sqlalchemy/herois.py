from sqlalchemy import create_engine
from sqlalchemy.sql import text

# Essa classe só representa uma exception com
# novo nome. Não mexa dentro dela.
# Escreva os imports (acima dela)
# E suas funcoes (depois dela)
class HeroiNaoExisteException(Exception):
    pass


# escreva suas funcoes aqui

engine = create_engine("sqlite:///rpg.db")


def heroi_existe(id_h):
    with engine.connect() as con:
        cod_sql = """SELECT * FROM Heroi WHERE id = :id_heroi"""
        rs = con.execute(cod_sql, id_heroi=id_h)
        primeira_linha = rs.fetchone()

        if not primeira_linha:
            return False
        return True
