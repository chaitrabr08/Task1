Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> z[0]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    z[0]
NameError: name 'z' is not defined
>>> a=9
>>> a
9
>>> a="welcome user to tumkur"
>>> b="logu"
>>> a[7:logu]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[7:logu]
NameError: name 'logu' is not defined
>>> a[0:7],b[0:4],a[12:]
('welcome', 'logu', ' to tumkur')
>>> a[0:7] b[0:4] a[12:]
SyntaxError: invalid syntax
>>> print (a[:8]+b+a[12:])
welcome logu to tumkur
>>> a.replace("user",b)
'welcome logu to tumkur'
