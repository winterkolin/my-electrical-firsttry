v = float(input()) #input the voltage 
r  = float(input()) #input the resistant 
i = v*r 
print(f"current is {i} Amplare")
for i in range(1,10):
    if i > 5 :
        v += 1
    else :
        v += 2 
print(f"current is {i} Amplare")