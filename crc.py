def xor_operation(dividend, divisor):
    """Performs XOR operation between dividend and divisor."""
    for i in range(len(divisor)):
        dividend[i] = 0 if dividend[i] == divisor[i] else 1

def crc_sender(frame, generator):
    """Sender side for CRC calculation."""
    frame_size = len(frame)
    generator_size = len(generator)
    remainder_size = generator_size - 1

    # Append zeros to the frame
    padded_frame = frame + [0] * remainder_size
    temp = padded_frame[:]

    # Perform division using XOR
    for i in range(frame_size):
        if temp[i] == 1:  # If the bit is 1, perform XOR
            xor_operation(temp[i:i + generator_size], generator)

    # Extract the CRC bits
    crc = temp[frame_size:]
    return crc

def crc_receiver(received_frame, generator):
    """Receiver side to verify CRC."""
    frame_size = len(received_frame) - (len(generator) - 1)
    generator_size = len(generator)
    temp = received_frame[:]

    # Perform division using XOR
    for i in range(frame_size):
        if temp[i] == 1:  # If the bit is 1, perform XOR
            xor_operation(temp[i:i + generator_size], generator)

    # Extract the remainder
    remainder = temp[frame_size:]
    return remainder

def main_crc():
    # Input Frame and Generator
    frame = list(map(int, input("Enter the Frame (space-separated bits): ").split()))
    generator = list(map(int, input("Enter the Generator (space-separated bits): ").split()))

    print("\nSender Side:")
    print(f"Frame: {''.join(map(str, frame))}")
    print(f"Generator: {''.join(map(str, generator))}")

    # Calculate CRC
    crc = crc_sender(frame, generator)
    print(f"CRC bits: {''.join(map(str, crc))}")

    # Transmitted Frame
    transmitted_frame = frame + crc
    print(f"Transmitted Frame: {''.join(map(str, transmitted_frame))}")

    # Input the received frame
    received_frame = list(map(int, input("\nEnter the Received Frame (space-separated bits): ").split()))

    print("\nReceiver Side:")
    print(f"Received Frame: {''.join(map(str, received_frame))}")

    # Verify the CRC at the receiver
    remainder = crc_receiver(received_frame, generator)
    print(f"Remainder: {''.join(map(str, remainder))}")

    if all(bit == 0 for bit in remainder):
        print("Since Remainder is 0, the message is correct.")
    else:
        print("Since Remainder is not 0, the message contains errors.")

if __name__ == "__main__":
    main_crc()
