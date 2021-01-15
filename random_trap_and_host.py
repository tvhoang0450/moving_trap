import os
import time
import random
from datetime import datetime, date
import numpy

def run_opencanary():
	os.system(' sudo ansible-playbook random_opencanary.yml'),

def run_dionaea():
	os.system(' sudo ansible-playbook random_dionaea.yml'),

def run_cowrie():
	os.system(' sudo ansible-playbook random_cowrie.yml'),
def run():
	while(1):
		print("thoi gian cho 30s")
		time.sleep(10)
		os.system(' sudo ansible-playbook remove_container.yml'),
		random_number = random.randint(0,2)
		switcher={
			0: run_opencanary,
                	1: run_dionaea,
			2: run_cowrie
		}
		func = switcher.get(random_number,lambda :"Invalid choice")
		return func()

list_duaration=[]
i = 0
while(i < 30):
	start=datetime.now().timestamp()
	run()
	end=datetime.now().timestamp()
	duaration=end - start - 10	
	list_duaration.append(duaration)
	avr = numpy.average(list_duaration)
	print("thoi gian trien khai bay ", duaration)
	print("so lan trien khai bay ", len(list_duaration))
	print("thoi gian trien khai bay trung binh ", avr)
	print("thoi gian trien khai it nhat ", min(list_duaration))
	print("thoi gian trien khai nhieu nhat ", max(list_duaration))
	i = i+1



