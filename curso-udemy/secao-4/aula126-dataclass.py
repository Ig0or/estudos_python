from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict


@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(f'Invalid type {type(self.nome).__name__} != str em {self}')

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('A', '5')
p2 = Pessoa('B', '3')
p3 = Pessoa('C', '2')
p4 = Pessoa('D', '77')

pessoas = [p1, p2, p3, p4]

print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, reverse=True))
print(p1)
print(p1 == p2)

print(asdict(p1))