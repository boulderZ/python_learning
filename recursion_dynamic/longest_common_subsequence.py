



def lcs_length(sta,stb):
    return subproblem(sta,stb,0,0)

def subproblem(sta,stb,i,j):
    if i == len(sta) or j == len(stb):
        print('')
        print('end of string i,j = ',i,j)
        print('')
        return 0
    elif sta[i] == stb[j]:
        print('in equal START i,j = ',i,j)
        val = subproblem(sta,stb,i+1,j+1)
        print('in equal END i,j = ',i,j,'val+1 = ',val+1)
        return 1 + val
    else:
        print('in max START i,j = ',i,j)
        a = subproblem(sta,stb,i+1,j)
        b = subproblem(sta,stb,i,j+1)
        print('in max END i,j = ',i,j,'a,b = ',a,b,'max = ',max(a,b))
        return max(a,b)

def lcs_length_m(sta,stb,L):
    return subproblem_m(sta,stb,0,0,L)

def subproblem_m(sta,stb,i,j,L):
    if L[i][j] < 0:
        if i==len(sta)+1 or j==len(stb)+1:
            L[i][j] = 0
        elif sta[i] == stb[j]:
            L[i][j] = 1 + subproblem_m(sta,stb,i+1,j+1,L)
        else:
            L[i][j] = max(subproblem_m(sta,stb,i+1,j,L),subproblem_m(sta,stb,i,j+1,L))
    return L[i][j]

def lcs_length_mg(sta,stb):
    return subproblem_m(sta,stb,0,0)

def subproblem_mg(sta,stb,i,j):
    global L
    if L[i][j] < 0:
        if i==len(sta) or j==len(stb):
            L[i][j] = 0
        elif sta[i] == stb[j]:
            L[i][j] = 1 + subproblem_mg(sta,stb,i+1,j+1)
        else:
            L[i][j] = max(subproblem_mg(sta,stb,i+1,j),subproblem_mg(sta,stb,i,j+1))
    return L[i][j]

def subproblem2(sta,stb,i,j,match):
    if i == len(sta) or j == len(stb):
        print('')
        print('end of string i,j = ',i,j)
        print('')
        return match
    elif sta[i] == stb[j]:
        print('in equal START i,j = ',i,j)
        match.append(sta[i])
        subproblem2(sta,stb,i+1,j+1,match)
        print('in equal END i,j = ',i,j)
        return match
    else:
        print('in max START i,j = ',i,j)
        a=subproblem2(sta,stb,i+1,j,match)
        b=subproblem2(sta,stb,i,j+1,match)
        return max(a,b)


def longest_common_substring(s1, s2):
   m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
   longest, x_longest = 0, 0
   for x in range(1, 1 + len(s1)):
       for y in range(1, 1 + len(s2)):
           if s1[x - 1] == s2[y - 1]:
               m[x][y] = m[x - 1][y - 1] + 1
               if m[x][y] > longest:
                   longest = m[x][y]
                   x_longest = x
           else:
               m[x][y] = 0
   return s1[x_longest - longest: x_longest]
'''
test
st1 = 'nema'
st2='emp'
In [56]: lcs_length(st1,st2)
in max i,j =  0 0
in equal i,j =  1 0
in equal i,j =  2 1
in max i,j =  3 2
end of string i,j =  4 2
end of string i,j =  3 3
in max i,j =  0 1
in max i,j =  1 1
in equal i,j =  2 1
in max i,j =  3 2
end of string i,j =  4 2
end of string i,j =  3 3
in max i,j =  1 2
in max i,j =  2 2
in max i,j =  3 2
end of string i,j =  4 2
end of string i,j =  3 3
end of string i,j =  2 3
end of string i,j =  1 3
in max i,j =  0 2
in max i,j =  1 2
in max i,j =  2 2
in max i,j =  3 2
end of string i,j =  4 2
end of string i,j =  3 3
end of string i,j =  2 3
end of string i,j =  1 3
end of string i,j =  0 3
Out[56]: 2
'''
