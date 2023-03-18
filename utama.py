import random
import sys
import time

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

mengetik("...Hallo, model ini sudah di training oleh author Hendri Mardani...\n\
...Ini adalah NLP deteksi kalimat negatif, netral dan positif.\n\
Contoh Penggunaan:\n\
1.Jangan dibeli barangnya jelek\n\
2.Mending beli ditoko sebelah aja daripada disini")\n
