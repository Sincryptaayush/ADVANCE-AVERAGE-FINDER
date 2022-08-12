#scripted by sincryptaayush
#sincryptionop
#advance average finder


from colorama import Fore
from os import system 
system(' clear ')

banner=Fore.GREEN+'''                 __     ___    _  _____ _    _ 
     /\        /\\ \   / / |  | |/ ____| |  | |
    /  \      /  \\ \_/ /| |  | | (___ | |__| |
   / /\ \    / /\ \\   / | |  | |\___ \|  __  |
  / ____ \  / ____ \| |  | |__| |____) | |  | |
 /_/    \_\/_/    \_\_|   \____/|_____/|_|  |_|
                                               
                                               '''

print(banner)

def formula(num1,num2):
	return (num1 + num2)/2

print('\n')

aayush=int(input(Fore.YELLOW+' enter the count to find average of your number ---> '))

list_sum=[ ]

for i in range(1,aayush+1):
	print('\n')
	aayush_one=int(input(Fore.MAGENTA+f' enter the number {i} ------> '))
	aayush_two=int(input(Fore.MAGENTA+f' enter the number {i} ------> '))
	list_sum.append(formula(aayush_one,aayush_two))
	
print('\n')


sum=1
for i in list_sum:
	for ayush in range(0,aayush+1):
		print('\n')
		print(Fore.RED+f' the average of numberset is {sum} === '+Fore.GREEN+ f' {i} ')
		sum= sum+1
		break
		
print('\n')