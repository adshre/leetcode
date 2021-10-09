- Variables act as "storage locations" for data in a program.
- virtually execute programs : https://cscircles.cemc.uwaterloo.ca/visualize
- Errors: 
  - print(trouble)<br /> NameError: name 'trouble' is not defined
  - 4 = x <br />  SyntaxError: can't assign to literal(While A = B and B = A are the same in mathematics, they are different in programming.)
- Swap variables. : https://www.geeksforgeeks.org/swap-two-numbers-without-using-temporary-variable/
- Identifier can not start with digits. Eg WRONG : 1_Num is wrong variable name, for = 4 is wrong as for is reserved word
- Change 1st and last character of string : strinp[-1:]+strinp[1:-1] + str[:1]
- Errors : runtime(num = 1/0), Syntax(print "x" instead of print("x")), logical( average = x + y/2 instead of (x+y)/2)
- The program with the run-time error created some output, but the one with the syntax error did not. This is because Python runs in two steps:
    - Python checks if your program has correct syntax, in order to determine its structure and parts.
    - If no syntax errors were encountered in step 1, then the program is executed.
    - So, a program with a syntax error will execute no steps at all, but a program with a run-time error will execute the steps that happened before the error occured.
- functions : max(), min(). example : three nos in ascending => min(x,y,z), (x+y+z - min(x,y,z) - max(x,y,z)), max(x,y,z)
- <pre>
      Fix the logic error in this program: it should 
      calculate the population of your country for the next 3 years,
      assuming it starts with 1000 people in 2012, and the number of people increases by 10% each year. 
      You can change at most three characters. 

      populationIn2012 = 1000
      populationIn2013 = populationIn2012 * 1.1
      populationIn2014 = populationIn2013 * 1.1
      populationIn2015 = populationIn2014 * 1.1
</pre>
- Finding min using max :  print(-1 * max(-A, -B)) or print(A+B - max(A,B))
- https://stackoverflow.com/questions/18115046/number-sort-using-min-max-and-variables
- In built func : float(), int() can parse string but e.g. float("sandwich") causes an error.
, fmod() func, math.trunc(10.3) will remove digits after decimal and return 10
- Sometimes, Python does let you combine strings and numbers using arithmetic operators. The statement print("hots" * 2) prints hotshots. Python's rule is that multiplying a string s by an integer n means to put n copies of the string one after another. We'll see later that "addition of two strings" is also well-defined in Python.
- Indentation in python can have any number of spaces but needs to be consistent
- <pre>
  print(A)
    print(A) 
  Block error : IndentationError: unexpected indent
  
    print(A)
   print(A)
   Block Error :IndentationError: unindent does not match any outer indentation level 
  </pre>
 - Note that in Python, when you use the bool values True and False directly in a program, they must be capitalized or you will get an error.
 - print(ord(chr(5))) => 5 : chr(value) gives character of value and ord() returns the value again.(i.e unicide value in this case say 5)
