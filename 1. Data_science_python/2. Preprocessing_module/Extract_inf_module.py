#!/usr/bin/env python
# coding: utf-8

# In[1]:

import re
import numpy as np


class ExtractInf():

    def __init__(self, string):
        self.str = string
        self.patt_email = "[0-9a-zA-Z_]+@[a-zA-Z]+\.[a-zA-Z]+"
        self.patt_phone_num = "[01영공일빵oO]{3}[-]?[0-9영공일이둘삼사오육칠팔구빵oO]{3,4}[-]?[0-9영공일이둘삼사오육칠팔구빵oO]{4}"
        self.patt_resid = "[0-9영공일이둘삼사오육칠팔구빵oO]{6}-?[1-4일이둘삼사]{1}[0-9영공일이둘삼사오육칠팔구빵oO]{6}"
        self.num_dic = {'영' : '0', '공' : '0', '일' :'1', '이' : '2', '둘' : '2', '삼' : '3', '사' : '4', '오' : '5', '육' : '6', '칠' : '7', '팔' : '8', '구' : '9', '빵' : '0',                        'o' : '0', 'O' : "0", '-' : '-', '0' : '0', '1' :'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}
   
    def email(self):
        email_ls = re.findall(self.patt_email, self.str) #이메일 처리 완료
        return email_ls

    def resid(self):
        resid_num_raw = re.findall(self.patt_resid, self.str)    #주민등록번호  #후처리 필요
        resid_num = []
        for i in range(len(resid_num_raw)): #주민번호를 숫자로 변환
            result = ''
            try:
                for num in resid_num_raw[i]:
                    result += self.num_dic['{}'.format(num)]
            except Exception as e:   #오류나면 메세지 호출
                print(e)#'error')
            result = re.sub("([0-9]{6})-?([1-4]{1})([0-9]{6})", "\g<1>"+'-'+'\g<2>'+'******', result)    # 주민번호 뒷번호 블라인드처리
            resid_num.append(result)
        return resid_num

    def phone(self):
        phone_num_raw = re.findall(self.patt_phone_num, self.str) #전화번호 #후처리 필요
        phone_num = []
        for i in range(len(phone_num_raw)):  #전화번호를 숫자로 변환
            result = ''
            try:
                for num in phone_num_raw[i]:
                    result += self.num_dic['{}'.format(num)]
            except Exception as e:    #오류나면 메세지 호출
                print(e)#'error')
            phone_num.append(result)
        return phone_num


# In[ ]:




