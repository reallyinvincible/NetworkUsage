import psutil
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
style.use("dark_background")
net_down = [0 for i in range(50)]
net_up = [0 for i in range(50)]
fig1 = plt.figure()
ax2 = plt.subplot(212)
ax1 = plt.subplot(211)
time = -50

def animate_cpu(i):
    global time,net_down, net_up
    ax1.clear()
    ax2.clear()
    net_down = net_down[1:]
    net_up = net_up[1:]
    net_down.append(psutil.net_io_counters()[1]/(1024*1024))
    net_up.append(psutil.net_io_counters()[0]/(1024*1024))
    ax1.plot([i for i in range(time, time+50)], net_down)
    ax1.set_ylabel("Downloaded Data")
    ax2.plot([i for i in range(time, time+50)], net_up)
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Uploaded Data")
    time += 1

ani_cpu = animation.FuncAnimation(fig1, animate_cpu, interval=1000)
plt.show()