import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.arange(0, 100)
y = x * 2
z = x ** 2

plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.plot(x, y, color='blue', marker='o', linestyle='-', linewidth=2, label='y = x * 2')
plt.plot(x, z, color='green', marker='s', linestyle='--', linewidth=2, label='z = x^2')
plt.title('Всі лінії на одному графіку')
plt.xlabel('Вісь X')
plt.ylabel('Вісь Y')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x, y, color='blue', marker='o', linestyle='-', linewidth=2, label='y = x * 2')
plt.title('Лінії на різних графіках')
plt.xlabel('Вісь X')
plt.ylabel('Вісь Y')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(x, z, color='green', marker='s', linestyle='--', linewidth=2, label='z = x^2')
plt.title('Лінії на різних графіках')
plt.xlabel('Вісь X')
plt.ylabel('Вісь Y')
plt.legend()

plt.tight_layout()
plt.show()


with open('test.txt', 'r') as file:
    lines = file.readlines()

xx = [float(line.split()[0]) for line in lines]
yy = [float(line.split()[1]) for line in lines]

plt.plot(xx, yy, marker='o', linestyle='-')

plt.title('Лінія з файлу')
plt.xlabel('Вісь X')
plt.ylabel('Вісь Y')

plt.show()
