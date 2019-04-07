# from https://www.devdungeon.com/content/working-binary-data-python

bytes_ = bytes(4)
print('bytes_', bytes_)
print(type(bytes_))

data = bytes(b'\xFF\xFF')  # b for binary, byte from 0 to 255 in hexadecimal, i.e. FF
print('data', data)

print('')

# Cast bytes to bytearray
mutable_bytes = bytearray(b'\x00\x0F')

# Bytearray allows modification
mutable_bytes[0] = 255
mutable_bytes.append(255)
print('mutable_bytes', mutable_bytes)

# Cast bytearray back to bytes
immutable_bytes = bytes(mutable_bytes)
print('immutable_bytes', immutable_bytes)

print('')

i = 16

# Create one byte from the integer 16
single_byte = i.to_bytes(1, byteorder='big', signed=True)
print(single_byte)

# Create four bytes from the integer
four_bytes = i.to_bytes(4, byteorder='big', signed=True)
print(four_bytes)

# Compare the difference to little endian
print(i.to_bytes(4, byteorder='little', signed=True))

# Create bytes from a list of integers with values from 0-255
bytes_from_list = bytes([255, 254, 253, 252])
print(bytes_from_list)

# base x integer
one_byte = [int('11110000', 2), int('0123456', 7), int('12389abcdef', 16)]
print(one_byte)

# tests

s = b'abcde1234    '  #  asii literals only
print('binary a b space space', s[0], s[1], s[-1], s[-2])
