immutabl_var_=([1,2,3,4,5],"вышел","зайчик","погулять")
print(immutabl_var_)
immutabl_var_=([1,2,3,4,5],"вышел","зайчик","погулять")
mutable_list=[[0.07],"Bond","Jemes","Bond",True]#при потытке изменения значения кортежа выходит ошибка, потому что неизменяемость является особенностью кортежа
print(mutable_list)
print(mutable_list*2)