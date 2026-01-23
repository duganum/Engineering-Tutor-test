import matplotlib.pyplot as plt
import numpy as np

def render_problem_diagram(prob_id):
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.set_aspect('equal')
    
    # ---------------------------------------------------------
    # 1. Statics (S_1.1 ~ S_1.4)
    # ---------------------------------------------------------
    if prob_id == "S_1.1_1": # 2-Cable Mass
        ax.plot(0, 0, 'ks', markersize=12)
        ax.annotate('', xy=(-2, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='-', lw=2, color='blue'))
        ax.annotate('', xy=(1.5, 1.5), xytext=(0, 0), arrowprops=dict(arrowstyle='-', lw=2, color='green'))
        ax.text(-1.8, 0.2, '$T_A$ (Horiz)')
        ax.text(0.8, 1.0, '$T_B (45^\circ)$')
        ax.annotate('', xy=(0, -1.5), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='red'))
    
    elif prob_id == "S_1.1_2": # Cylinder on Incline
        t = np.radians(30)
        ax.plot([-2, 2], [-2*np.tan(t), 2*np.tan(t)], 'k-', lw=2)
        ax.add_patch(plt.Circle((0, 0.58), 0.5, color='orange', alpha=0.7))
        ax.annotate('', xy=(0.5, 1.45), xytext=(0, 0.58), arrowprops=dict(arrowstyle='->', color='blue', lw=2))
        ax.text(0.3, 1.5, '$N$')

    elif prob_id == "S_1.1_3": # Beam with pin and cable
        ax.plot([-1.5, 1.5], [0, 0], 'k-', lw=4) # Beam
        ax.plot(-1.5, -0.2, 'k^') # Pin A
        ax.annotate('', xy=(1.5, 1.5), xytext=(1.5, 0), arrowprops=dict(arrowstyle='-', color='blue')) # Cable B
        ax.text(-1.7, -0.5, 'Pin A'); ax.text(1.3, 0.8, 'Cable B')

    elif prob_id == "S_1.2_1": # Symmetric Bridge Truss
        nodes = [[0, 0], [1, 1], [2, 0], [3, 1], [4, 0]]
        ax.plot([0, 2, 4, 3, 1, 0], [0, 0, 0, 1, 1, 0], 'k-o')
        ax.annotate('', xy=(2, -1), xytext=(2, 0), arrowprops=dict(arrowstyle='<-', color='red')) # Load at center

    elif prob_id == "S_1.2_2": # Triangle Truss (60 deg)
        ax.plot([0, 2, 1, 0], [0, 0, 1.73, 0], 'k-o', lw=2)
        ax.annotate('', xy=(1, 0.7), xytext=(1, 1.73), arrowprops=dict(arrowstyle='->', color='red'))

    elif prob_id == "S_1.2_3": # Pratt Truss (ZFM focus)
        for x in range(3): ax.plot([x, x+1], [0, 0], 'k-o')
        ax.plot([0, 1, 1, 0], [0, 1, 0, 0], 'k-') # Simplified Pratt unit
        ax.set_title("Pratt Truss Unit")

    elif prob_id == "S_1.3_1": # Centroid - Rectangle
        ax.add_patch(plt.Rectangle((-1, -1.5), 2, 3, fill=False, lw=2))
        ax.plot(0, 0, 'rx'); ax.text(0.1, 0, r'$\bar{y}=3m$')

    elif prob_id == "S_1.3_2": # Square Inertia
        ax.add_patch(plt.Rectangle((-1, -1), 2, 2, facecolor='gray', alpha=0.3))
        ax.axhline(0, color='red', ls='--'); ax.text(1.1, 0, 'X-axis')

    elif prob_id == "S_1.3_3": # Circle Area
        ax.add_patch(plt.Circle((0, 0), 1.5, fill=False, lw=2))
        ax.plot([0, 1.5], [0, 0], 'k-'); ax.text(0.5, -0.3, 'r=0.25m')

    elif prob_id == "S_1.4_1": # Lever Equilibrium
        ax.plot([-2, 2], [0, 0], 'k-', lw=4); ax.plot(0, -0.2, 'k^')
        ax.annotate('', xy=(-1, -1), xytext=(-1, 0), arrowprops=dict(arrowstyle='->', color='red'))
        ax.annotate('', xy=(2, -0.5), xytext=(2, 0), arrowprops=dict(arrowstyle='->', color='blue'))

    elif prob_id == "S_1.4_2": # Cantilever Moment
        ax.fill_between([-2.2, -2], -1, 1, color='gray') # Wall
        ax.plot([-2, 1.5], [0, 0], 'k-', lw=4)
        ax.annotate('', xy=(1.5, -1), xytext=(1.5, 0), arrowprops=dict(arrowstyle='->', color='red'))

    elif prob_id == "S_1.4_3": # Log carrying
        ax.plot([-2, 2], [0, 0], 'brown', lw=8)
        ax.annotate('', xy=(-2, 1), xytext=(-2, 0), arrowprops=dict(arrowstyle='<-', color='green'))
        ax.annotate('', xy=(0.66, 1), xytext=(0.66, 0), arrowprops=dict(arrowstyle='<-', color='blue'))

    # ---------------------------------------------------------
    # 2. Kinematics (K_2.1 ~ K_2.4)
    # ---------------------------------------------------------
    elif "K_2.1" in prob_id: # Rectilinear
        ax.add_patch(plt.Rectangle((-0.5, 0), 1, 0.5, color='blue', alpha=0.5))
        ax.annotate('', xy=(1.5, 0.25), xytext=(0.5, 0.25), arrowprops=dict(arrowstyle='->'))
        ax.text(0.8, 0.6, '$a, v$')

    elif "K_2.2" in prob_id: # Projectile (K_2.2_1, 2, 3)
        x = np.linspace(0, 3, 50)
        y = -x*(x-3) if prob_id != "K_2.2_3" else 2 - 0.2*x**2
        ax.plot(x, y, 'k--')
        if prob_id == "K_2.2_3": ax.plot(0, 2, 'ro') # Cliff fire
        else: ax.annotate('', xy=(0.5, 0.8), xytext=(0,0), arrowprops=dict(arrowstyle='->', color='blue'))

    elif "K_2.3" in prob_id: # Normal/Tangent
        circle = plt.Circle((0,0), 1.5, fill=False, ls='--')
        ax.add_patch(circle)
        ax.annotate('', xy=(1.1, 1.5), xytext=(1.5, 0.9), arrowprops=dict(arrowstyle='->', color='green')) # a_t
        ax.annotate('', xy=(0.5, 0.3), xytext=(1.5, 0.9), arrowprops=dict(arrowstyle='->', color='red')) # a_n

    elif "K_2.4" in prob_id: # Polar (Robotic Arm)
        ax.plot([0, 1.5], [0, 1], 'k-o', lw=3)
        ax.annotate('', xy=(1.8, 1.2), xytext=(1.5, 1), arrowprops=dict(arrowstyle='->', color='blue')) # v_r
        ax.annotate('', xy=(1.2, 1.4), xytext=(1.5, 1), arrowprops=dict(arrowstyle='->', color='orange')) # v_theta

    ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5); ax.axis('off')
    return fig
