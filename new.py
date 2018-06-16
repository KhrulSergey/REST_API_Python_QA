__author__ = 'Sergey Khrul'


list = ['2','1','5,4','5,4,5M','5,4,7','1,5,4,5M','4','1,4','5,4,7,5M','1,5,4','5','1,5','6,5','1,4,7','3','5,7','4,7','2,5,4','7','1,6','4,7,5M','1,6,5','6,4','6,5,4','1,6,5,4','4,5M','6','6,4,7','1,2','1,2,4','2,4','2,5,4,7','1,4,5M','1,5,4,7','2,5','2,5,4,5M','1,2,5,4','1,6,4','5M','2,4,7','5,5M','2,6','2,4,5M','6,5,7','2,6,5','2,7','6,7','1,5,5M','6,5,4,7','5,7,5M','2,5,4,7,5M','1,5M','1,2,4,5M','1,7','2,6,4','1,2,6,5','2,6,5,4','1,5,6','4,5,5M','4,5','5,6','1,4,5','1,4,5,5M','2,4,5','6,1','4,5,7','4,5M,7','4,5,5M,7','4,6','1,4,6','4,5,6','4,6,7','1,2,5,6','2,4,5,6','5,6,1','1,2,5','1,2,6','2,4,6','4,1,6','4,5,5M,1','1,4,5,5M,7','5,7,4,6','5M,4','1,5,6,7','5M,1,4','7,4,5','5,1','1,5M,4','2,4,5,5M','7,4','2,4,5M,7','5M,4,5','4,1,2,6','5,6,7','2,5M','1,4,5,6','5,7,4','2,5,6','4,5,6,7','5,5M,7','4,5,7,5M','1,4,5M,7','4,5,7,1','5M,7','4,1,5,6','5,6,4','1,4,5M,6']

my_dict = {
    '1': 'Residential',
    '2': 'Commercial',
    '3': 'Manufacturing',
    '4': 'Agricultural',
    '5': 'Undeveloped',
    '5M': 'Agricultural forest',
    '6': 'Productive Forest Land',
    '7': 'Other',
    ',': ''
}

comblist = []

for element in list:
    comb_element = ''
    str_element = element.split(',')
    for char in str_element:
        comb_element += my_dict[char] + ','
    # comb_element = comb_element. ','
    comblist.append(comb_element[0:len(comb_element)-1])

print(comblist)

file = open("testfile.txt", 'w')
file.write('\n'.join(str(p) for p in comblist))
