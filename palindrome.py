def recur(n, string):
    string_r = string[::-1]
    
    if n == len(string)-1:  # Base case
        return True
    
    if string[n] != string_r[n]:
        return False
    
    return recur(n + 1, string)
    
print(recur(0, "rotor"))
print(recur(0, "abc"))
