import subprocess

def run_app_multiple_times(times: int):
    for i in range(times):
        print(f"Running the app for the {i + 1} time...")
        subprocess.run(["python", "./software_company.py"])  # 替换为你的 app 所在的脚本路径
        print(f"Finished run {i + 1}")

if __name__ == "__main__":
    run_app_multiple_times(2)
