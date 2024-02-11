import subprocess
packdir = input("Enter package directory (full name; /home/leander/...): ")
files = input("Enter .c files: (full name; /home/leander/..., separated by comma): ").split(",")
packname = input("Enter package name: ")
subprocess.run([f"echo \"sudo gcc -o \\\"/usr/bin/{packname}\\\" \\"], shell=True)
for f in files:
    subprocess.run([f"{f} \\"], shell=True)
subprocess.run([f"\\\">> {packdir}/lspack_install_script.sh"])
print("Successfully generated lspack_install_script.sh!")
