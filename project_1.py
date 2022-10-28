def task_1(s1='В чащах юга жил бы цитрус? Да, но фальшивый экземпляр!\n',
           s2='Пиши: зять съел яйцо, ещё чан брюквы… эх! Ждем фигу!'):
    with open('test.txt', 'w+', encoding='utf8') as f:
        f.write(s1)
    with open('test.txt', 'a+', encoding='utf8') as f:
        f.write(s2)
    with open('test.txt', 'r+', encoding='utf8') as f:
        s = f.readlines()
        for n in range(len(s)):
            print(s[n])