
# coding: utf-8

# # 문자열 압축기

# - 문자열을 입력 받아 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하여 표시해줍니다.
# - 입력 예시: aaabbcccccca
# - 출력 예시: a3b2c6a1

# #### 스트링을 입력해주면 리스트로 출력해주는 함수 정의.

# In[1]:


def str_to_ls(string):
    Input_list = []
    for i in string:
        Input_list.append(i)
    return Input_list


# In[2]:


input_str = input("압축하고 싶은 문자열을 입력하세요 ex)aaabbcccdd : ")  # 입력
# string을 list로 변환하기
input_list = str_to_ls(input_str)
# 압축하기
result = []
count = 1
for i in range(len(input_list)):
    if i == len(input_list)-1:   #마지막 숫자에 도달하면
        result.append(input_list[i]) #마지막 알파벳 추가
        result.append(str(count))  #count 추가
        break
    elif input_list[i] == input_list[i+1]: # i번째 숫자와 다음 숫자가 같을 시 count만 올리기.
        count += 1
    else:
        result.append(input_list[i])   # i번째 숫자와 다음 숫자가 다를 시 숫자 세던 것 멈추고 result에 카운트한 결과들 추가.
        result.append(str(count))
        count = 1   # count 리셋
    
print( "{}은 ".format(input_str) + ''.join(result) + "로 압축이 됩니다.")

