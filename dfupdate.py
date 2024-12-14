
import pandas as pd
import os
import subprocess


# 샘플 데이터프레임 생성
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 50, 65],
    "city": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)

df.to_pickle('data.pkl')


# Git 저장소 경로
REPO_PATH = "C:/Users/sys89/Desktop/yss_code/prj1"

# Commit 메시지 설정
COMMIT_MESSAGE = "Update scripts and data"

# Git 명령 실행 함수
def run_git_command(commands):
    try:
        print('try:: ', commands)
        result = subprocess.run(commands, cwd=REPO_PATH, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

# Git 작업 함수
def update_and_clean_git():
    # Add all changes
    run_git_command(["git", "add", "."])
    # Commit changes
    run_git_command(["git", "commit", "-m", COMMIT_MESSAGE])
    # Push changes with --force
    run_git_command(["git", "push", "--set-upstream", "origin", "master", "--force"])

# 스크립트 실행
update_and_clean_git()
