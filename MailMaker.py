import win32com.client

# OutlookAppのインスタンス化
outlook = win32com.client.Dispatch("Outlook.Application")
# NameSpaceオブジェクトのインスタンス化
mapi = outlook.GetNameSpace("MAPI")

# メールオブジェクトの作成
mail_obj = outlook.CreateItem(0)

# 宛先
mail_obj.To = "×××@××.co.jp; ooo@ooo.co.jp"
# CC
mail_obj.CC = "×××@××.co.jp"
# BCC
mail_obj.BCC = "×××@××.co.jp"
# 件名
mail_obj.Subject = "××の件"

# mail_obj.SenderEmailAddress = "×××@××.co.jp"