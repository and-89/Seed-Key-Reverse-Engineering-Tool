Seed & Key Reverse Engineering Tool
This project consists of two separate Python scripts designed for reverse engineering of seed & key DLL files following the ASAM MCD-2 MC (ASAP2) standard and the Communication Control Protocol (CCP). The main purpose of these tools is to facilitate the discovery of the algorithms used within a DLL to generate keys from seeds, which can be particularly useful for automotive security research or as input for AI-driven analysis.

Overview
The project contains two scripts:

Random Key Generator: This script generates random seed values and computes the corresponding keys using the DLL. It serves as a way to quickly sample the behavior of the seed & key algorithm within the DLL.

Brute Force Key Generator: This script systematically generates all possible seed values (brute force method) and computes their corresponding keys. This exhaustive approach ensures no potential seed-key pair is missed, providing comprehensive insight into the DLL's algorithm.

Both scripts output the results into a CSV file with two columns: Seed and Key. This file can be instrumental in analyzing the pattern or logic behind the DLL's algorithm for generating keys from seeds.

Usage
Before running the scripts, ensure you have Python installed on your system and the required DLL file placed in an accessible location.

Random Key Generator:

bash
Copy code
python random_generator.py
Brute Force Key Generator:

bash
Copy code
python bruteforce.py
Output
The scripts generate a CSV file named seed_key_pairs.csv, containing two columns:

Seed: The seed value used to generate the key.
Key: The key generated from the corresponding seed.
This CSV file can aid in identifying the algorithm used within the DLL by providing a dataset that may reveal patterns or directly reflect the algorithm's logic. It's particularly useful for feeding into AI models designed to reverse-engineer such algorithms.

Note
These tools are intended for educational and research purposes to improve security measures and understand automotive protocols. Use them responsibly and ethically according to your local laws and guidelines.

Please adjust the script names (random_generator.py and bruteforce.py) and paths as necessary to match your project structure and filenames.