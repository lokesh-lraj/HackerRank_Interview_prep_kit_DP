'''
You can perform the following operations on the string a,
    Capitalize zero or more of a's lowercase letters.
    Delete all of the remaining lowercase letters in a.

Given two strings, a and b, determine if it's possible to make a equal to b as described. If so, print YES on a new line. Otherwise, print NO.

For example, given a = 'AbcDE' and b = 'ADDE', in a we can convert 'b' and delete 'c' to match b. If a = 'AbcDE' and b = 'AFDE', matching is not possible because 
letters may only be capitalized or discarded, not changed.

Input Format

The first line contains a single integer q, the number of queries.

Each of the next q pairs of lines is as follows:
- The first line of each query contains a single string, a.
- The second line of each query contains a single string, b.

Constraints
  1 <= |q| <= 10
  1 <= |a|, |b| <= 1000
  String a consists only of uppercase and lowercase English letters, ascii[A-Za-z].
  String b consists only of uppercase English letters, ascii[A-Z].
  
  Output Format

For each query, print YES on a new line if it's possible to make string
equal to string

. Otherwise, print NO.

Sample Input

1
daBcd
ABC

Sample Output

YES
'''
def abbreviation(a, b):
    n = len(a)
    m = len(b)
    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

    s = ''
    for i in range(1,n+1):
        s += a[i-1]
        dp[i][0] = s.islower()

    for j in range(m+1):
        dp[0][j] =  False

    dp[0][0] = True

    for i in range(1,n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            elif a[i-1].upper() == b[j-1]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-1]
            else:
                if a[i-1].isupper():
                    dp[i][j] = False
                else:
                    dp[i][j] = dp[i-1][j]
    return 'YES' if dp[-1][-1] else 'NO'
