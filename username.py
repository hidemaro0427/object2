"""
データ型宣言: UserName
    属性:
      実際のユーザー名
    ルール:
      ・ユーザー名は4文字以上20文字以下である
    できること => メソッド
      ・ユーザー名を大文字に変換する
"""

"""
type(1)
<class 'int'>
type("aaa")
<class 'str'>
type(0.1)
<class 'float'>
type(True)
<class 'bool'>
"""


class UserName:
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f"{name}は文字数のルール違反やで！")
        self.name = name

    # 名前の付け方は機能ではなくて、みんながわかる通称などの方が良い
    def screen_name(self):
        return self.name.upper


# UserNameクラスのインスタンス化
hibiki = UserName(name="hibiki")

print(hibiki.screen_name)
# print(type(hibiki))
# print(hibiki.name)

# sho = UserName("sho")
# print(sho.name)
