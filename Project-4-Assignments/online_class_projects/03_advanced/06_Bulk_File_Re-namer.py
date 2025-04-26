import os

def main():
    try:
        # Get directory path
        path = input("Enter directory path (default './'): ").strip() or './'
        
        # Verify path exists
        if not os.path.isdir(path):
            print(f"Error: Directory '{path}' does not exist")
            return

        # Get naming pattern once for all files
        base_name = input("Enter base filename (default 'img'): ").strip() or 'img'
        print("\nFiles to be renamed:")
        
        # Show files that will be renamed
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        for i, filename in enumerate(files, 1):
            print(f"{i}. {filename}")

        # Confirm before proceeding
        confirm = input(f"\nRename {len(files)} files? (y/n): ").lower()
        if confirm != 'y':
            print("Operation cancelled")
            return

        # Perform renaming
        for i, filename in enumerate(files, 1):
            # Split filename and extension
            name_part, ext_part = os.path.splitext(filename)
            
            # Use original extension if user didn't specify one
            new_ext = ext_part if ext_part else '.png'
            
            # Construct new filename
            new_name = f"{base_name}_{i}{new_ext}"
            
            # Full paths
            src = os.path.join(path, filename)
            dst = os.path.join(path, new_name)
            
            # Rename with error handling
            try:
                os.rename(src, dst)
                print(f"Renamed: {filename} -> {new_name}")
            except OSError as e:
                print(f"Error renaming {filename}: {str(e)}")

        print("\nOperation completed")

    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()