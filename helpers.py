import re 
  
# function code taken from https://stackoverflow.com/questions/8022530/how-to-check-for-valid-email-address/28982264#28982264


def check(email):
    match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)

    if match:
        return True
    else:
        return False