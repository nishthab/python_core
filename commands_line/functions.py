# Functions

def chk_mailId(mail_id):

    "the purpose is to check the validity of the email id"
    status =""
    if (mail_id.endswith("@gmail.com",2)):
        status = "valid mail id"
    else:
        status = "Invalid mail id"
    return (status, mail_id)


status,email = chk_mailId("nishtha@gmail.com")
print(status, email)
print(chk_mailId("nishtha@gmail.com"))

print("chk_mailId-->",chk_mailId.__doc__)

def display_all(*locations, **detalis):
    print("locations->",locations)
    print("Details->",detalis)

display_all('Germany', 'Delhi','Hyderabad',name='Nishtha',)