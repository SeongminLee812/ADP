import subprocess

def install_packages(requirements_file):
    with open(requirements_file, 'r') as f:
        packages = f.read().splitlines()

    successful_packages = []
    failed_packages = []

    for package in packages:
        try:
            subprocess.check_call(["pip", "install", package])
            successful_packages.append(package)
        except subprocess.CalledProcessError:
            print(f"Failed to install: {package}")
            failed_packages.append(package)

    print("Successful installations:")
    print("\n".join(successful_packages))

    print("\nFailed installations:")
    print("\n".join(failed_packages))

if __name__ == "__main__":
    requirements_file = "requirements.txt"
    install_packages(requirements_file)

