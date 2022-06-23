import re


class gellany_email_validator():

                 def __init__(self, email = None):

                             self.email = email

                 def main(self):
        
                             #1st - validation regex as email 
                             
                             a = re.search(r'[a-zA-Z][\w\.-]*@[a-zA-Z]*\.[a-zA-Z]{1,3}', self.email)
                             print(a)
                             if bool(a):
                                 print(self.email)
                                 #2nd - grep regex before and after @ 
                                 username = email[:self.email.index('@')]
                                 domain = self.email[self.email.index('@') + 1:]

                                 print(f"Your username is {username} & domain is {domain}")

                             else:
                                 print(f"{self.email} is not valid email name or domain, please check your email again")



email = 'test123!@gmail.com'

gellany_email_validator(email = email).main()