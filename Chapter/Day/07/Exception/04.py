import re


def validate_email(email):
    """ Test if an email is of a valid format """

    if type(email) is not str:
        raise Exception('Email is not a String')

    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if not re.search(regex, email):
        raise Exception('Email is Malformed')

    return True


# email_address = 'hello@udacity.com'
email_address = 1
try:
    if validate_email(email_address):
        print("Great Email")
except Exception as e:
    print("Excetion : {}".format(e))
    if str(e) == "Email is not a String":
        print("BAD EMAIL")
