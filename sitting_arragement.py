import random
Genders=['Boys','Girls']
Seats=['Window Side','Wall Side']
date=input('Date: ')
subject=input('Subject: ')
timing=input('time: ')
print('-'*10)
print(f''' *Date:* {date}
*Subject:* {subject}
*Timing:* {timing}
*Sitting Arrangement:* Window Side-{random.choice(Genders)}''')
