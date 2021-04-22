from random import seed
import random
from time import sleep

log_file = open('/home/sam/Dev/logio/test-logio/var/logs/test.log', 'a')

for i in range(0, 1000000):
    log_file.write(f'my random: {random.randint(1, 300)}\n')
    sleep(0.00001)

# print(random())
