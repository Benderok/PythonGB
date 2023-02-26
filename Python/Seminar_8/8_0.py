from os import path

file_base = "base.txt"
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_records():
    global all_data, id

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])
        return all_data

print(read_records())

def show_all():
    if not all_data:
        print("Empty base")
    else:
        print(*all_data, sep="\n")

def add_new():
    global id
    zapis = ['Surname ', 'Name ', 'Middle Name ', 'Phone Num ']
    string = ''
    for i in zapis:
        string += input(f'Enter {i} ') + ' '
    id += 1
    with open(file_base, 'a', encoding="utf-8") as f:
        f.write(f'{id} {string}\n')

def search():
    search_for = exist(0, input("Enter the data to search: "))
    if search_for:
        print(*search_for, sep="\n")
    else:
        print("The data is not correct!")

def exist(rec_id, data):

    if rec_id:
        people = [i for i in all_data if rec_id in i[0]]
    else:
        people = [i for i in all_data if data in i]
    return people

def delete():

    global all_data

    symbol = "\n"
    show_all()
    del_id = input("Enter the record id: ")

    if exist(del_id, ""):
        all_data = [k for k in all_data if k[0] != del_id]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Record deleted!\n")
    else:
        print("The data is not correct!")

def main_menu():
    play = True
    while play:
        answer = input("Phone book:\n"
                        "1. Show all records\n"
                        "2. Add new record\n"
                        "3. Search a record\n"
                        "4. Delete a record\n"
                        "5. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new()
            case "3":
                search()
            case "4":
                delete()
            case "5":
                play = False
            case _:
                print("Try again!!!\n")

main_menu()