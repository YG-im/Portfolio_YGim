
# coding: utf-8

# - 모스부호를 암호화하고 해독하는 프로그램입니다.
# - 문자열 형식으로 입력받은 모스 부호(dot: . dash:-)를 암호화하는 Encode 함수가 있습니다.
# - 문자열에서 모스부호로 바꿀 때, 글자와 글자 사이는 공백 하나, 단어와 단어 사이는 공백 두개로 구분합니다.
# - 모스부호를 해독하는 Decode함수가 잇습니다.

# In[1]:


#모스부호 처리하는 클래스

class Morse:

    #모스부호 데이터 전처리해서 딕셔너리로 만들기

    def dic_morse(self):
        morse1 = 'A .- B -... C -.-. D -.. E . F ..-. G --. H .... I .. J .--- K -.- L .-.. M -- N -. O --- P .--. '
        morse2 = 'Q --.- R .-. S ... T - U ..- V ...- W .-- X -..- Y -.-- Z --..' #모스부호들 정보 가져오기
        morse = morse1 + morse2
        morse_list = morse.split(" ")
        key = []
        value = []
        for i in range(len(morse_list)):
            if i%2 == 0:
                key.append(morse_list[i]) #moss에서 짝수면 키로 홀수면 값의 집합으로.
            else:
                value.append(morse_list[i])
        return {'encode' : dict(zip(key, value)), 'decode' : dict(zip(value, key))} #분류한것들 딕셔너리로 넣기.

    def Encode(self, string):
        
        input_str_up = string.upper() # 인코딩하려는 스트링을 모두 대문자로 바꾸기.
        result = ''
    
        for key in input_str_up:  
            if key == " ":   # 띄어쓰기는 두개띄어쓰기로 변형
                result += '  '
            else:
                result = result + self.dic_morse()['encode'][str(key)] + ' '  #알파벳은 모스부호로 바꾸고 그 뒤에 띄어쓰기 하기E
        
        return result
    
    def Decode(self, string):
        
        input_str_split = string.split('  ')
        result = ''
    
        for i in range(len(input_str_split)):
            input_str_split2 = input_str_split[i].split(' ')
            for key in input_str_split2:  
                if key == '':
                    result += ' '
                elif key in self.dic_morse()['decode']:
                    result = result + self.dic_morse()['decode'][str(key)]  #알파벳은 모스부호로 바꾸고 그 뒤에 띄어쓰기 하기
                else:
                    result = result + "'error'" + ' '
        return result


# In[2]:


#모스부호 암호화 체크
morse = Morse()

#moss.dic_moss()['decode']
morse.Encode('Hello Python')


# In[3]:


#모스부호 해독기 체크
morse.Decode(_)

