from ReadWriteMemory import ReadWriteMemory
import json

class GameModifier():
    def __init__(self, pname, offsets_path):
        self.pname = pname
        with open(offsets_path, 'r') as file:
            self.data = json.load(file)
        self.rwm = ReadWriteMemory()
        self.process = self.rwm.get_process_by_name(pname)

        # for _, value in self.data.items():
        #     if 'gamemd.exe+' in value['Address']:
        #         offset = value['Address'].replace('gamemd.exe+', '')
        #         print(offset)
        #         print(int(offset, 16))
        #         value['Address'] = hex(0x00400000 + int(offset, 16))
        
        # with open('ad.json', 'w') as file:
        #     self.data = json.dump(self.data, file)

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

if __name__ == '__main__':
    process_name = "gamemd.exe"
    gm = GameModifier(process_name, './ad.json')
    # # print(hex(GetModuleBase(6584, process_name)))
    # while True:
    #     if gm.get('InstantBuild') < 53:
    #         gm.run('InstantBuild', 53)

    # while True:
    #     if gm.get('InstantBuild') != 0 and gm.get('InstantBuild') != 54:
    #         gm.run('InstantBuild', 53)
    # print(gm.get('InstantBuild'))
    # print(0x00905A4D + 0x00683E34)