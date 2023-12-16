This repository is a 1-week coding interview email course by D. Parker Phinney of Interview Cake.

He states that the key to understanding and solving software interview problems is by recognizing and/or applying algorithmic patterns. Which may include:  
  
* Bottom-up  
    Going bottom-up is a way to avoid recursion, saving the memory cost that recursion incurs when it builds up the call stack.
    ```
        def factorial(n):
            #1... n-3 , n-2, n-1, n
            if (n > 1):
                return n * factorial(n - 1)
            return 1

        def factorial(n):
            #bottom-up approach
            #1, 2, 3, 4..., (n-1), n
            i = 1
            res = 1
            while i < n:
                i 
                res *= i
            return res
    ```

* Cut the problem in half and solve each half  
* Using a stack  

## parentheses.py 

You're working with an intern that keeps coming to you with JavaScript code that won't run because the braces, brackets, and parentheses are off. To save you both some time, you decide to write a braces/brackets/parentheses validator.

Let's say:

    '(', '{', '[' are called "openers."
    ')', '}', ']' are called "closers."

Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

Examples:

    "{ [ ] ( ) }" should return True
    "{ [ ( ] ) }" should return False
    "{ [ }" should return False

