
sec=int (input("insert second :"))

hour=int (sec/3600)
sec=sec%3600
min=int (sec/60)
sec=sec%60
print(str(hour).zfill(2) ,":" , str(min).zfill(2) , ":", str(sec).zfill(2) )