import matplotlib.pyplot as plt
import numpy as np

def render_problem_diagram(prob_id):
    pid = str(prob_id).strip()
    fig, ax = plt.subplots(figsize=(2, 1))
    ax.set_aspect('equal')
    found = False

    # ---------------------------------------------------------
    # 1. Statics (S_1.1 ~ S_1.4) - 기존 코드 유지
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
    elif pid == "S_1.2_3":
        for x in range(3): ax.plot([x, x+1], [0, 0], 'k-o')
        ax.plot([0, 1, 1, 0], [0, 1, 0, 0], 'k-'); found = True
    elif "S_1.3" in pid:
        if "1" in pid or "2" in pid: ax.add_patch(plt.Rectangle((-1, -1.5), 2, 3, fill=False, lw=2)); ax.plot(0, 0, 'rx')
        else: ax.add_patch(plt.Circle((0, 0), 1.5, fill=False, lw=2))
        found = True
    elif pid == "S_1.4_1":
        ax.plot([-2, 2], [0, 0], 'k-', lw=4); ax.plot(0, -0.2, 'k^')
        ax.annotate('', xy=(-1, -1), xytext=(-1, 0), arrowprops=dict(arrowstyle='->', color='red'))
        ax.annotate('', xy=(1.5, 0.75), xytext=(1.5, 0), arrowprops=dict(arrowstyle='->', color='blue'))
        found = True
    elif pid == "S_1.4_2":
        ax.fill_between([-2.2, -2], -1, 1, color='gray'); ax.plot([-2, 1.5], [0, 0], 'k-', lw=4)
        ax.annotate('', xy=(1.5, -1), xytext=(1.5, 0), arrowprops=dict(arrowstyle='->', color='red'))
        found = True
    elif pid == "S_1.4_3":
        ax.plot([-2, 2], [0, 0], color='brown', lw=8)
        ax.annotate('', xy=(-2, 1), xytext=(-2, 0), arrowprops=dict(arrowstyle='->', color='green', lw=2))
        ax.annotate('', xy=(0.67, 1), xytext=(0.67, 0), arrowprops=dict(arrowstyle='->', color='blue', lw=2))
        ax.annotate('', xy=(0, -1), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='red', lw=2))
        found = True

    # ---------------------------------------------------------
    # 2. Kinematics (K_2.1 ~ K_2.4) - 개별 분리 수정
    # ---------------------------------------------------------
    
# ... inside your function ...

    elif pid == "K_2.1_1": 
        t = np.linspace(0, 6, 100)
        v = 20*t**2 - 100*t + 50
        ax.plot(t, v, 'b-')
        ax.plot(2.5, -75, 'ro')
        ax.set_xlim(0, 6); ax.set_ylim(-80, 200) # Tailored limits
        ax.set_aspect('auto') # Graphs shouldn't be equal aspect
        found = True
        
    elif pid == "K_2.1_2": # 2/13: Vertical Projectile (Cliff)
        import os
        try:
            img_path = 'images/k212.png'
            if os.path.exists(img_path):
                img = plt.imread(img_path)
                
                # 1. Display the image
                ax.imshow(img)
                
                # 2. CRITICAL: Set limits to the image size (pixels)
                # This prevents the global '(-2.5, 2.5)' from hiding it
                height, width = img.shape[:2]
                ax.set_xlim(0, width)
                ax.set_ylim(height, 0) # Normal image orientation
                
                # 3. Force 'auto' aspect so it fills the figure space
                # ax.set_aspect('auto')
                ax.axis('off')
            else:
                ax.text(0.5, 0.5, "File Not Found", ha='center')
            
            found = True
        except Exception as e:
            ax.text(0.5, 0.5, f"Error: {str(e)}", ha='center')
            found = True

    elif pid == "K_2.1_3":
        t_acc = 0.889; t_tot = 4.0; v_max = 22.5
        ax.plot([0, t_acc, t_tot], [0, v_max, v_max], 'g-', lw=2)
        ax.set_xlim(-0.5, 4.5); ax.set_ylim(-5, 30) # Tailored limits
        ax.set_aspect('auto')
        found = True

     # K_2.2: 포물선 운동 (Projectile)
    elif pid == "K_2.2_1": # 최대 높이
        x = np.linspace(0, 4, 100); y = -0.5*(x-2)**2 + 2
        ax.plot(x, y, 'k--'); ax.plot(2, 2, 'ro')
        ax.annotate('', xy=(2, 2.5), xytext=(2, 2), arrowprops=dict(arrowstyle='<-', color='blue'))
        ax.text(2.1, 2.2, '$H_{max}$'); found = True
    elif pid == "K_2.2_2": # 수평 사거리
        x = np.linspace(0, 4, 100); y = -0.5*(x-2)**2 + 2
        ax.plot(x, y, 'k--'); ax.annotate('', xy=(4, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='<->'))
        ax.text(1.8, -0.4, 'Range $R$'); found = True
    elif pid == "K_2.2_3": # 절벽 투사
        x = np.linspace(0, 3, 50); y = 2 - 0.2*x**2
        ax.plot(x, y, 'k--'); ax.plot(0, 2, 'ko'); ax.plot([-0.5, 0], [0, 2], 'k-', lw=3)
        ax.set_title("Cliff Projectile"); found = True

    # K_2.3: 법선 및 접선 가속도 (n-t)
    elif pid == "K_2.3_1": # 원형 트랙 법선 가속도
        c = plt.Circle((0,0), 1.5, fill=False, ls='--'); ax.add_patch(c)
        ax.annotate('', xy=(0,0), xytext=(1.06, 1.06), arrowprops=dict(arrowstyle='->', color='red'))
        ax.text(0.4, 0.4, '$a_n$'); found = True
    elif pid == "K_2.3_2": # 총 가속도
        c = plt.Circle((0,0), 1.5, fill=False, ls='--'); ax.add_patch(c)
        ax.annotate('', xy=(0,0), xytext=(1.06, 1.06), arrowprops=dict(arrowstyle='->', color='red')) # an
        ax.annotate('', xy=(0.5, 1.6), xytext=(1.06, 1.06), arrowprops=dict(arrowstyle='->', color='green')) # at
        ax.annotate('', xy=(0, 1), xytext=(1.06, 1.06), arrowprops=dict(arrowstyle='->', color='purple')) # a_total
        found = True
    elif pid == "K_2.3_3": # 곡률 반경과 속도
        ax.plot(np.linspace(-2,2,100), 0.5*np.linspace(-2,2,100)**2, 'k-')
        ax.text(0, 1, r'$\rho=50m$'); found = True

    # K_2.4: 극좌표계 (Polar)
    elif pid == "K_2.4_1" or pid == "K_2.4_2": # 로봇 팔 속도
        ax.plot([0, 1.5], [0, 1.2], 'k-o', lw=4) # Arm
        ax.annotate('', xy=(2.0, 1.6), xytext=(1.5, 1.2), arrowprops=dict(arrowstyle='->', color='blue')) # vr
        ax.annotate('', xy=(1.1, 1.7), xytext=(1.5, 1.2), arrowprops=dict(arrowstyle='->', color='orange')) # v_theta
        ax.text(1.8, 1.8, '$v_r$'); ax.text(0.8, 1.8, '$v_{\\theta}$'); found = True
    elif pid == "K_2.4_3": # 원운동 가속도 (r=const)
        c = plt.Circle((0,0), 1.5, fill=False, ls='--'); ax.add_patch(c)
        ax.plot([0, 1.5], [0, 0], 'k-o', lw=3)
        ax.annotate('', xy=(-0.5, 0), xytext=(0,0), arrowprops=dict(arrowstyle='->', color='red'))
        ax.text(-0.8, 0.2, '$a$'); found = True

    # --- Error handling and default coordinate settings ---
    if not found:
        ax.text(0.5, 0.5, f"No Diagram for ID: {pid}", color='red', ha='center')
        ax.set_xlim(-2.5, 2.5)
        ax.set_ylim(-2.5, 2.5)
        ax.set_aspect('equal')
    
    # REMOVE any lines below this that reset xlim, ylim, or aspect ratio!
    ax.axis('off')
    plt.tight_layout()
    return fig
