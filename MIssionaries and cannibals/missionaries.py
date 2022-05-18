class State:

    def __init__(
        self,
        missionaries_left,
        missionaries_right,
        cannibals_left,
        cannibals_right,
        river_side,
    ):

        self.missionaries_left = missionaries_left
        self.missionaries_right = missionaries_right
        self.cannibals_left = cannibals_left
        self.cannibals_right = cannibals_right
        self.river_side = river_side
        self.parent = None
        self.children = []

    def __str__(self):

        return 'missionaries: {}\t| missionaries: {}\ncannibals:: {}\t| cannibals: {}'.format(self.missionaries_left,
                                                                                              self.missionaries_right, self.cannibals_left,
                                                                                              self.cannibals_right)

    def isValidState(self):

        if self.missionaries_left < 0 or self.missionaries_right < 0 \
                or self.cannibals_left < 0 or self.cannibals_right < 0:
            return False

        return (self.missionaries_left == 0 or self.missionaries_left
                >= self.cannibals_left) and (self.missionaries_right
                                             == 0 or self.missionaries_right >= self.cannibals_right)

    def isFinalState(self):

        resultado_esq = self.missionaries_left == self.cannibals_left \
            == 0
        resultado_dir = self.missionaries_right == self.cannibals_right \
            == 3
        return resultado_esq and resultado_dir

    def generateChildren(self):

        novo_lado_rio = ('right' if self.river_side == 'left'
                         else 'left')

        moves = [{'missionaries': 2, 'cannibals': 0},
                 {'missionaries': 1, 'cannibals': 0},
                 {'missionaries': 1, 'cannibals': 1},
                 {'missionaries': 0, 'cannibals': 1},
                 {'missionaries': 0, 'cannibals': 2}]

        for move in moves:
            if self.river_side == 'left':

                missionaries_left = self.missionaries_left \
                    - move['missionaries']
                missionaries_right = self.missionaries_right \
                    + move['missionaries']
                cannibals_left = self.cannibals_left - move['cannibals']
                cannibals_right = self.cannibals_right \
                    + move['cannibals']
            else:

                missionaries_right = self.missionaries_right \
                    - move['missionaries']
                missionaries_left = self.missionaries_left \
                    + move['missionaries']
                cannibals_right = self.cannibals_right \
                    - move['cannibals']
                cannibals_left = self.cannibals_left + move['cannibals']

            child = State(missionaries_left, missionaries_right,
                          cannibals_left, cannibals_right,
                          novo_lado_rio)
            child.parent = self
            if child.isValidState():
                self.children.append(child)


class Solve:

    def __init__(self, state):

        self.queue = [state]
        self.solution = None

    def generateSolution(self):

        for element in self.queue:
            if element.isFinalState():

                self.solution = [element]
                while element.parent:
                    self.solution.insert(0, element.parent)
                    element = element.parent
                break

            element.generateChildren()
            self.queue.extend(element.children)


def main():

    run = Solve(State(3, 0, 3, 0, 'left'))
    run.generateSolution()

    for validState in run.solution:
        print(validState)
        print('************************************')


if __name__ == '__main__':
    main()
