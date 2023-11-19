import re

__ANSWERS = """
1:
勇于承担
将会获得好的结果
A strong commitment will achieve good results

2:
谨慎处理
Approach cautiously

3:
绝对地
Definitely

4:
履行你应尽的义务
Follow through on your obligations

5:
如果你不抵触的话
If you don't resist

6:
这并不值得
放手一搏
It's not worth a struggle

7:
认真倾听
你就会知道
Listen more carefully
then you will know

8:
无论怎样
No matter what

9:
如果你能说“谢谢”
Provided you say
"Thank you"

10:
灵活变通
Remain flexible

11:
意料之外
Startling events

12:
这是你
永远不会忘记的
It is something you won't forget

13:
那将仍是不可预测的
It will remain umpredictable

14:
很有可能发生意外
Mishaps are highly probable

15:
将取决于你的选择
Others will depend on your choices

16:
重新斟酌你的方法
Reconsider your approach

17:
与另一种状况
息息相关
There is a substantial link
to another situation

18:
相信你的直觉
Trust your intuition

19:
尽你所能去进步
Upgrade any way you can

20:
走路要小心
Watch your step as you go

21:
你一定会得到支持
You are sure to have support

22:
你的行为
会使事物更加美好
Your actions will improve things

23:
局势尚未清晰
The situation is unclear

24:
大声说出来
Speak up about it

25:
找出更多办法来
Seek out more options

26:
立即停止
Press for closure

27:
行动起来
Move on

28:
笑一笑
Laugh about it

29:
貌似是有把握的
It seems assured

30:
调查了解之后
投人其中
Investigate and then enjoy it

31:
不要浪费你的时间
Don't waste your time

32:
别去赌
Don't bet on it

33:
耐心一点
Be patient

34:
绝对不
Absolutely not

35:
大方一点
Be more generous

36:
不要被压力
迫使着行事
Don't be pressured
into acting too quickly

37:
先去完成其他事
Finish something else first

38:
付出会有回报的
Gentle persistence will pay off

39:
那将是意外的
It could be extraordinary

40:
以好奇之心去探究
Explore it with playful curiosity

41:
那将是一件乐事
It will be a pleasure

42:
别犹豫
Don't hesitate

43:
此事不可取
It would be inadvisable

44:
拟一个清单
说明为什么
Make a list of why

45:
一人难成事
Not if you're alone

46:
重新考量一下
什么才是重要的
Reprioritize what is important

47:
三思而后行
Take more time to decide

48:
答案就在你身后
The answer is in your backyard

49:
你需要考虑
其他办法
You'll need to consider other ways

50:
有乐观的理由
There is good reason
to be optimistic

51:
你将得到支持
It will sustain you

52:
并非最佳时机
Unfavorable at this time

53:
不要被情绪左右
Don't get caught up
in your emotions

54:
拭目以待
Watch and see what happens

55:
你会发现
自己无法妥协
You could find yourself
unable to compromise

56:
带着你的善意
坚持到底
Follow through with your good intentions

57:
尝试剑走偏锋
Try a more unlikely solution

58:
毋庸置疑
Unquestionable

59:
为确保做出
最好的决定，
请冷静
To ensure the best decision, be calm

60:
其实你不是很在意
You don't really care

61:
相信你最初的想法
Trust your original thought

62:
发挥你的想象力
Use your imagination

63:
等一个更好的答复
Wait for a better offer

64:
等一等
Wait

65:
需要付出
足够的努力
A substantial effort
will be required

66:
你将不得不
放弃其他事物
You may have to drop other things

67:
对此表示怀疑
Doubt it

68:
赌一下
Bet on it

69:
一年后这件事
就没那么重要了
A year from now it won't matter

70:
跟随他人的引导
Follow someone else's lead

71:
把它写下来
Get it in writing

72:
记得找点乐子
Don't forget to have fun

73:
接受一个
日常上的改变
Accept a change to your routine

74:
你需要更多信息
you'll need more information

75:
鼓起勇气
adopt an adventurous attitude

76:
此时别再索求
Don't ask for any more at this time

77:
把精力放在
好好生活上
Focus on your home life

78:
让自己先休息一下
allow ourself to rest first

79:
最好再等等
Better to wait

80:
合作将是关键
Collaboration will be the key

81:
你必须立即行动
You must act now

82:
期望解决
Expect to settle

83:
欣喜地确认这一点
Be delightfully sure of it

84:
别傻了
Don't be ridiculous

85:
表现得就好像
这已经是真的了
Act as though it is already real

86:
别怀疑
Don't doubt it

87:
问问你爸爸
Ask your father

88:
听听过来人的意见
Follow the advice of experts

89:
辅助将会让你的
项目获得成功
Assistance would make
your progress a success

90:
你将会失望
You will be disappointed

91:
尽早去做
Do it carly

92:
问问你妈妈
Ask your mother

93:
规避第一种方案
avoid the first solution

94:
实际一点
Be practical

95:
把这当作一次机会
Consider it an opportunity

96:
数到10，再问一次
Count to 10, ask again

97:
以后再处理
Deal with it later

98:
那将是极好的
It's gonna be great

99:
别有顾虑
Don't be concerned

100:
追查一下其他线索
Follow something else's lead

101:
你必须在
离开的时候处理好
You'll have to make it up as you go

102:
找一个更清晰的视角
Get a clearer view

103:
付出你的全部
Give it all you've got

104:
要做就尽可能地
去做好，
不然就干脆别做
If it's done well; if not,
don't do it at all

105:
未知可否
It is uncertain

106:
不要忽视一般事实
Don't ignore the obvious

107:
不要做得太过
Don't overdo it

108:
别等了
Don't wait


109:
如果你能
按照叮嘱的去做
If you do as you're told

110:
其实你有很多选择
Realize that too many choices

111:
不会失败
It cannot fail

112:
保持开明
Keep an open mind

113:
必然的
It is certain

114:
节省你的精力
Save your chergy

115:
这并不重要
It is not significant

116:
告诉别人这对你来说
意味着什么
Tell someone what it means to you

117:
当局者迷
You are too close to sce

118:
这很重要
It is significant

119:
下不为例
Only do it once

120:
这必然会使事情
变得更加有趣
It is sure to make
things interesting

121:
你会获得最后的答复
You'll get the final word

122:
好事多磨
It is worth the trouble

123:
舍弃老方案
Leave behind old solutions

124:
此事可能已成定局
It may already be a done deal

125:
那将是浪费钱的
That would be a waste of money

126:
那可能不容易，
但你会发现它的价值
It may be difficult
but you will find value in it

127:
这将会影响
其他人对你的看法
It will affect how others see you

128:
是的
Yes

129:
它会带来好运的
It will bring good luck

130:
这将会引起轰动
It will create a stir

131:
负责
Take charge

132:
你最好把精力
放在自己的事情上
It would be better to
foras on the work

133:
你将被消耗
It'll cost you

134:
这正是
制订计划的好时候
It's good time to make plans

135:
以轻松的步伐前进
Proceed at a more relaxed pace

136:
你需要掌握主动权
You Il need to take the imitiative

137:
你该出发了
It's time for you to go

138:
不要告诉别人
Keep it to yourself

139:
事态瞬息万变
The circumstances
will change very quickly

140:
随它去吧
Let it go

141:
你可能会抵触
You may have opposition

142:
从不
Never

143:
现在你可以
Now you can

144:
当然
of course

145:
注意细节
Pay attention to the details

146:
你会后悔的
You'll regret it

147:
也许吧，当你成熟时
Perhaps, when you are older

148:
可能吧
Maybe

149:
不
No

150:
以防万一
Prepare for the unexpected

151:
你需要适应
You will need to accommodate

152:
相关问题
将会浮出水面
Related issues may surface

153:
你会发现
你所需要知道的一切
You will find out everything
you'll need to know

154:
消除自己的障碍
Remove your own obstacles

155:
遵守规则
Respect the rules

156:
确定优先顺序
是过程的必要部分
Setting priorities will be a
necessary part of the process

157:
立即解决
Settle it soon

158:
转移你的注意力
Shift your focus

159:
结果可能是
意料之外的
Startling events
may occur as a result

160:
把握机会
Take a chance

161:
你必须妥协
You'll have to compromise

162:
此事在你的控制之外
That's out of your control

163:
答案可能来自另一种语言
The answer may come to you
in another language

164:
最佳方案
未必容易被理解
The best solution may not be
the obvious one

165:
机会失不再米
The chance
will not come again scon

166:
结局将会是正面的
The outcome will be positive

167:
保证不了
There is no quarantee

168:
将会有困难
需要被克克服
There will be obstacles to overcome

169:
将会受到阻碍
There will be obstacles

170:
这正是
制订计划的好时候
It's good time to make plans

171:
无论你做什么，
结果都将是不可逆转的
Whatever you do,the results
will be lasting

172:
是的，但别勉强
Yes, but don't force it

173:
你比以前更清楚了
Vou know better now
than ever before

174:
你必须
You must

175:
你会发现
自己无法妥协
you could find yourself
unable to compromise

176:
把精力放在
好好生活上
Focus on your home life

177:
调查了解之后
投人其中
Tnvestigate and then enjoy it

178:
那将仍是不可预测的
It will remain unpredictable

179:
拭目以待
Watch and see what happens

180:
这将会影响
其他人对你的看法
It will affect how others see you

181:
此事在你的控制之外
That's out of your control

182:
谨慎处理
Approach cautiously

183:
这将会影响
其他人对你的看法
It will affect how others see you

184:
那将仍是不可预测的
It will remain unpredictable

185:
绝对地
Definitely

186:
如果你不抵触的话
If you don't resist

187:
认真倾听
你就会知道
Listen more carefully
then you will know

188:
如果你能说
“谢谢”
Provided you say
"Thank you"

189:
意料之外
Startling events

190:
那将仍是不可预测的
It will remain unpredictable

191:
其他事物
将取决于你的选择
Others will depend on your choices

192:
与另一种状况
息息相关
There is a substantial link
to another situation

193:
尽你所能去进步
tipgrade any way you can

194:
你一定会得到支持
You are sure to have support

195:
局势尚未清晰
The situation is unclear

196:
找出更多办法来
Seek out more options

197:
行动起来
Move on

198:
貌似是有把握的
It seems assured

199:
不要浪费你的时间
Don't waste your time

200:
耐心一点
Be patient

201:
大方一点
Be more generous

202:
先去完成其他事
Finish something else first

203:
那将是意外的
It could be extraordinary

204:
那将是一华乐事
It will be a pleasure

205:
此事不可取
It would be imadvisable

206:
一人难成事
Not if you're alone

207:
三思而后行
Take more time to decide

208:
你需要考虑
其他办法
you'll need to consider other ways

209:
你将得到支持
It will sustain you

210:
不要被情绪左右
Don't get caught up
in your emotions

211:
你会发现
自己无法妥协
You could find yourself
unable to compromise

212:
尝试剑走偏锋
Try a more unlikely solution

213:
为确保做出
最好的决定，
请冷静
To ensure the best decision, be calm

214:
相信你最初的想法
Trust your original thought

215:
等一个更好的答复
Wait for a better offer

216:
需要付出
足够的努力
A substantial effort
will be required

217:
对此表示怀疑
Doubt it

218:
一年后这件事
就没那么重要了
A year from now it won't matter


219:
把它写下来
Get it in writing

220:
接受三个
日常上的改变
Accept a change to your routine

221:
鼓起勇气
Adopt an adventurous attitude

222:
把精力放在
好好生活上
Focus on your home life

223:
最好再等等
Better to wait

224:
你必须立即行动
Vou must act now

225:
欣喜地确认这一点
Be delightfully sure of it

226:
表现得就好像
这已经是真的了
Act as though it is already real

227:
问问你爸爸
ask your father

228:
辅助将会让你的
项目获得成功
Assistance would make
your progress a success

229:
规避第一种方案
Avoid the first solution

230:
以后再处理
Deal with it later

231:
别有顾虑
Don't be concerned

232:
你必须在
离开的时候处理好
you'll have to make it up as you go

233:
付出你的全部
Give it all you've got

234:
未知可否
It is uncertain

235:
不要做得太过
Don't overdo it

236:
享受这段经历
Enjoy the experience

237:
其实你有很多选择
Realize that too many choices

238:
保持开明
Keep an open mind

239:
节省你的精力
Save your energy

240:
告诉别人这对你米说
意味着什么
Tell someone what it means to you

241:
这很重要
It is significant

242:
这必然会使事情
变得更加有趣
It is sure to make
things interesting

243:
好事多磨
It is worth the trouble

244:
此事可能已成定局
It may already be a done deal

245:
那可能不容易，
但你会发现它的价值
It may be difficult
but you will find value in it

246:
是的
yes

247:
这将会引起轰动
It will create a stir

248:
你最好把精力
放在自己的事情上
It would be better to
focus on the work

249:
这正是
制订计划的好时候
It's good time to make plans

250:
你需要掌握主动权
You'll need to take the imitiative
"""

ANSWER_TEMPLATE = """公主：
“{}”

>>>内容由AI翻书生成，仅供参考"""

answers_dict = {}
for answer in __ANSWERS.split("\n\n"):
    answer = answer.strip()
    if not answer:
        continue
    lines = answer.split("\n")
    idx = lines[0].strip().strip(":")
    content = "\n".join(lines[1:]).strip()
    answers_dict[idx] = content


def find_last_number(text):
    if text.startswith("@"):
        # 先去掉前面的@内容，取第一个空格之后的所有内容。
        text = text.split(" ", 1)[-1]
    pattern = r"\d+"
    matches = re.findall(pattern, text)
    filtered_numbers = [num for num in matches if int(num) <= 512]
    if filtered_numbers:
        last_number = filtered_numbers[-1]
        return last_number
    return None


def get_reply_content(number):
    number = str(number)
    if number in answers_dict:
        return ANSWER_TEMPLATE.format(answers_dict[number])
    return None
