my_list = ['Python', 'Java', 'C++', 'JavaScript']
with open('output.txt', 'w', encoding='utf-8') as f:
    for item in my_list:
        f.write(item + '\n')  # Ghi từng phần tử trên một dòng
