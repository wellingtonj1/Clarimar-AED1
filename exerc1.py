import matplotlib.pyplot as plt

# calculate how many bytes of storage are used by a image with 512 width and 512 height from 2 to 16 bits
width = 512
height = 512
dp_bits = 2

size = width * height
storage_size = []
arr_dp_bits = []

while dp_bits < 17:
    pieces = size * dp_bits
    storage_size.append(pieces/8)
    arr_dp_bits.append(dp_bits)
    dp_bits += 1
    print(pieces/8)
    print('\n\n')

# plot on graphic the storage size from 2 to 16 bits
plt.plot(arr_dp_bits, storage_size)
plt.ylabel('Storage size in bytes')
plt.xlabel('Bits')
plt.show()

print(storage_size)
