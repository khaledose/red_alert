from kink import di
from configparser import ConfigParser

def getAllCountries():
    config: ConfigParser = di['config'].config
    if not config.has_section('Countries'):
        return []
    countries = [x for _, x in config.items('Countries')]
    return countries

def getAllSides():
    config: ConfigParser = di['config'].config
    if not config.has_section('Sides'):
        return []
    countries = [x for x, _ in config.items('Sides')]
    return countries[:-2]

def getAllCountriesFromSide(side):
    config: ConfigParser = di['config'].config
    if not config.has_option('Sides', side):
        return []
    ctr = config.get('Sides', side)
    return ctr.split(',')

def getAllBaseUnits():
    config: ConfigParser = di['config'].config
    if not config.has_section('General'):
        return []
    return config.get('General', 'BaseUnit').split(',')

def getAllBases():
    config: ConfigParser = di['config'].config
    if not config.has_section('AI'):
        return []
    return config.get('AI', 'BuildConst').split(',')

def getBaseOwners(base):
    config: ConfigParser = di['config'].config
    if not config.has_section(base):
        return []
    return config.get(base, 'Owner').split(',')

def getAllTiberiums():
    config: ConfigParser = di['config'].config
    if not config.has_section('Tiberiums'):
        return []
    tiberiums = [x for _, x in config.items('Tiberiums')]
    return tiberiums

def getAllInfantries():
    config: ConfigParser = di['config'].config
    if not config.has_section('InfantryTypes'):
        return []
    infantries = [x for _, x in config.items('InfantryTypes')]
    return infantries

def getAllVehicles():
    config: ConfigParser = di['config'].config
    if not config.has_section('VehicleTypes'):
        return []
    vehicles = [x for _, x in config.items('VehicleTypes')]
    return vehicles

def getAllAircrafts():
    config: ConfigParser = di['config'].config
    if not config.has_section('AircraftTypes'):
        return []
    aircrafts = [x for _, x in config.items('AircraftTypes')]
    return aircrafts
