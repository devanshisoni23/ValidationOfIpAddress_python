import socket

def validate(ip):
    # binary IP address without dots
    if len(ip) == 32 and all(char in '01' for char in ip):
        binary_parts = [ip[i:i+8] for i in range(0, 32, 8)]
        ip = '.'.join(binary_parts)
        print(f"Converted to binary format with dots: {ip}")

    # decimal IP address without dots
    elif len(ip) == 12 and ip.isdigit():
        decimal_parts = [ip[i:i+3] for i in range(0, 12, 3)]
        ip = '.'.join(decimal_parts)
        print(f"Converted to decimal format with dots: {ip}")

    # Validation of IP address
    parts = ip.split('.') 
    if len(parts) == 4:
        binary_valid = True
        for part in parts:
            if len(part) != 8 or not all(char in '01' for char in part):
                binary_valid = False
                break
        if binary_valid:
            decimal_parts = []
            for part in parts:
                decimal_parts.append(str(int(part, 2)))
            decimal_ip = '.'.join(decimal_parts)
            return f"Valid binary IP address.\nConverted to decimal: {decimal_ip}"

        # Validate decimal IP
        decimal_valid = True
        for part in parts:
            if not part.isdigit() or not (0 <= int(part) <= 255):
                decimal_valid = False
                break

        if decimal_valid:
            return f"Valid decimal IP address: {ip}"

    return f"The entered IP address '{ip}' is invalid."


def is_ip_reachable(ip):
    try:
        socket.create_connection((ip, 80), timeout=5)
        return True
    except socket.error:
        return False


def check_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return f"The IP {ip} resolves to hostname: {hostname}"
    except socket.herror:
        return f"The IP {ip} does not resolve to any hostname."


def validate_with_socket(ip):
    validation_result = validate(ip)
    print(validation_result)

    if "Valid decimal IP address" in validation_result:
        reachable = is_ip_reachable(ip)
        print(f"Reachability: {'Reachable' if reachable else 'Not Reachable'}")

        hostname_result = check_hostname(ip)
        print(hostname_result)

    return "Validation completed."



def main_menu():
    while True:
        print("\n--- IP Validation Tool ---")
        print("1. Validate an IP Address")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            ip = input("Enter an IP address: ")
            print(validate_with_socket(ip))
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



main_menu()
