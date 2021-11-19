# 選択式ソート実装する

from typing import List

def selection_sort(numbers: List[int])->List[int]:
    len_numbers = len(numbers)
    # 最小値を決める
    for cnt_i in range(len_numbers):
        min_idx = cnt_i
        for cnt_j in range(cnt_i+1,len_numbers):
            if numbers[min_idx] > numbers[cnt_j]:
                min_idx = cnt_j
        
        numbers[min_idx] ,numbers[cnt_i] = numbers[cnt_i],numbers[min_idx]
    return numbers

if __name__ == '__main__':
    nums = [5,4,3,2,1,0]
    print(selection_sort(nums))