import matplotlib.pyplot as plt
import numpy as np
import os

def render_problem_diagram(prob_id):
    pid = str(prob_id).strip()
    
    # Initialize the small figure
    fig, ax = plt.subplots(figsize=(5, 4), dpi=1000)
    ax.set_aspect('equal')
    found = False

    # ---------------------------------------------------------
    # 1. Statics (S_1.1 ~ S_1.4)
    # ---------------------------------------------------------
    if pid == "S_1.1_1":
        ax.plot(0, 0, 'ks', markersize=15)
        ax.annotate('', xy=(-1.5, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='<-', lw=2, color='blue'))
        ax.annotate('', xy=(1.2, 1.2), xytext=(0, 0), arrowprops=dict(arrowstyle='<-', lw=2, color='green'))
        ax.annotate('', xy=(0, -1.5), xytext=(0, 0), arrowprops=dict(arrowstyle='->', lw=2, color='red'))
        found = True
    elif pid == "S_1.1_2":
        t = np.radians(30); ax.plot([-2, 2], [-2*np.tan(t), 2*np.tan(t)], 'k-', lw=2)
        ax.add_patch(plt.Circle((0, 0.58), 0.5, color='orange', alpha=0.7))
        ax.annotate('', xy=(0.5, 1.45), xytext=(0, 0.58), arrowprops=dict(arrowstyle='->', color='blue', lw=2))
        ax.annotate('', xy=(0, -0.8), xytext=(0, 0.58), arrowprops=dict(arrowstyle='->', color='red', lw=2))
        found = True
    elif pid == "S_1.1_3":
        ax.plot([-1.5, 1.5], [0, 0], 'k-', lw=4); ax.plot(-1.5, -0.2, 'k^')
        ax.annotate('', xy=(1.5, 1.5), xytext=(1.5, 0), arrowprops=dict(arrowstyle='<-', color='blue', lw=2))
        found = True
    elif pid == "S_1.2_1":
        ax.plot([0, 1, 2, 3, 4], [0, 1, 0, 1, 0], 'k-o'); ax.plot([0, 4], [0, 0], 'k-')
        ax.annotate('', xy=(2, -1), xytext=(2, 0), arrowprops=dict(arrowstyle='->', color='red', lw=2))
        found = True
    elif pid == "S_1.2_2":
        ax.plot([0, 2, 1, 0], [0, 0, 1.73, 0], 'k-o', lw=2)
        ax.annotate('', xy=(1, 0.7), xytext=(1, 1.73), arrowprops=dict(arrowstyle='->', color='red', lw=2))
        found = True
    elif pid == "S_1.4_1":
        ax.plot([-2, 2], [0, 0], 'k-', lw=4); ax.plot(0, -0.2, 'k^')
        ax.annotate('', xy=(-1, -1), xytext=(-1, 0), arrowprops=dict(arrowstyle='->', color='red'))
        ax.annotate('', xy=(1.5, 0.75), xytext=(1.5, 0), arrowprops=dict(arrowstyle='->', color='blue'))
        found = True

    # ---------------------------------------------------------
    # 2. Kinematics (K_2.1 ~ K_2.4)
    # ---------------------------------------------------------
    elif pid == "K_2.1_1": 
        t = np.linspace(0, 6, 100)
        v = 20*t**2 - 100*t + 50
        ax.plot(t, v, 'b-')
        ax.plot(2.5, -75, 'ro')
        ax.set_xlim(0, 6); ax.set_ylim(-80, 200)
        ax.set_aspect('auto') # Graphs stay auto to fill the box
        found = True
        
    elif pid == "K_2.1_2": # THE IMAGE FIX
        try:
            img_path = 'images/k212.png'
            if os.path.exists(img_path):
                img = plt.imread(img_path)
                ax.imshow(img)
                height, width = img.shape[:2]
                ax.set_xlim(0, width)
                ax.set_ylim(height, 0)
                
                # REVISION: Force equal aspect and force small size
                ax.set_aspect('equal')
                fig.set_size_inches(2.5, 2, forward=True) 
                ax.axis('off')
            else:
                ax.text(0.5, 0.5, "File Not Found", ha='center')
            found = True
        except Exception as e:
            ax.text(0.5, 0.5, f"Error: {str(e)}", ha='center')
            found = True

    elif pid == "K_2.1_3":
        ax.plot([0, 0.889, 4.0], [0, 22.5, 22.5], 'g-', lw=2)
        ax.set_xlim(-0.5, 4.5); ax.set_ylim(-5, 30)
        ax.set_aspect('auto')
        found = True

    elif pid == "K_2.2_1":
        x = np.linspace(0, 4, 100); y = -0.5*(x-2)**2 + 2
        ax.plot(x, y, 'k--'); ax.plot(2, 2, 'ro')
        ax.annotate('', xy=(2, 2.5), xytext=(2, 2), arrowprops=dict(arrowstyle='<-', color='blue'))
        ax.text(2.1, 2.2, '$H_{max}$'); found = True

    # ... [Other K_2.X logic remains the same] ...

    # --- Final Polish ---
    if not found:
        ax.text(0.5, 0.5, f"No Diagram\n{pid}", color='red', ha='center')
        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-2.5, 2.5)

    ax.axis('off')
    plt.tight_layout()
    return fig
