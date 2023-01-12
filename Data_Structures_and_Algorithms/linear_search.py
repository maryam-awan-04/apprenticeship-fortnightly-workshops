def get_words(file_path, item):
    with open(file_path, "r") as file:
        contents = file.read().split(",")
        for content in contents:
            if item == content:
                print("Item Found!")
                break
            else:
                print("Item not found")

get_words(
    r"/Users/maryam/Google Drive/BP Apprenticeship/Fortnightly Workshops/Data_Structures_and_Algorithms/words.txt",
    "above",
)
