numbers = [5,2,1,7,4]
numbers.append(20) #adiciona o numero
numbers.insert (0, 10) #adiciona o numero na posição
numbers.remove(5) #remove numero
numbers.clear #remove todos
numbers.pop() #remove o ultimo numero
print (numbers.index(4)) #mostra a posição do numero 
print (numbers)
print(50 in numbers) #false result 
print (numbers.count(5)) #conta o numero de 5
numbers.sort() #ordena os numeros 
numbers2 = numbers.copy() #copia as listas 
#exercise
numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers: 
    if number not in uniques: 
        uniques.append(number)
print(uniques)
