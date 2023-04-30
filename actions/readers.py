from kink import di

def getAllCountries():
    idx = di['config'].config.sections().index('Countries')
    countries = [x for _, x in di['config'].config.items(di['config'].config.sections()[idx])]
    return countries

def getAllSides():
    idx = di['config'].config.sections().index('Sides')
    countries = [x for x, _ in di['config'].config.items(di['config'].config.sections()[idx])]
    return countries[:-2]

def getAllCountriesFromSide(side):
    if not di['config'].config.has_option('Sides', side):
        return []
    ctr = di['config'].config.get('Sides', side)
    return ctr.split(',')

def getAllBaseUnits():
    idx = di['config'].config.sections().index('General')
    return di['config'].config.get(di['config'].config.sections()[idx], 'BaseUnit').split(',')

def getAllBases():
    idx = di['config'].config.sections().index('AI')
    return di['config'].config.get(di['config'].config.sections()[idx], 'BuildConst').split(',')

def getBaseOwners(base):
    idx = di['config'].config.sections().index(base)
    return di['config'].config.get(di['config'].config.sections()[idx], 'Owner').split(',')

def getAllTiberiums():
    idx = di['config'].config.sections().index('Tiberiums')
    tiberiums = [x for _, x in di['config'].config.items(di['config'].config.sections()[idx])]
    return tiberiums

def getAllInfantries():
    idx = di['config'].config.sections().index('InfantryTypes')
    infantries = [x for _, x in di['config'].config.items(di['config'].config.sections()[idx])]
    return infantries

def getAllVehicles():
    idx = di['config'].config.sections().index('VehicleTypes')
    vehicles = [x for _, x in di['config'].config.items(di['config'].config.sections()[idx])]
    return vehicles

def getAllAircrafts():
    idx = di['config'].config.sections().index('AircraftTypes')
    aircrafts = [x for _, x in di['config'].config.items(di['config'].config.sections()[idx])]
    return aircrafts

def getGeneralDefaults():
    costMultiplier = 1.0
    tiberiums = getAllTiberiums()
    for tiberium in tiberiums[:1]:
        idx = di['config'].config.sections().index(tiberium)
        oreGrowth = di['config'].config.get(di['config'].config.sections()[idx], 'Growth')
        oreGrowthPercent = di['config'].config.get(di['config'].config.sections()[idx], 'GrowthPercentage')
        oreSpread = di['config'].config.get(di['config'].config.sections()[idx], 'Spread')
        oreSpreadPercent = di['config'].config.get(di['config'].config.sections()[idx], 'SpreadPercentage')
        oreIncome = di['config'].config.get(di['config'].config.sections()[idx], 'Value')
    
    idx = di['config'].config.sections().index('General')
    buildSpeed = di['config'].config.get(di['config'].config.sections()[idx], 'BuildSpeed')

    return costMultiplier, oreGrowth, oreGrowthPercent, oreSpread, oreSpreadPercent, oreIncome, buildSpeed

