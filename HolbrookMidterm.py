#This variable will control the loop using the keep going function.
keep_going = 'Y'

def main():
    global keep_going
    while keep_going == 'Y':
        print()
        name = input('Please enter your name: ')
        age = int(input('Please enter your age: '))
        invalidAge(age)
        trafficViolations = int(input('Please enter the number of traffic violations you have recieved: '))
        Code1 = 'High Risk'
        Code2 = 'Moderate Risk'
        Code3 = 'Low Risk'
        Code4 = 'No Risk'
        
#Risk level of the user will be decided here based on traffic violations.
        if trafficViolations == 0:
            risk = Code4
        elif trafficViolations == 1:
            risk = Code3
        elif trafficViolations == 2 or trafficViolations == 3:
            risk = Code2
        else:
            risk = Code1


def price(age, risk, Code1, Code2, Code3, Code4):
        if age < 25 and risk == code1:
            price = 480
        elif age >= 25 and risk == code1:
            price = 410
        elif age < 25 and risk == code2:
            price = 450
        elif age >= 25 and risk == code2:
            price = 390
        elif age < 25 and risk == code2:
            price = 405
        elif age >= 25 and risk == code2:
            price = 365
        elif age < 25 and risk == code3:
            price = 380
        elif age >= 25 and risk == code3:
            price = 315
        elif age < 25 and risk == code4:
            price = 325
        else:
            price = 275

        invalidViolations(violations)
        quote(name, risk, price)
        keep_going = input('If you would like to recieve another quote, please enter Y:')


def invalidAge(age):
    if age < 16 or age > 105:
        print('Invalid: Please enter an age no less than 16 and no greater than 105.')
        age = int(input('Enter your age: '))

def invalidViolations(violations):
    if violations < 0:
        print('Violations must be no less than zero.')
        violations = int(input('Please enter the number of traffic violations you have recieved: '))
    
def output(name, risk, price):
    print(name, 'as a', risk, 'risk driver, your insurance will cost', format(price, '.2f'), sep='')
        
main()
    
