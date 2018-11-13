# Luis Ochoa
# 80508534
# 11:30
from HashTable import ChainingHashTable, Node


def solution_a():
    f = open('test.txt')
    line = f.readline()
    # Size is set so the load factor is .75
    dict = ChainingHashTable(473312)
    while line:
        # getting only the passwords from each line
        try:  # ignores line if irregularity with data
            dict.insert_a((line.rstrip().lower()))
        except:
            print()
        line = f.readline()

    f.close()
    word_input = input("word you want to check anagrams for")
    anagram_printer(word_input, dict)
    print("load factor is ",load_factor(dict))
    print("average collision is ", average_collision(dict))
def solution_b():
    f = open('test.txt')
    line = f.readline()
    # Size is set so the load factor is .75
    dict = ChainingHashTable(473312)
    while line:
        # getting only the passwords from each line
        try:  # ignores line if irregularity with data
            dict.insert_a((line.rstrip().lower()))
        except:
            print()
        line = f.readline()

    f.close()
    word_input = input("word you want to check anagrams for")
    anagram_printer(word_input, dict)
    print("load factor is ", load_factor(dict))
    print("average collision is ", average_collision(dict))

def solution_c():
    f = open('test.txt')
    line = f.readline()
    # Size is set so the load factor is .75
    dict = ChainingHashTable(473312)
    while line:
        # getting only the passwords from each line
        try:  # ignores line if irregularity with data
            dict.insert_a((line.rstrip().lower()))
        except:
            print()
        line = f.readline()

    f.close()
    word_input = input("word you want to check anagrams for")
    anagram_printer(word_input, dict)
    print("load factor is ", load_factor(dict))
    print("average collision is ", average_collision(dict))
# used to calculate average collision
def average_collision(dict):
    length = len(dict.table)

    return dict.collision_counter/length

# used to calculate load factor
# uses built int to class input counter
def load_factor(dict):

    length = len(dict.table)
    return dict.input_counter / length
# used to print anagrams of a word that exist in dictionary
def anagram_printer(key,dict):

    anagrams = all_perms(key)
    for i in range(1, len(anagrams)):
        if dict.search_a(anagrams[i]):
            print(anagrams[i])

# computes all anagrams of a word and returns them in a list/array
def all_perms(elements):
    temp_word = ""
    if len(elements) <=1:
        return elements
    else:
        tmp = []
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0:1] + perm[i:])
        return tmp


def main():
    solution_a()
main()