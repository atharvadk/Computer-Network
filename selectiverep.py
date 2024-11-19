import random
import time
import sys

def send_frame(frame_number):
    print(f"Sending Frame {frame_number}...")
    return random.randint(0, 1)  

def selective_repeat(window_size, total_frames):
    ack = [-1] * total_frames  
    current_frame = 0
    total_transmissions = 0

    while current_frame < total_frames:
        for i in range(window_size):
            if current_frame + i < total_frames:
                if ack[current_frame + i] == -1:
                    ack_status = send_frame(current_frame + i + 1)
                    total_transmissions += 1

                    if ack_status == 0:
                        print(f"Acknowledgment received for Frame {current_frame + i + 1}")
                        ack[current_frame + i] = 1
                    else:
                        print(f"Frame {current_frame + i + 1} lost, will retransmit later")

        while current_frame < total_frames and ack[current_frame] == 1:
            current_frame += 1

        print("\n")

    print(f"Total number of frames which were sent and resent: {total_transmissions}")

def main():
    random.seed(time.time())
    total_frames = int(input("Enter the Total number of frames: "))
    window_size = int(input("Enter the Window Size: "))

    selective_repeat(window_size, total_frames)

def exit_on_key_press():
    input("Press any key to exit...")
    sys.exit()

if __name__ == "__main__":
    main()
    exit_on_key_press()

