# libraries
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

# initialize figure
fig, ax = plt.subplots()

#t = np.arange(0, 2*np.pi, 0.001)
#s = np.sin(t)
#line = plt.plot(t, s)

# set correct axis position
ax = plt.axis([0, 2*np.pi, -1, 1])

# starting position of red dot
red_dot, = plt.plot(0, np.sin(0), 'ro')

# movement
def animate(i):
    red_dot.set_data(i, np.sin(i))
    return red_dot,


# create animation
anim = animation.FuncAnimation(fig, animate,
                frames=np.arange(0, 2*np.pi, 0.1), interval=10)
# save animation
anim.save('animation.gif', writer=animation.PillowWriter())
# show animation
plt.show()
