'''
isStringPermutation(...) 🧶
Implement the function isStringPermutation() that takes two Strings as parameters and 
returns a Boolean denoting whether the first string is a permutation of the second string.

def isStringPermutation(s1: str, s2: str) -> bool:

Below are some examples:
isStringPermutation(s1: “asdf”, s2: “fsda”) == true
isStringPermutation(s1: “asdf”, s2: “fsa”) == false
isStringPermutation(s1: “asdf”, s2: “fsax”) == false

Questions & Observations:
- Are capital letters included, and if so, are they the same as lowercase letters? 
    - Ex: s1 = "Snapple", s2 = "nsapple"
- Can the strings be empty?
    - Ex: s1 = "", s2 = "snapple"
- Do spaces count?
    - Ex: s1 = "sn app le", s2 = "aspnpel"
- Are special characters included? - not going to affect
- In order for a string to be a permutation of another string, they must have same size
and characters

Approaches:
- We could use a dictionary or an array to keep track of what letters we have seen
- For an array, we could add each letter in the first string to an empty array and 
remove it if we find the same letter in the second string. If the array is empty, then the
first string is a permutation of the other string. 
- We could use a dictionary to keep track of what letters we have seen and decrement the value
it is associated with if we see it in the second string. If all keys correspond to the value
0, then the first string is a permutation of the other string. 

We're gonna go with the dictionary approach since in the array approach, we'd have to loop
through the array over and over again to find each letter.
'''

def isStringPermutation(s1, s2):
    seen = {}
    for i in s1:
        if i not in seen: # in case of 2 or more of same character
            seen[i] = 0
        seen[i] += 1

    for i in s2:
        if i in seen:
            seen[i] -= 1
        else:
            return False # return False early if s2 have different letters

    for i in seen:
        if seen[i] != 0:
            return False

    return True

# Time complexity: O(n)
# Space complexity: O(n)

print(isStringPermutation("asdf", "fsda")) # true
print(isStringPermutation("asdf", "fsa")) # false
print(isStringPermutation("asdf", "fsax")) # false

# Additional test cases
print(isStringPermutation("pony", "yopnnn")) #false
print(isStringPermutation("ppppppp", "ppp")) #false
print(isStringPermutation("", "hey")) #false
print(isStringPermutation("p", "p")) #true
print(isStringPermutation("unicorn", "nrcouni")) #true
print(isStringPermutation("p!", "!p")) #true

'''
Question #2
pairsThatEqualSum(...)

Implement the function pairsThatEqualSum() that takes an array of integers 
and a target integer and returns an array of pairs (i.e., an array of tuples) where 
each pair contains two numbers from the input array and the sum of each pair equals the 
target integer. (Order of the output does not matter).

def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:

Below are some examples:
pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 5) == [(1, 4), (2, 3)]
pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 1) == []
pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 7) == [(2, 5), (3, 4)]

Questions & Observations:
- Number that matches integer i is targetSum - i
- Can there be duplicates? Can numbers match with themselves?
    - Ex: inputArray: [2, 2, 3, 4, 5], targetSum: 4 == [(2, 2)]
    - Ex: inputArray: [2, 3, 4, 5], targetSum: 4  == [(2, 2)] or []
    - Ex: inputArray: [2, 2, 2, 2, 3, 4, 5], targetSum: 4  == [(2, 2), (2, 2)] or [(2, 2)]
- Can the input array be empty? 
- Can the integers be negative numbers? - not going to affect

Approach:
Create an empty dictionary and an empty result array. Loop through the inputArray 
and if target int - i is in the dictionary, add the tuple to the result array. Else, add i 
to the dictionary.

'''

def pairsThatEqualSum(list, int):
    result = []
    seen = {}

    for i in list:
        x = int - i
        if x in seen and [x,i] not in result:
            result.append([x, i])
        else:
            seen[i] = 0
    
    return result

# Time complexity: O(n)
# Space complexity: O(n)

print(pairsThatEqualSum([1, 2, 3, 4, 5], 5)) # [(1, 4), (2, 3)]
print(pairsThatEqualSum([1, 2, 3, 4, 5], 1)) # []
print(pairsThatEqualSum([1, 2, 3, 4, 5], 7)) # [(2, 5), (3, 4)]

# Additional Test cases
print(pairsThatEqualSum([1, 2, 4, 4, 8, 0], 8)) # [[4, 4], [8, 0]]
print(pairsThatEqualSum([], 1)) # []
print(pairsThatEqualSum([1, 2, 3, 4, 5, 4, 4, 5, 8], 9)) # [[4, 5], [1, 8]]



