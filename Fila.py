


class Fila:

    def __init__(self):
        self.dados = []


    def insere(self, elem):
        self.dados.append(elem)

    def remove(self):
        if not self.vazia():
            return self.dados.pop(0)

        else:
            print("Fila vazia!")

    def tamanho(self):
        return len(self.dados)

    def vazia(self):
        return len(self.dados) == 0

    def primeiro(self):
        if not self.vazia():
            return self.dados[0]

        else:
            print("Fila vazia!")

    def print(self):
        while not self.vazia():
            print(self.primeiro())
            self.remove()