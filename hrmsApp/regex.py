import re
#Username validation
def validate_username(username):
    return re.match(r'^[a-z0-9]+([._]?[a-z0-9]+)*@[a-z0-9]+([.-]?[a-z0-9]+)*\.[a-z]{2,}$', username) is not None

#Password validation
def validate_password(password):
    return re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password) is not None

#Email Validation
def validate_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None

#Contact number validation
def validate_phone(phone):
    return re.match(r'^(\+91[\-\s]?)?[0]?(91)?[6789]\d{9}$', phone) is not None
