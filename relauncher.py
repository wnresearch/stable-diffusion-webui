import os, time

n = 0
while(n<1):
    print('Relauncher: Launching...')
    if n > 0:
        print(f'\tRelaunch count: {n}')
    os.system("fuser -k 3000/tcp")
    launch_string = "/workspace/stable-diffusion-webui/webui.sh -f"
    os.system(launch_string)
    print('Relauncher: Process is ending. Relaunching in 2s...')
    n += 1
    time.sleep(2)
