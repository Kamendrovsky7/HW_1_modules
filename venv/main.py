from application.salary import calculate_salary as calc
from application.db.people import get_employees as empl
from datetime import datetime
import cowsay


def get_time():
       print (f'Today is: {datetime.today().strftime("%d/%m/%Y Time: %H:%M:%S")}')

def say():
    print(cowsay.get_output_string('meow', "I am a module"))

if __name__ == '__main__':
    
    calc()
    empl()
    get_time()
    say()