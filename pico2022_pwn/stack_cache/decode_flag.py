flag_leaked = ['0x080c9a04','0x804007d', '0x35373332', '0x38396239', '0x5f597230', '0x6d334d5f','0x50755f4e',
              '0x34656c43', '0x7b465443','0x6f636970','0x80c9a04','0x804007d','0x35373332',
              '0x38396239','0x5f597230','0x6d334d5f', '0x50755f4e','0x34656c43','0x7b465443', '0x6f636970']
flag = b""
for part in flag_leaked:
    part = part[2:] ## remove 0x
    part = bytes.fromhex(part.rjust(8, '0'))
    print(part)
    flag += part
print(flag[::-1])