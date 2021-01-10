# Python projct on Cloudxlab course
# Python project - Churn Emails
# i have used the cloudxlab dataset
# and solved the problem on cloudxlab jupytr account



# project part 1
# Count the numbers of lines



# Define a function number_of_lines
# Open the file mbox-short.txt which is located at /cxldata/datasets/project/mbox-short.txt
# Read the file into one string by using read method on file handle
# Write logic to count the number of lines
# Return the count of the number of lines


def num_of_lines():
        fhand = open('/cxldata/datasets/project/mbox-short.txt')
        inp = fhand.read()
        fhand.close()
        count = 0
        for c in inp:
            if c == '\n':
                count += 1
        return count

# Project part 2
# Write a function count_number_of_lines which returns the count of the number of lines starting with Subject:
# in the file /cxldata/datasets/project/mbox-short.txt
# PS - If your logic is correct then your function should return 27.

def count_number_of_lines():
    with open('/cxldata/datasets/project/mbox-short.txt') as f:
        count = 0
        for line in f:
            line = line.rstrip() # Remove new line characters from right
            if line.startswith('Subject:'):
                count = count + 1
    return count

count_number_of_lines()

# Project part 3
# Write a function find_email_sent_days which reads the file
# /cxldata/datasets/project/mbox-short.txt and categorizes each mail message by which day of the week the email was sent.
#
# To do this do the following:
#
# Open the file and read it line by line
# Look for lines that start with "From"
# For those lines which start from "From",
# then look for the third word and keep a running count of each of the days of the week.
# How do you find the day of the week, is an exercise for you.
# Note: You have to store the results in a dictionary. Only store those day of the week that exists.
# For Example, if there is no line for Mon then it should not be in the dictionary elements.
#
# At the end of the program return the contents of your dictionary (order does not matter)

def find_email_sent_days():
    daysdict = {}
    dayslist = []

    with open("/cxldata/datasets/project/mbox-short.txt") as f:
      for line in f:
        dayslist = line.split()
        if len(dayslist) > 3 and line.startswith('From'):
            day = dayslist[2]
            if day not in daysdict:
                daysdict[day] = 1
            else:
                daysdict[day] += 1
    return daysdict


# Define a function average_spam_confidence which calculates the average spam confidence and returns it
# Open the file mbox-short.txt which is located at /cxldata/datasets/project/mbox-short.txt
# Loop through the file handle
# Select only those lines starts with X-DSPAM-Confidence:
# Split the lines at : and take the float value which is spam confidence
# Find the average of this spam confidence in the entire file and return it.
# PS - If your logic is correct then the correct spam confidence score should be 0.7507185185185187.
#

def average_spam_confidence():
    with open('/cxldata/datasets/project/mbox-short.txt') as f:
        count = 0
        spam_confidence_sum = 0
        for line in f:
            line = line.rstrip() # Remove new line characters from right
            if line.startswith('X-DSPAM-Confidence:'):
                var, value = line.split(':')
                spam_confidence_sum = spam_confidence_sum + float(value)
                count = count + 1
    return spam_confidence_sum/count



# Write a function count_message_from_domain which reads the file /cxldata/datasets/project/mbox-short.txt.
#
# This function builds a histogram using a dictionary to count how many messages
# have come from each domain(Instead of from email address), and returns the dictionary.
#
# If your logic is correct then your function should return below dictionary
#
# {'uct.ac.za': 6,
#  'media.berkeley.edu': 4,
#  'umich.edu': 7,
#  'iupui.edu': 8,
#  'caret.cam.ac.uk': 1,
#  'gmail.com': 1}

def count_message_from_domain():
    lineslist=[]
    domaindict={}
    with open("/cxldata/datasets/project/mbox-short.txt") as f:
        for line in f:
            lineslist = line.split()
            if line.startswith('From:'):
                email=lineslist[1]
                domain = email.split('@')[1]
                if domain not in domaindict:
                    domaindict[domain] = 1
                else:
                    domaindict[domain] += 1
    return domaindict


# Write a function count_message_from_email which reads the file /cxldata/datasets/project/mbox-short.txt.
#
# This function builds a histogram using a dictionary to count how many
# messages have come from each email address and returns the dictionary.
#
# Output:
#
# If your logic is correct then your function should return a dictionary like the following:
#
# {'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3,
# 'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5,
# 'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1, 'antranig@caret.cam.ac.uk': 1,
# 'gopal.ramasammycook@gmail.com': 1, 'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}

def count_message_from_email():
    lineslist=[]
    emaildict={}
    with open("/cxldata/datasets/project/mbox-short.txt") as f:
      for line in f:
        lineslist = line.split()
        if line.startswith('From:'):
          email=lineslist[1]
          if email not in emaildict:
            emaildict[email] = 1
          else:
            emaildict[email] += 1
    return emaildict