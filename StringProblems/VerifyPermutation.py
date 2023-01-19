'''
This problem is taken from Ctci book.
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.

There are two ways that I could think of, to solve the problem
1) Sort the string and then compare both string, however this is minimum O(nlogn) time complexity
2) To conclude that the given other string is permutation of first string, it should contain same numer of characters
This approach would take O(n) and space complexity I think should remain same since I am using 2 int variables to keep track of count
'''
def verPermBySort(inp):
    if len(inp[0]) != len(inp[1]):
        return False
    str1 = sorted(inp[0])
    str2 = sorted(inp[1])
    if str1==str2:
        return True
    return False
def verPermByCount(inp):
    countstr1, countstr2 =0,0
    for char in inp[0]:
        countstr1 += ord(char) -ord('a')
    for char in inp[1]:
        countstr2 += ord(char) -ord('a')

    if countstr1==countstr2:
        return True
    return False
def main():
    testcases = [
        ["stab","bats"], ["cap","pack"], ["stak","task"]
    ]
    testfuncs = [verPermBySort, verPermByCount]
    for func in testfuncs:
        print("===================")
        for case in testcases:
            print(f'strings {case} ,are permutation of each other: {func(case)} using {func.__name__}')

if __name__ == "__main__":
    main()