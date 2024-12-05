import random as ran

"""print(random.randint(1,20))"""

A = 1
B = 0
while A > B:

    x=ran.randint(1,3)
    hand = None
    C = 1
    D = 0
    while C > D:
       hand = input("グーかチョキかパーを入力してください")
       if hand != "グー" and hand != "チョキ" and hand != "パー":
           D += 0
           print("入力できるのは「グー」か「チョキ」か「パー」じゃ")
       else:
           D += 1


    "1=gu 2=tyoki 3=pa-"
    if hand== "グー":
        if x == 1:
            B += 0
            print("あいこ")
        elif x == 2:
            B += 1
            print("you win")
        else:
            B += 1
            print("you lose")
            
    elif hand == "チョキ":
        if x == 1:
            B += 1
            print("you lose")
        elif x == 2:
            B += 0
            print("あいこ")
        else:
            B += 1
            print("you win")
            
    else:
        if x == 1:
            B += 1
            print("you win")
        elif x == 2:
            B += 1
            print("you lose")
        else:
            B += 0
            print("あいこ")

#メモー予定
#次の目標　Tkinter使ってGUI要素を組み込む　グッチョッパはクリックで選択できるようにする
#最終的にはもっとコンパクトにしたい　関数使えば23～54行目の処理を繰り返し書かなくて済みそう
