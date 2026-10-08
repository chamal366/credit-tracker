import shutil
from datetime import datetime, timedelta
from pathlib import Path

extension_mapping = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp",
                ".svg", ".tiff", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls",
                  ".xlsx", ".ppt", ".pptx", ".odt", ".ods",],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg",
              ".wma", ".m4a"],
    "Video": [".mp4", ".mkv", ".avi", ".mov", ".wmv",
              ".flv", ".webm"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".java", ".c", ".cpp", ".js", ".html",
             ".css", ".php", ".rb", ".go", ".rs"],
    "Executables": [".exe", ".msi", ".bat", ".sh", ".dmg", ".pkg"],
    "Spreadsheets": [".csv", ".xls", ".xlsx", ".ods"],
    "Presentations": [".ppt", ".pptx", ".odp"]}
def get_category(extension):
    for category, extensions in extension_mapping.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path, archive_days = None):
    folder_path = Path(folder_path)

    if not folder_path.is_dir():
        print(f"Error: {folder_path} is not a valid directory.")
        return

    now = datetime.now()
    archive_cutoff = now - timedelta(
        days=archive_days) if archive_days else None

    for item in folder_path.iterdir():
        if not item.is_file():
            continue

        extension = item.suffix
        modified_time = datetime.fromtimestamp(item.stat().st_mtime)

        if archive_cutoff and modified_time < archive_cutoff:
            target_folder = folder_path / "Archive"
        else:
            category = get_category(extension)
            target_folder = folder_path / category

        target_folder.mkdir(parents=True, exist_ok=True)
        target_path = target_folder / item.name

        if target_path.exists():
            base = item.stem
            ext = item.suffix
            counter = 1
            while target_path.exists():
                target_path = target_folder / f"{base}_{counter}{ext}"
                counter += 1

        shutil.move(item, target_path)
        print(f"Moved: {item.name} -> {target_path.name}")

def main():
    default_folder = Path.home() / "Downloads"

    folder_input = input(f"Enter the path of the folder you want to organize (default: {default_folder}): ")
    folder_path = Path(folder_input) if folder_input else default_folder

    archive_input = input("Enter the number of days after which files should be archived (leave blank for no archiving): ")
    archive_days = int(archive_input) if archive_input.isdigit() else None

    organize_folder(folder_path, archive_days)
    print("Done.")

if __name__ == "__main__":
    main()