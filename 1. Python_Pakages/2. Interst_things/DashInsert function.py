
# coding: utf-8

# # DashInsert 함수

# - DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤, 문자열 내에서 홀수가 연속되면 두 수 사이에 - 를 추가하고, 짝수가 연속되면 \* 를 추가하는 기능을 갖고 있다. (예, 454 => 454, 4546793 => 454\*67-9-3)
# 
# - 입력 : 화면에서 숫자로 된 문자열을 입력받는다.
# 13423626134
# - 출력 : \*, -가 적절히 추가된 문자열을 화면에 출력한다.
# 1-34*236*2*61-34

# In[1]:


def DashInsert(a):
    a_str = str(a)   # 숫자로 받은 값을 indexing을 위해서 string으로 변환.
    a_mod = ''       # 비어있는 string.
    for i in range(len(a_str)) : # a의 값들을 하나씩 불러낸다.
        if i == len(a_str)-1 :   # a의 마지막 값까지 오면 \*도 -도 안붙일 것이기때문에 기대로 끝.
            a_mod += a_str[i]    # a_mod에 추가
        elif int(a_str[i])%2 == 0 and int(a_str[i+1])%2 == 0 : # a_str[i]과 그 다음 것이 짝수인지 체크.
            a_mod = a_mod + a_str[i] + '*'                     # 그렇다면 \*붙이기
        elif int(a_str[i])%2 == 1 and int(a_str[i+1])%2 == 1 : # a_str[i]과 그 다음 것이 홀수인지 체크.
            a_mod = a_mod + a_str[i] + '-'                     # 그렇다면 -붙이기
        else :
            a_mod = a_mod + a_str[i]                           # 나머지 경우엔 그냥 붙여넣기
    return a_mod   #a_mod출력


# In[10]:


DashInsert(13423626134)

