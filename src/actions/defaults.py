from kink import di
from configparser import ConfigParser
from .readers import *
from src.utils.migrate import add_section_details

def resetAll():
    resetCost()
    resetOre()
    resetBuildSpeed()
    resetBuildLimit()
    resetRequirements()
    resetBuildingAdjacency()
    resetAutoRepair()
    resetBases()
    resetVeteranRatio()
    resetChronoDelay()
    resetRequiredHouses()
    resetStolenTech()

def resetCost():
    ref: ConfigParser = di['config'].refConfig
    config: ConfigParser = di['config'].config

    for section in ref.sections():
        if ref.has_option(section, 'Cost'):
            cost = ref.get(section, 'Cost')
            config.set(section, 'Cost', cost)

def resetOre():
    ref: ConfigParser = di['config'].refConfig
    config: ConfigParser = di['config'].config

    for ore in getAllTiberiums():
        config.remove_section(ore)
        add_section_details(ref, config, ore)

def resetBuildSpeed():
    ref: ConfigParser = di['config'].refConfig
    config: ConfigParser = di['config'].config

    speed = ref.get('General', 'BuildSpeed')
    config.set('General', 'BuildSpeed', speed)

def resetBuildLimit():
    ref: ConfigParser = di['config'].refConfig
    config: ConfigParser = di['config'].config

    for section in ref.sections():
        if ref.has_option(section, 'BuildLimit'):
            limit = ref.get(section, 'BuildLimit')
            config.set(section, 'BuildLimit', limit)

def resetRequirements():
    # TODO
    print('not implemented')

def resetBuildingAdjacency():
    ref: ConfigParser = di['config'].refConfig
    config: ConfigParser = di['config'].config

    for section in ref.sections():
        if ref.has_option(section, 'Adjacent'):
            adj = ref.get(section, 'Adjacent')
            config.set(section, 'Adjacent', adj)

def resetAutoRepair():
    ref: ConfigParser = di['config'].refConfig
    config: ConfigParser = di['config'].config

    repair = ref.get('IQ', 'RepairSell')
    config.set('IQ', 'RepairSell', repair)

def resetBases():
    ref: ConfigParser = di['config'].refConfig
    config: ConfigParser = di['config'].config

    bases = getAllBaseUnits()

    for base in bases:
        config.remove_section(base)
        add_section_details(ref, config, base)

def resetVeteranRatio():
    ref: ConfigParser = di['config'].refConfig
    config: ConfigParser = di['config'].config

    ratio = ref.get('General', 'VeteranRatio')
    config.set('General', 'VeteranRatio', ratio)

def resetChronoDelay():
    ref: ConfigParser = di['config'].refConfig
    config: ConfigParser = di['config'].config

    chronoTrigger = ref.get('General', 'ChronoTrigger')
    config.set('General', 'ChronoTrigger', chronoTrigger)

def resetRequiredHouses():
    ref: ConfigParser = di['config'].refConfig
    config: ConfigParser = di['config'].config

    for section in ref.sections():
        if ref.has_option(section, 'RequiredHouses'):
            houses = ref.get(section, 'RequiredHouses')
            config.set(section, 'RequiredHouses', houses)

def resetStolenTech():
    ref: ConfigParser = di['config'].refConfig
    config: ConfigParser = di['config'].config

    stolenTech = ['CCOMAND', 'PTROOP', 'CIVAN']
    for tech in stolenTech:
        if ref.has_section(tech):
            config.remove_section(tech)
            add_section_details(ref, config, tech)



