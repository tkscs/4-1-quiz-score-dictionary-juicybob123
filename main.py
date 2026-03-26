# 1. Write a function `make_dictionary` that takes two lists and returns a
# dictionary with the names as keys and the scores as values.

def make_dictionary(keys_list, values_list):
    
    """
    turn 2 lists into a dictionary
    
    Here are some tests. Make sure your code can handle these cases!
    >>> make_dictionary(["a", "b"], [1, 2])
    {'a': 1, 'b': 2}
    >>> make_dictionary([1, 2, 3], [5, 6, 7])
    {1:5, 2: 6, 3: 7}
    >>> make_dictionary(["a", "b", "c", "b"], ["apple", "banana", "clementine", "date"])
    {'a': 'apple', 'b': 'banana', 'c': 'clementine', 'd': 'date'}
    >>> make_dictionary(["key"], ["value"])
    {'key': 'value'}
    """
    
    mylist = {}
    x = len(keys_list)
    for i in range(len(keys_list) -1):
        mylist[keys_list[i]] = values_list[i]
           
    
   

    return mylist


    return 
    #### YOUR CODE HERE

    
print(make_dictionary(["cats", "dogs"],[1 , 2]))

print(make_dictionary(["a", "b"], [1, 2]))
print(make_dictionary([1, 2, 3], [5, 6, 7]))
print(make_dictionary(["a", "b", "c", "b"], ["apple", "banana", "clementine", "date"]))
print(make_dictionary(["key"], ["value"]))

# You have been given the following list fo students and their test scores:
names = ["Maria", "Nushi", "Mohammed", "Jose", "Wei"]
scores = [10, 23, 13, 18, 12]
print(len(names))

# Assign the result of make_dictionary to score_dict, which will be used in the
# exercises that follow.
score_dict = make_dictionary(names, scores)


# 2. Using `score_dict`, find the score for "Nushi"
#### YOUR CODE HERE

print(score_dict["Nushi"])
total = 0
# 3. Add a score 19 for "John"
#### YOUR CODE HERE
score_dict["John"] = 19
print(score_dict)
# 4. Calculate the average of all the scores in `score_dict`
#### YOUR CODE HERE
for y in range(len(score_dict)):
    total += scores[y]
print(total/len(scores))
# 5. Update the score for "Wei" to be 13
#### YOUR CODE HERE
score_dict["Wei"] = 13
print(score_dict)
# 6. Nushi has just dropped this class. Delete "Nushi" and his score from
# `score_dict`
#### YOUR CODE HERE
del score_dict["Nushi"] 
print(score_dict)