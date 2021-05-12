import random
import time

log_file = open('/home/sam/Dev/useful-logger/test-logio/var/logs/test.log', 'a', 0)

for i in range(0, 100):
    log_file.write(b'my random: {random.randint(1, 300)}\n')
    time.sleep(1)

# print(random())
