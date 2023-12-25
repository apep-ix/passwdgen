#!/usr/bin/env python3
import argparse
import secrets
import string
import random

def main():
    parser = argparse.ArgumentParser(prog='passwdgen', description='generate random password')

    parser.add_argument('-l', '--len', type=int, required=True, metavar='', help='total password length must be betwen 6-256 (inclusive)')
    parser.add_argument('-c', '--char', type=int, required=True, metavar='', help='number of characters')
    parser.add_argument('-n', '--num', type=int, required=True, metavar='', help='number of digits')
    parser.add_argument('-s', '--spec', type=int, required=True, metavar='', help='number of special characters')

    args = parser.parse_args()

    if args.len > 256 or args.len < 6:
        raise ValueError('Total password length must be betwen 6-256 (inclusive)')
    elif args.char + args.num + args.spec > args.len or args.char + args.num + args.spec  < args.len:
        raise ValueError('The sum of character set lengths does not match the specified length')
    elif args.char < 0 or args.num < 0 or args.spec < 0:
        raise ValueError('Value must be greater than or equal to 0')
    
    gen_passwd(args.len, args.char, args.num, args.spec)
               
def gen_passwd(l, c, n, s):
    characters = ''.join(secrets.choice(string.ascii_letters) for _ in range(c)) 
    numbers = ''.join(secrets.choice(string.digits) for _ in range(n))
    special = ''.join(secrets.choice(string.punctuation) for _ in range(s))

    passwd_list = [characters, numbers, special]
    secrets.SystemRandom().shuffle(passwd_list)
    passwd = ''.join(passwd_list)
    shuffled_passwd = ''.join(random.sample(passwd, len(passwd)))
    print(f'\nPassword: {shuffled_passwd}')

if __name__ == '__main__':
    main()
