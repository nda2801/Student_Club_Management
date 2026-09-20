import os
import time
import requests

puml_dir = r"docs\plantuml"
images_dir = r"images"

os.makedirs(images_dir, exist_ok=True)

puml_files = sorted([f for f in os.listdir(puml_dir) if f.endswith(".puml")])

print(f"Found {len(puml_files)} PUML diagram files to render into {images_dir}/...")

success_count = 0
for idx, puml_file in enumerate(puml_files, 1):
    src_path = os.path.join(puml_dir, puml_file)
    base_name = os.path.splitext(puml_file)[0]
    dest_png = os.path.join(images_dir, f"{base_name}.png")
    
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    print(f"[{idx}/{len(puml_files)}] Rendering {puml_file} -> {base_name}.png ...", end=" ", flush=True)
    
    # Try Kroki first, with retries
    rendered = False
    for attempt in range(3):
        try:
            resp = requests.post(
                "https://kroki.io/plantuml/png",
                data=content.encode("utf-8"),
                headers={"Content-Type": "text/plain; charset=utf-8"},
                timeout=25
            )
            if resp.status_code == 200 and len(resp.content) > 500:
                with open(dest_png, "wb") as out_f:
                    out_f.write(resp.content)
                size_kb = len(resp.content) / 1024
                print(f"DONE ({size_kb:.1f} KB)")
                rendered = True
                success_count += 1
                break
            else:
                print(f"[HTTP {resp.status_code}] Retrying...", end=" ", flush=True)
                time.sleep(1)
        except Exception as e:
            print(f"[Err: {e}] Retrying...", end=" ", flush=True)
            time.sleep(1)
            
    if not rendered:
        print("FAILED!")

print(f"\n==========================================")
print(f"Successfully generated {success_count}/{len(puml_files)} diagram images in {images_dir}!")
print(f"==========================================")
