import matplotlib.pyplot as plt

times = [19.242268, 18.663658, 18.885113, 19.889281, 36.200852, 92.869016]

threads = [10000, 100000, 1000000, 10000000, 100000000, 1000000000]

t1 = times[0]

speedup = [t1 / t for t in times]

fig, ax = plt.subplots()

ax.plot(threads, speedup, marker='o')

ax.set_xlabel('THRESHOLD')
ax.set_ylabel('Коэффициент ускорения (S)')
ax.set_title('Зависимость коэффициента ускорения от THRESHOLD')
ax.grid(True)

plt.savefig('график3.png')

plt.show()
