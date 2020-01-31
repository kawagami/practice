#! python3

# 考慮到輸入為負數、浮點數的狀況 所以套上abs()、float()
n = int(abs(float(input("請輸入正整數\n"))))

print("您輸入的n是", n, "\n")

Fibonacci = dict()
Fibonacci[0] = 0
Fibonacci[1] = 1


def MathFunction(order):
    if order == 0:
        print("序列", order, "的斐波那契數是", Fibonacci[order], ",")
    elif order == 1:
        print("序列", order, "的斐波那契數是", Fibonacci[order], ",")
    else:
        for i in range(order):

            # 因為起始為0 所以左項設為i+2
            Fibonacci[i+2] = Fibonacci[i+1]+Fibonacci[i]
            if i+2 == order:
                print("序列", i+2, "的斐波那契數是", format(Fibonacci[i+2], ","))
                break
            # # 顯示從第0項到第n-1項的數列
            # print("Fibonacci[", i+2, "]", "is", format(Fibonacci[i+2], ","))


MathFunction(n)

# n_time = 0
# # 當n大於1時
# if n > 1:
#     while n_time < n:
#         n_time += 1
#         if n_time == 0 or 1:
#             Fibonacci[n_time] = n_time
#         elif n_time > 1:
#             Fibonacci[n_time] = Fibonacci[n_time-1]+Fibonacci[n_time-2]
# print("Fibonacci Number Is", Fibonacci[n])
