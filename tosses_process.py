import random

# 定义初始条件
initial_balance = 100  # 初始金额为100美元
current_bet = 1  # 初始赌注为1美元
consecutive_tails = 0  # 连续反面次数初始为0
prob_head_initial = 0.7  # 第一次投掷获得正面的概率为0.7
prob_head_after_tail1 = 0.94  # 出现一次反面后再次投掷获得正面的概率为0.94
prob_head_after_tail2 = 1.0  # 出现两次反面后再次投掷获得正面的概率为1.0
win_multiplier = 1.25  # 赢得赌局时的赢钱倍数
loss_multiplier = 0.91  # 输掉赌局时的损失倍数

# 用于保存每次投掷后的余额
balance_history = []
toss_results = []

# 模拟50次硬币投掷
for _ in range(50):
    # 模拟一次硬币投掷
    toss_result = 'H' if random.random() < prob_head_initial else 'T'
    toss_results.append(toss_result)

    # 根据投掷结果和连续反面次数更新赌注和概率
    if toss_result == 'T':
        consecutive_tails += 1
        if consecutive_tails == 1:
            current_bet = 2  # 第一次反面，赌注变为2美元
        elif consecutive_tails == 2:
            current_bet = 4  # 连续两次反面，赌注变为4美元
    else:
        # 投掷为正面，重置连续反面次数和赌注
        consecutive_tails = 0
        current_bet = 1

    # 根据规则更新获胜概率
    if consecutive_tails == 1:
        prob_head_initial = prob_head_after_tail1
    elif consecutive_tails == 2:
        prob_head_initial = prob_head_after_tail2

    # 模拟赢得或输掉赌局，更新余额
    if toss_result == 'H':
        initial_balance += current_bet * win_multiplier  # 赢得赌局，余额增加
    else:
        initial_balance -= current_bet * loss_multiplier  # 输掉赌局，余额减少

    # 将当前余额添加到历史记录中
    balance_history.append(initial_balance)

# 输出每次投掷后的余额历史
print("Balance history after each toss:", balance_history)
print("Toss results:", toss_results)
