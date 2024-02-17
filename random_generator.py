import csv
import ctypes
from ctypes import c_ubyte, c_ulong, byref
from random import randint

# Loading DLL
dll = ctypes.CDLL('path_to_dll')

# Setting up function prototype
ASAP1A_CCP_ComputeKeyFromSeed = dll.ASAP1A_CCP_ComputeKeyFromSeed
ASAP1A_CCP_ComputeKeyFromSeed.argtypes = [
    ctypes.POINTER(c_ubyte),  # pointer to the seed array
    ctypes.c_ulong,           # length of the seed array
    ctypes.POINTER(c_ubyte),  # pointer to the buffer for the key
    ctypes.c_ulong,           # maximum length of the key buffer
    ctypes.POINTER(c_ulong)   # pointer to the actual length of the generated key
]
ASAP1A_CCP_ComputeKeyFromSeed.restype = ctypes.c_int  # assuming the function returns int as status

def brute_force_seed_key(csv_filename, num_iterations):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Seed', 'Key']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_iterations):
            # Generating random seed
            seed_value = [randint(0, 255) for _ in range(4)]
            seed_array = (c_ubyte * 4)(*seed_value)
            key_array = (c_ubyte * 4)()
            key_length = c_ulong(0)

            # Calling the DLL function
            result = ASAP1A_CCP_ComputeKeyFromSeed(seed_array, len(seed_array), key_array, len(key_array), byref(key_length))
            if result == 1:  # assuming the function returns 1 as success
                seed_hex = ''.join(f"{b:02X}" for b in seed_array)
                key_hex = ''.join(f"{b:02X}" for b in key_array[:key_length.value])
                writer.writerow({'Seed': seed_hex, 'Key': key_hex})

csv_file_path = 'seed_key_pairs.csv'
brute_force_seed_key(csv_file_path, 1000)  # Number of iterations can be changed as needed
