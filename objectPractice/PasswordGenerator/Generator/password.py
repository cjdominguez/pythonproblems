"""
    This is what this does

    The secrets module is used for generating cryptographically
    strong random numbers suitable for managing data such as
    passwords, account authentication, security tokens,and related
    secrets.

    In particular, secrets should be used in preference to the
    default pseudo-random number generator in the random module,
    which is designed for modelling and simulation, not security
    or cryptography.

"""

import string
import secrets

class Passwd:

    def __init__(self, user_length):
        self.user_length = user_length

    def password(self):
        alphabet_1 = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet_1) for i in range(self.user_length))
        return(password)


user_tim = Passwd(32)
print(user_tim.password())
