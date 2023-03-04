# 入力
input_line = input().split()

user_info = []
for i in range(int(input_line[0])):
    user_info.append(input().split())

update_info = []
for i in range(int(input_line[1])):
    update_info.append(input().split())

# 宣言(準備)
class User:
    def __init__(self, nickname, old, birth, state):
        self.nickname = nickname
        self.old = old
        self.birth = birth
        self.state = state

#本処理
result_users = []

for i in range(len(user_info)):
    result_users.append(User(user_info[i][0], user_info[i][1], user_info[i][2], user_info[i][3]))

for i in range(len(update_info)):
    result_users[int(update_info[i][0])-1].nickname = update_info[i][1]


print(result_users)
print(result_users[0].nickname)
print(result_users[1].nickname)
print(result_users[2].nickname)

# result_users.append(User("test1", "test2", "test3", "test4"))
# print(result_users)
# print(result_users[0])
# print(result_users[1])
#出力



        
# ↓練習用コード
# class User:
#     tmp = "unko"
#     tmpunko = "unko"
#     tmptoshio = "unko"
#     tmpitio = "unko"
    
#     def __init__(self, nickname, old, birth, state):
#         # self.nickname = realpart
#         # self.old = imagpart
#         self.test = nickname
#         self.old = old
#         self.birth = birth
#         self.state = state
        

tmp = User("test1", "test2", "test3", "test4")

# print("tmp.test:", tmp.test)
# print("tmp.tmp:", tmp.tmp)
# print("tmp.tmptoshio:", tmp.tmptoshio)

# user1 = User("mako", "13", "08/08", "nara")

# print("user1.test:", user1.test)

# print("user1.tmp:", user1.tmp)
# print("user1.tmptoshio:", user1.tmptoshio)
# tmp = User()
# tmp1 = User()
# tmp2 = User()


# print("tmp:", tmp)
# print("tmp:", tmp.tmp)

# print("tmp1:", tmp1)
# print("tmp1:", tmp1.tmp)
# print("tmp1:", tmp1.tmptoshio)

# print("tmp2:", tmp2)
# print("tmp2:", tmp2.tmp)
# print("tmp2:", tmp2.tmpitio)
# print("tmp:", tmp.nickname)
# print("tmp:", tmp.old)
# print("tmp:", tmp.birth)
# print("tmp:", tmp.state)
