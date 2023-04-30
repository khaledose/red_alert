from actions.readers import getGeneralDefaults
from pathlib import Path
import configparser
import subprocess

class UtilRepo():
    def __init__(self, read_file, path='') -> None:
        self.read_file = read_file
        self.game_dir = Path(path)
        self.rules_path = Path(read_file)
        self.config = configparser.ConfigParser()
        self.config.optionxform = str
        self.config.read(self.rules_path.as_posix())

    def setGameDir(self, path):
        self.game_dir = Path(path)

    def launchGame(self):
        try:
            game_exe = self.game_dir.joinpath('gamemd.exe')
            subprocess.Popen(game_exe.as_posix())
        except:
            print('error')

    def saveConfig(self):
        try:
            save_path = self.game_dir.joinpath(self.read_file).as_posix()
            with open(self.read_file, 'w') as configfile:
                self.config.write(configfile)
        except:
            print('error')

class GeneralDefaults():
    def __init__(self) -> None:
        (self.costMultiplier, 
        self.oreGrowth, 
        self.oreGrowthPercent, 
        self.oreSpread, 
        self.oreSpreadPercent, 
        self.oreIncome, 
        self.buildSpeed) = getGeneralDefaults()