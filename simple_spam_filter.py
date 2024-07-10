'''A spam comment is defined as a text containing following keywords:
'Make a lot of money', 'buy now', 'subscribe this', 'click this'. Write a program to detect these spams.'''

p1 = 'Make a lot of money'.lower()
p2 = 'Buy now'.lower()
p3 = 'Subscribe this'.lower()
p4 = 'Click this'.lower()

msg = input('Enter Your Comment: ').lower()

if (p1 in msg or p2 in msg or p3 in msg or p4 in msg):
    print('SPAM!')
else:
    print('Valid comment')