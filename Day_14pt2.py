from itertools import product

filename = 'aoc-14.txt'

def load(infile):
    with open(infile) as f:
        reader = f.readlines()
        masks = [line.replace('\n','').replace('mask = ','') for line in reader if 'mask' in line]
        mems = [line.replace('\n','').replace('mem[', '').replace('] ','').replace(' ','').split('=') if 'mem' in line else 'z' for line in reader]
    return masks, mems


def convert_address(address,mask):
    address = bin(int(address))[2:].zfill(36)

    for i in range(len(mask)):
        address = list(address)
        if mask[i] == '1':
            address[i] = '1'
        if mask[i] == 'X':
            address[i] = 'X'

        address = ''.join(address)

    return address


def get_all_addresses(bitaddress):
    count = list(bitaddress).count('X')
    p = list(product(range(2),repeat=count))
    bitaddress = list(bitaddress)
    all_addresses = []
    new_address = bitaddress[:]
    k = 0

    for i in range(len(p)):
        for j in range(len(bitaddress)):
            if bitaddress[j] == 'X':
                new_address[j] = str(p[i][k])
                k += 1
                if k == len(p[0]):
                    k = 0
        all_addresses.append(''.join(new_address))
    
    return all_addresses


def convert_to_binary_and_back(data):
    masks = data[0] + ['stop']
    addresses = [d[0] for d in data[1] if d != 'z']
    chip_values = {}
    nums = data[1]
    i = 0
    k = 0
    
    while masks[i+1] != 'stop':
        for num in nums[1:]:
            if num != 'z':
                c = convert_address(addresses[k],masks[i])
                a = get_all_addresses(c)

                for x in a:
                    chip_values[x] = int(num[1])
                k += 1

            else:
                i += 1
            
    return sum(chip_values.values())
            
info = load(filename)
print(convert_to_binary_and_back(info))


