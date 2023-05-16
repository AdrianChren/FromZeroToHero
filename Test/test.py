print("hello word")

# rad cisel
i = 1
while i < 6:
    print(i)
    i += 1
    
#rad cisel inak
for x in range (6):
    print(x)
 
# rad cisel, s podmienkou do ktoreho cisla   
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
  
# rad cisel, s podmienkou vynechania vybraneho cisla    
i = 0
while i < 6:
     i += 1
     if i == 3:
         continue
     print (i)     
     
# rad cisel, s podmienkou do ktoreho cisla 
i = 1
while i <6:
    print (i)
    i += 1
else:
    print ("i nie je nadalej menej nez 6")
    
mylist = []
mylist.append(1)
mylist.append(2)
for item in mylist:
    print(item) # vysledok 1+2
    
num = 200
if num > 0:
    print("Num je vacsie ako nula")
else:
    print("Num je mensie nez nula")
    
#volanie funkcie
def my_function():
    print("Cau funkcia")

my_function()

#link suboru
#   with open("subor.txt", "r", encoding='utf8') as file: #r-read, a-append, w-write, c-create
#    for line in file:
#        print(line)
        
#priemer average
from statistics import mean

inp_lst = [12,4,15,52,58,65,48,85,23]

sum_lst = sum(inp_lst)

lst_avg = sum_lst/len(inp_lst)
print("Priemer hodnot z listu je:\n")
print(lst_avg)
print("Priemer hodnot z listu na 3 desatine miesta je:\n")
print(round(lst_avg,3))

#median
import statistics

print(statistics.median([1, 3, 5, 7, 9, 11, 13]))