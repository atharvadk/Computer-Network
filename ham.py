def calculate_parity(data):
    """Calculates parity bits for Hamming Code."""
    data[4] = data[5] ^ data[6] ^ data[7]
    data[2] = data[3] ^ data[6] ^ data[7]
    data[1] = data[3] ^ data[5] ^ data[7]

def detect_and_correct(dataatrec):
    """Detects and corrects errors in the received data."""
    c1 = dataatrec[1] ^ dataatrec[3] ^ dataatrec[5] ^ dataatrec[7]
    c2 = dataatrec[2] ^ dataatrec[3] ^ dataatrec[6] ^ dataatrec[7]
    c3 = dataatrec[4] ^ dataatrec[5] ^ dataatrec[6] ^ dataatrec[7]
    c = c3 * 4 + c2 * 2 + c1

    if c == 0:
        print("Congratulations! There is no error in the received data.")
    else:
        print(f"Error detected at position: {c}")
        dataatrec[c] ^= 1  # Correct the error
        print(f"Corrected message is: {''.join(map(str, dataatrec[1:]))}")

def main_hamming():
    # Input 4 bits of data
    data = [0] * 8
    print("Enter 4 bits of data one by one:")
    data[7] = int(input())
    data[6] = int(input())
    data[5] = int(input())
    data[3] = int(input())

    # Calculate parity bits
    calculate_parity(data)
    print(f"\nEncoded data is: {''.join(map(str, data[1:]))}")

    # Receive data bits
    dataatrec = [0] * 8
    print("\nEnter received data bits one by one:")
    for i in range(1, 8):
        dataatrec[i] = int(input())

    # Detect and correct errors
    detect_and_correct(dataatrec)

if __name__ == "__main__":
    main_hamming()
