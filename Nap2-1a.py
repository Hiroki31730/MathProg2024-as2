#欲張り法を用いて前回レポートa1を解くプログラム

import numpy as np


#重さあたりの価値を算出し、ソートする関数
def sort_weight_value(we, va, number):
    s_list = [] 
    
    for i in range(number):
        s_list.append((i+1,we[i],va[i],float(va[i]/we[i])))

    #ソートしたリスト
    sorted_s_list = []

    #ソートする
    for x,y,z,w in sorted(s_list,key=lambda x:x[3],reverse = True):
        sorted_s_list.append((x,y,z,w))
        
    return sorted_s_list

#荷物数、ソートしたリスト、限界容量を代入してナップザックに荷物を入れる関数
def Nap_greedy(number,sort_list,C):  
    sum=0  #ナップザックの現在の容量
    sol = np.zeros(number)   #要素0の配列を生成
    for i in range(number):
        #重量あたりの価値が大きい物からナップザックに入れていく
        sum+=sort_list[i][1]
        if sum <= C:
            sol[sort_list[i][0]-1]=1         #容量オーバーしないなら入れる
        else:
            sum-=sort_list[i][1]
            sol[sort_list[i][0]-1]=0         #容量オーバーするので入れない
            
    
    return sol

#最大の容量、最大の価値を求める関数
def Nap_result(number,value,weight,sol):
    sum_value = 0 #最大の価値
    sum_weight = 0 #最大の重さ
    for i in range(number): #荷物を入れるかは0,1で決まっているため、乗算すれば最大が求められる。
        sum_value += sol[i]*value[i]
        sum_weight += sol[i]*weight[i]
    return sum_value,sum_weight



C = 25             #ナップザックの大きさ
number = 8          #品物の数

weight = [3, 6, 5, 4, 8, 5, 3, 4] #重さ
value = [7, 12, 9, 7, 13, 8, 4, 5] #価値

#重さあたりの価値を求めてソート
sort_list = sort_weight_value(weight,value,number)

#ナップザックにどの荷物が入るかのリスト
sol = Nap_greedy(number,sort_list,C)

#最大の価値、重さを求める
sum_value,sum_weight = Nap_result(number,value,weight,sol)


print("ナップザックの大きさ"+str(C))
print("価値")
print(np.round(value,3))
print("重さ")
print(np.round(weight,3))
print("選んだ品物")
print(sol)

print("選んだ品物の総価値")
print(str(sum_value))
print("選んだ品物の総容量")
print(str(sum_weight))

