import hashlib
import os

def calculate_sha256(file_path):
    """Calculate SHA256 hash of a file"""
    sha256_hash = hashlib.sha256()

    try:
        with open(file_path, 'rb') as file:
            # Read the file in chunks to handle large files efficiently
            for chunk in iter(lambda: file.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return None

def main():
    current_dir = "."

    print("Calculating SHA256 hash for all files in current directory...")
    print("=" * 60)

    # Get all files in current directory
    try:
        items = os.listdir(current_dir)
        files = [item for item in items if os.path.isfile(item)]

        if not files:
            print("No files found in current directory.")
            return

        # Sort files alphabetically for consistent output
        files.sort()

        successful_hashes = 0

        for filename in files:
            print(f"Processing: {filename}")
            hash_value = calculate_sha256(filename)

            if hash_value:
                print(f"File: {filename}")
                print(f"SHA256: {hash_value}")
                successful_hashes += 1
            else:
                print(f"Failed to calculate hash for: {filename}")
            print("-" * 60)

        print(f"\nSummary: Successfully calculated hashes for {successful_hashes} out of {len(files)} files.")

    except Exception as e:
        print(f"Error accessing current directory: {e}")

if __name__ == "__main__":
    main()
