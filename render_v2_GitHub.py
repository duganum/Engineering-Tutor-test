import matplotlib.pyplot as plt
import numpy as np

def render_problem_diagram(prob_id):
    # 1. ID 문자열 전처리 (공백 제거 및 확실한 문자열 변환)
    pid = str(prob_id).strip()
    
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.set_aspect('equal')
    found = False

    # ---------------------------------------------------------
    # 1. Statics (S_1.1 ~ S_1.4)
    # ---------------------------------------------------------
    
    # --- S_1.1: Free Body Diagrams ---
    if pid == "S_1.1_1":
        ax.plot(0, 0, 'ks', markersize=12)
        ax.annotate('', xy=(-2, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='-', lw=2, color='blue'))
        ax.annotate('', xy=(1.5, 1.5), xytext=(0, 0), arrowprops=dict(arrowstyle='-', lw=2, color='green'))
        ax.text(-1.8, 0.2, '$T_A$')
        ax.text(0.8, 1.0, '$T_B (45^\circ)$')
        ax.annotate('', xy=(0, -1.5), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='red'))
        found = True

    elif pid == "S_1.1_2":
        t = np.radians(30)
        ax.plot([-2, 2], [-2*np.tan(t), 2*np.tan(t)], 'k-', lw=2)
        ax.add_patch(plt.Circle((0, 0.58), 0.5, color='orange', alpha=0.7))
        ax.annotate('', xy=(0.5, 1.45), xytext=(0, 0.58), arrowprops=dict(arrowstyle='->', color='blue', lw=2))
        ax.text(0.3, 1.5, '$N$')
        found = True

    elif pid == "S_1.1_3":
        ax.plot([-1.5, 1.5], [0, 0], 'k-', lw=4)
        ax.plot(-1.5, -0.2, 'k^')
        ax.annotate('', xy=(1.5, 1.5), xytext=(1.5, 0), arrowprops=dict(arrowstyle='-', color='blue'))
        ax.text(-1.7, -0.5, 'Pin A'); ax.text(1.3, 0.8, 'Cable B')
        found = True

    # --- S_1.2: Trusses ---
    elif pid == "S_1.2_1":
        ax.plot([0, 2, 4, 3, 1, 0], [0, 0, 0, 1, 1, 0], 'k-o')
        ax.annotate('', xy=(2, -1), xytext=(2, 0), arrowprops=dict(arrowstyle='<-', color='red'))
        found = True

    elif pid == "S_1.2_2":
        ax.plot([0, 2, 1, 0], [0, 0, 1.73, 0], 'k-o', lw=2)
        ax.annotate('', xy=(1, 0.7), xytext=(1, 1.73), arrowprops=dict(arrowstyle='->', color='red'))
        found = True

    elif pid == "S_1.2_3":
        for x in range(3): ax.plot([x, x+1], [0, 0], 'k-o')
        ax.plot([0, 1, 1, 0], [0, 1, 0, 0], 'k-')
        ax.set_title("Pratt Truss Unit")
        found = True

    # --- S_1.3: Geometric Properties ---
    elif pid == "S_1.3_1":
        ax.add_patch(plt.Rectangle((-1, -1.5), 2, 3, fill=False, lw=2))
        ax.plot(0, 0, 'rx'); ax.text(0.1, 0, r'$\bar{y}=3m$')
        found = True

    elif pid == "S_1.3_2":
        ax.add_patch(plt.Rectangle((-1, -1), 2, 2, facecolor='gray', alpha=0.3))
        ax.axhline(0, color='red', ls='--')
        found = True

    elif pid == "S_1.3_3":
        ax.add_patch(plt.Circle((0, 0), 1.5, fill=False, lw=2))
        ax.plot([0, 1.5], [0, 0], 'k-')
        found = True

    # --- S_1.4: Equilibrium ---
    elif pid == "S_1.4_1":
        ax.plot([-2, 2], [0, 0], 'k-', lw=4); ax.plot(0, -0.2, 'k^')
        ax.annotate('', xy=(-1, -1), xytext=(-1, 0), arrowprops=dict(arrowstyle='->', color='red'))
        ax.annotate('', xy=(2, -0.5), xytext=(2, 0), arrowprops=dict(arrowstyle='->', color='blue'))
        found = True

    elif pid == "S_1.4_2":
        ax.fill_between([-2.2, -2], -1, 1, color='gray')
        ax.plot([-2, 1.5], [0, 0], 'k-', lw=4)
        ax.annotate('', xy=(1.5, -1), xytext=(1.5, 0), arrowprops=dict(arrowstyle='->', color='red'))
        found = True

    elif pid == "S_1.4_3":
        ax.plot([-2, 2], [0, 0], color='brown', lw=8) # Log
        ax.annotate('', xy=(-2, 1), xytext=(-2, 0), arrowprops=dict(arrowstyle='<-', color='green', lw=2))
        ax.text(-2.2, 1.2, '$F_A$', color='green')
        ax.annotate('', xy=(0.67, 1), xytext=(0.67, 0), arrowprops=dict(arrowstyle='<-', color='blue', lw=2))
        ax.text(0.5, 1.2, '$F_B$', color='blue')
        ax.annotate('', xy=(0, -1), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='red', lw=2))
        ax.text(-0.3, -1.3, '$W$', color='red')
        found = True

    # ---------------------------------------------------------
    # 2. Kinematics (K_2.1 ~ K_2.4)
    # ---------------------------------------------------------
    elif "K_2.1" in pid:
        ax.add_patch(plt.Rectangle((-0.5, 0), 1, 0.5, color='blue', alpha=0.5))
        ax.annotate('', xy=(1.5, 0.25), xytext=(0.5, 0.25), arrowprops=dict(arrowstyle='->'))
        found = True

    elif "K_2.2" in pid:
        x = np.linspace(0, 3, 50)
        y = -x*(x-3) if pid != "K_2.2_3" else 2 - 0.2*x**2
        ax.plot(x, y, 'k--')
        if pid == "K_2.2_3": ax.plot(0, 2, 'ro')
        else: ax.annotate('', xy=(0.5, 0.8), xytext=(0,0), arrowprops=dict(arrowstyle='->', color='blue'))
        found = True

    elif "K_2.3" in pid:
        circle = plt.Circle((0,0), 1.5, fill=False, ls='--')
        ax.add_patch(circle)
        ax.annotate('', xy=(1.1, 1.5), xytext=(1.5, 0.9), arrowprops=dict(arrowstyle='->', color='green'))
        ax.annotate('', xy=(0.5, 0.3), xytext=(1.5, 0.9), arrowprops=dict(arrowstyle='->', color='red'))
        found = True

    elif "K_2.4" in pid:
        ax.plot([0, 1.5], [0, 1], 'k-o', lw=3)
        ax.annotate('', xy=(1.8, 1.2), xytext=(1.5, 1), arrowprops=dict(arrowstyle='->', color='blue'))
        ax.annotate('', xy=(1.2, 1.4), xytext=(1.5, 1), arrowprops=dict(arrowstyle='->', color='orange'))
        found = True

    # --- 에러 핸들링 (ID를 찾지 못했을 때) ---
    if not found:
        ax.text(0, 0, f"No Diagram for ID: {pid}", color='red', ha='center')
        ax.set_xlim(-1, 1); ax.set_ylim(-1, 1)

    ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5); ax.axis('off')
    return fig
