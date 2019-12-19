from tkinter import *

#画面表示
root = Tk()

#ウィンドウ名
root.title("calculator")

#文字入力
def func(v):
    var1.set(var1.get() + v)
    
#C機能（一文字削除)
def clear():
    one_word = var1.get()
    one_word = one_word[:-1]
    var1.set(one_word)

#AC機能
def all_clear():
    var1.set("")
    
#結果
def result():
    try:
        var1.set(eval(var1.get()))
    except SyntaxError:
        var1.set("SyntaxError")
    except ZeroDivisionError:
        var1.set("ZeroDivisionError")
    except NameError:
        var1.set("NameError")
        
#画面表示
var1 = StringVar()

label = Label(root, textvariable=var1, fg="#ffffff",
              bg="#000000", anchor=E, height=2)
label.grid(row=0, column=0, columnspan=4, sticky="EW")

#1列目
btn_c = Button(root, text="C", command=clear, width=5, height=2)
btn_c.grid(row=1, column=0)
btn_ac = Button(root, text="AC", command=all_clear, width=5, height=2)
btn_ac.grid(row=1, column=1)
btn_p = Button(root, text = "%", command = lambda: func("%"), width = 5, height = 2)
btn_p.grid(row = 5, column = 2)
btn_add = Button(root, text="+", command=lambda: func("+"), width=5, height=2)
btn_add.grid(row=1, column=3)

#2列目
btn_7 = Button(root, text="7", command=lambda: func("7"), width=5, height=2)
btn_7.grid(row=2, column=0)
btn_8 = Button(root, text="8", command=lambda: func("8"), width=5, height=2)
btn_8.grid(row=2, column=1)
btn_9 = Button(root, text="9", command=lambda: func("9"), width=5, height=2)
btn_9.grid(row=2, column=2)
btn_div = Button(root, text="/", command=lambda: func("/"), width=5, height=2)
btn_div.grid(row = 2, column = 3)

#３列目
btn_4 = Button(root, text="4", command=lambda: func("4"), width=5, height=2)
btn_4.grid(row=3, column=0)
btn_5 = Button(root, text="5", command=lambda: func("5"), width=5, height=2)
btn_5.grid(row=3, column=1)
btn_6 = Button(root, text="6", command=lambda: func("6"), width=5, height=2)
btn_6.grid(row=3, column=2)
btn_mul = Button(root, text="*", command=lambda: func("*"), width=5, height=2)
btn_mul.grid(row=3, column=3)

#４列目
btn_1 = Button(root, text="1", command=lambda: func("1"), width=5, height=2)
btn_1.grid(row=4, column=0)
btn_2 = Button(root, text="2", command=lambda: func("2"), width=5, height=2)
btn_2.grid(row=4, column=1)
btn_3 = Button(root, text="3", command=lambda: func("3"), width=5, height=2)
btn_3.grid(row=4, column=2)
btn_sub = Button(root, text="-", command=lambda: func("-"), width=5, height=2)
btn_sub.grid(row=4, column=3)

#５列目
btn_0 = Button(root, text="0", command=lambda: func("0"), width=5, height=2)
btn_0.grid(row=5, column=0)
btn_pt = Button(root, text=".", command=lambda: func("."), width=5, height=2)
btn_pt.grid(row=5, column=1)
btn_pt = Button(root, text="=", command=result, width=5, height=2)
btn_pt.grid(row=5, column=3)

#絶対に必要な処理（これがないと動かない）
root.mainloop()
