n = int(input("N: "))

out = {
    "True": 0,
    "False": 0,
}

for i in range(n):
    inp = input(f"in_{i+1}: ").split()
    
    if len(inp) != 4:
        continue
    if inp[3] not in out:
        continue
    
    out[inp[3]] += 1
    
print(f"out: {" ".join(map(str, out.values()))}")