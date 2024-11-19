import ipaddress

def print_binary(n):
    """Convert a number to its 8-bit binary representation."""
    return ''.join(str((n >> i) & 1) for i in range(7, -1, -1))

def calculate_subnet_mask(prefix):
    """Calculate and display the subnet mask for a given CIDR prefix."""
    mask = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF
    mask_bytes = [(mask >> i) & 0xFF for i in (24, 16, 8, 0)]
    
    print(f"Subnet Mask (CIDR /{prefix}): {'.'.join(map(str, mask_bytes))}")
    print("Binary representation: " + ".".join(print_binary(byte) for byte in mask_bytes))

def calculate_network_address(ip, prefix):
    """Calculate and display the network address for an IP and CIDR prefix."""
    network = ipaddress.IPv4Network(f"{ip}/{prefix}", strict=False)
    print(f"Network Address: {network.network_address}")

def main():
    """Main program to demonstrate subnetting."""
    ip = input("Enter an IP address (e.g., 192.168.1.1): ")
    try:
        prefix = int(input("Enter the CIDR prefix (e.g., 24): "))
    except ValueError:
        print("Invalid prefix. CIDR prefix should be an integer.")
        return
    
    if prefix < 0 or prefix > 32:
        print("Invalid prefix. CIDR prefix should be between 0 and 32.")
        return

    # Display the subnet mask for the given CIDR prefix
    calculate_subnet_mask(prefix)

    # Display the network address for the given IP and subnet mask
    calculate_network_address(ip, prefix)

if __name__ == "__main__":
    main()
