import sys
import random
from datetime import datetime
import time
from colorama import init
init()
from colorama import Fore, Back, Style

while True:
	print("Меню")
	print(Fore.GREEN + "1) Старт", Style.RESET_ALL)
	print(Fore.YELLOW + "2) Информация", Style.RESET_ALL)
	print(Fore.RED + "3) Выход", Style.RESET_ALL)
	what = input("\nВведите номер действия: ")

	if what == "3":
		print("\n", Back.RED, Fore.WHITE + "Выход...", Style.RESET_ALL)
		time.sleep(3)
		sys.exit()

	elif what == "2":
		print("""

	██╗░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░░░░  ░██╗░░░░░░░██╗░█████╗░██████╗░██╗░░░░░██████╗░██╗
	██║░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗░░░  ░██║░░██╗░░██║██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║
	███████║█████╗░░██║░░░░░██║░░░░░██║░░██║░░░  ░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░░░░██║░░██║██║
	██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║██╗  ░░████╔═████║░██║░░██║██╔══██╗██║░░░░░██║░░██║╚═╝
	██║░░██║███████╗███████╗███████╗╚█████╔╝╚█║  ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║███████╗██████╔╝██╗
	╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░░╚╝  ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝
			""")
		print("Привет. Это небольшая игра, в ней нужно убить врага.\nУрон начисляется если правильно решен простой математический пример.\n\nЭта игра - лишь моя практика в Python ^^\n")
		print("------------------------")

	elif what == "1":
		name = input("\nВведите имя вашего героя: ")
		print("\nИ так,", name.capitalize(), "отправился в путешествие. На пути ему встретился огромный троль.",name.capitalize(),"тут же схватил палку и начался бой.")
		print(Fore.GREEN + "\nНажмите Enter для продолжения..." + Style.RESET_ALL)
		input()

		troll = 5
		heroy = 3

		print("\nЗа каждый верно решенный пример, вы наносите врагу урон (",Fore.RED + "1 ед." + Style.RESET_ALL, ")")
		print("В противном случаи, враг наносит урон вам (",Fore.RED + "1 ед." + Style.RESET_ALL, ")")
		print(Fore.GREEN + "\nНажмите Enter для продолжения..." + Style.RESET_ALL)
		input()

		print("\nВаше здоровье:", Fore.GREEN + " 3 ед." + Style.RESET_ALL)
		print("\nЗдоровье врага:", Fore.RED + "5 ед.")
		print(Fore.GREEN + "\nНажмите Enter для старта...\n" + Style.RESET_ALL)
		input()

		while True:
			a = random.randrange(1,10)
			b = random.randrange(1,10)
			res = a + b
			print("Решите простой пример: ", Fore.YELLOW , a, "+", b, Style.RESET_ALL)
			try:
				time = datetime.now()
				user = int(input("Ответ: "))
				if res == user:
					print(Fore.GREEN + "\nВерно!",Style.RESET_ALL)
					print(Back.WHITE, Fore.BLACK,"Время ответа: ", datetime.now() - time, Style.RESET_ALL,"\n")
					troll -= 1
				else:
					print(Fore.RED + "\nНеверно!\n", Style.RESET_ALL)
					heroy -= 1
			except ValueError:
				print("\n", Back.RED, Fore.WHITE + "ОШИБКА! Введите число!",Style.RESET_ALL, "\n")

			if troll == 0:
				print("\n" + Fore.GREEN + "Вы победили! Враг повержен!",Style.RESET_ALL,)
				print("Game Over.\n\n")
				print("------------------------")
				break
			if heroy == 0:
				print("\n" + Fore.RED + "Вы проиграли!",Style.RESET_ALL)
				print("Game Over.\n\n")				
				print("------------------------")
				break