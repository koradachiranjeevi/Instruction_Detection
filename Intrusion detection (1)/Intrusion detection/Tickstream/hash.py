import hashlib

def compute_hash(file_path):
   
    hash_algo = hashlib.sha256()  
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

def compare_files(original_file, modified_file):
   
    original_hash = compute_hash(original_file)
    modified_hash = compute_hash(modified_file)

    print(f"Original file hash: {original_hash}")
    print(f"Modified file hash: {modified_hash}")

    if original_hash == modified_hash:
        print("Data integrity intact: Files are the same.")
        return True
    else:
        print("Data integrity compromised: Files are different.")
        return False

if __name__ == "__main__":
    original_file_path = "Tickstream\AAPL.csv"  
    modified_file_path = "modified_AAPL.csv"  

   
    compare_files(original_file_path, modified_file_path)
