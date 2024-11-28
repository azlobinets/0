#2
immutable_var=([0,1,2,3],4,5,(6,7),"home",True)

#3
print(immutable_var)

#4
# immutable_var[0]=[8,9,10,11] // Не сработает, т.к. нельзя вместо элемента кортежа поместить другой элемент.

#5
mutable_list=[[0,1,2,3],4,5,(6,7),"home",True]
mutable_list[0]="house"
print(mutable_list)