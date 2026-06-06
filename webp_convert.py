import os
from pathlib import Path
from PIL import Image

def convert_all_to_webp(input_dir, output_dir, quality=80):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    output_path.mkdir(parents=True, exist_ok=True)
    
    valid_extensions = {'.png', '.jpeg', '.jpg', '.bmp', '.tiff', '.tif', '.gif'}
    all_files = list(input_path.iterdir())
    image_files = [f for f in all_files if f.suffix.lower() in valid_extensions]
    
    if not image_files:
        print(f"\nNo compatible images found in {input_dir}")
        return

    print(f"\nFound {len(image_files)} images. Starting conversion...")
    
    # Track success and failures
    successful_count = 0
    failed_files = {}  # Stores filename: error message

    for file in image_files:
        try:
            with Image.open(file) as img:
                new_filename = file.stem + ".webp"
                destination = output_path / new_filename

                if file.suffix.lower() == '.gif' and getattr(img, "is_animated", False):
                    img.save(destination, "WEBP", quality=quality, save_all=True)
                else:
                    if img.mode not in ('RGB', 'RGBA'):
                        img = img.convert('RGB')
                    img.save(destination, "WEBP", quality=quality)
                    
                print(f"✅ Converted: {file.name} -> {new_filename}")
                successful_count += 1
                
        except Exception as e:
            print(f"❌ Failed: {file.name}")
            failed_files[file.name] = str(e)

    # --- FINAL REPORT ---
    print("\n==============================")
    print("      CONVERSION SUMMARY      ")
    print("==============================")
    print(f"Successfully converted: {successful_count} image(s)")
    print(f"Failed conversions:     {len(failed_files)} image(s)")
    
    if failed_files:
        print("\n------------------------------")
        print("        ERROR DETAILS         ")
        print("------------------------------")
        for filename, error_msg in failed_files.items():
            print(f"📄 File:  {filename}")
            print(f"⚠️ Error: {error_msg}\n")
    else:
        print("\n🎉 Everything converted perfectly with zero errors!")
    print("==============================")

# --- INTERACTIVE USER INPUT ---
if __name__ == "__main__":
    print("=== Image to WebP Converter ===")
    
    while True:
        user_source = input("Enter the path to your source image folder (or '.' for current folder): ").strip()
        source_path = Path(user_source)
        
        if source_path.exists() and source_path.is_dir():
            break
            
        print("❌ Error: That path does not exist or is not a folder. Please try again.\n")
    
    user_target = input("Enter the target folder name for WebP output [Default: ./webp_output]: ").strip()
    if not user_target:
        user_target = "./webp_output"
        
    user_quality = input("Enter compression quality (1-100) [Default: 80]: ").strip()
    if user_quality.isdigit() and 1 <= int(user_quality) <= 100:
        quality_val = int(user_quality)
    else:
        quality_val = 80

    # Run the converter
    convert_all_to_webp(source_path, user_target, quality_val)
    
    # Keeps the window open on double-click runs so you can read the log
    print("\n")
    input("Press ENTER to exit the program...")
