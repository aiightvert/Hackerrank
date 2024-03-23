Basic Python Glossary
Written By : Dennis Imanuel

1. Tuples : Tuples are used to store multiple items in a single variable.
            Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
            A tuple is a collection which is ordered and unchangeable.
            Tuples are written with round brackets "()".

2. Hash :   The Python hash() built-in function returns an integer value for every object which is hashable. 
            The hash method is used in programming to return integer values that can be used to compare dictionary keys using a dictionary look-up function. 
            If an item has a hash value that never changes during its lifespan, it is hashable.

example -> 
            if __name__ == '__main__':
                n = int(input())
                integer_list = map(int, input().split())
                
                t = tuple(integer_list)
                t_hash = hash(t)
                
                print(t_hash)

3. swapcase : Make the lower case letters upper case and the upper case letters lower case

example ->
            def swap_case(s):
                swapped = s.swapcase()
                return swapped

4. split and join : We use split to get data from CSV and join to write data to CSV. In Python, we can use the function split() to split a string and join() to join a string.

example ->
            def split_and_join(line):
                string_split = line.split(" ")
                string_join = "-".join(string_split)
                
                return string_join

example ->
            def print_full_name(first, last):
                full_name = first + " " + last
                full_name_join = "".join(full_name)+"!"
                intro = print("Hello", full_name_join, "You just delved into python.")
                
                return intro

output: Hello Ross Taylor! You just delved into python.

5. 
