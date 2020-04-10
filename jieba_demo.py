#-*- coding:utf-8 -*-
import jieba
import jieba.posseg as pseg

sent="Minecraft所呈现的世界并不是华丽的画面与特效，而是注重在游戏性上面。玩家可以在游戏中的三维空间里创造和破坏游戏里的方块，甚至在多人服务器与单人世界中体验不同的游戏模式，打造精妙绝伦的建筑物，创造物和艺术品。Minecraft着重于让玩家去探索、交互、并且改变一个由一立方米大小的方块动态生成的地图。除了方块以外，环境单体还包括植物、生物与物品。游戏里的各种活动包括采集矿石、与敌对生物战斗、合成新的方块与收集各种在游戏中找到的资源的工具。游戏中的无限制模式让玩家在各种多人游戏服务器或他们的单人模式中进行创造建筑物、作品与艺术创作。其他功能包括逻辑运算与远程动作的红石电路、矿车及轨道，以及称之为“下界”的维度。最终，可以前往一个叫做“末地”的维度冒险，并击败末影龙。"

#全模式：把句子中所有可以成词的词语都扫描出来，速度非常快，但是不能解决歧义。
#这种全模式，会根据字典，将所有出现的字词全部匹配划分，所以会出现重复，显然，这不是我们需要的。
wordlist=jieba.cut(sent,cut_all=True)
print("|".join(wordlist))


#精确模式：试图将句子最精确地切开，适合文本分析（类似LTP分词方式）
#而这种精确模式就比较接近我们想要的了。
wordlist=jieba.cut(sent)#cut_all=Flase,和不写cut_all效果一样
print("|".join(wordlist))


#搜索引擎模式：在精确模式的基础上对长词再次切分，提高召回率，适合用于搜索引擎分词。
wordlist=jieba.cut_for_search(sent)
print('|'.join(wordlist))


#用户自定义模式
jieba.load_userdict('D:\\anaconda\\anaconda\\Lib\\site-packages\\jieba\\testdic.txt')
wordlist=jieba.cut(sent)#cut_all=Flase
print("|".join(wordlist))

#输出词性
words = pseg.cut("我是mc骨灰级玩家")
for word, flag in words:
    print('%s %s' % (word, flag))
