# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. If the function is passed a valid PIN string, return true, else return false.

# "1234"   -->  true
# "12345"  -->  false
# # "a234"   -->  false


def PINChecker (pin) : 
    validPin = 1234
    if pin == validPin : 
        print('True')
    else : 
        print('False')


PINChecker(1234)