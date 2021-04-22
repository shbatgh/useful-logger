from random import seed
import random
from time import sleep

log_file = open('/home/sam/Dev/logio/test-logio/var/logs/test2.log', 'a')

for i in range(0, 1000000):
    log_file.write(f'pp random: {random.randint(301, 600)}\n')
    sleep(0.001)

# print(random())
