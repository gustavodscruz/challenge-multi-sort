#pip install pandas
# só para criar o arquivo
import random
num = 0
lista = []
sep = ', '
while num < 100000:
    lista.append(str(random.randint(1, 100000)))
    num +=1

result = sep.join(lista)

with open ('numbers.txt', 'w') as file:
    file.write(result)
    
# pd.to_csv('/numbers.txt', index=False)

# arquivo =  pd.read_csv('/numbers.txt', sep=',')
