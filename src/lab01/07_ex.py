def find_first_index(s: str) -> int | None:
    for i in range(len(s)):
        if s[i].isupper():
            return i
    return

def find_step(capital_index: int, s: str) -> int | None:
    step = 0
    for i in range(capital_index, len(s)):
        step+=1
        if s[i].isdigit():
            return step
    return

def decrypt(s) -> str:
    capital_index = find_first_index(s)
    if capital_index == None:
        raise BaseException("There is no capital character in cypher!")
    
    step = find_step(capital_index, s)
    if step == None:
        raise BaseException("Step cant be None")
    
    final = ""
    for i in range(capital_index, len(s), step):
        final += s[i]
        if s[i] == ".":
            break
        
    return final

print(decrypt(input("in: ")))