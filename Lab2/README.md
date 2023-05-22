# Сбор и аналитическая обработка информации о сетевом трафике
Давыдова Дарья BISO-01-20

# Лабораторная работа №2

# Сбор и аналитическая обработка информации о сетевом трафике

### Цель работы

1.  Развить практические навыки использования современного стека
    инструментов сбора и аналитической обработки информации о сетвом
    трафике
2.  Освоить базовые подходы блокировки нежелательного сетевого трафика
3.  Закрепить знания о современных сетевых протоколах прикладного уровня

## Задание

1.  Собрать сетевой трафик (объемом не менее 100 Мб)
2.  Выделить метаинформацию сетевого трафика с помощью утилиты Zeek
3.  Собрать данные об источниках нежелательного трафика, например –
    https://github.com/StevenBlack
4.  Написать программу на любом удобном языке (python, bash, R …),
    котрая подсчитывает процент нежелательного трафика в собранном на
    этапе 1.
5.  Оформить отчет в соответствии с шаблоном

## Ход работы:

### 1 - Сбор сетевого трафика в файл my_trash.pcapng

1.  Использовался сетевой анализатор – Wireshark
2.  Для формирования необходимого объема Интернет был изучен на предмет
    различных “вредных” сайтов.

```  
ls -lah /home/threat_hunting/Lab2/Dasha/data/packets2203.pcap
```

    -rw-r--r-- 1 dasha dasha 597M мая 19 21:50 /home/threat_hunting/Lab2/Dasha/data/packets2203.pcap

### 2 - Выделение метаинформации сетевого трафика с помощью утилиты Zeek

Zeek сортирует метаинформацию о трафике в соответствующие папки по
протоколам. Нас будет интересовать прежде всего папка DNS запросов.

    docker pull zeek/zeek:lts

```  
docker run -w /data -v /home/threat_hunting/Lab2/Dasha/data:/data zeek/zeek:lts zeek -C -r packets2203.pcap
```

### 3 - Сбор данных об источниках нежелательного трафика из репозитория https://github.com/StevenBlack

```  
curl https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts -o hosts
```

      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed

      0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
     52 5814k   52 3055k    0     0  3880k      0  0:00:01 --:--:--  0:00:01 3878k
    100 5814k  100 5814k    0     0  4633k      0  0:00:01  0:00:01 --:--:-- 4636k

### 4 - Подсчет трафика на языке Python

``` python
bad_hosts = [] # нежелательные хосты
with open('hosts') as file:
    for line in file.readlines()[40:]:
        if line[0] == '#':
            continue
        try:
            bad_hosts.append(line.split()[1])
        except IndexError:
            continue
        
hosts = [] # все хосты
with open('dns.log') as file:
    for line in file.readlines():
        if line[0] == '#':
            continue
        try:
            hosts.append(line.split()[9])
        except IndexError:
            continue
```

##### Процент нежелательного трафика:

``` python
bad_count = len([host for host in hosts if host in bad_hosts])
percentile = round(bad_count/len(hosts),3)*100
print("Количество нежелательных хостов: {}.".format(str(bad_count)),
"Процент нежелательного трафика: {}%.".format(str(percentile)),sep='\n')
```

    Количество нежелательных хостов: 613.
    Процент нежелательного трафика: 4.0%.

## Оценка результата

В результате лабораторной работы научились определять нежелательный
трафик.

## Вывод

Таким образом, мы научились анализировать сетевой трафик.
