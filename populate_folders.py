# pointlessly put an empty file into each folder because otherwise git won't add them to a commit.
import os

def populate(folder_path):
    items = os.listdir(folder_path)
    if len(items) == 0:
        with open(folder_path + '/pointless_token.txt','w') as doc: 
            doc.write("I'm not so good with github. \nI added these pointless token files because git wouldn't allow me to commit empty folders.")
    else:
        for item in items:
            new_path = f'{folder_path}/{item}'
            if os.path.isdir(new_path):
                populate(new_path)

if __name__ == '__main__':
    populate('./')