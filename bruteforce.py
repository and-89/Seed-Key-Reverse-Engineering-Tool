import csv
import ctypes
from ctypes import c_ubyte, c_ulong, c_int, POINTER, byref

# Loading DLL
dll = ctypes.CDLL('path_to_dll')

# Setting up function prototype
ASAP1A_CCP_ComputeKeyFromSeed = dll.ASAP1A_CCP_ComputeKeyFromSeed
ASAP1A_CCP_ComputeKeyFromSeed.argtypes = [
    POINTER(c_ubyte), c_ulong,
    POINTER(c_ubyte), c_ulong,
    POINTER(c_ulong)
]
ASAP1A_CCP_ComputeKeyFromSeed.restype = c_int

def brute_force_seed_key(csv_filename, max_iterations, max_results):
    results_count = 0
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Seed', 'Key']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for seed_value in range(max_iterations):
            if results_count >= max_results:
                break  # End if the maximum number of results has been reached

            # Generating consecutive seeds
            seed_array = (c_ubyte * 4)(*seed_value.to_bytes(4, byteorder='big'))
            key_array = (c_ubyte * 4)()
            key_length = c_ulong(0)

            # Calling the DLL function
            if dll.ASAP1A_CCP_ComputeKeyFromSeed(seed_array, 4, key_array, 4, byref(key_length)):
                seed_hex = ''.join(f"{b:02X}" for b in seed_array)
                key_hex = ''.join(f"{b:02X}" for b in key_array[:key_length.value])
                writer.writerow({'Seed': seed_hex, 'Key': key_hex})
                results_count += 1

                # Updating progress in the same line
                progress = (results_count / max_results) * 100
                print(f"\rProgress: {progress:.2f}% ({results_count}/{max_results} results)", end='', flush=True)

        print()  # Adds a new line at the end, so the next output is not on the same line

csv_file_path = 'seed_key_pairs.csv'
max_iterations = 0xFFFFFFFF  # Maximum number of iterations
max_results = 4294967  # Maximum number of results 4294967296
brute_force_seed_key(csv_file_path, max_iterations, max_results)
