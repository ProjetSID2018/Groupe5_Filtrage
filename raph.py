
from os import listdir

path_post_filt_target = '/var/www/html/projet2018/data/clean/temporary_filtering/post_tfidf'
path_post_tf_target = '/var/www/html/projet2018/data/clean/temporary_filtering/post_filtering'


for file in listdir(path_post_filt_target):
    print(file)


for file in listdir(path_post_tf_target):
    print(file)
