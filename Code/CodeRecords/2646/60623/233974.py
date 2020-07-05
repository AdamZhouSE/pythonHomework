# 在《尼姆游戏》中，两名玩家轮流从堆或石头堆中移出物体。
# 假设有两个玩家A和B在玩游戏。每个都只能从堆中取出一块石头。挑选堆最后一块石头的玩家将赢得比赛。给定N堆中的石头数，如果玩家A开始游戏，则任务是找到获胜者。
size=int(input())
a=0
while a<size:
	b=input()
	if b%2==0:
		print("Player B")
	else:
		print("Player A")
	a=a+1