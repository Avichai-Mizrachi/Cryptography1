def initialize_sbox(sbox, key, key_length):
    # Initialize the S-box with values from 0 to 255
    for i in range(256):
        sbox[i] = i

    # Shuffle the S-box values using the key
    j = 0
    for i in range(256):
        # Calculate the index to swap with
        j = (j + sbox[i] + key[i % key_length]) % 256
        # Swap the values at indices i and j
        sbox[i], sbox[j] = sbox[j], sbox[i]


def rc4_encrypt(input_bytes, key):
    # Initialize the S-box using the provided key
    sbox = list(range(256))
    key_length = len(key)
    initialize_sbox(sbox, key, key_length)

    i, j = 0, 0
    output = bytearray()

    # Generate the keystream and perform XOR with the input to get the ciphertext
    for byte in input_bytes:
        i = (i + 1) % 256
        j = (j + sbox[i]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]

        t = (sbox[i] + sbox[j]) % 256
        encrypted_byte = byte ^ sbox[t]
        output.append(encrypted_byte)

    return output


# Example quote
input_bytes = b'No place is too far, no task is too difficult - Golani forever'

# Example key
key = b'AVI'

encrypted_data = rc4_encrypt(input_bytes, key)

print(encrypted_data)
print("\nCreating key...\n")
print(encrypted_data.hex())
print("\nKey created.\n")