**Anonymous function**: a function without a name, such as **lambda expressions**
**Eager evaluation**: Evaluating a function's arguments before we run it    
**Lazy evaluation**: pass the argument sub-lists into the function and let it evaluate them when it needed their value
- Con: It's a bit more work
- Pro: It allows the function to inspect the expressions it has been called with and to decide how to handle them

**Call stack**: the environment which is a list of dictionaries      
**Stack frame**: the dictionary in the Call stack 

**Dynamic scoping**: Searching through all active stack frames for a variable, it is easy to implement     
**Lexical scoping**: figure out what a variable name refers to based on the structure of the program text. it is easy to understand,particularly in large program.

**Closure**
