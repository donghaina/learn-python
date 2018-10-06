first_dict = {
    'Apple': '苹果',
    'Google': '谷歌',
    'Facebook': '脸书',
    'MicroSoft': '微软',
    'Amazon': '亚马逊'}
print(first_dict)
first_dict['PG'] = '宝洁'
first_dict['Apple'] = '伟大的水果公司'
print(first_dict)
print(first_dict['Apple'])
print(first_dict['Google'])
print(first_dict['Facebook'])
print(first_dict['Amazon'])
print(first_dict['MicroSoft'])
print(first_dict['PG'])

del first_dict['PG']
print(first_dict)
