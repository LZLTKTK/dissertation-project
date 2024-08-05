import os
import shutil

def extract_sequence_ids(fasta_file):
  
    sequence_ids = set()
    with open(fasta_file, 'r') as file:
        for line in file:
            if line.startswith('>'):
                sequence_id = line.split()[0][1:]  
                sequence_id = sequence_id.split(':')[0]  
                sequence_id = sequence_id.lower() 
                sequence_ids.add(sequence_id)
    return sequence_ids

def move_matching_pdb_files(sequence_ids, pdb_dir, target_dir):
  
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for pdb_file in os.listdir(pdb_dir):
        if pdb_file.endswith('.pdb'):
            pdb_filename = os.path.splitext(pdb_file)[0]
            for sequence_id in sequence_ids:
                if pdb_filename.startswith(sequence_id):
                    source_path = os.path.join(pdb_dir, pdb_file)
                    target_path = os.path.join(target_dir, pdb_file)
                    shutil.move(source_path, target_path)
                    print(f'Moved {pdb_file} to {target_path}')
                    break


fasta_file = '/root/working/05 CD-hit Fasta/ONLY_PLM_cdhit.fasta'
pdb_dir = '/root/working/03 ONLY/ONLY_PLM'
target_dir = '/root/working/06 PDB for DE/ONLY_PLM_cdhit'


sequence_ids = extract_sequence_ids(fasta_file)


move_matching_pdb_files(sequence_ids, pdb_dir, target_dir)




