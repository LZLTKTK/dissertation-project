import os
import shutil

def filter_and_move_pdb_files(source_folder, destination_folder, size_limit_kb):

    os.makedirs(destination_folder, exist_ok=True)
    
   
    for filename in os.listdir(source_folder):
        
        file_path = os.path.join(source_folder, filename)
        
       
        if filename.endswith(".pdb") and os.path.getsize(file_path) > size_limit_kb * 1024:
            
            shutil.move(file_path, os.path.join(destination_folder, filename))
            print(f"Moved: {filename}")


source_folder = "/root/working/06_PDB_for_DE/ONLY_PLM_cdhit"
destination_folder = "/root/working/09_PDB_too_large/PLM"  
size_limit_kb = 1250 

filter_and_move_pdb_files(source_folder, destination_folder, size_limit_kb)
