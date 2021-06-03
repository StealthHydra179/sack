# sack
A tiny compiled language, based on BASIC and Lua

[example code](./example.sk)


# Documentation (WIP)
## Programing in .sk
### Creating a variable
Using the keyword `LET` to create a variable. There is no type declaration.

<br>
Example:

Creating a variable called `a`

<code>
LET a
</code>

<br>

### Comments
Comments are simple and similar to python. A singleline comment is created by using `#` before the comment.

<br>
Example:

Creating a comment with the content `This is a comment`

<code>
#This is a comment
</code>


<br>

## Example Program
<code>
# Compute average of given values.

LET a = 0
WHILE a < 1 REPEAT
  PRINT "Enter number of scores: "
  INPUT a
ENDWHILE

LET b = 0
LET s = 0
PRINT "Enter one value at a time: "
WHILE b < a REPEAT
  INPUT c
  LET s = s + c
  LET b = b + 1
ENDWHILE

PRINT s / a
</code>