from enviroplus.noise import Noise

noise = Noise()

while True:
    low, mid, high, amp = noise.get_noise_profile()
    low *= 128
    mid *= 128
    high *= 128
    amp *= 64
    print(int(low),int(mid),int(high),amp)