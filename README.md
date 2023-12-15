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