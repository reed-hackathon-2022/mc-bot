import re
#Gets fed a string an returns True if it contains sensitive info, false otherwise
def sensitiveInfoChecker(MCstring):
    stringBreakdown = MCstring.split()
    #Regex for any kind of formatted phone number
    regChecker = re.compile("(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?")
    numbSplit = re.split(regChecker,MCstring)
    #List of email endings common in MCs, can be modified or added to if needed
    emailList = ["@reed.edu", "@gmail.com"]
    spacednum = re.split("^(?:\s*\d){8}$",MCstring)
    

    #Checks if an email is contained in string
    for x in emailList:
        if any(x in string for string in stringBreakdown):
            return True

    #Checks if a Phone number is contained
    if None in numbSplit:
        return True
    if '' in spacednum:
        return True
    return False

#Debug
"""
print(sensitiveInfoChecker("7654352412 1 324 7768 786868 123-456-7890 finnphill@reed.edu finn@gmail.com"))
print(sensitiveInfoChecker("Hello I like commons food"))
print(sensitiveInfoChecker("1 324 7768"))
print(sensitiveInfoChecker("Hello I like commons@gmail.com"))
print(sensitiveInfoChecker("Hello I like commons food 6666666666"))
"""
