__author__ = "FXHibon"

from math import exp


class Neurone:
    def __init__(self, weight, seuil, pas):
        self.input = []
        self.weight = weight
        self.state = False
        self.seuil = seuil
        self.pas = pas

    def sum(self):
        res = 0
        i = 0
        for val in self.input:
            res += self.weight[i] * val
            i += 1

        return res

    def activation(self, x):
        return 1 / (1 + exp(-x))

    def evaluate(self):
        if self.activation(self.sum()) >= self.seuil:
            self.state = True
        else:
            self.state = False

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
    for i in range(100):
        n.train([1, 1], 1)
        n.train([1, 0], 1)
        n.train([0, 1], 1)
        n.train([0, 0], 0)

    n.input = [0, 1]
    n.evaluate()
    print(n.state)