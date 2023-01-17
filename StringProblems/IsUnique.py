''' This question is from CtCI book the question is as follows
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

Question specifies there are no auxillary storage to be used,
however I will try to implement with both with and without extra storage
'''

def IsUniqueWithSort(s):
    # This solution has time complexity of O(NlogN) as we would sort and then check previous character with current one
    # If they are same then we return False
    s = ''.join(sorted(s))
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            return False
    return True

def IsUniqueWithDict(s):
    # Idea is to store chars in dict, it uses auxiallary storage that is dict, if char exist as key then return False
    strdict ={}
    for ch in s:
        if ch not in strdict.keys():
            strdict[ch]=True
        else:
            return False
    return True

def IsUniqueWithArrays(s):
    chrarr = [False]*128
    for ch in s:
        index = ord(ch)
        if chrarr[index]==True:
            return False
        else:
            chrarr[index]=True
    return True
def main():
    testcases = [
        "abc", "aabc", "User two","User twoo"
    ]
    testfuncs = [IsUniqueWithSort,IsUniqueWithDict,IsUniqueWithArrays]
    for func in testfuncs:
        print("===================")
        for case in testcases:
            print(f'For string {case} ,it has unique characters: {func(case)} using {func.__name__}')

if __name__ == "__main__":
    main()

