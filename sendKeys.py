#!/usr/bin/env python3

import time

NULL_CHAR = chr(0)


KEY_RIGHT = 79
KEY_LEFT = 80
KEY_DOWN = 81
KEY_UP = 82

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        time.sleep(0.8)
        print(report)
        fd.write(report.encode())
        return

    print("returning")
    
print("waiting to send keys")
time.sleep(1)
print("sending keys")

# H (press shift and H)
# write_report(chr(32)+NULL_CHAR+chr(11)+NULL_CHAR*5)

# e

write_report(NULL_CHAR*2+chr(KEY_RIGHT)+NULL_CHAR*5)
write_report(NULL_CHAR*2+chr(KEY_LEFT)+NULL_CHAR*5)
write_report(NULL_CHAR*2+chr(KEY_DOWN)+NULL_CHAR*5)
write_report(NULL_CHAR*2+chr(KEY_UP)+NULL_CHAR*5)
write_report(NULL_CHAR*2+chr(KEY_UP)+chr(KEY_DOWN)+NULL_CHAR*4)


write_report(NULL_CHAR*8)

# ll
# write_report(NULL_CHAR*2+chr(15)+NULL_CHAR*5)
# write_report(NULL_CHAR*8)
# write_report(NULL_CHAR*2+chr(15)+NULL_CHAR*5)

# o
# write_report(NULL_CHAR*2+chr(18)+NULL_CHAR*5)

# SPACE
# write_report(NULL_CHAR*2+chr(44)+NULL_CHAR*5)

# W (press shift and W)
# write_report(chr(32)+NULL_CHAR+chr(26)+NULL_CHAR*5)

# o
# write_report(NULL_CHAR*2+chr(18)+NULL_CHAR*5)

# r
# write_report(NULL_CHAR*2+chr(21)+NULL_CHAR*5)

# l
# write_report(NULL_CHAR*2+chr(15)+NULL_CHAR*5)

# d
# write_report(NULL_CHAR*2+chr(7)+NULL_CHAR*5)

# ! (press shift and 1)
# write_report(chr(32)+NULL_CHAR+chr(30)+NULL_CHAR*5)

# Release all keys
