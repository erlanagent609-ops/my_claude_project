import os
import zipfile

def zip_workspace(output_filename="my_agent_home.zip"):
    exclude_dirs = {'.git', '__pycache__', '.aider'}
    exclude_files = {output_filename, '.DS_Store'}
    
    print(f"Creating zip archive: {output_filename}...")
    
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        for foldername, subfolders, filenames in os.walk(root_dir):
            # Modify subfolders in-place to skip excluded directories
            subfolders[:] = [d for d in subfolders if d not in exclude_dirs]
            
            for filename in filenames:
                if filename in exclude_files:
                    continue
                filepath = os.path.join(foldername, filename)
                arcname = os.path.relpath(filepath, root_dir)
                zipf.write(filepath, arcname)
                
    print(f"Workspace successfully zipped into {output_filename}!")

if __name__ == "__main__":
    zip_workspace()
