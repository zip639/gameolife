from subject import Subject


class Model(Subject):
    def __init__(self, lines, columns):
        super().__init__()
        self._lifeoids = [[False for i in range(columns)] for j in range(lines)]
        self._lifeoids[int(lines/2)][int(columns/2)] = True

    @property
    def lifeoids(self):
        return self._lifeoids

    @lifeoids.setter
    def lifeoids(self, value):
        self._lifeoids = value
        self._notify()

    def _notify(self):
        for observer in self._observers:
            observer.refresh(self._lifeoids)
