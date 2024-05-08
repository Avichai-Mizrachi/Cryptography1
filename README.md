# RC4 Encryption and Decryption Tool

## Overview

This project provides Python scripts for encrypting and decrypting messages using the RC4 algorithm. The `RC4.py` script implements the RC4 encryption algorithm, while `RC4_attacker.py` is used to perform a brute-force attack on RC4-encrypted ciphertext.

## Requirements

- Python 3.x

## Usage

### Encryption (RC4.py)

To encrypt plaintext using RC4, execute the `RC4.py` script. Provide the plaintext message and encryption key as input when prompted. The script will output the encrypted ciphertext.

### Decryption (RC4_attacker.py)

To decrypt ciphertext encrypted with RC4, execute the `RC4_attacker.py` script. This script performs a brute-force attack to decrypt the ciphertext. Provide the encrypted ciphertext as input when prompted. The script will attempt to decrypt the ciphertext using all possible keys.

## Usage Notes

- Before running the decryption script (`RC4_attacker.py`), ensure that you have the ciphertext and the key length used for encryption.
- The encryption script (`RC4.py`) prompts the user to input the plaintext message and encryption key interactively.

## File Descriptions

- `RC4.py`: Contains functions for RC4 encryption.
- `RC4_attacker.py`: Implements a brute-force attack to decrypt RC4-encrypted ciphertext.
- `README.md`: This file, providing information about the project.

## Author  

- Avichai Mizrachi