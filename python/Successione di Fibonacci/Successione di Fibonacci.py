#! python3

n = int(abs(float(input("請輸入正整數\n"))))

print("您輸入的n是", n, "\n")

Fibonacci = dict()
Fibonacci[0] = 0
Fibonacci[1] = 1


def MathFunction(order):
    for i in range(order):
        Fibonacci[i+2] = Fibonacci[i]+Fibonacci[i+1]
        if i+2 == order:
            print(Fibonacci[i+2])
            break


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
