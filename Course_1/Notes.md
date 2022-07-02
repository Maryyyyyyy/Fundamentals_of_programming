# **An introduction to interactive programming in python Part 1** 

## Week 1 Arithemtic expression
- In Python 2, the result of dividing two integers is another integer.  (The exact answer rounded down to the nearest integer.) *Eg: -9/4 --> -3*
- operator precedence = (), ** (^), *, /, +,-
- sqrt should be written as **(0.5)

## Week 2: Functions and logic
> Function
- Everything indent is the component of the function
    ```def triangle_area(base,height):
    area = (1/2)*base*height
    return area 
    ```
- Return run the output of the function
- It will return things only after we recall the function
    ``` 
    al = triangle_area (3,7)
    print(al)
    ```
- If already have a function, can call the function inside another function
    ```
    def fahrenheit2celsius(fahrenheit):
        celsius = (5.0 / 9) * (fahrenheit - 32)
        return celsius

    def fahrenheit2kelvin(fahrenheit):
        celsius = fahrenheit2celsius(fahrenheit)
        kelvin = celsius + 273.15
        return kelvin
    ```
-  If function does not have return, it will return false. 
-  % will be operated early than + and -. 
-  Remainders can be used to calculate time hour and also screen wraparound
    ```
    width = 800
    position = 797
    move = 5
    position = (position + move) % width
    print position
    ```
- Library: simplegui(draw operations for interactive applications); math(standard math functions); random(generate random numbers). 
- Random module
    ```
    random.randrange(2, 20, 2)
    #Returns any random integer from 2 to 20 with step 2

    random.randint(0, 9)
    #Returns any random integer from 0 to 9

    random.sample(range(0, 1000), 10)
    #Returns a list of random numbers
    ```

> Logic and comparison
- True and False: AND and OR
- OR: if one value is TRUE, it is TRUE. If both false, it returns false
- TRUE or False --> True
- comparison operator: >, <, ==, !=, >=, <=.

> Conditional
- If loop
  ```
    def greet(friend, money):
        if friend and (money > 20):
        print "Hi!"
        money = money - 20
    elif friend:
        print "Hello"
    else:
        print "Ha ha"
        money = money + 10
    return money
    ```
- If: if the statement is true, then execute the program. 
  ```
  def is_leap_year(year):
    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False
    ```
- Attribute error: For example, misspelling a constant or a call to a function in library (random/math) cause an AttributeError.
- In a function, the return will lead to the end of the function
  ```
  def do_stuff():
    print "Hello world"
    return "Is it over yet?"
    print "Goodbye cruel world!"
    
    print do_stuff()
  ```
- The function will return "Hellow world and is it over yet?" 

## Week 3: Event-driven program
> Event driven program
- Events chain

    1. Input --> button / text box
    2. keyboard --> key down / up
    3. Mouse --> click / drag
    4. Timer
    
    ![Event Queue](Notes/Week%202.jpg)

> Local and global variables
- num1 write outside is global variables
- num2 assign in a function is a local variables
  ```
  num1 = 1
  def fun():
    num2 = num1 +1 
    print num2
    ```
- To assign global variables in function, need to write global 
     ```
  num1 = 1
  def fun():
    global num1
    num1 = 5
    print num1
    ```
- Will give us output num1 = 5
- Practice: 
     ```
    def d(y):
    y = x+y
    return y
    # x use as global x 
    ```
     ```
    def b(x,y):
    x = x+y
    return x
    # x use as local x 
    ```
     ```
    def a(y):
    y = x+y
    return y
    # x need to be defined as global, no x will appear
    ```
     ```
    def c(y):
    return x+y
    # Correct
    ```
> SimpleGUI (Codeskript only)
- Program structure 
  1. Define globals (state)
  2. Define helpful functions
  3. Define classes
  4. Define event handler
  5. Create a frame
  6. Register event handler
  7. start frame & timer

> Function
- For function def(), if not add return or print at the end, the number will not be recorded 
  ```
  def increment():
    global n
    n = n+1
    # Will return as n = None

- If a == True and b == False is the same as if not a and b
- True table 
    ![And table](Notes/And%20table.png)
    ![Or table](Notes/Or%20table.png)