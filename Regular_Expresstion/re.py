import re

"""
A regular Expression ( abbreviated Regex  or Regexp) is a sequence of character
that forms a search pattern, mainly to use pattern matching with strings,
or string matching, i.e "find and replace" like operations
"""


# input a string
while(True):
    string = input("Enter any string:-")

    if(string == 'end'):
        break

    # simple search (re.search)

    if(re.search('python',string, re.I)): # it same as python in string re.I is ignore case
        print('Python is present')
    else:
        print('Python is not present')
    print("----------------------------------------------------")

    # Anchors
    # ^ Starting with; $ Ending with
    if (re.search('^python', string, re.I)):  # string.startswith('python')
        print('^Python is present')
    else:
        print('^Python is not present')

    if (re.search('python$', string, re.I)):  # string.endswith('python')
        print('Python$ is present')
    else:
        print('Python$ is not present')

    if (re.search('^$', string, re.I)):  # string == '' or len(string) == 0
        print('^$ is satisfied')
    else:
        print('^$ is not satisfied')

    if (re.search('^python$', string, re.I)):  # string == 'python' exect match
        print('^python$ is satisfied')
    else:
        print('^python$ is not satisfied')

    # Range of characters -[0-9], [a-z], [A-Z], [a-z,A-Z], [0-9a-zA-Z]
    # we have three types of Metacharacters
    # 1. + matches one or more occurrence of the previous character
    # 2. * matches zero or more occurrence of the previous character
    # 3. ? matches zero or one occurrence of the previous character

    if (re.search('^[0-9][a-z]+[A-Z]$', string)):
        print('^[0-9][a-z]+[A-Z]$ is satisfied')
    else:
        print('^[0-9][a-z]+[A-Z]$ is not satisfied')

    if (re.search('^[0-9][a-z]*[A-Z]$', string)):
        print('^[0-9][a-z]*[A-Z]$ is satisfied')
    else:
        print('^[0-9][a-z]*[A-Z]$ is not satisfied')

    if (re.search('^[0-9][a-z]?[A-Z]$', string)):
        print('^[0-9][a-z]?[A-Z]$ is satisfied')
    else:
        print('^[0-9][a-z]?[A-Z]$ is not satisfied')

    if (re.search('^[0-9].[A-Z]$', string)): # . means in between [0-9] and [A-Z] and one character will cllow it may be _ space any charachte
        print('^[0-9].[A-Z]$ is satisfied')
    else:
        print('^[0-9].[A-Z]$ is not satisfied')

    if (re.search('^[0-9].*[A-Z]$', string)): # .* in between any number of characters there is no limit
        print('^[0-9].*[A-Z]$ is satisfied')
    else:
        print('^[0-9].*[A-Z]$ is not satisfied')

    # Grouping and quantifiers
    # {m} matches exactly m occurrences
    # {m, n) matches minimum m and maximun n
    # {m,} matches minimum m and maximum 'unbounded'
    # {,n } matches minimum 0 and maximum n
    if (re.search('^([0-9][a-z]){3}[A-Z]$', string)): #4b6m7bA one number is followed by the one lower alphabet three times
        print('^([0-9][a-z]){3}[A-Z]$ is satisfied')
    else:
        print('^([0-9][a-z]){3}[A-Z]$ is not satisfied')

    # choices and Alternatives
    # [abs] Matches any one from 'a', 'b' or 'c'
    # [^abc] Matches other than 'a', 'b' and 'c' it will exclude

    if (re.search('^a[bcd]e$', string)):
        print('^a[bcd]e$ is satisfied')
    else:
        print('^a[bcd]e$ is not satisfied')

    if (re.search('^a[^bcd]e$', string)):
        print('^a[^bcd]e$ is satisfied')
    else:
        print('^a[^bcd]e$ is not satisfied')
    print("----------------------------------------------------")
    # Character class Escape Sequence
    # \d [0-9]; \D other than 0 to 9 like [^0-9]
    # \w [0-9a-zA-Z_] any one character from this set; \W [^0-9a-zA-Z_]
    # \s matches single space and tab charater; \S other than space and tab

    if (re.search('^\d{10}$', string)):
        print('^\d{10}$ is satisfied')
    else:
        print('^\d{10}$ is not satisfied')
    print("----------------------------------------------------")

    # compile method is used check the regular expression pattern has any errors and
    # also reusablilty of petterns
    # if you want to use a pattern across you code or methods you can use compile
    # pattern = re.compile('\d{3}') this is my pattern
    # this pattern we can invoke in each and every methods it starts reusablility
    # checks syntax of the regex and for re-usability
    pattern = re.compile('\d{3}')

    # search and match
    searched = pattern.search(string) #re.search('pattern' , string)
    if(searched):
        print("Searched", searched.group()) # searched.start(), searched.end() ,searched.span()
    else:
        print("search is not satisfied")

    matched = pattern.match(string) # #re.match('pattern' , string
    if (matched):
        print("Matched", matched.group())
    else:
        print("Match is not satisfied")

    # search look for the pattern any where in the string
    # but match look for the pattern only in the begining of the  string

    print("----------------------------------------------------")

    # findall consider there are lot of inputs means lot of matched patterns
    # search will return only first occerrance only but findall will return all matches

    all_matched = pattern.findall(string) # re.findall('pattern' , string)
    print("All_matched", all_matched)

    # split
    spt_str = pattern.split(string) # re.split('pattern' , string)
    print("Splited",spt_str)

    # sub - find and replacing the pattern
    rep_str = pattern.sub(' 555 ', string) # re.sup('pattern', '555',string)

    print("Replaced ", rep_str)




