from threading import Thread
from time import sleep
from threading import Lock

# Exemplo 1
#
# class MeuThread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo
#
#         super().__init__()
#
#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)
#
#
# t1 = MeuThread('Thread 1', 2)
# t1.start()
#
# t2 = MeuThread('Thread 2', 3)
# t2.start()
#
# t3 = MeuThread('Thread 3', 5)
# t3.start()
#
# for i in range(10):
#     print(i)
#     sleep(1)


# Exemplo 2
#
# def vai_demorar(tempo, texto):
#     sleep(tempo)
#     print(texto)
#
# t1 = Thread(target=vai_demorar, args=(6, 'Olá'))
# t1.start()
#
# while t1.is_alive():
#     print('Esperando a thread...')
#     sleep(0.5)
#
# print('Thread acabou')

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). Ainda temos {self.estoque} em estoque')

        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(21)

    threads = []

    for i in range(1, 10):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    executando = True
    while executando:
        executando = False
        for t in threads:
            if t.is_alive():
                executando = True
                break

    print(ingressos.estoque)

