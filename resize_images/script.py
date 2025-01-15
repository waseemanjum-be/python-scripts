from PIL import Image

# Replace 'input.jpg' with the path to your original image
input_path = "input.png"

# Paths for the two output files
output_path_1000x750 = "output_1000x750.jpg"
output_path_4000x4000 = "output_4000x4000.jpg"

# Open the original image
with Image.open(input_path) as img:
    # 1) Resize to 1000×750
    resized_1000x750 = img.resize((1000, 750), Image.LANCZOS)
    resized_1000x750.save(output_path_1000x750)

    # 2) Resize to 4000×4000
    resized_4000x4000 = img.resize((4000, 4000), Image.LANCZOS)
    resized_4000x4000.save(output_path_4000x4000)

print("Images successfully resized and saved!")
