from kink import di
from src.gui.app import App
from src.actions.trainer import GameModifier
from src.actions.util import UtilRepo

if __name__ == '__main__':
    di['config'] = UtilRepo() # rulesmd.ini - rulesmo.ini
    di['trainer'] = GameModifier('gamemd.exe', './db/addresses.json')

    app = App()
    app.mainloop()