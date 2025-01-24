import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText

# 配置邮件信息
sender_email = "hanyicraft@gmail.com"  # 发件人邮箱
sender_password = "hanyi2007518"  # 发件人邮箱密码（如果是 Gmail 等，可能需要应用专用密码）
receiver_email = "hanyicraft@gmail.com"  # 收件人邮箱

# 创建主窗口
root = tk.Tk()
root.title("Hanyi mit KI UmfrageA")

# 定义变量来存储用户输入
welcome_var = tk.StringVar()
name_var = tk.StringVar()
favorite_colours_var = tk.StringVar()
favorite_pet_var = tk.StringVar()


# 定义一个函数来处理提交按钮的点击事件
def submit():
    welcome = welcome_var.get()
    if welcome.lower() != "yes":
        messagebox.showinfo("WARNUNG", "Du würden Gehackt, von hanyi")
        root.destroy()
        return
    name = name_var.get()
    favorite_colours = favorite_colours_var.get()
    favorite_pet = favorite_pet_var.get()
    result = f"{name} favorite colour is {favorite_colours} and favorite pet is {favorite_pet}"

    # 构建邮件内容
    msg = MIMEText(result)
    msg['Subject'] = "用户问答信息"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        # 连接到 SMTP 服务器
        server = smtplib.SMTP('smtp.gmail.com', 587)  # 以 Gmail 为例，如果使用其他邮箱，需要修改服务器地址和端口
        server.starttls()
        # 登录发件人邮箱
        server.login(sender_email, sender_password)
        # 发送邮件
        server.sendmail(sender_email, receiver_email, msg.as_string())
        # 关闭连接
        server.quit()
        messagebox.showinfo("Erledigt", "Deins Nachricht würde gesendet！")
    except Exception as e:
        messagebox.showerror("Falsch", f"Nachricht können nicht sendet：{str(e)}")


# 创建标签和输入框
tk.Label(root, text="Hello, Welcome to Hanyi Program!").pack(pady=10)
tk.Entry(root, textvariable=welcome_var).pack(pady=5)

tk.Label(root, text="Whats your name?").pack(pady=10)
tk.Entry(root, textvariable=name_var).pack(pady=5)

tk.Label(root, text="Whats your favorite Colour?").pack(pady=10)
tk.Entry(root, textvariable=favorite_colours_var).pack(pady=5)

tk.Label(root, text="Whats your favorite pet?").pack(pady=10)
tk.Entry(root, textvariable=favorite_pet_var).pack(pady=5)

# 创建提交按钮
tk.Button(root, text="Eingeben", command=submit).pack(pady=20)

# 运行主循环
root.mainloop()
