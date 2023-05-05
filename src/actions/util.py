from pathlib import Path
import configparser
import subprocess

class UtilRepo():
    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.config.optionxform = str
        self.refConfig = configparser.ConfigParser()
        self.refConfig.optionxform = str

    def launchGame(self):
        try:
            game_exe = self.game_dir.joinpath('gamemd.exe')
            subprocess.Popen(game_exe.as_posix())
        except:
            print('error')

    def loadConfig(self, file):
        self.config.read(file)
        self.refConfig.read(file)

    def saveConfig(self, file):
        try:
            with open(file, 'w') as configfile:
                self.config.write(configfile)
        except:
            print('error')