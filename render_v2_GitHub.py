import matplotlib.pyplot as plt
import numpy as np

def render_problem_diagram(prob_id):
    """
    문제 ID를 입력받아 Matplotlib을 이용해 공학적 다이어그램을 생성합니다.
    """
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.set_aspect('equal')
    
    # --- 1. Statics: Free Body Diagram (S_1.1_1 ~ S_1.1_3) ---
    if prob_id == "S_1.1_1":
        # 50kg Mass suspended by two cables
        ax.plot(0, 0, 'ks', markersize=15) # Mass
        ax.annotate('', xy=(-2, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='-', lw=2, color='blue')) # Cable A
        ax.annotate('', xy=(1.5, 1.5), xytext=(0, 0), arrowprops=dict(arrowstyle='-', lw=2, color='green')) # Cable B
        ax.text(-1.8, 0.2, '$T_A$ (Horizontal)', color='blue')
        ax.text(0.8, 1.0, '$T_B$ ($45^\circ$)', color='green')
        ax.annotate('', xy=(0, -1.5), xytext=(0, 0), arrowprops=dict(arrowstyle='->', lw=1.5, color='red'))
        ax.text(0.1, -1.3, '$W=50kg$', color='red')

    elif prob_id == "S_1.1_2":
        # 20kg Cylinder on 30-degree incline
        theta = np.radians(30)
        # Slope
        ax.plot([-2, 2], [-2*np.tan(theta), 2*np.tan(theta)], 'k-', lw=2)
        # Cylinder
        circle = plt.Circle((0, 0.6), 0.5, color='orange', alpha=0.7)
        ax.add_patch(circle)
        # Normal Force
        ax.annotate('', xy=(0.5, 1.46), xytext=(0, 0.6), arrowprops=dict(arrowstyle='->', color='blue', lw=2))
        ax.text(0.3, 1.5, '$N$', color='blue', fontsize=12)
        ax.text(-1.5, -0.5, '$30^\circ$', fontsize=10)

    # --- 2. Statics: Truss (S_1.2_1 ~ S_1.2_2) ---
    elif "S_1.2" in prob_id:
        # Simple Triangle Truss
        nodes = np.array([[0, 0], [2, 0], [1, 1.732]])
        ax.plot([0, 2, 1, 0], [0, 0, 1.732, 0], 'k-o', lw=3)
        ax.annotate('', xy=(1, 0.5), xytext=(1, 1.732), arrowprops=dict(arrowstyle='->', color='red', lw=2))
        ax.text(1.1, 1.5, 'Load', color='red')
        ax.text(0, -0.3, 'Support A')
        ax.text(1.5, -0.3, 'Support B')

    # --- 3. Kinematics: Projectile Motion (K_2.2_1 ~ K_2.2_3) ---
    elif "K_2.2" in prob_id:
        # Projectile Trajectory
        x = np.linspace(0, 4, 100)
        y = -0.5 * (x-2)**2 + 2
        ax.plot(x, y, 'k--', alpha=0.5)
        ax.annotate('', xy=(0.5, 0.5), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='blue', lw=2))
        ax.text(0.1, 0.6, '$v_0, \\theta$', color='blue')
        ax.plot(0, 0, 'ro') # Ball
        ax.set_title("Projectile Motion Path")

    # --- 4. Kinematics: Normal/Tangent & Polar (K_2.3_1, K_2.4_1) ---
    elif "K_2.3" in prob_id or "K_2.4" in prob_id:
        # Circular Path / Robotic Arm
        circle = plt.Circle((0, 0), 1.5, color='gray', fill=False, ls='--')
        ax.add_patch(circle)
        ax.plot([0, 1.06], [0, 1.06], 'k-o', lw=3) # Arm
        ax.annotate('', xy=(0.5, 1.5), xytext=(1.06, 1.06), arrowprops=dict(arrowstyle='->', color='green'))
        ax.text(0.8, 1.3, '$a_n$', color='green')
        ax.text(0.2, 0.5, '$r, \\theta$')

    # 공통 레이아웃 정리
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.axis('off')
    plt.tight_layout()
    return fig

