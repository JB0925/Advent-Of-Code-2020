filename = 'aoc-14.txt'

def load(infile):
    with open(infile) as f:
        reader = f.readlines()
        masks = [line.replace('\n','').replace('mask = ','') for line in reader if 'mask' in line]
        mems = [line.replace('\n','').replace('mem[', '').replace('] ','').replace(' ','').split('=') if 'mem' in line else 'z' for line in reader]
    return masks, mems


def convert_to_binary_and_back(data):
    masks = data[0] + ['stop']
    addresses = [d[0] for d in data[1] if d != 'z']
    chip_values = dict(zip(addresses, list(range(len(addresses)))))
    nums = data[1]
    i = 0
    
    while masks[i+1] != 'stop':
        for num in nums[1:]:
            if num != 'z':
                value = bin(int(num[1]))[2:].zfill(36)
                value = list(value)
                for j in range(len(masks[i])):
                    if masks[i][j].isnumeric() and masks[i][j] == '1' and value[j] == '0':
                        value[j] = '1'
                    if masks[i][j].isnumeric() and masks[i][j] == '0' and value[j] == '1':
                        value[j] = '0'
                value = int(''.join(value),2)
                values[num[0]] = value
            else:
                i += 1
            
    
    return sum(values.values())
                

info = load(filename)
print(convert_to_binary_and_back(info))





    

        