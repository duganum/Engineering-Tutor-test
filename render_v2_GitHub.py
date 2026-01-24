import matplotlib.pyplot as plt
import numpy as np
import os
import io

def render_problem_diagram(prob_id):
    pid = str(prob_id).strip()
    
    # Initialize Figure
    fig, ax = plt.subplots(figsize=(4, 3), dpi=150)
    ax.set_aspect('equal')
    found = False

    # ---------------------------------------------------------
    # 1. Statics Logic
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
        found = True
    elif pid == "S_1.1_3":
        ax.plot([-1.5, 1.5], [0, 0], 'k-', lw=4); ax.plot(-1.5, -0.2, 'k^')
        found = True
    elif pid == "S_1.2_1":
        ax.plot([0, 1, 2, 3, 4], [0, 1, 0, 1, 0], 'k-o'); ax.plot([0, 4], [0, 0], 'k-')
        found = True
    elif pid == "S_1.4_1":
        ax.plot([-2, 2], [0, 0], 'k-', lw=4); ax.plot(0, -0.2, 'k^')
        found = True
    elif pid == "S_1.4_2":
        ax.fill_between([-2.2, -2], -1, 1, color='gray'); ax.plot([-2, 1.5], [0, 0], 'k-', lw=4)
        found = True

    # ---------------------------------------------------------
    # 2. Kinematics Logic
    # ---------------------------------------------------------
    elif pid == "K_2.1_1": 
        t = np.linspace(0, 6, 100); v = 20*t**2 - 100*t + 50
        ax.plot(t, v, 'b-')
        ax.set_xlim(0, 6); ax.set_ylim(-80, 200)
        ax.set_aspect('auto')
        found = True
    elif pid == "K_2.1_2": # 2/13: Vertical Projectile (Cliff)
        try:
            img_path = 'images/k212.png'
            if os.path.exists(img_path):
                img = plt.imread(img_path)
                ax.imshow(img)
                h, w = img.shape[:2]
                ax.set_xlim(0, w)
                ax.set_ylim(h, 0)
                # ASPECT RATIO FIX:
                ax.set_aspect('equal')
            else:
                ax.text(0.5, 0.5, "Image File\nNot Found", ha='center')
            found = True
        except Exception as e:
            ax.text(0.5, 0.5, f"Error: {str(e)}", ha='center')
            found = True
    elif pid == "K_2.1_3":
        ax.plot([0, 0.889, 4.0], [0, 22.5, 22.5], 'g-', lw=2)
        ax.set_xlim(-0.5, 4.5); ax.set_ylim(-5, 30)
        ax.set_aspect('auto')
        found = True
    elif pid == "K_2.2_3":
        x = np.linspace(0, 3, 50); y = 2 - 0.2*x**2
        ax.plot(x, y, 'k--'); ax.plot(0, 2, 'ko')
        found = True

    # ---------------------------------------------------------
    # 3. Final Processing
    # ---------------------------------------------------------
    if not found:
        ax.text(0.5, 0.5, f"No Diagram for\n{pid}", color='red', ha='center')
        ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5)

    ax.axis('off')
    plt.tight_layout()

    # Create the buffer
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return buf
