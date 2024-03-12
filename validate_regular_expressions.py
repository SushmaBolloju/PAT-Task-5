import re

def validate_email(email):
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' # Regular expression for email validation
    
    regex = re.compile(pattern) # Compiling the pattern
    
   
    if regex.match(email): # Matching the email against the pattern
        print("Given input %s is a valid email" %email)
    else:
        print("Given input %s is not valid email" %email)


def validate_bangladesh_mobile_number(number):
    
    pattern = r'^01[3-9]\d{8}$'# Regular expression for Bangladeshi mobile numbers
    
    regex = re.compile(pattern) # Compiling the pattern
    
    if regex.match(number):# Match the number against the pattern
        print("Given input %s is a valid Bangladesh mobile number" %number)
    else:
        print("Given input %s is not a valid Bangladesh mobile number" %number)


def validate_usa_telephone_number(number):
  
    pattern = r'^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})$'  # Regular expression for US telephone numbers
    
    regex = re.compile(pattern)# Compiling the pattern
    
    if regex.match(number):# Match the number against the pattern
        print("Given input %s is a valid US telephone number" %number)
    else:
        print("Given input %s is not a valid US telephone number" %number)


def validate_password(password):
    # Regular expression for the password validation
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    
    # Compile the pattern
    regex = re.compile(pattern)
    
    # Match the password against the pattern
    if regex.match(password):
        print("Given input %s is a valid password." %password)
    else:
        print("Given input %s is not a valid password." %password)


#Passing input to validation methods and checking if valid.
 
 #validating emails
validate_email("sushma@gmail.com")
validate_email("sushmagmail.com")
validate_email("sushma@gmailcom")

 #validating Bangladesh phone numbers
validate_bangladesh_mobile_number("01716997895")
validate_bangladesh_mobile_number("01716997895666")

 #validating US phone numbers
validate_usa_telephone_number("234-789-7654")
validate_usa_telephone_number("234-7898-7654")
validate_usa_telephone_number("234-789-76545")

 #validating password strings
validate_password("Sushma@1grt56723")
validate_password("Sushma1grt56723")
validate_password("Sushma@grt")