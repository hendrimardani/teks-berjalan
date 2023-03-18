import random
import sys
import time

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

mengetik("...Hallo, Model ini sudah di training oleh author Hendri Mardani...\n...ini adalah NLP deteksi kalimat negatif, netral dan positif.")