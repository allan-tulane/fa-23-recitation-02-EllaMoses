# CMPS 2200  Recitation 02

**Name (Team Member 1):** Ella Moses  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

    When f(n) = 1, the work at each level is changing by a factor of a so the tree is leaf dominated when a > 1 and balanced if a = 1. This means when a > 1 it is O(n^log_b a), where n^log_b(a) is the number of leaves, and O(n^log_b(a) logn) when a = 1, where n^log_b a is the number of leaves and logn is the number of levels. When f(n) = n  the work is changing by a factor of a/b. if a > b, the tree is root dominated so it is O(n). If a < b  it is leaf dominated so it is O(n^log_b a), where n^log_b(a) is the number of leaves. It is O(n^log_b(a) logn) when a = b because it is balanced, where n^log_b a is the number of nodes and logn is the number of levels. For f(n) = logn, in all cases it will be balanced since it does not grow geometically. I used the test_compare_work functions for values a = 2 and b = 2 and obtained the results below. In this case f(n) = 1 should have complexity O(n). We can see from column one of the first table that this is approximately linear. f(n) should be balanced and have a complexity of O(nlogn), we can see that this approximately matches the second column in table 1. For f(n) = logn, in all cases it will be balanced since it does not grow geometically. We can see from column 2 of table 2 that this is reflected in my results.

    Table 1: 

      |     n |   W_1 |    W_2 |
      |-------|-------|--------|
      |    10 |    15 |     36 |
      |    20 |    31 |     92 |
      |    50 |    63 |    276 |
      |   100 |   127 |    652 |
      |  1000 |  1023 |   9120 |
      |  5000 |  8191 |  61728 |
      | 10000 | 16383 | 133456 |

      Table 2:
      |     n |    W_1 |       W_2 |
      |-------|--------|-----------|
      |    10 |     36 |    16.294 |
      |    20 |     92 |    35.584 |
      |    50 |    276 |    84.201 |
      |   100 |    652 |   173.008 |
      |  1000 |   9120 |  1471.608 |
      |  5000 |  61728 |  9919.326 |
      | 10000 | 133456 | 19847.862 |

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

    If we analyze the asymptotic behavior we can see that the root cost is n^c and the level one cost is a X (n/b)^c. this means that the cost at each level is changing by a factor of a/(b^c). if c= log_b (a) then b^c = a.the tree is balanced since it is increasing by a/a, so it is O(nlogn). if c < log_b (a), then b^c < a. the tree is leaf dominated since (a/(b^c)) > 1,so it is O(n^log_b a), since n^log_b a is the number of nodes. if c > log_b (a), then b^c > a. the tree is root dominated since (a/(b^c)) < 1,so it is O(n^log_b a), since n^log_b a is the cost of the root node. This means that W(n) has the same asymptotic behavior if c < log_b (a) and c > log_b (a). Using test_compare_work, I can see that if I consider a = 4 and b = 2 (so log_b a = 2), when c = 2 the 
    
    the work comparisions  grow at approximately the same rate when c < log_b a and when c > log_b a (see table 1)

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

    The asymptotic behaviors of the spans of functions in part 4 can be calculated in the same way as work, but disregarding a. this means that for f(1) the span is balanced and is O(nlogn). The span of logn is also balanced since it is not changing geometrically, so it is also O(nlogn). For f(n)= n, it is root dominated so it is O(n). From table one we can see that f(n)=n (column 2) is approximately linear in growth. From column one we can see that f(1) grows at approximatley at logn rate. From column 2 of table 2, we can see that logn grows at approximatley an nlogn rate. 
    Table 1:
      |     n |   W_1 |   W_2 |
      |-------|-------|-------|
      |    10 |     4 |    18 |
      |    20 |     5 |    38 |
      |    50 |     6 |    97 |
      |   100 |     7 |   197 |
      |  1000 |    10 |  1994 |
      |  5000 |    13 |  9995 |
      | 10000 |    14 | 19995 |
    Table 2: 
      |     n |   W_1 |    W_2 |
      |-------|-------|--------|
      |    10 |    18 |  5.605 |
      |    20 |    38 |  8.601 |
      |    50 |    97 | 13.506 |
      |   100 |   197 | 18.111 |
      |  1000 |  1994 | 37.786 |
      |  5000 |  9995 | 56.944 |
      | 10000 | 19995 | 66.154 |
