import os
import subprocess

def run_cdhit_on_fasta_files(input_dir, output_dir, c=0.9, n=5):
    
    os.makedirs(output_dir, exist_ok=True)
    
  
    for filename in os.listdir(input_dir):
        if filename.endswith(".fasta"):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_cdhit.fasta")
            
          
            cmd = [
                "cd-hit",
                "-i", input_file,
                "-o", output_file,
                "-c", str(c),
                "-n", str(n)
            ]
            
          
            print(f"Processing {input_file}...")
            subprocess.run(cmd, check=True)
            print(f"Output written to {output_file}")

    print("所有FASTA文件已处理完成。")

if __name__ == "__main__":
  
    input_dir = "/root/working/04 Fasta"  
    output_dir = "/root/working/05 CD-hit Fasta"      
    

    run_cdhit_on_fasta_files(input_dir, output_dir)
