# day 5
import re

def is_nice(string):
    def three_vowels(string):
        # contains at least three vowels
        return len(re.findall(r'[aeiou]', string)) >= 3
    
    def pair(string):
        # contain a least one pair of consecutive identical characters
        return bool(re.search(r'((\w)\2{1})', string))
    
    def no_forbiden_pairs(string):
        # no occurence of a forbiden pairs ab, cd, pq or xy
        return not bool(re.search(r'(ab|cd|pq|xy)', string))
    
    return three_vowels(string) and pair(string) and no_forbiden_pairs(string)


def is_nice_2(string):

    def pairs_no_overlapping(string):
        '''contains a pair of any two letters that appears at least twice in the string without overlapping'''
        return bool(re.search(r'(..).*\1', string))

    def shoulder_pair(string):
        '''It contains at least one letter which repeats with exactly one letter between them, like xyx, 
        abcdefeghi (efe),or even aaa'''
        return bool(re.search(r'(.).\1', string))
    
    return pairs_no_overlapping(string) and shoulder_pair(string)


with open('AOC2015_5.data', 'r') as f:
    data = f.read().split()

print('Part 1:', sum(is_nice(string) for string in data))
print('Part 2:', sum(is_nice_2(string) for string in data))
