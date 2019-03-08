
# coding: utf-8

# - 0부터 9까지의 숫자로 이루어진 문자열을 입력받습니다.
# - 이 입력값이 0~9까지의 모든 숫자가 각각 한 번씩만 사용된 것인지 확인시켜줍니다.

# In[6]:


def str_to_ls(string):  #문자열을 리스트로 바꿔주는 함수
    Input_list = []
    for i in string:
        Input_list.append(i)
    return Input_list

def duplicate_num(input_str):
    #input에는 string을 넣으세요.
    input_ls = str_to_ls(input_str)   #입력값을 list로 만들어준다.
    input_ls.sort()                   #입력값을 sorting 시켜준다. 순서대로 만들어준다.
    z_to_n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  #비교군 데이터 입력
    i = 0
    while i <= len(z_to_n):             
        if len(input_ls) != len(z_to_n):  # 순서대로 만들었는대도 두 list의 길이가 다르면 일단 다른것이니 false 출력
            return False
            break
        elif i == len(z_to_n): # i를 차곡차곡 올려서 10개 성분에대한 검토가 끝나는 지점 체크
            return True        # 루프가 무사히 끝났다면 z_to_n가 완전히 같다는 것이니 True출력.
            break             # 루프를 끝낸다.
        elif input_ls[i] == z_to_n[i]: # 첫번째 if 조건에서 길이가 같았으면 성분들도 같은지 테스트
            i += 1                     # 같다는게 확인 될때마다 i를 1씩 높여주며 다음 성분을 비교한다.
        else:
            return input_ls[i] == z_to_n[i] # 성분들이 같지 않다면 false를 출력하고 루프 멈춤.
            break


# In[5]:


test_set = ['0123456789', '01234', '01234567890', '6789012345', '012322456789']   
test_result = [True, False, False, True, False]

for i in range(len(test_set)):
    print(duplicate_num(test_set[i]) == test_result[i])

