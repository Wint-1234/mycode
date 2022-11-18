#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
successful = 0 # total times we see pattern, "-] Authorization failed"

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            print(f"IP address of user with failed login = {line.split()[-1]}")
            loginfail += 1 
        else:
            successful += 1

# display the number of failed log in attempts
print("The number of failed log in attempts is", loginfail)

# display the number of successful log in attempts
print("The number of successful log ins is", successful)

