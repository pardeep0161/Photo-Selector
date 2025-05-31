import os

wedding_root_dir = "C:/Users/Parde/Downloads/Wedding"

selection_root_dir = "C:/Projects/Photo-Selector/photo_selector/selection_files"


def revisit_selection_files():
    print(" --- Revisit selection files --- ")
    # for dirpath, _, filenames in os.walk(wedding_root_dir):
    #     for filename in filenames:
    #         full_path = os.path.join(dirpath, filename)
    #         relative_path = full_path.replace(wedding_root_dir,"")
    #         with open(selection_root_dir+"/full.txt", 'a') as file:
    #             file.writelines(relative_path+"\n")

    accepted_list = []
    with open(selection_root_dir+"/accepted.txt", 'r') as file:
        accepted_list = [line.strip() for line in file]

    rejected_list = []
    with open(selection_root_dir+"/rejected.txt", 'r') as file:
        rejected_list = [line.strip() for line in file]

    not_sure_list = []
    with open(selection_root_dir+"/not_Sure.txt", 'r') as file:
        not_sure_list = [line.strip() for line in file]

    unvisited = []
    with open(selection_root_dir+"/full.txt", 'r') as file:
        for line in file:
            escaped_line = line.strip()
            if escaped_line not in accepted_list and escaped_line not in rejected_list and escaped_line not in not_sure_list:
                unvisited.append(line)

    with open(selection_root_dir+"/unvisited.txt", 'w') as file:
        file.writelines(unvisited)
    return None


revisit_selection_files()
