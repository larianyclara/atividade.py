A = 10
B = 15
C = 20

if A>B and A>C and B>C:
    print("A,B,C")
elif A>B and A>C and C>B:
    print("A,C,B")
elif B>A and B>C and A>C:
    print("B,A,C")
elif B>A and B>C and C>A:
    print("B,C,A")
elif C>A and C>B and A>B:
    print("C,A,B")
elif C>A and C>B and B>A:
    print("C,B,A")
