import string
import csv


def read_tweet_file(path, separator="\t"):
    result = []
    # get all data, each row is a dict
    reader = csv.DictReader(open(path), delimiter='\t')
    for row in reader:
        id = row["ID "]
        word = row["words "]
        context = row["context"]
        type = row["type"]
        result.append([id, word, context, type])
    return result

# process starts
# pre define separator and file path
separator = "\t"
file_path = "semeval2016-task6-trainingdata_sents_utf8.predict"
# get all tweets
all_info_list = read_tweet_file(file_path, separator)
# print some results: count, first and last line
print "Count of all: ", len(all_info_list)
print all_info_list[0]
print "..."
print all_info_list[-1]
print

