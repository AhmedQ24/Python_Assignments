x=input("Please enter a sentence: ")
a=tuple(x)
for letter in x:
    if(letter=='B' or letter=='b' or letter=='C' or letter=='c' or letter=='D' or letter=='d' or letter=='F' or
       letter=='f' or letter=='G' or letter=='g' or letter=='J' or letter=='j' or letter=='K' or letter=='k' or
       letter=='L' or letter=='l' or letter=='M' or letter=='m' or letter=='N' or letter=='n' or letter=='P' or
       letter=='p' or letter=='Q' or letter=='q' or letter=='S' or letter=='s' or letter=='T' or letter=='t' or
       letter=='V' or letter=='v' or letter=='X' or letter=='x' or letter=='Z' or letter=='z' or letter=='H' or
       letter=='h' or letter=='R' or letter=='r' or letter=='W' or letter=='w'):
           print(letter + ": is NOT a vowel")
    elif(letter==" "):
             print(letter + ": is a space")
    elif(letter=="!" or letter=='@' or letter=='#' or letter=='$' or letter=='%' or letter=='^' or letter=='&'
         or letter=='*' or letter=='(' or letter==')'):
             print(letter + ": is a special character")
    else:
         continue