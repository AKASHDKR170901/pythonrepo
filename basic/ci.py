print("Enter principal amount:")
p=int(input())
print("Enter rate of interest:")
r=int(input())
print("Enter time:")
t=int(input())
a=p*(pow((1 + r/100),t))
ci=a-p
print("Compound interest:",ci)