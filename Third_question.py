#1
import numpy as np

today = np.datetime64('today', 'D')
yesterday = today - np.timedelta64(1, 'D')
tomorrow = today + np.timedelta64(1, 'D')

print("תאריך היום:", today)
print("תאריך אתמול:", yesterday)
print("תאריך מחר:", tomorrow)


#2
encoded = [
    b'\x97\xa8\xa3\x88\x96\x95@\x85\xa7\x85\x99\x83\x89\xa2\x85\xa2',
    b'\xd7\xc8\xd7', 
    b'\x91\x81\xa5\x81', 
    b'\xc3NN'
]

decoded_string = b''.join(encoded).decode('utf-8', errors='ignore')

print("הצופן המפוענח:", decoded_string)
