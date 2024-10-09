import numpy as np


x = np.linspace(0, 10, 101)
print(x)

sin_wave = np.sin(x)
cos_wave = np.cos(x)

np.save('task7_sin.npy',sin_wave)
np.save('task7_cos.npy',cos_wave)

print("Sine and cosine waves saved succesfully")
