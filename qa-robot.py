q_dict = {
    "你好": "你好",
    "很高兴见到您": "我也很能高兴见到你",
    "你喜欢吃什么水果 ": "我喜欢橘子",
    "你今年多大了": "26 岁了",
    "你很漂亮": "谢谢"
}

flag = 'c'

work = True

print('你好，我是Python机器人')
print('你有时间跟我聊聊吗')
while flag == 'c' or 't':
    flag = input('您可以选择是否跟我聊天（c）,还是决定练习下wide对话能力（t）,或者让我退下（q）：')
    if flag == 't':
        question = input('输入你想问的：')
        answer = input('请输入问题答案：')
        q_dict[str(question)] = str(answer)
        print('学习成功！')
        print('现在我已经学会了%d个问题' % len(q_dict))
        continue
    elif flag == 'c':
        if len(q_dict) == 0:
            print('现在我还不会回答任何问题，请先让我学习：')
            continue
        chat_word = input('谢谢你跟我聊天，你想对我说些什么：')

        for key in sorted(q_dict.keys()):
            if str(chat_word) == key:
                work = True
                print(q_dict[key])
                break
            else:
                work = False

        if work == False:
            print('Sorry,这个问题我回答不上来')
            work = True
    elif flag == 'q':
        print('好的，那我们下次再聊')
        break
    else:
        print('请输入提示指令')
        continue
