from configparser import ConfigParser
from kink import di
from .readers import *
from .defaults import *

# -------- general actions ---------

def setCost(cost):
    config: ConfigParser = di['config'].config
    for section in config.sections():
        if config.has_option(section, 'Cost'):
            config.set(section, 'Cost', str(cost))

def setOreGrowthRate(rate=0.5):
    setOreGrowth(1000*rate)
    setOreGrowthPercent(rate)
    setOreSpread(1000*rate)
    setOreSpreadPercent(rate)

def setOreGrowth(growth=1):
    config: ConfigParser = di['config'].config
    tiberiums = getAllTiberiums()
    for tiberium in tiberiums:
        idx = config.sections().index(tiberium)
        config.set(config.sections()[idx], 'Growth', str(growth))
    
    for section in config.sections():
        if config.has_option(section, 'AnimationProbability'):
            config.set(section, 'AnimationProbability', '1')

def setOreGrowthPercent(growthPercent=1):
    config: ConfigParser = di['config'].config
    tiberiums = getAllTiberiums()
    for tiberium in tiberiums:
        idx = config.sections().index(tiberium)
        config.set(config.sections()[idx], 'GrowthPercentage', str(growthPercent))

def setOreSpread(spread=200):
    config: ConfigParser = di['config'].config
    tiberiums = getAllTiberiums()
    for tiberium in tiberiums:
        idx = config.sections().index(tiberium)
        config.set(config.sections()[idx], 'Spread', str(spread))

def setOreSpreadPercent(spreadPercent=1):
    config: ConfigParser = di['config'].config
    tiberiums = getAllTiberiums()
    for tiberium in tiberiums:
        idx = config.sections().index(tiberium)
        config.set(config.sections()[idx], 'SpreadPercentage', str(spreadPercent))

def setOreIncome(income=100):
    config: ConfigParser = di['config'].config
    tiberiums = getAllTiberiums()
    for tiberium in tiberiums:
        idx = config.sections().index(tiberium)
        config.set(config.sections()[idx], 'Value', str(income))

def setBuildSpeed(speed=0.01):
    config: ConfigParser = di['config'].config
    idx = config.sections().index('General')
    config.set(config.sections()[idx], 'BuildSpeed', str(speed))

def removeBuildLimit(state=True):
    config: ConfigParser = di['config'].config
    if not state:
        resetBuildLimit()
        return
    for section in config.sections():
        if config.has_option(section, 'BuildLimit'):
            config.remove_option(section, 'BuildLimit')

def removeRequirements(state=True):
    config: ConfigParser = di['config'].config
    for section in config.sections():
        if not config.has_option(section, 'Prerequisite'):
            continue
        if 'AILOCK' in config.get(section, 'Prerequisite'):
            continue
        if not config.has_option(section, 'TechLevel'):
            continue
        tech = int(config.get(section, 'TechLevel'))
        if tech < 0 or tech > 10:
            continue
        
        config.remove_option(section, 'Prerequisite')
        config.set(section, 'TechLevel', '1')

# ----------------------------------

# -------- building actions --------

def setBuildingAdjacency(adjacency=500):
    config: ConfigParser = di['config'].config
    for section in config.sections():
        if config.has_option(section, 'Adjacent'):
            config.set(section, 'Adjacent', str(adjacency))

def toggleAutoRepair(state=True):
    config: ConfigParser = di['config'].config
    val = '0' if state else '1'
    idx = config.sections().index('IQ')
    config.set(config.sections()[idx], 'RepairSell', val)

def allowAllBases(state=True):
    if not state:
        resetBases()
        return
    countries = getAllCountries()
    countriesStr = ','.join(countries)
    return allowAllBasesForCountry(countriesStr)

def allowAllBasesForCountry(country):
    config: ConfigParser = di['config'].config
    bases = getAllBaseUnits()
    for base in bases:
        idx = config.sections().index(base)
        config.remove_option(config.sections()[idx], 'Prerequisite')
        original_owners = getBaseOwners(base)
        if country not in original_owners:
            original_owners.append(country)
            config.set(config.sections()[idx], 'Owner', ','.join(original_owners))

# ----------------------------------

# ---------- unit actions ----------

def setSpeedMultiplier(multiplier=2):
    config: ConfigParser = di['config'].config
    for section in config.sections():
        if config.has_option(section, 'Speed'):
            speed = config.get(section, 'Speed')
            try:
                speed = int(speed)*multiplier
                config.set(section, 'Speed', str(speed))
            except:
                print(f'Error: {speed}' )

def setVeteranRatio(ratio=0.01):
    config: ConfigParser = di['config'].config
    idx = config.sections().index('General')
    config.set(config.sections()[idx], 'VeteranRatio', str(ratio))

def removeChronoDelay(state=True):
    config: ConfigParser = di['config'].config
    val = 'no' if state else 'yes'
    config.set('General', 'ChronoTrigger', val)

def removeRequiredHousesFromUnits(state=True):
    config: ConfigParser = di['config'].config
    if not state:
        resetRequiredHouses()
        return
    for section in config.sections():
        if config.has_option(section, 'RequiredHouses'):
            config.remove_option(section, 'RequiredHouses')

def AllowStolenTech(state=True):
    config: ConfigParser = di['config'].config
    if not state:
        resetStolenTech()
        return
    idx = config.sections().index('CCOMAND')
    config.remove_option(config.sections()[idx], 'RequiresStolenAlliedTech')

    idx = config.sections().index('CIVAN')
    config.remove_option(config.sections()[idx], 'RequiresStolenSovietTech')

    idx = config.sections().index('PTROOP')
    config.remove_option(config.sections()[idx], 'RequiresStolenThirdTech')

# ----------------------------------

# ---------- super actions ---------

def allowAlliedParaDrop(state=True):
    config: ConfigParser = di['config'].config
    value = 'ParaDropSpecial' if state else ''
    config.set('GACNST', 'SuperWeapon', value)

def setAlliedParaDropUnit(unit='E1'):
    config: ConfigParser = di['config'].config
    idx = config.sections().index('General')
    config.set(config.sections()[idx], 'AllyParaDropInf', unit)

def setAlliedParaDropCount(count=10):
    config: ConfigParser = di['config'].config
    idx = config.sections().index('General')
    config.set(config.sections()[idx], 'AllyParaDropNum', str(count))

def allowSovietParaDrop(state=True):
    config: ConfigParser = di['config'].config
    value = 'ParaDropSpecial' if state else ''
    config.set('NACNST', 'SuperWeapon', value)

def setSovietParaDropUnit(unit='E2'):
    config: ConfigParser = di['config'].config
    idx = config.sections().index('General')
    config.set(config.sections()[idx], 'SovParaDropInf', unit)

def setSovietParaDropCount(count=10):
    config: ConfigParser = di['config'].config
    idx = config.sections().index('General')
    config.set(config.sections()[idx], 'SovParaDropNum', str(count))

def allowYuriParaDrop(state=True):
    config: ConfigParser = di['config'].config
    value = 'ParaDropSpecial' if state else ''
    config.set('YACNST', 'SuperWeapon', value)

def setYuriParaDropUnit(unit='INIT'):
    config: ConfigParser = di['config'].config
    idx = config.sections().index('General')
    config.set(config.sections()[idx], 'YuriParaDropInf', unit)

def setYuriParaDropCount(count=10):
    config: ConfigParser = di['config'].config
    idx = config.sections().index('General')
    config.set(config.sections()[idx], 'YuriParaDropNum', str(count))

def setParaDropCooldown(rechargeTime=1):
    config: ConfigParser = di['config'].config
    idx = config.sections().index('ParaDropSpecial')
    config.set(config.sections()[idx], 'RechargeTime', str(rechargeTime))

# ----------------------------------