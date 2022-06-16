"""
    basic class script to test for future password generator
    project, this class returns a password using the secrets
    and string modules

    The secrets module is used for generating cryptographically
    strong random numbers suitable for managing data such as
    passwords, account authentication, security tokens,and related
    secrets.

    In particular, secrets should be used in preference to the
    default pseudo-random number generator in the random module,
    which is designed for modelling and simulation, not security
    or cryptography.

    The string module provides th euser with a plethora of options
    for different ASCII characters

"""

import string
import secrets

class Passwd:

    def __init__(self, user_length = None):
        self.user_length = user_length

    def password(self):

        """
        string.printable # string will have the follwoing ascii letters to pull from String of ASCII
        characters which are considered printable. This is a combination of digits, ascii_letters,
        punctuation, and whitespace but the white space is upredictable so I left the abilty to use
        either.

        I prefer to use alphabet_1

        constiting of the following:
        0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

        """

        #alphabet_0 = string.printable     # string will have the follwoing ascii letters to pull from String of ASCII characters which are considered printable. This is a combination of digits, ascii_letters, punctuation, and whitespace 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        alphabet_1 = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet_1) for i in range(self.user_length))
        return(password)


#user_lengthy = int(input("Input how many numbers you want in your password: "))
user_tim = Passwd()
user_tim.user_length = 32
print(user_tim.password())
