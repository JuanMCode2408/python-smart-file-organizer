import os
import shutil

folder_path = input("Enter the folder path to organize: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Programs": [".exe", ".msi"]
}

for filename in os.listdir(folder_path):

    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):

        extension = os.path.splitext(filename)[1].lower()

        moved = False

        for folder_name, extensions in file_types.items():

            if extension in extensions:

                destination_folder = os.path.join(folder_path, folder_name)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                new_path = os.path.join(destination_folder, filename)

                # evitar sobrescribir archivos
                if os.path.exists(new_path):
                    base, ext = os.path.splitext(filename)
                    counter = 1

                    while os.path.exists(new_path):
                        new_filename = f"{base}_{counter}{ext}"
                        new_path = os.path.join(destination_folder, new_filename)
                        counter += 1

                shutil.move(file_path, new_path)
                print(f"Moved: {filename} → {folder_name}")
                moved = True
                break

        if not moved:
            print(f"Skipped: {filename}")

print("Organization completed successfully!")