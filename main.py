import time
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
        content = ""
        
    return content
 
        
def load_dictionary():
    dictionary_path = "slowa.txt"
    if os.path.exists(dictionary_path):
        with open(dictionary_path, 'r', encoding='utf-8') as file:
            words = file.read().splitlines()
            return set(words)
    return set()


def check_spelling(word, dictionary):
    return word.lower() not in dictionary


def highlight_errors(line, dictionary):
    words = line.split()
    highlighted_line = ""
    for word in words:
        if check_spelling(word, dictionary):
            highlighted_line += f"\033[91m{word}\033[0m"
        else:
            highlighted_line += f"{word}"
        highlighted_line += " "
    return highlighted_line.strip()


def main():
    
    file_path = "plik.txt"
    
    while True:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                #file.seek(last_size)
                content = file.read()
                
            if content:
                for line in content.splitlines():
                    highlighted_line = highlight_errors(line, load_dictionary())
                    print(highlighted_line)
                
                #last_size = len(file_path)
            
            time.sleep(1)
        
        except FileExistsError:
            print(f"File '{file_path}' not found. Waiting for it to be created.")
            
        except PermissionError:
            print(f"File '{file_path}' is not accessible. It might be closed. Exiting.")
            break
   
            
if __name__=="__main__":
    main()