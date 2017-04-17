



def lcs_length(sta,stb):
    return subproblem(sta,stb,0,0)

def subproblem(sta,stb,i,j):
    if i == len(sta) or j == len(stb):
        print('end of string i,j = ',i,j)
        return 0
    elif sta[i] == stb[j]:
        print('in equal i,j = ',i,j)
        return 1 + subproblem(sta,stb,i+1,j+1)
    else:
        print('in max i,j = ',i,j)
        return max(subproblem(sta,stb,i+1,j),subproblem(sta,stb,i,j+1))

def subproblem(sta,stb,i,j):
    if i == len(sta) or j == len(stb):
        print('end of string i,j = ',i,j)
        return 0
    elif sta[i] == stb[j]:
        print('in equal i,j = ',i,j)
        val = subproblem(sta,stb,i+1,j+1)
        return 1 + val
    else:
        print('in max i,j = ',i,j)
        a = subproblem(sta,stb,i+1,j)
        b = subproblem(sta,stb,i,j+1)
        return max(a,b)

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
