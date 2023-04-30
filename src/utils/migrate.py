import configparser
import struct
import os

class Config:
    def __init__(self, type) -> None:
        self.type = type
        self.rules = load_config(f'./db/rules{type}.ini')
        self.sound = load_config(f'./db/sound{type}.ini')
        self.art = load_config(f'./db/art{type}.ini')
    
    def save_rules(self):
        with open(f'./mod/rules{self.type}.ini', 'w') as f:
            self.rules.write(f)
    
    def save_sound(self):
        with open(f'./mod/sound{self.type}.ini', 'w') as f:
            self.sound.write(f)

    def save_art(self):
        with open(f'./mod/art{self.type}.ini', 'w') as f:
            self.art.write(f)

def load_config(path):
    config = configparser.RawConfigParser()
    config.optionxform = str
    config.read(path)
    return config

def unprotect_mix(mix_file):
    with open(mix_file, "rb") as f:
        contents = bytearray(f.read())

        hex_strings = [struct.pack("B", byte) for byte in contents]
        num_files = hex_strings[5] + hex_strings[4]
        num_files = (int.from_bytes(num_files, 'big') * 12) + 10

        file_size = os.stat(f.fileno()).st_size

        body_size = file_size - num_files
        print(body_size)
        body_size = body_size.to_bytes(4, "little")
        
        i = 6
        for b in body_size:
            hex_strings[i] = struct.pack("B", b)
            i+=1

        with open(f"./unprotected_mixes/{mix_file}", "wb") as f:
            for hex_string in hex_strings:
                f.write(hex_string)

def find_infantries(md, mo):
    idx = md.sections().index('InfantryTypes')
    mdInf = [x for _, x in md.items(md.sections()[idx])]

    idx = mo.sections().index('InfantryTypes')
    moInf = [x for _, x in mo.items(mo.sections()[idx])]

    mo_miss = []
    for item in mdInf:
        if item not in moInf:
            mo_miss.append(item)

    return mo_miss

def find_vehicles(md, mo):
    idx = md.sections().index('VehicleTypes')
    mdInf = [x for _, x in md.items(md.sections()[idx])]

    idx = mo.sections().index('VehicleTypes')
    moInf = [x for _, x in mo.items(mo.sections()[idx])]

    mo_miss = []
    for item in mdInf:
        if item not in moInf:
            mo_miss.append(item)

    return mo_miss

def find_buildings(md, mo):
    idx = md.sections().index('BuildingTypes')
    mdInf = [x for _, x in md.items(md.sections()[idx])]

    idx = mo.sections().index('BuildingTypes')
    moInf = [x for _, x in mo.items(mo.sections()[idx])]

    miss = []
    for item in mdInf:
        if item not in moInf:
            miss.append(item)

    mo_miss = []
    for building in miss:
        if md.has_section(building) and int(md.get(building, 'TechLevel')) > 0:
            mo_miss.append(building)
            

    return mo_miss

def append_list(config, section, id):
    opts = config.options(section)
    idx = int(opts[-1]) + 1
    config.set(section, str(idx), id)
    return config

def add_section_details(config1, config2, id):
    opts = config1.items(id)
    config2.add_section(id)
    for opt in opts:
        config2.set(id, opt[0], opt[1])
    return config2

def restore_chrono_commando(md: Config, mo: Config):
    id = 'CCOMAND'
    append_list(mo.rules, 'InfantryTypes', id)
    add_section_details(md.rules, mo.rules, id)
    add_section_details(md.rules, mo.rules, 'ChronoMP5')
    add_section_details(md.rules, mo.rules, 'ChronoMP5E')
    append_list(mo.rules, 'Warheads', 'HollowPointNoBuilding')
    add_section_details(md.rules, mo.rules, 'HollowPointNoBuilding')
    add_section_details(md.rules, mo.rules, 'FakeC4')
    append_list(mo.sound, 'SoundList', 'ChronoCommandoSelect')
    add_section_details(md.sound, mo.sound, 'ChronoCommandoSelect')
    append_list(mo.sound, 'SoundList', 'ChronoCommandoMove')
    add_section_details(md.sound, mo.sound, 'ChronoCommandoMove')
    append_list(mo.sound, 'SoundList', 'ChronoCommandoAttackCommand')
    add_section_details(md.sound, mo.sound, 'ChronoCommandoAttackCommand')
    append_list(mo.sound, 'SoundList', 'ChronoCommandoSpecialAttack')
    add_section_details(md.sound, mo.sound, 'ChronoCommandoSpecialAttack')
    append_list(mo.sound, 'SoundList', 'ChronoCommandoCreated')
    add_section_details(md.sound, mo.sound, 'ChronoCommandoCreated')
    add_section_details(md.art, mo.art, 'ComandoSequence')
    mo.art.remove_section(id)
    add_section_details(md.art, mo.art, id)
    mo.art.remove_option(id, 'Cameo')
    mo.art.remove_option(id, 'AltCameo')
    mo.art.set(id, 'CameoPCX', 'ccmdicon.pcx')
    mo.art.set(id, 'AltCameoPCX', 'ccmduico.pcx')

def restore_chrono_ivan(md: Config, mo: Config):
    id = 'CIVAN'
    append_list(mo.rules, 'InfantryTypes', id)
    add_section_details(md.rules, mo.rules, id)
    mo.rules.remove_section('IvanBomber')
    add_section_details(md.rules, mo.rules, 'IvanBomber')
    add_section_details(md.art, mo.art, 'CIvanSequence')
    add_section_details(md.art, mo.art, id)
    mo.art.remove_option(id, 'Cameo')
    mo.art.set(id, 'CameoPCX', 'ivncicon.pcx')
    mo.art.set(id, 'AltCameoPCX', 'ivncuico.pcx')

def restore_psi_corp(md: Config, mo: Config):
    id = 'PTROOP'
    append_list(mo.rules, 'InfantryTypes', id)
    add_section_details(md.rules, mo.rules, id)
    mo.art.set(id, 'CameoPCX', 'psicicon.pcx')
    mo.art.set(id, 'AltCameoPCX', 'psicuico.pcx')

def restore_boris(md: Config, mo: Config):
    id = 'BORIS'
    append_list(mo.rules, 'InfantryTypes', id)
    add_section_details(md.rules, mo.rules, id)

def restore_infantries(md: Config, mo: Config):
    restore_chrono_commando(md, mo)
    restore_chrono_ivan(md, mo)
    restore_psi_corp(md, mo)
    restore_boris(md, mo)

if __name__ == '__main__':
    md = Config('md')
    mo = Config('mo')

    restore_infantries(md, mo)

    mo.save_rules()
    mo.save_sound()
    mo.save_art()
    # unprotect_mix('./expandmo93.mix')


