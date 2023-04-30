from ReadWriteMemory import ReadWriteMemory
from kink import di
import json
import threading
import pyMeow

class GameModifier():
    def __init__(self, pname, offsets_path):
        self.pname = pname
        with open(offsets_path, 'r') as file:
            self.data = json.load(file)
        self.rwm = ReadWriteMemory()
        self.process = self.rwm.get_process_by_name(pname)

    def write(self, address, offsets, value):
        address = int(address, 16)
        offsets = [int(i, 16) for i in offsets]
        p = self.process.get_pointer(address, offsets)
        print(p)
        self.process.write(p, value)

    def read(self, address, offsets):
        address = int(address, 16)
        offsets = [int(i, 16) for i in offsets]
        p = self.process.get_pointer(address, offsets)
        return self.process.read(p)
    
    def run(self, key, value):
        self.process.open()
        data = self.data[key]
        self.write(data['Address'], data['Offsets'], value)
        self.process.close()
    
    def get(self, key):
        self.process.open()
        data = self.data[key]
        value = self.read(data['Address'], data['Offsets'])
        self.process.close()
        return value

def  calc_distance(dest, start):
    offset = dest - start
    byte_offset = offset.to_bytes(4, byteorder='little', signed=True)
    return byte_offset

def instant_build(enable):
    process = pyMeow.open_process("gamemd.exe")
    start_point = 0x400000 + 0xCA120
    
    if enable:
        new_mem = pyMeow.allocate_memory(process, 1000)
        ret = calc_distance(new_mem, (start_point + 5))
        pyMeow.w_bytes(process, start_point, b'\xE9' + ret)
        ret = calc_distance(start_point+5, new_mem + 5 + 25)
        pyMeow.w_bytes(process, new_mem, b'\x81\x79\x24\x35\x00\x00\x00\x0F\x8D\x07\x00\x00\x00\xC7\x41\x24\x35\x00\x00\x00\x8B\x41\x24\xC3\x90\xE9' + ret)
    else:
        pyMeow.w_bytes(process, start_point, b'\x8B\x41\x24\xC3\x90')

def set_money(amount):
    di['trainer'].run('Money', amount)

def set_tech_level(tech):
    di['trainer'].run('TechLevel', tech)

def set_power(power):
    di['trainer'].run('Power', power)

def set_drain(drain):
    di['trainer'].run('Power', drain)

def unlimited_energy(state):
    process = pyMeow.open_process("gamemd.exe")
    energy_mem = pyMeow.allocate_memory(process, 2048)

    start_point =  0x00400000 + 0x108D01

    if state:
        pyMeow.w_bytes(process, energy_mem, b'\x3B\x35\x4C\x3D\xA8\x00\x0F\x84\x0B\x00\x00\x00\x89\x8E\xA4\x53\x00\x00')

        ret = calc_distance((start_point + 6), (energy_mem + 18) + 5)
        pyMeow.w_bytes(process, energy_mem + 18, b'\xE9' + ret + b'\xC7\x86\xA4\x53\x00\x00\xFF\xE3\x0B\x54')

        ret = calc_distance((start_point + 6), (energy_mem + 33) + 5)
        pyMeow.w_bytes(process, energy_mem + 33, b'\xE9' + ret)

        ret = calc_distance(energy_mem, (start_point) + 5)
        pyMeow.w_bytes(process, start_point, b'\xE9' + ret + b'\x90')
    else:
        pyMeow.w_bytes(process, start_point, b'\x89\x8E\xA4\x53\x00\x00')
    pyMeow.close_process(process)

def reveal_map(enable):
    process = pyMeow.open_process("gamemd.exe")

    block1 = 0x400000 + 0x108E07
    block2 = 0x400000 + 0x108EAD
    block3 = 0x400000 + 0x108F6E

    if enable:
        pyMeow.w_bytes(process, block1, b'\x8B\x81\xB8\x02\x00\x00\x53\x55\x56\x8B\xB1\xB0\x02\x00\x00\x57\x83\xFE\xFF\xC6\x44\x24\x10\x00\x74\x0C\x8B\x15\x84\xED\xA8\x00\x01\xD0\x29\xF0\x7F\x0A\x85\xC0\x0F\x85\xFA\x00\x00\x00\x90\x90')
        
        pyMeow.w_bytes(process, block2, b'\x8B\x98\x20\x05\x00\x00\xEB\x07\x90\x90\x90\x90\x90\x90\x90\x8A\x9B\x7A\x15\x00\x00\x84\xDB\x74\x42')

        pyMeow.w_bytes(process, block3, b'\x8B\x6E\x78\x85\xED\x0F\x8E\x89\x00\x00\x00\x8B\x7E\x6C\x8B\x0F\x85\xC9\x74\x74\x39\x35\x4C\x3D\xA8\x00\x75\x6C\x8A\x86\x7A\x57\x00\x00\x38\x05\x9C\xED\xA8\x00\x7F\x5E\x90\x90\x90\x8A\x41\x74\x84\xC0\x74\x54')
    else:
        pyMeow.w_bytes(process, block3, b'\x8B\x6E\x78\x85\xED\x0F\x8E\x89\x00\x00\x00\x8B\x7E\x6C\x8B\x0F\x85\xC9\x74\x74\x8B\x81\x20\x05\x00\x00\x80\xB8\xA5\x16\x00\x00\x00\x74\x65\x8A\x81\x81\x00\x00\x00\x84\xC0\x75\x5B\x8A\x41\x74\x84\xC0\x74\x54\xA1\x38\xB2\xA8\x00\x85\xC0\x75\x16\x8A\x86\xEC\x01\x00\x00\x84\xC0\x75\x19\x8A\x86\xED\x01\x00\x00\x84\xC0\x74\x22\xEB\x0D\x3B\x35\x4C\x3D\xA8\x00\x0F\x94\xC0\x84\xC0\x74\x13')
        
        pyMeow.w_bytes(process, block2, b'\x8B\x98\x20\x05\x00\x00\x80\xBB\xA4\x16\x00\x00\x00\x74\x4C\x8A\x98\x81\x00\x00\x00\x84\xDB\x75\x42\x8A\x58\x74\x84\xDB\x74\x3B\x85\xED\x75\x14\x8A\x99\xEC\x01\x00\x00\x84\xDB\x75\x0A\x8A\x99\xED\x01\x00\x00\x84\xDB\x74\x0E\x8A\x98\x1B\x04\x00\x00')

        pyMeow.w_bytes(process, block1, b'\x8B\x81\xB8\x02\x00\x00\x53\x55\x56\x8B\xB1\xB0\x02\x00\x00\x57\x83\xFE\xFF\xC6\x44\x24\x10\x00\x74\x0E\x8B\x15\x84\xED\xA8\x00\x2B\xD6\x3B\xD0\x7D\x0A\x2B\xC2\x85\xC0\x0F\x85\xF8\x00\x00\x00')

def train_elites(enable):
    process = pyMeow.open_process("gamemd.exe")

    block1 = 0x400000 + 0x335647
    block2 = 0x400000 + 0x31207F
    block3 = 0x400000 + 0x117D2A
    block4 = 0x400000 + 0x31204C
    block5 = 0x400000 + 0xF798A

    if enable:
        pyMeow.w_bytes(process, block1, b'\x39\x05\x4C\x3D\xA8\x00\x75\x29\x90\x90\x8B\x86\xC4\x06\x00\x00\x8A\x88\xCE\x0C\x00\x00\x84\xC9\x90\x90\x8A\x88\x8E\x0C\x00\x00\x84\xC9\x74\x0D\x31\xC9\x41\xC1\xE1\x1E\x89\x8E\x50\x01\x00\x00\x90\xE9\x83\xA9\x43\x07\x90')

        pyMeow.w_bytes(process, block2, b'\x39\x05\x4C\x3D\xA8\x00\x75\x38\x90\x90')

        pyMeow.w_bytes(process, block3, b'\x39\x05\x4C\x3D\xA8\x00\x75\x1F\x90\x90\x8B\x86\xC0\x06\x00\x00\x8A\x88\x8E\x0C\x00\x00\x84\xC9\x74\x0D\x31\xC9\x41\xC1\xE1\x1E\x89\x8E\x50\x01\x00\x00\x90')

        pyMeow.w_bytes(process, block4, b'\x39\x05\x4C\x3D\xA8\x00\x75\x27\x90\x90')

        pyMeow.w_bytes(process, block5, b'\x8B\x05\x4C\x3D\xA8\x00\x39\xC5\x74\x28\x90\x8B\x44\x24\x18\xBE\xB8\x4D\x7E\x00\x89\x74\x24\x14\x31\xFF\x39\xF8\x0F\x84\x74\x05\x00\x00\x8A\x4C\x24\x21\x84\xC9\x0F\x84\x68\x05\x00\x00\xE9\x56\x05\x00\x00\x8A\x87\x9C\x0D\x00\x00\x84\xC0\x74\x09\x8B\x05\x4C\x3D\xA8\x00\x39\xC5\x75\xC3\x90\x8A\x87\x9B\x0D\x00\x00\x84\xC0\x74\x08\x8B\x05\x4C\x3D\xA8\x00\x39\xC5\x75\xAE\x90')
    else:
        pyMeow.w_bytes(process, block5, b'\x8A\x85\xBE\x02\x00\x00\x84\xC0\x75\x28\x8B\x44\x24\x18\xBE\xB8\x4D\x7E\x00\x89\x74\x24\x14\x33\xFF\x3B\xC7\x0F\x84\x75\x05\x00\x00\x8A\x4C\x24\x21\x84\xC9\x0F\x84\x69\x05\x00\x00\xE9\x57\x05\x00\x00\x8A\x87\x9C\x0D\x00\x00\x84\xC0\x74\x0A\x8A\x85\xBD\x02\x00\x00\x84\xC0\x74\xC4\x8A\x87\x9B\x0D\x00\x00\x84\xC0\x74\x0A\x8A\x85\xBC\x02\x00\x00\x84\xC0\x74\xB0\x8B\x87\xA0\x0D\x00\x00')

        pyMeow.w_bytes(process, block3, b'\x8A\x88\xBF\x02\x00\x00\x84\xC9\x74\x1D\x8B\x86\xC0\x06\x00\x00\x8A\x88\x8E\x0C\x00\x00\x84\xC9\x74\x0D\x6A\x01\x8D\x8E\x50\x01\x00\x00\xE8\x3F\x83\x23\x00\x8B\x86\xC0\x06\x00\x00')

        pyMeow.w_bytes(process, block4, b'\x8A\x88\xBF\x02\x00\x00\x84\xC9\x74\x25\x8B\x06\x8B\xCE\xFF\x50\x2C\x83\xF8\x10\x75\x14\x8B\x86\x10\x07\x00\x00\x85\xC0\x74\x0A')

        pyMeow.w_bytes(process, block2, b'\x8A\x88\xC0\x02\x00\x00\x84\xC9\x74\x36\x8B\x16\x8B\xCE\xFF\x52\x2C\x83\xF8\x28\x74\x16\x8B\x06\x8B\xCE')

        pyMeow.w_bytes(process, block1, b'\x8A\x88\xC0\x02\x00\x00\x84\xC9\x74\x27\x8B\x86\xC4\x06\x00\x00\x8A\x88\xCE\x0C\x00\x00\x84\xC9\x75\x17\x8A\x88\x8E\x0C\x00\x00\x84\xC9\x74\x0D\x6A\x01\x8D\x8E\x50\x01\x00\x00\xE8\x18\xAA\x01\x00')
