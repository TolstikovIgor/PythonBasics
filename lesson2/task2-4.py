list_words = [str(i) for i in input('Введите через пробел несколько слов: ').split()]
i = 1;
for word in list_words:
    print(f'#{i}: {word[0:10:1]}')
    i+=1
