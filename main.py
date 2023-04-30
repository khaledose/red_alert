from kink import di
from src.gui.app import App
from src.actions.trainer import GameModifier
from src.actions.util import UtilRepo

if __name__ == '__main__':
    di['config'] = UtilRepo('./mod/rulesmo.ini') # rulesmd.ini - rulesmo.ini
    try:
        di['trainer'] = GameModifier('gamemd.exe', './db/addresses.json')
    except:
        print('error')
    app = App()
    app.mainloop()