from pythonds.basic.stack import Stack

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(25,8))

"""
Summary
A stack is a type of data structure. It is a collection of 
ordered items. Similar to stacked trays at a cafeteria, a
stack can be added BUT only the top of stack can be removed.
This principle is known as LIFO (Last-in, first-out)
"""

