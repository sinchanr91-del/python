print("enter marks for four subjects out of hundred")
math = int(input("math = "))
sci = int(input("science = "))
eng = int(input("english = "))
code = int(input("coding = "))
sum = math+sci+eng+code
per = (sum/400)*100
print("total marks = ",sum)
print("percentage = ",per)