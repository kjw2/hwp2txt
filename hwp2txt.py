import os
import hwp

input_folder = "a"
output_folder = "b"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".hwp"):
        input_file_path = os.path.join(input_folder, filename)
        print(input_file_path)
        output_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".txt")
        print(output_file_path)
        # hwp_to_txt(input_file_path, output_file_path)
        text = hwp.get_text(input_file_path)
        with open(output_file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(text)

print("변환 완료")