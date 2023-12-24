# passwdgen

passwdgen is a simple command-line tool for generating random passwords with customizable length, characters, digits, and special characters.

## Usage


python passwdgen.py -l -c -n -s 

# Arguments

    -l: total length of the password must be between 6-256 inclusive (required).
    -c: number of characters in the password (use 0 for no characters) (required).
    -n: number of digits in the password (use 0 for no digits) (required).
    -s: number of special characters in the password (use 0 for no special ch) (required).
    
# Examples

Generate a 12-character password, including 4 characters, 6 digits, and 2 special characters:


python passwdgen.py -l 12 -c 4 -n 6 -s 2

Generate a password with only characters (no digits or special characters):


python passwdgen.py -l 8 -c 8 -n 0 -s 0


