from view import View
from model import Model
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib

class Controller:
    def __init__(self, lines, columns):
        self._model = Model(lines, columns)
        GLib.timeout_add(100, self.makeLifeHappen)
        self._view = View(self._model)

    def makeLifeHappen(self):
        oldLifeoids = self._model.lifeoids
        newLifeoids = [row[:] for row in oldLifeoids]

        lines = len(oldLifeoids)
        columns = len(oldLifeoids[0])

        for line in range(0, lines):
            if line == 0:
                previousLine = lines-1
                nextLine = line+1
            elif line == lines-1:
                previousLine = line-1
                nextLine = 0
            else:
                previousLine = line-1
                nextLine = line+1
            for column in range(0, columns):
                if column == 0:
                    previousColumn = columns -1
                    nextColumn = column+1
                elif column == columns-1:
                    previousColumn = column -1
                    nextColumn = 0
                else:
                    previousColumn = column -1
                    nextColumn = column+1
                if oldLifeoids[line][column]:
                    if not oldLifeoids[line][previousColumn] and not oldLifeoids[line][nextColumn] and not oldLifeoids[previousLine][column] and not oldLifeoids[nextLine][column]:
                        newLifeoids[line][previousColumn] = True
                        newLifeoids[line][nextColumn] = True
                        newLifeoids[previousLine][column] = True
                        newLifeoids[nextLine][column] = True
                    if oldLifeoids[line][previousColumn] and oldLifeoids[line][nextColumn] and oldLifeoids[previousLine][column] and oldLifeoids[nextLine][column]:
                        newLifeoids[line][column] = False

        self._model.lifeoids = newLifeoids
        return True
