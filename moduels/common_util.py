def chk_mailId(mail_id):

    """the purpose is to check the validity of the email id"""

    status =""
    if (mail_id.endswith("@gmail.com",2)):
        status = "valid mail id"
    else:
        status = "Invalid mail id"
    return (status, mail_id)

def welcome_user(user):
    return ("Hello "+ user + "!!! - welcome to Python programming")