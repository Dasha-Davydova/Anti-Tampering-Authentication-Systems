Получение сведений о системе
================
Дарья Давыдова

### Системы аутентификации и защиты от несанкционированного доступа

Лабораторная работа №1

### Цель

Вывести информацию о системе

### Исходные данные

1.  ОС Windows 10
2.  RStudio Desktop
3.  Интерпретатор языка R 4.2.2

### План

1.  Выполнить команду system2(“systeminfo”, stdout = TRUE)
2.  Выполнить команду system(“wmic cpu get name”)
3.  Выполнить команду system(“powershell.exe Get-EventLog -LogName
    System -Newest 30”)

### Шаги

1\. Сначала выполним команду system2(“systeminfo”, stdout = TRUE) для
вывода информации о системе

``` r
system2("systeminfo", stdout = TRUE)
```

     [1] ""                                                                                             
     [2] "Host Name:                 LAPTOP-7LOAOALQ"                                                   
     [3] "OS Name:                   Microsoft Windows 11 Home Single Language"                         
     [4] "OS Version:                10.0.22000 N/A Build 22000"                                        
     [5] "OS Manufacturer:           Microsoft Corporation"                                             
     [6] "OS Configuration:          Standalone Workstation"                                            
     [7] "OS Build Type:             Multiprocessor Free"                                               
     [8] "Registered Owner:          huawei"                                                            
     [9] "Registered Organization:   N/A"                                                               
    [10] "Product ID:                00342-40162-00002-AAOEM"                                           
    [11] "Original Install Date:     05.05.2023, 3:39:49"                                               
    [12] "System Boot Time:          22.05.2023, 14:18:50"                                              
    [13] "System Manufacturer:       HUAWEI"                                                            
    [14] "System Model:              HKD-WXX"                                                           
    [15] "System Type:               x64-based PC"                                                      
    [16] "Processor(s):              1 Processor(s) Installed."                                         
    [17] "                           [01]: Intel64 Family 6 Model 140 Stepping 1 GenuineIntel ~3302 Mhz"
    [18] "BIOS Version:              HUAWEI 1.15, 30.11.2021"                                           
    [19] "Windows Directory:         C:\\Windows"                                                       
    [20] "System Directory:          C:\\Windows\\system32"                                             
    [21] "Boot Device:               \\Device\\HarddiskVolume1"                                         
    [22] "System Locale:             ru;Russian"                                                        
    [23] "Input Locale:              ru;Russian"                                                        
    [24] "Time Zone:                 (UTC+03:00) Moscow, St. Petersburg"                                
    [25] "Total Physical Memory:     16 167 MB"                                                         
    [26] "Available Physical Memory: 8 854 MB"                                                          
    [27] "Virtual Memory: Max Size:  19 111 MB"                                                         
    [28] "Virtual Memory: Available: 8 887 MB"                                                          
    [29] "Virtual Memory: In Use:    10 224 MB"                                                         
    [30] "Page File Location(s):     C:\\pagefile.sys"                                                  
    [31] "Domain:                    WORKGROUP"                                                         
    [32] "Logon Server:              \\\\LAPTOP-7LOAOALQ"                                               
    [33] "Hotfix(s):                 5 Hotfix(s) Installed."                                            
    [34] "                           [01]: KB5022505"                                                   
    [35] "                           [02]: KB5014869"                                                   
    [36] "                           [03]: KB5026368"                                                   
    [37] "                           [04]: KB5025316"                                                   
    [38] "                           [05]: KB5007414"                                                   
    [39] "Network Card(s):           3 NIC(s) Installed."                                               
    [40] "                           [01]: Intel(R) Wi-Fi 6 AX201 160MHz"                               
    [41] "                                 Connection Name: Беспроводная сеть"                          
    [42] "                                 DHCP Enabled:    Yes"                                        
    [43] "                                 DHCP Server:     192.168.8.1"                                
    [44] "                                 IP address(es)"                                              
    [45] "                                 [01]: 192.168.8.106"                                         
    [46] "                                 [02]: fe80::9b76:75ee:a5f7:1d7b"                             
    [47] "                           [02]: Bluetooth Device (Personal Area Network)"                    
    [48] "                                 Connection Name: Сетевое подключение Bluetooth"              
    [49] "                                 Status:          Media disconnected"                         
    [50] "                           [03]: VirtualBox Host-Only Ethernet Adapter"                       
    [51] "                                 Connection Name: VirtualBox Host-Only Network"               
    [52] "                                 DHCP Enabled:    No"                                         
    [53] "                                 IP address(es)"                                              
    [54] "                                 [01]: 192.168.56.1"                                          
    [55] "                                 [02]: fe80::e83b:f7a5:8420:7f94"                             
    [56] "Hyper-V Requirements:      VM Monitor Mode Extensions: Yes"                                   
    [57] "                           Virtualization Enabled In Firmware: Yes"                           
    [58] "                           Second Level Address Translation: Yes"                             
    [59] "                           Data Execution Prevention Available: Yes"                          

2\. Далее команда system(“wmic cpu get name”) для вывода информации о
процессоре

``` r
system2("cmd", args = c("/c", "wmic cpu get name"), stdout = TRUE)
```

    [1] "Name                                            \r"
    [2] "11th Gen Intel(R) Core(TM) i7-11370H @ 3.30GHz  \r"
    [3] "\r"                                                

3\. Также выполним команду system(“powershell.exe Get-EventLog -LogName
System -Newest 30”) для вывода логов

``` r
system2("powershell.exe", args = c("Get-EventLog", "-LogName", "System", "-Newest", "30"), stdout = TRUE)
```

     [1] ""                                                                                                                          
     [2] "   Index Time          EntryType   Source                 InstanceID Message                                           "   
     [3] "   ----- ----          ---------   ------                 ---------- -------                                           "   
     [4] "    4337 май 22 15:09  Information Microsoft-Windows...           16 The description for Event ID '16' in Source 'Mi..."   
     [5] "    4336 май 22 15:04  Information Microsoft-Windows...           12 Process C:\\Windows\\System32\\svchost.exe (proces..."
     [6] "    4335 май 22 15:00  Information Microsoft-Windows...           12 Process C:\\Windows\\System32\\svchost.exe (proces..."
     [7] "    4334 май 22 15:00  Information Microsoft-Windows...           12 Process C:\\Windows\\System32\\svchost.exe (proces..."
     [8] "    4333 май 22 15:00  Information Microsoft-Windows...           12 Process C:\\Windows\\System32\\svchost.exe (proces..."
     [9] "    4332 май 22 15:00  Information Microsoft-Windows...           12 Process C:\\Windows\\System32\\svchost.exe (proces..."
    [10] "    4331 май 22 15:00  Information Microsoft-Windows...           12 Process C:\\Windows\\System32\\svchost.exe (proces..."
    [11] "    4330 май 22 15:00  Information Microsoft-Windows...           12 Process C:\\Windows\\System32\\svchost.exe (proces..."
    [12] "    4329 май 22 15:00  Information Microsoft-Windows...           12 Process C:\\Windows\\System32\\svchost.exe (proces..."
    [13] "    4328 май 22 15:00  Information Microsoft-Windows...           12 Process C:\\Windows\\System32\\svchost.exe (proces..."
    [14] "    4327 май 22 15:00  Information Microsoft-Windows...           12 Process C:\\Windows\\System32\\svchost.exe (proces..."
    [15] "    4326 май 22 14:59  Information Microsoft-Windows...           12 Process C:\\Windows\\System32\\svchost.exe (proces..."
    [16] "    4325 май 22 14:32  Information Service Control M...   1073748864 The start type of the Фоновая интеллектуальная ..."   
    [17] "    4324 май 22 14:30  Information Service Control M...   1073748864 The start type of the Фоновая интеллектуальная ..."   
    [18] "    4323 май 22 14:29  Information Microsoft-Windows...           19 Installation Successful: Windows successfully i..."   
    [19] "    4322 май 22 14:29  Information Service Control M...   1073748869 A service was installed in the system....         "   
    [20] "    4321 май 22 14:29  Information Microsoft-Windows...           43 Installation Started: Windows has started insta..."   
    [21] "    4320 май 22 14:29  Information Microsoft-Windows...           44 Windows Update started downloading an update.     "   
    [22] "    4319 май 22 14:24  Information Microsoft-Windows...           12 Process C:\\Windows\\System32\\svchost.exe (proces..."
    [23] "    4318 май 22 14:23  Information Service Control M...   1073748864 The start type of the Фоновая интеллектуальная ..."   
    [24] "    4317 май 22 14:21  Information Microsoft-Windows...           16 The description for Event ID '16' in Source 'Mi..."   
    [25] "    4316 май 22 14:21  Information Service Control M...   1073748869 A service was installed in the system....         "   
    [26] "    4315 май 22 14:20  Warning     DCOM                        10016 The description for Event ID '10016' in Source ..."   
    [27] "    4314 май 22 14:20  Warning     DCOM                        10016 The description for Event ID '10016' in Source ..."   
    [28] "    4313 май 22 14:20  Warning     DCOM                        10016 The description for Event ID '10016' in Source ..."   
    [29] "    4312 май 22 14:20  Error       DCOM                        10010 The description for Event ID '10010' in Source ..."   
    [30] "    4311 май 22 14:19  Warning     DCOM                        10016 The description for Event ID '10016' in Source ..."   
    [31] "    4310 май 22 14:19  Warning     DCOM                        10016 The description for Event ID '10016' in Source ..."   
    [32] "    4309 май 22 14:19  Warning     DCOM                        10016 The description for Event ID '10016' in Source ..."   
    [33] "    4308 май 22 14:19  Warning     Netwtw10               2147489710 6062 - Lso was triggered                          "   
    [34] ""                                                                                                                          
    [35] ""                                                                                                                          

### Оценка результата

В результате лабораторной работы мы получили основную информацию об ОС,
процессоре и логи системы.

### Вывод

Таким образом, мы научились работать с базовыми командами командой
строки и получать информацию об операционной системе.
