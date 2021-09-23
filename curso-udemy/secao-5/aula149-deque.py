from collections import deque

# LIFO
livros = list()

for i in range(10):
    livros.append(f'Livro {i+1}')

print(livros)

livro_removido = livros.pop()
print(livros)
print(livro_removido)

print('#'*30)

# FIFO
fila = deque()
fila.append('José')
fila.append('Maria')
fila.append('Marcos')
fila.append('Rosa')

nome_removido = fila.popleft()
print(fila)
print(nome_removido)
