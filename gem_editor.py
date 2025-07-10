import os

offsets = {
    0x5EC4: "Sonic Light Dash",
    0x5EC8: "Sonic Anti-Gravity",
    0x5ECC: "Sonic Bound Bracelet",
    0x5ED0: "Sonic Unused Bracelet",
    0x5ED4: "Sonic Green Gem",
    0x5ED8: "Sonic Red Gem",
    0x5EDC: "Sonic Blue Gem",
    0x5EE0: "Sonic White Gem",
    0x5EE4: "Sonic Sky Gem",
    0x5EE8: "Sonic Yellow Gem",
    0x5EEC: "Sonic Purple Gem",
    0x5EF0: "Sonic Rainbow Gem",
}

name_to_offset = {v: k for k, v in offsets.items()}

def read_gem_status(filename):
    with open(filename, 'rb') as file:
        data = file.read()
        result = {}
        for offset, name in offsets.items():
            result[name] = (data[offset] == 1)
        return result
    
def write_gem_status(filename, changes: dict):
    with open(filename, 'rb') as file:
        data = bytearray(file.read())

    for name, state in changes.items():
        if name in name_to_offset:
            data[name_to_offset[name]] = 0x01 if state else 0x00

    new_filename = f"{os.path.splitext(filename)[0]}_modificado.bin"
    with open(new_filename, 'wb') as new_file:
        new_file.write(data)

    return new_filename
