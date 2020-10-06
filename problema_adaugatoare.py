n=int(input("dati o suma de bani:"))
b_1000=n//1000
b_500=(n%1000)//500
b_200=((n%1000)%500)//200
b_100=(((n%1000)%500)%200)//100
b_50=((((n%1000)%500)%200)%100)//50
b_20=(((((n%1000)%500)%200)%100)%50)//20
b_10=((((((n%1000)%500)%200)%100)%50)%20)//10
b_5=(((((((n%1000)%500)%200)%100)%50)%20)%10)//5
b_2=((((((((n%1000)%500)%200)%100)%50)%20)%10)%5)//2
b_1=(((((((((n%1000)%500)%200)%100)%50)%20)%10)%5)%2)//1
print("Va fi nevoie de " 
,b_1000,"bancnote de o mie de lei;" 
,b_500,"bancnote de cincisute de lei;" 
,b_200,"bancnote de doua sute lei;" 
,b_100,"bancnote de o suta de lei;" 
,b_50,"bancnote de cinci zeci lei;" 
,b_20,"bancnote de doua zeci lei;" 
,b_10,"bancnote de zece lei;" 
,b_5,"bancnote de cinci lei;" 
,b_2,"bancnote de 2 lei;" 
,b_1,"bancnote de ul leu;")
