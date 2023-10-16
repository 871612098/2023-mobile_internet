import jieba
import  re


def get_text(txt):
   # txt = open("1.txt", "r", encoding='UTF-8').read()
   # txt = txt.lower()
   for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~\\n':
      txt = txt.replace(ch, " ")  # 将文本中特殊字符替换为空格
   return txt

def get_data(str):
   result = []
   with open('./data/1.txt','r') as f:
     for line in f.readlines():
         line  = line.strip('\n')
         for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~，。、；：！@#¥%……':
            line = line.replace(ch, "")  # 将文本中特殊字符替换为空格
         if line=='':
            continue
         temp = jieba.lcut(line)
         print(temp)
      # text = get_text(text)
   # text = [line.strip("\n") for line in text]

   # print(result)
   return result
if __name__ == '__main__':
   str = "中国科学院大学是一所以研究生教育为主、精英化本科的高等教育院校。"
   get_data(str)