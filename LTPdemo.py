# -*- coding: utf-8 -*-
__author__ = 'oukohou'
__time__ = '17-3-23 下午6:53'

# If this runs wrong, don't ask me, I don't know why;
# If this runs right, thank god, and I don't know why.
# Maybe the answer, my friend, is blowing in the wind.

from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
from pyltp import Parser
from pyltp import SementicRoleLabeller

paragraph1 = "如何调用ltp进行命名实体识别。"
paragraph2 = "hello there。 幸会,ccsilence。"

# 分句
sentences = SentenceSplitter.split(paragraph2)
print ("分句：\n\t " + "\t\t".join(sentences))

# 分词
sengentor = Segmentor()
sengentor.load("/home/oukohou/study/python/LTP/ltp_data/cws.model")
words = sengentor.segment(paragraph1)
words_list = list(words)
print ("分词：\n\t " + "|".join(words))
sengentor.release() # 释放模型

# 词性标注
postagger = Postagger()
postagger.load("/home/oukohou/study/python/LTP/ltp_data/pos.model")
# words = ["hello", "静静", "好美"]
postags = postagger.postag(words)
print ("词性标注：\n\t " + "|".join(postags))
postagger.release() # 释放模型

# 命名实体识别
recognizer = NamedEntityRecognizer()
recognizer.load("/home/oukohou/study/python/LTP/ltp_data/ner.model")
netags = recognizer.recognize(words, postags)
print ("命名实体识别：\n\t " +"|".join(netags))
recognizer.release() # 释放模型

# 依存句法分析
parser = Parser()
parser.load("/home/oukohou/study/python/LTP/ltp_data/parser.model")
arcs = parser.parse(words, postags)
print ("依存句法分析： \n\t" + "\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
parser.release() # 释放模型

# 角色标注
labeller = SementicRoleLabeller()
labeller.load("/home/oukohou/study/python/LTP/ltp_data/srl")
roles = labeller.label(words, postags, netags, arcs)
print ("角色标注： ")
for role in roles:
    print (role.index, "".join(["%s:(%d, %d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments]))
labeller.release()  # 释放模型
