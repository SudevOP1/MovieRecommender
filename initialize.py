import os, shutil, subprocess
from pathlib import Path

# config
notebook_paths = [
    Path("ml_stuff/movieRecommendationSystem.ipynb"),
]
pkl_paths = [
    [Path("ml_stuff/similarity.pkl"), Path("backend/base/similarity.pkl"),],
    [Path("ml_stuff/movies_dict.pkl"), Path("backend/base/movies_dict.pkl"),],
]

def run_notebook(notebook_path: Path):

    # try running notebook
    print(f"🟡 Running notebook: {notebook_path}")
    result = subprocess.run(
        [
            "python", "-m", "jupyter",
            "nbconvert",
            "--to", "notebook",
            "--execute", "--inplace",
            str(notebook_path)
        ],
        capture_output=True,
        text=True
    )

    # check for error in running notebook
    if result.returncode != 0:
        print(f"❌ Failed to run notebook: {notebook_path}")
        print(result.stderr)
        exit(1)
    print(f"✅ Notebook executed successfully: {notebook_path}")

def copy_pkl_file(src: Path, dest: Path):
    if not src.exists():
        print(f"❌ pkl file not found: {src}")
        exit(1)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src, dest)
    print(f"✅ Copied pkl file to: {dest}")

def main():
    print("🟡 Initializing model...\n")
    for path in notebook_paths:
        run_notebook(path)
    for [src, dest] in pkl_paths:
        copy_pkl_file(src, dest)
    print("\n✅ Initialization complete!")

if __name__ == "__main__":
    main()
