import configparser
import subprocess

def readConfig(path):
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(path)
    return config

def launchGame():
    # specify the path to the .exe file
    exe_path = r'D:/Games/Other/Red Alert 2/Game/_MOD/gamemd.exe'

    # launch the .exe file
    subprocess.Popen(exe_path)

def saveConfig(path):
    with open(path, 'w') as configfile:
        config.write(configfile)

def getAllCountries():
    idx = sections.index('Countries')
    countries = [x for _, x in config.items(sections[idx])]
    return countries

def getAllBaseUnits():
    idx = sections.index('General')
    return config.get(sections[idx], 'BaseUnit').split(',')

def getAllBases():
    idx = sections.index('AI')
    return config.get(sections[idx], 'BuildConst').split(',')

def getAllTiberiums():
    idx = sections.index('Tiberiums')
    tiberiums = [x for _, x in config.items(sections[idx])]
    return tiberiums

def getAllInfantries():
    idx = sections.index('InfantryTypes')
    infantries = [x for _, x in config.items(sections[idx])]
    return infantries

def getAllVehicles():
    idx = sections.index('VehicleTypes')
    vehicles = [x for _, x in config.items(sections[idx])]
    return vehicles

def getAllAircrafts():
    idx = sections.index('AircraftTypes')
    aircrafts = [x for _, x in config.items(sections[idx])]
    return aircrafts

def allowAllBases():
    countries = getAllCountries()
    countriesStr = ','.join(countries)
    allowAllBasesForCountry(countriesStr)

def allowAllBasesForCountry(country):
    bases = getAllBaseUnits()
    for base in bases:
        idx = sections.index(base)
        config.remove_option(sections[idx], 'Prerequisite')
        config.set(sections[idx], 'Owner', country)

def setCost(cost):
    for section in sections:
        if config.has_option(section, 'Cost'):
            config.set(section, 'Cost', str(cost))

def allowAlliedParaDrop(unit='E1', count=10):
    config.set('GACNST', 'SuperWeapon', 'ParaDropSpecial')
    idx = sections.index('General')
    config.set(sections[idx], 'AllyParaDropInf', unit)
    config.set(sections[idx], 'AllyParaDropNum', str(count))

def allowSovietParaDrop(unit='E2', count=10):
    config.set('NACNST', 'SuperWeapon', 'ParaDropSpecial')
    idx = sections.index('General')
    config.set(sections[idx], 'SovParaDropInf', unit)
    config.set(sections[idx], 'SovParaDropNum', str(count))

def allowYuriParaDrop(unit='INIT', count=10):
    config.set('YACNST', 'SuperWeapon', 'ParaDropSpecial')
    idx = sections.index('General')
    config.set(sections[idx], 'YuriParaDropInf', unit)
    config.set(sections[idx], 'YuriParaDropNum', str(count))

def setParaDropCooldown(rechargeTime=1):
    idx = sections.index('AmericanParaDropSpecial')
    config.set(sections[idx], 'RechargeTime', str(rechargeTime))

def setBuildingAdjacency(adjacency=500):
    for section in sections:
        if config.has_option(section, 'Adjacent'):
            config.set(section, 'Adjacent', str(adjacency))

def setSpeedMultiplier(multiplier=2):
    for section in sections:
        if config.has_option(section, 'Speed'):
            speed = config.get(section, 'Speed')
            try:
                speed = int(speed)*multiplier
                config.set(section, 'Speed', str(speed))
            except:
                print(f'Error: {speed}' )

def setOreGrowth(growth=1, growthPercent=1, spread=200, spreadPercent=1, income=100):
    tiberiums = getAllTiberiums()
    for tiberium in tiberiums:
        idx = sections.index(tiberium)
        config.set(sections[idx], 'Growth', str(growth))
        config.set(sections[idx], 'GrowthPercentage', str(growthPercent))
        config.set(sections[idx], 'Spread', str(spread))
        config.set(sections[idx], 'SpreadPercentage', str(spreadPercent))
        config.set(sections[idx], 'Value', str(income))
    for section in sections:
        if config.has_option(section, 'AnimationProbability'):
            config.set(section, 'AnimationProbability', '1')

def setVeteranRatio(ratio=0.01):
    idx = sections.index('General')
    config.set(sections[idx], 'VeteranRatio', str(ratio))

def allowAutoRepair():
    idx = sections.index('IQ')
    config.set(sections[idx], 'RepairSell', '0')

def setChronoDelay(delay=0):
    idx = sections.index('General')
    config.set(sections[idx], 'ChronoDelay', str(delay))
    config.set(sections[idx], 'ChronoReinfDelay', str(delay))
    config.set(sections[idx], 'ChronoTrigger', 'no')
    config.set(sections[idx], 'ChronoMinimumDelay', '0')

def removeRequiredHousesFromUnits():
    for section in sections:
        if config.has_option(section, 'RequiredHouses'):
            config.remove_option(section, 'RequiredHouses')

def allowCommandoUnit():
    idx = sections.index('CCOMAND')
    config.remove_option(sections[idx], 'RequiresStolenAlliedTech')

def setBuildSpeed(speed=0.01):
    idx = sections.index('General')
    config.set(sections[idx], 'BuildSpeed', str(speed))

def removeBuildLimit():
    for section in sections:
        if config.has_option(section, 'BuildLimit'):
            config.remove_option(section, 'BuildLimit')

if __name__ == '__main__':
    save_loc = 'D:/Games/Other/Red Alert 2/Game/_MOD/rulesmd.ini'
    config = readConfig('rulesmd_og.ini')
    sections = config.sections()
    
    allowAllBases()
    allowAlliedParaDrop()
    allowSovietParaDrop()
    allowYuriParaDrop()
    setParaDropCooldown()
    setBuildingAdjacency()
    setOreGrowth()
    setSpeedMultiplier()
    setVeteranRatio()
    setChronoDelay()
    removeRequiredHousesFromUnits()
    allowCommandoUnit()
    setBuildSpeed()
    removeBuildLimit()
    allowAutoRepair()
    saveConfig(save_loc)
    launchGame()



import re

# Regular expression to match comments
comment_re = re.compile(r'\s*[#;].*$')

with open('./old/artmd.ini', 'r') as infile, open('artmd.ini', 'w') as outfile:
    for line in infile:
        # Remove any comments from the line
        line = comment_re.sub('', line)
        # Write the modified line to the output file
        outfile.write(line)