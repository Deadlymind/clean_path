# Import the Path class from the pathlib module for working with file paths
from pathlib import Path

# Import the shutil module for file operations
import shutil

# Define the cleanpath function, which organizes files in a specified directory
def cleanpath(directory='.'):
    # Create a Path object representing the specified directory
    path = Path(directory)

    # Define mappings associating file extensions with destination folders
    mappings = {
        ('.png', '.jpg', '.jpeg', '.webp', '.avif', '.bmp', '.tiff', '.gif'): 'Images',
        ('.mp4', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.m4v', '.mpg', '.mpeg'): 'Videos',
        ('.py', '.ipynb', '.html', '.css', '.js', '.php', '.cpp', '.c', '.java'): 'Code',
        ('.zip', '.rar', '.tar', '.gz', '.7z', '.bz2', '.xz'): 'Archives',
        ('.txt', '.pdf', '.doc', '.docx', '.md', '.odt', '.rtf'): 'Documents',
        ('.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a', '.wma'): 'Audio',
        ('.xls', '.xlsx', '.csv', '.ods', '.xlsm', '.xlsb'): 'Spreadsheets',
        ('.ppt', '.pptx', '.odp', '.key'): 'Presentations',
        ('.psd', '.ai', '.eps', '.svg', '.indd', '.xd', '.sketch'): 'Design',
        ('.db', '.sql', '.mdb', '.accdb', '.sqlite', '.dbf', '.sqlitedb'): 'Databases',
        ('.exe', '.msi', '.bat', '.sh', '.jar', '.app', '.apk'): 'Executables',
        ('.3ds', '.obj', '.fbx', '.blend', '.stl', '.dae', '.max'): '3D_Models',
        ('.ttf', '.otf', '.woff', '.woff2', '.eot'): 'Fonts',
        ('.epub', '.mobi', '.azw3', '.pdf', '.djvu', '.cbz'): 'eBooks',
        ('.iso', '.dmg', '.img', '.bin', '.cue'): 'Disk_Images',
        ('.log', '.ini', '.cfg', '.conf'): 'Configuration_Files',
        ('.vmdk', '.vdi', '.vhd', '.hdd'): 'Virtual_Machine_Files'
    }

    # Iterate over each file in the specified directory
    for file in path.iterdir():
        # Check if the current item is a file
        if file.is_file():
            # Get the lowercase file extension
            file_extension = file.suffix.lower()

            # Iterate over mappings to find a matching file extension
            for extensions, folder_name in mappings.items():
                if file_extension in (ext.lower() for ext in extensions):
                    # Define the destination folder path
                    dest = path / folder_name
                    # Create the destination folder if it doesn't exist
                    dest.mkdir(exist_ok=True)

                    # Handling file name conflict
                    new_file_name = file.name
                    counter = 1
                    while (dest / new_file_name).exists():
                        new_file_name = f"{file.stem}_{counter}{file.suffix}"
                        counter += 1

                    # Move the file to the destination folder with the new file name
                    shutil.move(str(file), str(dest / new_file_name))
                    break

# Check if the script is executed directly
if __name__ == "__main__":
    # Prompt the user to enter the directory to clean, defaulting to the current directory
    path_to_clean = input("Enter directory to clean (default is current directory): ") or '.'
    # Call the cleanpath function with the specified directory
    cleanpath(path_to_clean)
