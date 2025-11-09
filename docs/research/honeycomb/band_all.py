import os
import subprocess

# 設定
root = "/home/h.negishi/FLEX_for_negishi_ver_2025_0422/honey_bilayer/tperp_change"
template_path = os.path.join(os.getcwd(), "band_template.py")
# パラメータリスト
nk_list=[24, 32, 36, 48, 64]
nk=36
nw_list=[128, 256, 512, 1024, 2048]
nw=1024
T_list=[0.05, 0.025, 0.0125, 0.00625]
T=0.025
U_list = [4.0, 8.0, 12.0]
U=4.0
psym_list=[0, 1]
psym=0
tperp_list = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
tperp=0.5
rfill_list = [round(x*0.20, 2) for x in range(10, 19+1)]  # 2.00～3.60

#=============================================================================================

def rfill_dir(rfill):
    val = int(rfill*100)
    return f"n_{val//100}_{val%100:02d}"
with open(template_path, "r") as f:
    template = f.read()

for tperp in tperp_list:
    dir1 = f"nk{nk}_nw{nw}_T{T}_psym{psym}/tperp{tperp}"
    for U in U_list:
        dir2 = f"U{U}"
        for rfill in rfill_list:
            rfill_subdir = rfill_dir(rfill)
            target_dir = os.path.join(root, dir1, dir2, rfill_subdir)
            if os.path.isdir(target_dir):
                print(f"--- {target_dir} ---")
                code = template.format(
                    tperp=tperp,
                    rfill=rfill
                )
                script_path = os.path.join(target_dir, "plot_band.py")
                with open(script_path, "w") as fscript:
                    fscript.write(code)
                # python3を明示
                subprocess.run(f"cd {target_dir} && python3 plot_band.py", shell=True)
