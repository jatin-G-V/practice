# Build fluency by writting small, correct functions.

import string
from collections import Counter
# Problem 1 : Make a function word_count(text) that returns a dictionary of words to count, lowercase, and stripped of punctuation.

def word_count(text):
    text = text.lower()
    for a in text:
        if a in string.punctuation:
            text = text.replace(a, "")

    words = text.split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

# print("Output of word_count function:")
# print(word_count("Hello, world! Hello, everyone."))

# Output: {'hello': 2, 'world': 1, 'everyone': 1}

# Problem 2 : Write word_count(text) using a collections.Counter and check if previous implementation and this one are equivalent.

def word_count_counter(text):
    text = text.lower()
    for a in text:
        if a in string.punctuation:
            text = text.replace(a, "")

    words = text.split()
    return dict(Counter(words))

# print("Output of word_count_counter function:")
# print(word_count_counter("Hello, world! Hello, everyone."))

# s = "Hello, world! Hello, everyone."
# if(word_count(s) == word_count_counter(s)):
#     print("True,Both implementations are equivalent.")

# Problem 3 : Make a function flatten(list_of_lists) that return a single flat list, once with loops and once with a comprehension.

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

def flatten_with_loops(list_of_lists):
    result = []
    for sublist in list_of_lists:
        for item in sublist:
            result.append(item)
    return result

def flatten_with_comprehension(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

# print("Output of flatten_with_loops function:")
# print(flatten_with_loops(nested_list))

# print("Output of flatten_with_comprehension function:")
# print(flatten_with_comprehension(nested_list))

#Problem 4 : Make a function mean_of_file(path) that reads a file of numbers, skips bad line with try and except, and returns the mean of the numbers.

def mean_of_file(path):
    total = 0
    count = 0
    try :
        with open(path, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    total += number
                    count += 1
                
                except ValueError:
                    continue
        if(count == 0):
            return "No valid numbers found."
        return total / count
    except FileNotFoundError:
        return "File not found."  
    
# print(mean_of_file("week1/lab2/numbers.txt"))
# print(mean_of_file("week1/lab2/alpha.txt"))
# print(mean_of_file("week1/lab2/number.txt"))

# Problem 5 :Show the difference between a list comprehension and a generator expression in a short comment, and say when the generator is better

def compare_list_and_generator():
    # A list comprehension creates a list in memory.
    list_comp = [x * x for x in range(5)]

    # a generator expression creates an iterator that yields items one at a time.
    gen_exp = (x * x for x in range(5))

    print("List Comprehension:", list_comp)
    print("Generator Expression:", gen_exp)

    print("\nGenerator values:")
    for value in gen_exp:
        print(value)
# compare_list_and_generator()

# Problem 6 : Add an if __name__ == "__main__": block that exercises all functions and demonstrates error handling by attempting to open a missing file.

def main():
    # Question 1
    text = "Hello, World! Hello Python."
    print("Word Count (Manual):")
    print(word_count(text))

    print("\nWord Count (Counter):")
    print(word_count_counter(text))

    # Question 3
    nested = [[1, 2], [3, 4], [5]]

    print("\nFlatten using loops:")
    print(flatten_with_loops(nested))

    print("\nFlatten using list comprehension:")
    print(flatten_with_comprehension(nested))

    # Question 4
    print("\nMean of numbers.txt:")
    print(mean_of_file("week1//lab2/numbers.txt"))

    # Error handling demonstration
    print("\nMissing file:")
    print(mean_of_file("missing.txt"))

    # Question 5
    print("\nList Comprehension vs Generator:")
    compare_list_and_generator()


if __name__ == "__main__":
    main()