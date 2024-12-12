import os

def copy_file_names_to_txt(folder_path, txt_file_path):
    with open(txt_file_path, 'w') as txt_file:
        for filename in os.listdir(folder_path):
            txt_file.write(filename + '\n')

# Specify the folder path containing the files
folder_path = r'C:\Users\pieru\Desktop\Magistrale\Distributed System\Slides\Teoria'

# Specify the path of the text file where you want to paste the file names
txt_file_path =r'C:\Users\pieru\Desktop\Magistrale\Distributed System\elenco_slides'

# Call the function
copy_file_names_to_txt(folder_path, txt_file_path)

print("File names copied to", txt_file_path)
print("hello")
