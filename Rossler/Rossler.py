import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import webbrowser # To open the browser on click

# 1. Equations of the Rössler system
def rossler(t, state, a, b, c):
    x, y, z = state
    dxdt = -y - z
    dydt = x + a * y
    dzdt = b + z * (x - c)
    return [dxdt, dydt, dzdt]

# Parameters (standard chaotic values)
a = 0.2
b = 0.2
c = 5.7

initial_state = [0.1, 0.0, 0.0]
t_span = (0, 250)
t_eval = np.linspace(0, 250, 20000)

# 2. Solving the equations
solution = solve_ivp(rossler, t_span, initial_state, args=(a, b, c), t_eval=t_eval)
x, y, z = solution.y

# 3. Figure and 3D axis setup
fig = plt.figure(figsize=(11, 9), facecolor='#0d0d0d')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('#0d0d0d')

# Matplotlib 3D panel color fix
ax.xaxis.set_pane_color((0.05, 0.05, 0.05, 1.0))
ax.yaxis.set_pane_color((0.05, 0.05, 0.05, 1.0))
ax.zaxis.set_pane_color((0.05, 0.05, 0.05, 1.0))

ax.tick_params(colors='gray', labelsize=8)
ax.set_title("Rössler Attractor", color='#ff66b2', fontsize=22, pad=20, fontname='Georgia', fontweight='bold')

# 4. Plotting the colored 3D graph
ax.scatter(x, y, z, c=np.linspace(0, 1, len(x)), cmap='turbo', s=0.8, alpha=0.6)

# 5. Mathematical formula (LaTeX) - will be on the left side
formula_text = (
    r"$\frac{dx}{dt} = -y - z$" "\n\n"
    r"$\frac{dy}{dt} = x + ay$" "\n\n"
    r"$\frac{dz}{dt} = b + z(x - c)$"
)
fig.text(0.08, 0.15, formula_text, color='#ff66b2', fontsize=13, 
         bbox=dict(facecolor='black', alpha=0.7, edgecolor='#ff66b2', boxstyle='round,pad=1'))

# 6. YouTube channel description story - will be on the right side (no broken emojis)
youtube_text = (
    "  @iqram-visual  \n"
    "-------------------------\n"
    "Unlocking the hidden beauty of math\n"
    "and coding. From complex chaotic\n"
    "attractors to creative visual designs,\n"
    "we turn code into pure art.\n\n"
    "Subscribe for more visual coding magic!"
)
fig.text(0.63, 0.22, youtube_text, color='#00ffcc', fontsize=11, fontname='Arial',
         bbox=dict(facecolor='black', alpha=0.7, edgecolor='#00ffcc', boxstyle='round,pad=1'))

# 7. Subscribe button (clickable text box - tracker property removed)
subscribe_btn = fig.text(0.72, 0.13, "  SUBSCRIBE  ", color='white', fontsize=12, fontweight='bold',
                         fontname='Arial',
                         bbox=dict(facecolor='#ff0000', alpha=0.9, edgecolor='none', boxstyle='round,pad=0.5'))

# Click logic (Event Handler)
def on_click(event):
    if event.inaxes is None and subscribe_btn.get_window_extent().contains(event.x, event.y):
        webbrowser.open("https://www.youtube.com/@iqram-visual")

# Connect mouse click event to the figure
fig.canvas.mpl_connect('button_press_event', on_click)

# view angle
ax.view_init(elev=25, azim=45)

# Graph display
plt.show()