__author__ = "FXHibon"

from math import exp


class Neurone:
    # Construit le neurone
    # weight: liste des poids
    # threshold: seuil
    # pas: utilisé dans le calcul des nouveaux poids
    #
    def __init__(self, weight, threshold, pas):
        self.input = []
        self.weight = weight
        self.state = False
        self.threshold = threshold
        self.pas = pas

    # Sum pondéré des (input, poids)
    def sum(self):
        res = 0
        i = 0
        for val in self.input:
            res += self.weight[i] * val
            i += 1

        return res

    # Fonciton d'activation: sigmoide
    def activation(self, x):
        return 1 / (1 + exp(-x))

    # calcule l'état du neurone, activé ou non
    def evaluate(self):
        if self.activation(self.sum()) >= self.threshold:
            self.state = True
        else:
            self.state = False

    # prend les valeurs d'entrée 'input', les valeurs attendues 'output' et entraîne le neurone
    # (recalcul des poids à chaque itération)
    def train(self, input, output):
        self.input = input
        self.evaluate()
        i = 0
        for val in self.weight:
            if self.state:
                output -= 1
            self.weight[i] += output * self.pas * self.input[i]
            i += 1


if __name__ == "__main__":
    n = Neurone([2, 2], 0.8, 1)

    # entraine le neurone pour la fonction OR
    for i in range(100):
        n.train([1, 1], 1)
        n.train([1, 0], 1)
        n.train([0, 1], 1)
        n.train([0, 0], 0)

    n.input = [0, 1]
    n.evaluate()
    print(n.state)