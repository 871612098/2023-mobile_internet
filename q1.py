'''
(分词算法)后向最大匹配算法BMM
'''

if __name__ == '__main__':

    ch_dict = ['移动','互联网','网','中国','科学','院',"开设","2023年","秋季","学期","课程","大学","技术"]       #中文的词典库，用于匹配句子中的词语
    sentence = '移动互联网技术是中国科学院大学开设的2023年秋季学期课程'          #例句，需要进行分词
    segment_list = []                      #存放分词后的分词词组

    #例句不为空时，循环地进行分词操作
    while len(sentence) >= 1:
        max_match_len = 5
        #当匹配单词长度大于1时，循环判断分词
        while max_match_len > 1:

            #判断前 max_match_len 个字符是否存在于字典
            if sentence[-max_match_len:] in ch_dict:
                segment_list.append(sentence[-max_match_len:])              #追加到分词词组中
                print(sentence[-max_match_len:])
                sentence = sentence[:-max_match_len]            #将符合的词语从原例句中截取
                break                   #退出循环，重新从max_match_len最长匹配数开始匹配截取

            max_match_len -= 1          #max_match_len累减，开始匹配4个字符，3个字符，，，

        #只剩下一个汉字时，说明当前不再存在任何符合的词语，直接截取一个汉字作为词组
        if max_match_len == 1:
            segment_list.append(sentence[-1:])          #追加单个汉字词语
            sentence = sentence[:-1]                    #截取例句

    # 输出进行分词后的例句
    # print('/'.join(segment_list))

    #对分词列表进行倒序
    segment_list = segment_list[::-1]
    #再次输出进行分词后的例句
    print('/'.join(segment_list))               # 我们/经常/有意见/分歧

