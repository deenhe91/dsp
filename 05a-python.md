# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both collections of data but a tuple contains different data types, whereas a list contains only one data type. You can't add elements to a tuple like you can to a list, but you can see whether en element exists in a tuple as you do in a list. A list will work as keys in dictionaries because you are able to modify them and add or remove them.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are unordered and contain only unique elements. This is different to lists, which can contain multiples and are numbered. 

>> A list is useful if the order of the elements is important, so finding where something is in relation to something else. Or perhaps how often it came up.

>> If you just want to see if something is in a data set at all, or see whether something occurs in two datasets but the order or number of times it appears is not important, it is useful to use sets. You can look for overlap or difference between two sets or see whether something is present in a set.

>> It is more efficient to find an element in a set than in a list because you're guaranteed that once you've found the element that's the only one there is, whereas in a list you have to search the whole list. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda allows you to create a one-line function that isn't bound to a name. You don't define or return as you do with functions. Lambda can be nested inside functions and is callable. In the sorted() function, using key=lambda, you can change the elements before they are sorted without creating a separate function first.

>> It would look something like this - sorted(iterable, key=lambda))

>>For example, I use capitals a lot to express myself when I'm writing to people. When words are sorted, the words starting with an uppercase letter are sorted alphabetically before the words starting with a lowercase letter. If you wanted to sort all the words alphabetically you could make sure they were all lowercase before sorting them

>>      sorted(['Jerry', 'ate', 'ALL', 'the', 'peaches'], key=lambda word : word.lower())
        >> ['all', 'ate', 'jerry', 'peaches', 'the']
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions allow you to concisely create a list where each element is the result of a calculation or operation. 
>> For example:

>>              list = [x**3 for x in range(10)]
        >>            [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

>> This can also be achieved with map() and filter() functions. map() applies a function to all members of an iterable, but you have to have the function already or use lambda.

>>      def cube(x):  #pre defined function
        >>    return x**3

>>      cubes = map(cube, range(10))
>>      print(cubes)

>>      cubes = map(lambda x: x**3, range(10))
>>      print(cubes)

>>filter() takes a function returning True or False and returns a list of the members which return True. So conditionals can be applied with filter(). For example, if you want to return only the cubes above a certain value, you can use filter() to do so.

>>  - -  unfinished - -


        

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





