import datetime


def miladi_to_shamsi(gy, gm, gd,yy,mm,dd):
 g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
 if (gm > 2):
  gy2 = gy + 1
 else:
  gy2 = gy
 days = 355666 + (365 * gy) + ((gy2 + 3) // 4) - ((gy2 + 99) // 100) + ((gy2 + 399) // 400) + gd + g_d_m[gm - 1]
 jy = -1595 + (33 * (days // 12053))
 days %= 12053
 jy += 4 * (days // 1461)
 days %= 1461
 if (days > 365):
  jy += (days - 1) // 365
  days = (days - 1) % 365
 if (days < 186):
  jm = 1 + (days // 31)
  jd = 1 + (days % 31)
 else:
  jm = 7 + ((days - 186) // 30)
  jd = 1 + ((days - 186) % 30)
 
 print(jy,jm,jd)
 yy=int(yy)
 mm=int(mm) 
 dd=int(dd)
 
 if(jd < dd):
    jm-=1
    jd+=30
        
 if(jm < mm):
    jm += 12
    jy -= 1
 """
 if (jd < dd):
     dd=dd-jd
 else:
     dd = jd - dd
 """

 yy = jy - yy
 mm = jm - mm
 dd = jd - dd
 

 if yy>=1:
    h=yy*362*24
    min=h*60
    sec=min*60
 else :
     if mm>=1:
        h=mm*7*24
        min=h*60
        sec=min*60
     else:
        h=dd*24
        min=h*60
        sec=min*60 

 return print("you live for ", yy ," years  ", mm ," month ", dd," day ", h ," hours ",min," minutes and ",sec," seconds . ")

x = datetime.datetime.now()
y=x.year
m=x.month
d=x.day
a=input("enter the date of your birthday : ( year month day )")
yy,mm,dd=a.split("/")
miladi_to_shamsi(y,m,d,yy,mm,dd)
