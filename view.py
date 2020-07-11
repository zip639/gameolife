import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class View(Gtk.Window):
    def __init__(self, model):
        Gtk.Window.__init__(self, title="Life game")
        self.connect("destroy", Gtk.main_quit)
        model.attach(self)
        self._drawArea = Gtk.DrawingArea()
        self._drawArea.set_size_request(len(model.lifeoids)*10, len(model.lifeoids[0])*10)
        self._drawArea.connect('draw', self.on_draw)
        self._lifeoids = model.lifeoids
        self._drawArea.queue_draw()

        self.add(self._drawArea)
        self.show_all()
        Gtk.main()

    def on_draw(self, da, ctx):
        nbColumns = len(self._lifeoids[0])
        for line in range(len(self._lifeoids)):
            for column in range(nbColumns):
                lifeoid = self._lifeoids[line][column]
                if lifeoid:
                    ctx.set_source_rgb(0,0,0)
                    ctx.rectangle(line*10,column*10, 10, 10)
                    ctx.fill()
                else:
                    ctx.set_source_rgb(0.1,0.1,0.1)
                    ctx.rectangle(line*10,column*10, 10, 10)
                    ctx.fill()

    def refresh(self, lifeoids):
        self._lifeoids = lifeoids
        self._drawArea.queue_draw()
