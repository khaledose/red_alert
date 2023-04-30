from kink import di
from .readers import *

# -------- general actions ---------
def setCostMultiplier(cost):
    for section in di['config'].config.sections():
        if di['config'].config.has_option(section, 'Cost'):
            di['config'].config.set(section, 'Cost', str(cost))

def setOreGrowthRate(rate=0.5):
    setOreGrowth(1000*rate)
    setOreGrowthPercent(rate)
    setOreSpread(1000*rate)
    setOreSpreadPercent(rate)

def setOreGrowth(growth=1):
    tiberiums = getAllTiberiums()
    for tiberium in tiberiums:
        idx = di['config'].config.sections().index(tiberium)
        di['config'].config.set(di['config'].config.sections()[idx], 'Growth', str(growth))
    
    for section in di['config'].config.sections():
        if di['config'].config.has_option(section, 'AnimationProbability'):
            di['config'].config.set(section, 'AnimationProbability', '1')

def setOreGrowthPercent(growthPercent=1):
    tiberiums = getAllTiberiums()
    for tiberium in tiberiums:
        idx = di['config'].config.sections().index(tiberium)
        di['config'].config.set(di['config'].config.sections()[idx], 'GrowthPercentage', str(growthPercent))

def setOreSpread(spread=200):
    tiberiums = getAllTiberiums()
    for tiberium in tiberiums:
        idx = di['config'].config.sections().index(tiberium)
        di['config'].config.set(di['config'].config.sections()[idx], 'Spread', str(spread))

def setOreSpreadPercent(spreadPercent=1):
    tiberiums = getAllTiberiums()
    for tiberium in tiberiums:
        idx = di['config'].config.sections().index(tiberium)
        di['config'].config.set(di['config'].config.sections()[idx], 'SpreadPercentage', str(spreadPercent))

def setOreIncome(income=100):
    tiberiums = getAllTiberiums()
    for tiberium in tiberiums:
        idx = di['config'].config.sections().index(tiberium)
        di['config'].config.set(di['config'].config.sections()[idx], 'Value', str(income))

def setBuildSpeed(speed=0.01):
    idx = di['config'].config.sections().index('General')
    di['config'].config.set(di['config'].config.sections()[idx], 'BuildSpeed', str(speed))

def removeBuildLimit(state=True):
    for section in di['config'].config.sections():
        if di['config'].config.has_option(section, 'BuildLimit'):
            di['config'].config.remove_option(section, 'BuildLimit')

def removeRequirements(state=True):
    countries = getAllCountries()
    countriesStr = ','.join(countries)
    for section in di['config'].config.sections():
        if not di['config'].config.has_option(section, 'Prerequisite'):
            continue
        if 'AILOCK' in di['config'].config.get(section, 'Prerequisite'):
            continue
        if not di['config'].config.has_option(section, 'TechLevel'):
            continue
        tech = int(di['config'].config.get(section, 'TechLevel'))
        if tech < 0 or tech > 10:
            continue
        
        di['config'].config.remove_option(section, 'Prerequisite')
        di['config'].config.set(section, 'TechLevel', '1')
        # if di['config'].config.has_option(section, 'Prerequisite'):
        #     di['config'].config.remove_option(section, 'Prerequisite')
        # if di['config'].config.has_option(section, 'TechLevel'):
        #     if int(di['config'].config.get(section, 'TechLevel')) > 0:
        #         di['config'].config.set(section, 'TechLevel', '1')
        # if di['config'].config.has_option(section, 'Owner') and di['config'].config.get(section, 'Owner') == 'Europeans,UnitedStates,Pacific':
        #     di['config'].config.remove_option(section, 'Prerequisite')
        #     di['config'].config.set(section, 'Owner', countriesStr)

# ----------------------------------

# -------- building actions --------

def setBuildingAdjacency(adjacency=500):
    for section in di['config'].config.sections():
        if di['config'].config.has_option(section, 'Adjacent'):
            di['config'].config.set(section, 'Adjacent', str(adjacency))

def toggleAutoRepair(state=True):
    val = '0' if state else '1'
    idx = di['config'].config.sections().index('IQ')
    di['config'].config.set(di['config'].config.sections()[idx], 'RepairSell', val)

def allowAllBases(state=True):
    countries = getAllCountries()
    countriesStr = ','.join(countries)
    return allowAllBasesForCountry(countriesStr)

def allowAllBasesForCountry(country):
    bases = getAllBaseUnits()
    for base in bases:
        idx = di['config'].config.sections().index(base)
        di['config'].config.remove_option(di['config'].config.sections()[idx], 'Prerequisite')
        original_owners = getBaseOwners(base)
        if country not in original_owners:
            original_owners.append(country)
            di['config'].config.set(di['config'].config.sections()[idx], 'Owner', ','.join(original_owners))

# ----------------------------------

# ---------- unit actions ----------

def setSpeedMultiplier(multiplier=2):
    for section in di['config'].config.sections():
        if di['config'].config.has_option(section, 'Speed'):
            speed = di['config'].config.get(section, 'Speed')
            try:
                speed = int(speed)*multiplier
                di['config'].config.set(section, 'Speed', str(speed))
            except:
                print(f'Error: {speed}' )

def setVeteranRatio(ratio=0.01):
    idx = di['config'].config.sections().index('General')
    di['config'].config.set(di['config'].config.sections()[idx], 'VeteranRatio', str(ratio))

def setChronoDelay(delay=0):
    idx = di['config'].config.sections().index('General')
    di['config'].config.set(di['config'].config.sections()[idx], 'ChronoDelay', str(delay))
    di['config'].config.set(di['config'].config.sections()[idx], 'ChronoReinfDelay', str(delay))
    di['config'].config.set(di['config'].config.sections()[idx], 'ChronoTrigger', 'no')
    di['config'].config.set(di['config'].config.sections()[idx], 'ChronoMinimumDelay', '0')

def removeRequiredHousesFromUnits(state=True):
    for section in di['config'].config.sections():
        if di['config'].config.has_option(section, 'RequiredHouses'):
            di['config'].config.remove_option(section, 'RequiredHouses')

def AllowStolenTech(state=True):
    idx = di['config'].config.sections().index('CCOMAND')
    di['config'].config.remove_option(di['config'].config.sections()[idx], 'RequiresStolenAlliedTech')

    idx = di['config'].config.sections().index('CIVAN')
    di['config'].config.remove_option(di['config'].config.sections()[idx], 'RequiresStolenSovietTech')

    idx = di['config'].config.sections().index('PTROOP')
    di['config'].config.remove_option(di['config'].config.sections()[idx], 'RequiresStolenThirdTech')

# ----------------------------------

# ---------- super actions ---------

def allowAlliedParaDrop(state=True):
    value = 'ParaDropSpecial' if state else ''
    di['config'].config.set('GACNST', 'SuperWeapon', value)

def setAlliedParaDropUnit(unit='E1'):
    idx = di['config'].config.sections().index('General')
    di['config'].config.set(di['config'].config.sections()[idx], 'AllyParaDropInf', unit)

def setAlliedParaDropCount(count=10):
    idx = di['config'].config.sections().index('General')
    di['config'].config.set(di['config'].config.sections()[idx], 'AllyParaDropNum', str(count))

def allowSovietParaDrop(state=True):
    value = 'ParaDropSpecial' if state else ''
    di['config'].config.set('NACNST', 'SuperWeapon', value)

def setSovietParaDropUnit(unit='E2'):
    idx = di['config'].config.sections().index('General')
    di['config'].config.set(di['config'].config.sections()[idx], 'SovParaDropInf', unit)

def setSovietParaDropCount(count=10):
    idx = di['config'].config.sections().index('General')
    di['config'].config.set(di['config'].config.sections()[idx], 'SovParaDropNum', str(count))

def allowYuriParaDrop(state=True):
    value = 'ParaDropSpecial' if state else ''
    di['config'].config.set('YACNST', 'SuperWeapon', value)

def setYuriParaDropUnit(unit='INIT'):
    idx = di['config'].config.sections().index('General')
    di['config'].config.set(di['config'].config.sections()[idx], 'YuriParaDropInf', unit)

def setYuriParaDropCount(count=10):
    idx = di['config'].config.sections().index('General')
    di['config'].config.set(di['config'].config.sections()[idx], 'YuriParaDropNum', str(count))

def setParaDropCooldown(rechargeTime=1):
    idx = di['config'].config.sections().index('ParaDropSpecial')
    di['config'].config.set(di['config'].config.sections()[idx], 'RechargeTime', str(rechargeTime))

# ----------------------------------