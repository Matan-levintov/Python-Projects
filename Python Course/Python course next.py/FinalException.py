import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, index, char):
        self.index = index
        self.char = char

    def __str__(self):
        return f'Username containts an illegal character "{self.char}" at index {self.index} '


class UserNameTooShort(Exception):
    def __str__(self):
        return "Username has less than 3 chars thus it's too short"


class UserNameTooLong(Exception):
    def __str__(self):
        return "Username has more than 16 chars, thus its too long"


class PasswordMissingChars(Exception):
    def __str__(self):
        return "Password does not contain atleast one of the mandatory characters"


class PasswordUpperCase(PasswordMissingChars):
    def __str__(self):

        # forgot the () after the __str__ that's why it didn't work, __str__ is a function that's why it needs() after it to be called
        return f"{PasswordMissingChars.__str__(self)} (Upper)"


class PasswordLowerCase(PasswordMissingChars):
    def __str__(self):
        return f"{super().__str__(self)} (Lower)"


class PasswordDigit(PasswordMissingChars):
    def __str__(self):
        return f"{super().__str__(self)} (Digit)"


class PasswordSpecial(PasswordMissingChars):
    def __str__(self):
        return f"{super().__str__(self)} (Special)"


class PasswordTooShort(Exception):
    def __str__(self):
        return "Password has less than 8 characters, thus its too short"


class PasswordTooLong(Exception):
    def __str__(self):
        return "Password has more than 40 characters, thus its too long"


def checks_if_has_lower_letters(password):
    for char in password:
        if char in string.ascii_lowercase:
            return True
    return False


def checks_if_has_digits(password):
    for char in password:
        if char in string.digits:
            return True
    return False


def checks_if_has_special_char(password):
    for char in password:
        if char in string.punctuation:
            return True
    return False


def checks_if_has_cap_letters(password):
    for char in password:
        if char in string.ascii_uppercase:
            return True
    return False


def check_input(username, password):
    # checking username
    # ----------------------------------------------------------------
    # making a list of all the valid characters
    list_of_valid_chars = list(string.ascii_letters+string.digits+'_')
    if len(username) < 3:
        raise UserNameTooShort
    elif len(username) > 16:
        raise UserNameTooLong
    for index, char in enumerate(username):
        if char not in list_of_valid_chars:
            raise UsernameContainsIllegalCharacter(index, char)
    # ----------------------------------------------------------------
    # checking password
    if len(password) < 7:
        raise PasswordTooShort
    elif len(password) > 41:
        raise PasswordTooLong
    # if checks_if_has_lower_letters(password) and checks_if_has_cap_letters(password) and checks_if_has_digits(password) and checks_if_has_special_char(password):
    #     pass
    # else:
    #     raise PasswordMissingChars
    if checks_if_has_lower_letters(password):
        if checks_if_has_cap_letters(password):
            if checks_if_has_digits(password):
                if checks_if_has_special_char(password):
                    pass
                else:
                    raise PasswordSpecial
            else:
                raise PasswordDigit
        else:
            raise PasswordUpperCase
    else:
        raise PasswordLowerCase
    print('Ok')  # prints ok only if no errors occured


# check_input("1", "2")
# check_input("0123456789ABCDEFG", "2")
# check_input("A_a1.", "12345678")
# check_input("A_1", "2")
# check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
# check_input("A_1", "abcdefghijklmnop")
# check_input("A_1", "ABCDEFGHIJLKMNOP")
# check_input("A_1", "ABCDEFGhijklmnop")
# check_input("A_1", "4BCD3F6h1jk1mn0p")
# check_input("A_1", "4BCD3F6.1jk1mn0p")

def main():
    while True:
        try:
            username = input('enter your username ')
            password = input('enter your password ')
            check_input(username, password)
        except Exception as e:
            print(e)  # print calls under the hood the __str__ attribute


if __name__ == "__main__":
    main()
