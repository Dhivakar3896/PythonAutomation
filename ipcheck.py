def validate_ip(octet):
    octet = octet.split('.')
    if len(octet) != 4:
        return False
    for i in octet:
        if not i.isdigit():
            return False
        i = int(i)
        if i < 0 or i > 255:
            return False
    return True

def main():
    octet = input("Enter IP address: ")
    if validate_ip(octet):
        print("Valid IP")
    else:
        print("Invalid IP")

if __name__ == '__main__':
    main()
