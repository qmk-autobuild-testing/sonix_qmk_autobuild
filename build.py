import subprocess
import os
import sys
import re
KEYBOARDS = []
# Search the repository for Sonix SN32F2 keyboard directories
command = "cd ../../ && grep -rl 'MCU = SN32F2' | sed -e 's/keyboards\///g' -e 's/\/rules.mk//g'| sort"
# Grab the list of enabled keyboards
enabled_kb_command = "cat ../../KEYBOARD_LIST"
enabled_kb_ret = subprocess.run(enabled_kb_command, capture_output=True, shell=True)
ENABLED_BOARDS = enabled_kb_ret.stdout.decode().split('\n')

ret = subprocess.run(command, capture_output=True, shell=True)
BOARDS = ret.stdout.decode().split('\n')
def main():
    print ('Enabled keyboards (parsed): ', ENABLED_BOARDS)
    print ('All keyboards (parsed): ', BOARDS)
    for line in BOARDS:
        # We need to manipulate some non-standard directories
        if line.strip() != "" and line.strip() != "lib/python/build_all.py" and line.strip() in ENABLED_BOARDS:
            if re.match("^(gmmk)",line.strip()):
                KEYBOARDS.append(line.strip()+"/rev2")
                KEYBOARDS.append(line.strip()+"/rev3")
            if re.match("^(keychron/k)",line.strip()):
                KEYBOARDS.append(line.strip())
                # keychron K series white don't have yet via/optical support
                if re.match("(?!.*white)",line.strip()):
                    KEYBOARDS.append(line.strip()+"/via")
                    KEYBOARDS.append(line.strip()+"/optical")
                    KEYBOARDS.append(line.strip()+"/optical_via")
            else: KEYBOARDS.append(line.strip())
    print ('Filtered and processed boards: ', KEYBOARDS)
    

if __name__ == '__main__':
    main()

error = False
for kb in KEYBOARDS:
    # We are building for different chips, and some things need a clean pass, so make sure it's clean
    build_command = f"qmk clean && qmk compile -kb {kb} -km all -j{os.cpu_count()}"
    if subprocess.run(build_command, shell=True).returncode != 0:
        error = True
if error:
    sys.exit(1)
