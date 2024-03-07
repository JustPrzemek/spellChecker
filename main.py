import os

def open_and_save(file_name):
    try:
        if not os.path.exists(file_name):
            print("File created")
            with open(file_name, 'w'):
                pass
        os.system(f'notepad.exe {file_name}')
 
        with open(file_name, 'r') as file:
            content = file.read()
            print("New file")
    
    except Exception as e:
        print(f"Error {e}")
        
        
if __name__ == "__main__":
    filename = "plik.txt"
    open_and_save(filename)
        