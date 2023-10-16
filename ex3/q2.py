# n-gram-list
def create_ngram_list(input_list, ngram_num):
    ngram_list = []
    if len(input_list) <= ngram_num:
        ngram_list.append(input_list)
    else:
        for tmp in zip(*[input_list[i:] for i in range(ngram_num)]):
            tmp = "".join(tmp)
            ngram_list.append(tmp)
    return ngram_list

# 对比的文档
doc1 = "我去吃饭。不去吃饭"
doc2 = "我去吃饭。不去理发"

ngram_num = 2  #int(input("切分长度："))
wordslist1 = create_ngram_list(doc1, ngram_num) # 列表形式
wordslist2 = create_ngram_list(doc2, ngram_num)

words1_set = set(wordslist1) #得到n-gram词语的集合
words2_set = set(wordslist2)