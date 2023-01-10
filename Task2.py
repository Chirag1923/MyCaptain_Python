"""
Write a Python program to accept a filename from the user and print the extension of that. 

Input the Filename: abc.py 
The extension of the file is : 'python'
"""

d1 = { "py":"python", "txt" : "text", "java" : "java","c":"C"}
filename=input("Input The Filename: ")
extension = filename.split(".")
result = extension[1]
result = d1[result]
print("The extension of the file is : ", result)
