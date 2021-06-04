# Documentation (WIP)
## Programing in .sk
### Creating a variable
Using the keyword `LET` to create a variable. There is no type declaration.

<br>
Example:

Creating a variable called `a`



```
LET a = 0

LET a = "hi"
```

<br>

### Comments
Comments are simple and similar to python. A singleline comment is created by using `#` before the comment.

<br>
Example:

Creating a comment with the content `This is a comment`

```
# This is a comment
```


<br>

## Example Program
The following program will take numbers as input and find the average of them
```
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
```