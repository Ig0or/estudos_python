from sqlalchemy import create_engine

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
        consulta = """SELECT * FROM Heroi WHERE id = :id_heroi"""
        bd = con.execute(consulta, id_heroi=id_h)
        primeira_linha = bd.fetchone()

        if not primeira_linha:
            return False
        return True


def consultar_heroi(id_h):
    with engine.connect() as con:
        consulta = """SELECT * FROM heroi WHERE id = :id_heroi"""
        bd = con.execute(consulta, id_heroi=id_h)
        if heroi_existe(id_h):
            heroi = bd.fetchone()
            return dict(heroi)
        else:
            raise HeroiNaoExisteException()
