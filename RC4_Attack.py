import threading
import queue
import math
import time

KEY_LENGTH = 3
MAX_QUEUE_SIZE = math.pow(2, KEY_LENGTH * 8)
NUM_THREADS = 4  # Youc can adjust based on your environment


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


def rc4_decrypt(input_bytes, key):
    # Convert input_bytes from hexadecimal string to bytes
    bytes_result = bytes.fromhex(input_bytes)

    # Initialize the S-box using the provided key
    sbox = list(range(256))
    key_length = len(key)
    initialize_sbox(sbox, key, key_length)

    # Perform RC4 decryption
    output = bytearray()
    i, j = 0, 0
    for char in bytes_result:
        i = (i + 1) % 256
        j = (j + sbox[i]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]
        decrypted_byte = char ^ sbox[(sbox[i] + sbox[j]) % 256]
        output.append(decrypted_byte)

    return bytes(output)


# Function to convert a long integer to a byte array
def long_to_bytes(num):
    return num.to_bytes(KEY_LENGTH, 'little')


def brute_force_thread(queue, ciphertext):
    while True:
        num = queue.get()
        if num == -1:
            break  # Exit condition

        key = num.to_bytes(KEY_LENGTH, 'little')
        decrypted_text = rc4_decrypt(ciphertext, key)

        if is_printable(decrypted_text):
            decrypted_str = decrypted_text.decode()
            if decrypted_str == "No place is too far, no task is too difficult - Golani forever":
                print(f"Decrypted text with key {key}: {decrypted_str}")
                end_time = time.time()
                print("Time in seconds:", end_time - start_time)

        queue.task_done()


def is_printable(text):
    return all(32 <= c < 127 for c in text)


def main():
    global start_time
    start_time = time.time()
    print("Starting...")

    # Example ciphertext (as bytes for simplicity)
    ciphertext = "977853879f9f1ace694fed96fe72667b4313688e987d4241940b74543ca8396f816aaeef61e78d5eefac5364ac4108735f36327692b7f3d7bc732daf9560"

    # Setting up queue
    q = queue.Queue(maxsize=MAX_QUEUE_SIZE)

    # Starting worker threads
    threads = [threading.Thread(target=brute_force_thread, args=(q, ciphertext)) for _ in range(NUM_THREADS)]
    for t in threads:
        t.start()

    # Enqueue tasks
    bits = 8 * KEY_LENGTH
    limit = 1 << bits
    counter, count = 100000000, 150000
    for num in range(limit):
        q.put(num)
        if num == count:
            print("Working...")
        if num == counter:
            print(counter)
            counter += 100000000

    # Signal no more tasks
    for _ in range(NUM_THREADS):
        q.put(-1)

    # Wait for all tasks to be completed
    q.join()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("Done.")


if __name__ == "__main__":
    main()