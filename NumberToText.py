# Converting integers to text, ex. 123 - One Hundred Twenty Three


tens = {1 : ' One',
        2 : ' Two',
		3 : ' Three',
		4 : ' Four',
		5 : ' Five',
		6 : ' Six',
		7 : ' Seven',
		8 : ' Eight',
		9 : ' Nine',
		10 : ' Ten',
		11 : ' Eleven',
		12 : ' Twelve',
		13 : ' Thirteen',
		14 : ' Fourteen',
		15 : ' Fifteen',
		16 : ' Sixteen',
		17 : ' seventeen',
		18 : ' Eighteen',
		19 : ' Ninteen',
		20 : ' Twenty',
		30 : ' Thirty',
		40 : ' Forty',
		50 : ' Fifty',
		60 : ' Sixty',
		70 : ' Seventy',
		80 : ' Eighty',
		90 : ' Ninty'}
		
		
		
Rest = {1000 : ' Thousand',
		1000000 : ' Million',
		1000000000 : ' Billion'}

hundreds = {10 : ' Ten',
            100 : ' Hundred'}

def pr_hundreds(x):
    # calls here if x mod 1000 is greater that 0
    s = ''
    if int(x/100) > 0:
        s = s + tens[int(x/100)] + hundreds[100]
        x = int(x % 100)
    if x > 0 and x > 19:
        s = s + tens[int(x/10)*10]
        x =int(x%10)
    if x > 0 and x < 19:
        s = s + tens[int(x)]

    return(s)

def convert_to_Text(n):
    text = ''
    for d in list(Rest.keys())[::-1]:
        if int(n/d) != 0:
            text = text + pr_hundreds(int(n/d)) + Rest[d]
            n = int(n%d)
    text = text + pr_hundreds(int(n))
    print(text)

while True:
    try:
        number = int(input('Enter a number : '))
    except ValueError as e:
        print(f'{e} - Try again or enter 0')
        continue
    if number == 0:
        break
    convert_to_Text(number)
