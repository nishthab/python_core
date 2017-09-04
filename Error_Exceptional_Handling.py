# Exceptional Handling

try:
    num = 1/1
    print("string")
    print( 5 +3)
except ZeroDivisionError as ze:
    print(ze)
except (NameError,TypeError) as ne: # common Exceptional handler
    print("Handle two Exception", ne)

except Exception as e: # Exception is the super class IT is nothing but generic exception handling
    print("Error Occured!!!", e)
    print("Exception Name-->", e.__class__.__name__)
else:
    print("No Exception")
finally:
    print("Always Executed")

print("After Division")
print("-------------------------------------------------------")

# User Define Exception
class InvalidEmailId(Exception):
    error_msg = "User has entered and invalid email id"

try:
    mail_id = input("Enter the email_id")
    if(mail_id.endswith("@gmail.com",2)):
        print("Invalid mail_id",mail_id)
    else:
        raise InvalidEmailId

except InvalidEmailId as inv:
    print("User enter wronge mail id", inv.error_msg)
else:
    print("there is no error")



print("------------------------------------------------")

for num in range(11):
    print("Numbdr is:--",num)
    assert num < 9, "num has to be leser than 9"

print("--------------------------------------------------")