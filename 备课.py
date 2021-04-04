import os

file_name = []
cat_name = []
file_list = []
article_name = []
map1 = {}
file_dir = r"C:\Users\jerry\Documents\GitHub\Project\XiaoMingLibrary\Libraries"
for root, dirs, files in os.walk(file_dir):
    file_name = files
    for i in range(0, len(file_name)):
        file_list.append(file_name[i].split("_"))
    for a in range(0, len(file_list)):
        cat_name.append(file_list[a][0])
        article_name.append(file_list[a][1])
        article_name[a] = article_name[a].replace(".txt", "")
        map1['%s' % article_name[a]] = '%s' % cat_name[a]
cat_name = list(set(cat_name))
print('file_name:', file_name)
print('cat_name:', cat_name)
print('article_name:', article_name)
print('map1:', map1)
