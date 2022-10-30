import random
jednosci = ["jeden","dwa","trzy","cztery","pięć","sześć","siedem","osiem","dziewięć"]
dziesiatki = ['dwadzieścia','trzydzieści','czterdzieści','pięćdziesiąt','sześćdziesiąt','siedemdziesiąt','osiemdziesiąt','dziewięćdziesiąt']
setki = ['sto','dwieście','trzysta','czterysta','pięćset','sześćset','siedemset','osiemset','dziewięćset']
nastki = ['dziesięć','jedenaście','dwanaście','trzynaście','czternaście','piętnaście','szesnaście','siedemnaście','osiemnaście','dziewiętnaście']
liczba = random.randint(1,999)
#liczba = 600
print(liczba)
if liczba > 99:
    print(setki[((liczba-(liczba%100))//100)-1], end=" ")
if liczba > 9:
    if 9 < liczba%100 < 20:
       print(nastki[(liczba%10)], end=' ')
    elif liczba%100 > 19:
        print(dziesiatki[((liczba%100)-liczba%10)//10 - 2], end=' ')
        if liczba%10 != 0:
            print(jednosci[(liczba%10)-1], end=' ')
    elif liczba%100 < 10 and liczba%10 != 0:
        print(jednosci[(liczba % 10) - 1], end=' ')
elif liczba < 10:
    print(jednosci[(liczba % 10) - 1], end=' ')
