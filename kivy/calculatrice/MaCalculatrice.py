
import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class GridLayoutCalc(GridLayout):
    def calculer(self, calcul):
        if calcul:
            try:
                self.display.text = str(eval(calcul))
            except Exception:
                self.display.text = "ERREUR"

class MaCalculatriceApp(App):
    def build(self):
        return GridLayoutCalc()

maCalc = MaCalculatriceApp()
maCalc.run()