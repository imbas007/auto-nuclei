import subprocess
import sys
import os

def run_subfinder(domain):
    output_file = f"{domain}_subdomains.txt"
    command = f"subfinder -d {domain} -o {output_file}"
    subprocess.run(command, shell=True)
    return output_file

def run_httpx(subdomains_file):
    output_file = f"{os.path.splitext(subdomains_file)[0]}_httpx.txt"
    command = f"httpx -l {subdomains_file} -threads 50 -o {output_file}"
    subprocess.run(command, shell=True)
    return output_file

def run_nuclei(httpx_file):
    output_file = f"{os.path.splitext(httpx_file)[0]}_nuclei.txt"
    command = f"nuclei -l {httpx_file} -t ~/nuclei-templates/ -o {output_file}"
    subprocess.run(command, shell=True)
    return output_file

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]

    print(f"Running Subfinder on {domain}...")
    subdomains_file = run_subfinder(domain)
    print(f"Subdomains saved to {subdomains_file}")

    print(f"Running HTTPX on {subdomains_file}...")
    httpx_file = run_httpx(subdomains_file)
    print(f"HTTPX results saved to {httpx_file}")

    print(f"Running Nuclei on {httpx_file}...")
    nuclei_file = run_nuclei(httpx_file)
    print(f"Nuclei results saved to {nuclei_file}")

if __name__ == "__main__":
    main()
