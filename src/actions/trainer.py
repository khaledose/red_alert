from pymem.ptypes import RemotePointer
from pymem import Pymem, memory
from kink import di
import json

class GameModifier():
    def __init__(self, pname, offsets_path):
        self.pname = pname
        with open(offsets_path, 'r') as file:
            self.data = json.load(file)

    def write(self, address, offsets, value):
        address = int(address, 16)
        offsets = [int(i, 16) for i in offsets]
        p = self.get_pointer(address, offsets)
        self.pm.write_int(p, value)

    def read(self, address, offsets):
        address = int(address, 16)
        offsets = [int(i, 16) for i in offsets]
        p = self.get_pointer(address, offsets)
        return self.pm.read_int(p)
    
    def run(self, key, value):
        self.pm = Pymem(self.pname)
        data = self.data[key]
        self.write(data['Address'], data['Offsets'], value)
        self.pm.close_process()
    
    def get(self, key):
        self.pm = Pymem(self.pname)
        data = self.data[key]
        value = self.read(data['Address'], data['Offsets'])
        self.pm.close_process()
        return value
    
    def get_pointer(self, base, offsets):
        remote_pointer = RemotePointer(self.pm.process_handle, base)
        for offset in offsets:
            if offset != offsets[-1]:
                remote_pointer = RemotePointer(self.pm.process_handle, remote_pointer.value + offset)
            else:
                return remote_pointer.value + offset

def set_money(amount):
    trainer: GameModifier = di['trainer']
    trainer.run('Money', amount)

def set_tech_level(tech):
    trainer: GameModifier = di['trainer']
    trainer.run('TechLevel', tech)

def set_power(power):
    trainer: GameModifier = di['trainer']
    trainer.run('Power', power)

def set_drain(drain):
    trainer: GameModifier = di['trainer']
    trainer.run('Power', drain)

def allied_stolen_tech(enable):
    trainer: GameModifier = di['trainer']
    tech = trainer.get("StolenTech")
    if enable:
        tech += 0x802
    else:
        tech -= 0x802
    trainer.run("StolenTech", tech)

def soviet_stolen_tech(enable):
    trainer: GameModifier = di['trainer']
    tech = trainer.get("StolenTech")
    if enable:
        tech += 0x1004
    else:
        tech -= 0x1004
    trainer.run("StolenTech", tech)

def yuri_stolen_tech(enable):
    trainer: GameModifier = di['trainer']
    tech = trainer.get("StolenTech")
    if enable:
        tech += 0x2008
    else:
        tech -= 0x2008
    trainer.run("StolenTech", tech)

def foehn_stolen_tech(enable):
    trainer: GameModifier = di['trainer']
    tech = trainer.get("StolenTech")
    if enable:
        tech += 0x4010
    else:
        tech -= 0x4010
    trainer.run("StolenTech", tech)

def calc_distance(dest, start):
    offset = dest - start
    byte_offset = offset.to_bytes(4, byteorder='little', signed=True)
    return byte_offset

def instant_build(enable):
    process = Pymem("gamemd.exe")
    start_point = 0x400000 + 0xCA120

    if enable:
        new_mem = memory.allocate_memory(process.process_handle, 1000)
        ret = calc_distance(new_mem, (start_point + 5))
        memory.write_bytes(process.process_handle, start_point, b'\xE9' + ret, len(b'\xE9' + ret))
        ret = calc_distance(start_point+5, new_mem + 5 + 25)
        memory.write_bytes(process.process_handle, new_mem, b'\x81\x79\x24\x35\x00\x00\x00\x0F\x8D\x07\x00\x00\x00\xC7\x41\x24\x35\x00\x00\x00\x8B\x41\x24\xC3\x90\xE9' + ret, len(b'\x81\x79\x24\x35\x00\x00\x00\x0F\x8D\x07\x00\x00\x00\xC7\x41\x24\x35\x00\x00\x00\x8B\x41\x24\xC3\x90\xE9' + ret))
    else:
        memory.write_bytes(process.process_handle, start_point, b'\x8B\x41\x24\xC3\x90', len(b'\x8B\x41\x24\xC3\x90'))

def unlimited_energy(state):
    process = Pymem("gamemd.exe")
    energy_mem = memory.allocate_memory(process.process_handle, 2048)

    start_point =  0x00400000 + 0x108D01

    if state:
        memory.write_bytes(process.process_handle, energy_mem, b'\x3B\x35\x4C\x3D\xA8\x00\x0F\x84\x0B\x00\x00\x00\x89\x8E\xA4\x53\x00\x00', len(b'\x3B\x35\x4C\x3D\xA8\x00\x0F\x84\x0B\x00\x00\x00\x89\x8E\xA4\x53\x00\x00'))

        ret = calc_distance((start_point + 6), (energy_mem + 18) + 5)
        memory.write_bytes(process.process_handle, energy_mem + 18, b'\xE9' + ret + b'\xC7\x86\xA4\x53\x00\x00\xFF\xE3\x0B\x54', len(b'\xE9' + ret + b'\xC7\x86\xA4\x53\x00\x00\xFF\xE3\x0B\x54'))

        ret = calc_distance((start_point + 6), (energy_mem + 33) + 5)
        memory.write_bytes(process.process_handle, energy_mem + 33, b'\xE9' + ret, len(b'\xE9' + ret))

        ret = calc_distance(energy_mem, (start_point) + 5)
        memory.write_bytes(process.process_handle, start_point, b'\xE9' + ret + b'\x90', len(b'\xE9' + ret + b'\x90'))
    else:
        memory.write_bytes(process.process_handle, start_point, b'\x89\x8E\xA4\x53\x00\x00', len(b'\x89\x8E\xA4\x53\x00\x00'))

    process.close_process()

def reveal_map(enable):
    process = Pymem("gamemd.exe")

    block1 = 0x400000 + 0x108E07
    block2 = 0x400000 + 0x108EAD
    block3 = 0x400000 + 0x108F6E

    if enable:
        bts = {
            block1 : '8B 81 B8 02 00 00 53 55 56 8B B1 B0 02 00 00 57 83 FE FF C6 44 24 10 00 74 0C 8B 15 84 ED A8 00 01 D0 29 F0 7F 0A 85 C0 0F 85 FA 00 00 00 90 90',
            block2 :  '8B 98 20 05 00 00 EB 07 90 90 90 90 90 90 90 8A 9B 7A 15 00 00 84 DB 74 42',
            block3 : '8B 6E 78 85 ED 0F 8E 89 00 00 00 8B 7E 6C 8B 0F 85 C9 74 74 39 35 4C 3D A8 00 75 6C 8A 86 7A 57 00 00 38 05 9C ED A8 00 7F 5E 90 90 90 8A 41 74 84 C0 74 54'
        }
        
        for address, data in bts.items():
            b = bytes.fromhex(data)
            memory.write_bytes(process.process_handle, address, b, len(b))
    else:
        bts = {
            block3 : '8B 6E 78 85 ED 0F 8E 89 00 00 00 8B 7E 6C 8B 0F 85 C9 74 74 8B 81 20 05 00 00 80 B8 A5 16 00 00 00 74 65 8A 81 81 00 00 00 84 C0 75 5B 8A 41 74 84 C0 74 54 A1 38 B2 A8 00 85 C0 75 16 8A 86 EC 01 00 00 84 C0 75 19 8A 86 ED 01 00 00 84 C0 74 22 EB 0D 3B 35 4C 3D A8 00 0F 94 C0 84 C0 74 13',
            block2 : '8B 98 20 05 00 00 80 BB A4 16 00 00 00 74 4C 8A 98 81 00 00 00 84 DB 75 42 8A 58 74 84 DB 74 3B 85 ED 75 14 8A 99 EC 01 00 00 84 DB 75 0A 8A 99 ED 01 00 00 84 DB 74 0E 8A 98 1B 04 00 00',
            block1 : '8B 81 B8 02 00 00 53 55 56 8B B1 B0 02 00 00 57 83 FE FF C6 44 24 10 00 74 0E 8B 15 84 ED A8 00 2B D6 3B D0 7D 0A 2B C2 85 C0 0F 85 F8 00 00 00'
        }
        
        for address, data in bts.items():
            b = bytes.fromhex(data)
            memory.write_bytes(process.process_handle, address, b, len(b))

def train_elites(enable):
    process = Pymem("gamemd.exe")

    block1 = 0x400000 + 0x335647
    block2 = 0x400000 + 0x31207F
    block3 = 0x400000 + 0x117D2A
    block4 = 0x400000 + 0x31204C
    block5 = 0x400000 + 0xF798A

    if enable:
        bts = {
            block1 : '39 05 4C 3D A8 00 75 29 90 90 8B 86 C4 06 00 00 8A 88 CE 0C 00 00 84 C9 90 90 8A 88 8E 0C 00 00 84 C9 74 0D 31 C9 41 C1 E1 1E 89 8E 50 01 00 00 90 E9 83 A9 43 07 90',
            block2 : '39 05 4C 3D A8 00 75 38 90 90',
            block3 : '39 05 4C 3D A8 00 75 1F 90 90 8B 86 C0 06 00 00 8A 88 8E 0C 00 00 84 C9 74 0D 31 C9 41 C1 E1 1E 89 8E 50 01 00 00 90',
            block4 : '39 05 4C 3D A8 00 75 27 90 90',
            block5 : '8B 05 4C 3D A8 00 39 C5 74 28 90 8B 44 24 18 BE B8 4D 7E 00 89 74 24 14 31 FF 39 F8 0F 84 74 05 00 00 8A 4C 24 21 84 C9 0F 84 68 05 00 00 E9 56 05 00 00 8A 87 9C 0D 00 00 84 C0 74 09 8B 05 4C 3D A8 00 39 C5 75 C3 90 8A 87 9B 0D 00 00 84 C0 74 08 8B 05 4C 3D A8 00 39 C5 75 AE 90'
        }
        
        for address, data in bts.items():
            b = bytes.fromhex(data)
            memory.write_bytes(process.process_handle, address, b, len(b))
    else:
        bts = {
            block5 : '8A 85 BE 02 00 00 84 C0 75 28 8B 44 24 18 BE B8 4D 7E 00 89 74 24 14 33 FF 3B C7 0F 84 75 05 00 00 8A 4C 24 21 84 C9 0F 84 69 05 00 00 E9 57 05 00 00 8A 87 9C 0D 00 00 84 C0 74 0A 8A 85 BD 02 00 00 84 C0 74 C4 8A 87 9B 0D 00 00 84 C0 74 0A 8A 85 BC 02 00 00 84 C0 74 B0 8B 87 A0 0D 00 00',
            block3 : '8A 88 BF 02 00 00 84 C9 74 1D 8B 86 C0 06 00 00 8A 88 8E 0C 00 00 84 C9 74 0D 6A 01 8D 8E 50 01 00 00 E8 3F 83 23 00 8B 86 C0 06 00 00',
            block4 : '8A 88 BF 02 00 00 84 C9 74 25 8B 06 8B CE FF 50 2C 83 F8 10 75 14 8B 86 10 07 00 00 85 C0 74 0A',
            block2 : '8A 88 C0 02 00 00 84 C9 74 36 8B 16 8B CE FF 52 2C 83 F8 28 74 16 8B 06 8B CE',
            block1 : '8A 88 C0 02 00 00 84 C9 74 27 8B 86 C4 06 00 00 8A 88 CE 0C 00 00 84 C9 75 17 8A 88 8E 0C 00 00 84 C9 74 0D 6A 01 8D 8E 50 01 00 00 E8 18 AA 01 00'
        }
        
        for address, data in bts.items():
            b = bytes.fromhex(data)
            memory.write_bytes(process.process_handle, address, b, len(b))

def build_anywhere(enable):
    process = Pymem("gamemd.exe")
    start_point = 0x4A8F61

    if enable:
        bts = bytes.fromhex('C6 44 24 3C 01')
    else:
        bts = bytes.fromhex('C6 44 24 3C 00')

    process.write_bytes(start_point, bts, len(bts))