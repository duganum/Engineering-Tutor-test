import matplotlib.pyplot as plt
import numpy as np
import os
import io

def render_problem_diagram(prob):
    """Loads images from nested HW subdirectories or generates FBD placeholders."""
    if isinstance(prob, dict):
        pid = str(prob.get('id', '')).strip()
    else:
        pid = str(prob).strip()
        prob = {}

    fig, ax = plt.subplots(figsize=(4, 3), dpi=100)
    ax.set_aspect('equal')
    found = False

    # --- HW Directory Image Loader ---
    hw_title = prob.get("hw_title")
    hw_subtitle = prob.get("hw_subtitle")
    
    if hw_title and hw_subtitle:
        # Path: images/HW 6 (subtitle)/images/1.png
        folder_name = f"{hw_title} ({hw_subtitle})"
        image_id = pid.split('_')[-1] 
        img_path = os.path.join('images', folder_name, 'images', f"{image_id}.png")
        
        try:
            if os.path.exists(img_path):
                img = plt.imread(img_path)
                ax.imshow(img)
                h, w = img.shape[:2]
                ax.set_xlim(0, w); ax.set_ylim(h, 0)
                found = True
        except Exception:
            pass

    if not found:
        ax.text(0.5, 0.5, f"Diagram\n{pid}", color='gray', ha='center', va='center')
        ax.set_xlim(0, 1); ax.set_ylim(0, 1)

    ax.axis('off')
    plt.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return buf

def render_lecture_visual(topic, params=None):
    fig, ax = plt.subplots(figsize=(6, 6), dpi=150)
    if params is None: params = {}
    ax.axhline(0, color='black', lw=1.5); ax.axvline(0, color='black', lw=1.5)
    ax.grid(True, linestyle=':', alpha=0.6); ax.set_aspect('equal')
    
    if topic == "Relative Motion":
        vA, vB = params.get('vA', [15, 5]), params.get('vB', [10, -5])
        v_rel = [vA[0]-vB[0], vA[1]-vB[1]]
        ax.quiver(0, 0, vA[0], vA[1], color='blue', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v}_A$')
        ax.quiver(0, 0, vB[0], vB[1], color='red', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v}_B$')
        ax.quiver(vB[0], vB[1], v_rel[0], v_rel[1], color='green', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v}_{A/B}$')
        limit = max(np.abs(vA+vB)) + 5
        ax.set_xlim(-limit, limit); ax.set_ylim(-limit, limit); ax.legend()
    elif topic == "Projectile Motion":
        v0, theta = params.get('v0', 30), np.radians(params.get('angle', 45))
        t = np.linspace(0, (2*v0*np.sin(theta))/9.81, 100)
        ax.plot(v0*np.cos(theta)*t, v0*np.sin(theta)*t - 0.5*9.81*t**2, 'g-')
    
    plt.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return buf
