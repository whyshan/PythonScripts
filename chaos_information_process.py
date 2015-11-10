import csv


# this function is to find out the enlarged range
def get_range(int_list):
    min_id = min(int_list)
    max_id = max(int_list)
    return [min_id, max_id]


# to process each group of lines
def process_group(words_group):
    result = []
    combinations = []

    # 1st round, found all "MWE" and make combinations
    for line in words_group:
        id = line[1]
        context = line[3]
        if line[4] == "MWE":
            line_added = False
            # if combination exists, enlarge the range
            for item in combinations:
                min = item[0]
                max = item[1]
                if (context >= min and context <= max) or (id >= min and id <= max):
                    new_item = get_range([min, max, id, context])
                    combinations.remove(item)
                    combinations.append(new_item)
                    line_added = True
            # if combination doesn't exist, create one
            if line_added is False:
                id_range = get_range([context, id])
                combinations.append(id_range)

    # 2nd round, add missing lines into combinations and enlarge the range
    # actually, the process of enlarging should be repeated until the result is constant #LAZY
    for line in words_group:
        id = line[1]
        context = line[3]
        for item in combinations:
            min = item[0]
            max = item[1]
            if context >= min and context <= max:
                new_item = get_range([min, max, id, context])
                combinations.remove(item)
                combinations.append(new_item)

    # return results
    for item in combinations:
        min = item[0]
        max = item[1]
        result_string = str(words_group[min - 1][0]) + ": " # print line number for readability
        for i in range(min - 1, max):
            result_string += words_group[i][2] + " "
        # print result_string
        result.append(result_string)
    return result


def read_chaos_file(path, separator="\t"):
    result = []
    words_group = []
    # get all data, each row is a dict
    reader = csv.reader(open(path), delimiter='\t')
    line_number = 0
    for row in reader:
        line_number += 1
        if len(row) > 0:
            id = int(row[0])
            word = row[1]
            # print line_number, row[1]
            context = int(row[6])
            type = row[7]
            words_group.append([line_number, id, word, context, type])
        else:
            # it means the end of one group
            group_result = process_group(words_group)
            if group_result is not None:
                result.extend(group_result)
            words_group = []
    return result


def process_file(file_path, str1, str2):
    lines = open(file_path).readline()
    fp = open(file_path, 'w')
    for s in lines:
        fp.write(s.replace(str1, str2))
    fp.close()


# process starts
# pre define separator and file path
separator = "\t"
file_path = "semeval2016-task6-trainingdata_sents_utf8.predict"
# process_file(file_path, "'", "\'")
# process_file(file_path, '"', '\"')
# get all tweets
all_info_list = read_chaos_file(file_path, separator)
# print some results: count, first and last line
print "Count of all: ", len(all_info_list)
for info in all_info_list:
    print info
