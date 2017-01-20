### Lista 4 Ex1

# 'Fizz' se o número for divisível por 3 e não for divisível por 5;
# 'Buzz' se o número for divisível por 5 e não for divisível por 3;
# 'FizzBuzz' se o número for divisível por 3 e por 5;


def fizzbuzz(num):

	div3 = num % 3
	div5 = num % 5


	if div3 == 0 and div5 != 0:
		return "Fizz"
	else:
		if div3 != 0 and div5 == 0:
			return "Buzz"
		else:
			if div3 == 0 and div5 == 0:
				return "FizzBuzz"
			else:
				if div3 != 0 and div5 != 0:
					return num



num = int(input("Digie o num: "))

print(fizzbuzz(num))