#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns #Visulization

sns.set()

from scipy.stats import norm, skew



#root_meam_squared_error
def rmse(predictions, targets):
    '''
    root mean squared error을 계산해주는 함수.
    predictions : 예측치를 data frame으로 입력
    targets : 정답을 data frame으로 입력
    '''
    return np.sqrt(((predictions - targets) ** 2).mean())

def functions_list():
    # preprocessing_module 의 함수 list 출력
    from inspect import getmembers, isfunction
    #import preprocessing_module
    
    return [o[0] for o in getmembers(numpy) if isfunction(o[1])]
    

# In[2]:


def categ_or_contin(df, criterion=15, cat_or_cont=True, print_col = True):
    '''
    df의 column을 이루고 있는 value들 종류 갯수를 파악하여 연속형 변수와 범주형 변수로 구분해주는 함수.
    cat_or_cont = True (default) : 연속형 변수 출력
    cat_or_cont = False : 범주형 변수 출력
    criterion(default = 15) : 연속과 범주형의 기준 제시.
    ex) criterion = 15 : value의 종류가 15종이하이면 범주형 변수, 넘으면 연속형 변수
    ex) categ_or_contin(house6[0],15,False)
    '''   
    target_skew = df
    categorical = []
    continuous = []

    for column in target_skew: 
        if len(set(target_skew[column])) > criterion: # 범주형과 연속형 변수 구분 필요함. 
            continuous.append(column)  # 연속형
        else:
            categorical.append(column) #범주형
    if print_col == True:
        print('- categorical variables : ', categorical, '\n- continuous variables : ', continuous)
    return continuous if cat_or_cont==True else categorical


# In[4]:


def test_for_transf(df, col_str,transf_ls):
    '''
    Continous variable의 적절한 전처리를 위하여 '입력된 수식들로 변환된 column' vs 'frequency'의 그래프를 출력하는 함수.
    어떤 변환이 유용한지 한번에 여러 그래프 출력해서 비교해보고 싶을 때 유용.
    df : 해당 데이터프레임 입력
    col_str : df에서 확인해보고 싶은 column 하나를 string으로 입력 ex) 'price'
    transf_ls : 변환시켜 그려보고 싶은 변환 공식을 입력한다. 
        - 입력되어있는 수식은 다음과 같은 str형태로 입력 : 'x', 'log(x)', 'log(1+x)' 
          cf)  자주사용하는 함수 내에 equations dictionary에  입력해놓서 customize하면 편리.
        - 원하는 나만의 수식이 있을 시 lambda 함수 혹은 def function을 입력.
        - 입력 예시 : transf_ls = ['x', 'np.log(x)', lambda x : (x - house6[0]['price'].min())**(3/2)]
    '''
    # 자주사용하는 eqauation들 아래 dictionary에 입력해놓으면 편리함.
    equations = {'x' : lambda x: x, 'log(x)' : lambda x: np.log(x), 'log(1+x)' : lambda x: np.log(1+x)}

    target_col = col_str
    target = df[target_col]
    target_transf = transf_ls # test해보고 싶은 transf 수식들 다 list 안에 넣기
    
    df_transf = []
    for eq in target_transf:
        if type(eq) is type(lambda x : x): # eq의 type이 함수면 그대로 eq사용.
            eq = eq   
        elif type(eq) is str:    # eq의 type이 string이면 
            if eq in equations.keys(): # equations에서 불러올 수 잇는 함수가 있는지 체크
                eq = equations[eq]     # 불러올게 있다면 불러온다.
            else:                      # 없다면 경고문 출력
                print("{} 또는 lambda 함수를 입력해주세요 ex) 'lambda x: function'".format(list(equations.keys())))
        else: # 해당사항들 없으면 경고문 출력
            print("{} 또는 lambda 함수를 입력해주세요 ex) 'lambda x: function'".format(list(equations.keys())))
        df_transf.append(df[col_str].apply(eq)) # 어쨋든 함수 eq를 df[col_str]에 적용하고 list로 만듦. 이걸로 그래프그릴것임.
    
    for i in range(len(df_transf)):
        # let's plot a histogram with the fitted parameters used by the function
        sns.distplot(df_transf[i] , fit=norm); #df_transf에서 하나씩 꺼내서 그래프 그리기
        # get mean and standard deviation
        (mu, sigma) = norm.fit(df_transf[i]) ##
        # add legends to the plot
        plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(mu, sigma)],
                    loc='best')
        plt.ylabel('Frequency')
#        plt.title(target_col)
        plt.show()

# In[5]:


def check_skew(df, column_list_=None, skewness=1.5, criterion_of_cont_var=15, print_col_=True):
    '''
    df의 column인 column_list 중 왜도(skewness)가 1.5(default)보다 큰 column을 출력하는 함수.
    column_list(default=df.column, True = 연속형, False = 범주형, list = 그 list) 
            : df의 column들 중 왜도를 확인해볼 column list 입력. 
    skewness(default=1.5) : 기준 왜도값 입력.
    print_col_(default=True) : True이면 연속형 변수와 범주형 변수들을 리스트 형태로 보여줌
    '''
    target_skew = df
    if column_list_ == None: #구분할 행을 입력하지 않으면 df의 전체 행을 입력해준다.
        column_list=list(df.columns)
    elif column_list_ == True:
        column_list=categ_or_contin(target_skew,criterion_of_cont_var,True, print_col=print_col_)
    elif column_list_ == False:
        column_list=categ_or_contin(target_skew,criterion_of_cont_var,False, print_col=print_col_)
    else :
        column_list=column_list_
    # df.skew(): 열별 왜도
    biased_condition = abs(target_skew[column_list].skew()) > skewness # biased_condition : 1.5보다 크면 치우쳤다고 간주함
    # biased_variables: 왜도의 절대 값이 1.5보다 큰 변수
    biased_variables = target_skew[column_list].columns[biased_condition] 
    print('Columns {}에서 \n skewness가 {}보다 높은 columns은 {}이다.\n'.format(column_list, skewness, list(biased_variables)))
    


# In[6]:


def Remove_outliers(IQR_target_df,  col_target=None, dropna_inplace=False, criterion_of_cont_var=15, criterion_Q1=0.25, criterion_Q3=0.75):
    '''
    IQR rule에 따라 입력된 columns 또는 연속형 변수의 이상치를 제거해주는 함수.
    IQR rule : Q3-1.5*IQR보다 크거나 Q1-1.5*IQR보다 작으면 이상치라고 판단. 삭제
    IQR_target_df : 타겟이 될 데이터 프레임
    dropna_inplace : (True : NAN이 있는 행과 열 제거 한다) or (False : 제거 안하고 대상 행렬별 NAN 갯수 출력)
    col_target (default=None): 원하는 columns list 입력, 입력 안하면 전체 연속변수가 대상 
    criterion_of_cont_var (default=15) : 연속형 변수의 기준.
    ex) Remove_outliers(house4_1[0], 20)
    '''
    IQR_target = IQR_target_df 
    if col_target == None:
        col_target = categ_or_contin(IQR_target,criterion_of_cont_var,print_col=False)
        
    len_before = len(IQR_target)
    Q1 = IQR_target[col_target].quantile(criterion_Q1)
    Q3 = IQR_target[col_target].quantile(criterion_Q3)
    IQR = Q3 - Q1
    condition1 = Q1 - 1.5*IQR < IQR_target[col_target]
    condition2 = Q3 + 1.5*IQR > IQR_target[col_target]
    # IQR rule : Q3-1.5*IQR보다 크거나 Q1-1.5*IQR보다 작으면 이상치라고 판단. 삭제

    if dropna_inplace == True:
        IQR_target[col_target] = IQR_target[col_target][condition1 & condition2]
        IQR_target.dropna(inplace= True)
        IQR_target.reset_index(drop=True, inplace=True)
        len_after = len(IQR_target)
        print('Outliers are completely removed. Length is redeced from {} to {}'.format(len_before, len_after))
        return IQR_target
    else:
        return pd.DataFrame(IQR_target[col_target][condition1 & condition2].isnull().sum().rename('# of NAN'))
# In[7]:


def count_category(target, col_target=None, criterion_of_cont_var=15, sort_category = False):
    '''
    target의 columns 중 categorical variable의 category 종류 및 각 category에 대한 샘플의 수를 count해주는 함수.
    target : 원하는 dataframe을 입력.
    col_target (default=None) : 특정 column에 대해 확인해보고 싶을시 list 형태로 입력
    criterion_of_cont_var (default=10) : categorical variable의 기준을 입력.
        ex) criterion_of_cont_var=10 : variable이 10 종 이하로 전부 분류되면 categorical variable.
    sort_category (default = False) : False면 sample수가 많은 카테고리 순으로 배열, True면 카테고리를 오름차순으로 배열
    '''
    count_target = target
    result = []
    if col_target == None: # 원하는 col을 따로 입력 안할 시 모든 categorical var에대해 체크
        categ_var = categ_or_contin(count_target,criterion_of_cont_var,False,False)
    else : 
        categ_var = col_target
    
    for i in range(len(categ_var)):
        pd_count = count_target[categ_var[i]].value_counts()
        pd_count = pd_count.reset_index().rename(columns = {'index': 'category'})
        if sort_category == True:
            pd_count.sort_values(by = ['category'], ascending=sort_category, inplace=True)
            pd_count.reset_index(drop=True, inplace=True)
        result.append(pd_count)
    return pd.concat(result,axis=1)


# In[8]:

def rowXcol_for_subfig(length):
    '''
    입력된 길이를 포함 할 수 있는 적절한 행과 열을 결정해준다. cf) row_len, col_len = rowXcol_for_subfig(len(df))
    ex) rowXcol_for_subfig(len(df)) : df의 feature(의 그래프)를 행렬로 만들기 위한 행의 길이와 열의 길이을 결정해준다.
    '''
    row_len = int(round(length**(1/2),0))
    col_len = int(round(length/row_len,0))+1 if row_len*round(length/row_len,0) < length else int(round(length/row_len,0))
    return row_len, col_len

def one_feature_vs_freqency(df_target, col_name, loc_='best'):
    '''
    f_target의 feature인 col_name의 분포(frequency)를 행렬 그래프로 그리는 함수(왜도, 평균, 표준편차 표시)
    df_target : 그래프를 그려볼 data frame
    col_name : 그래프를 그려볼 featreu 이름 type = str
    loc_ : lengend 위치 설정
        ex) loc_ = 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 
            'center left', 'center right', 'lower center', 'upper center', 'center' 
    '''
    target = df_target[col_name]
    col_target = col_name
    
    # skewness 체크
    print("Skewness: %f" % target.skew())
    
    # let's plot a histogram with the fitted parameters used by the function
    sns.distplot(target , fit=norm);
    # get mean and standard deviation
    (mu, sigma) = norm.fit(target)
    # add legends to the plot
    plt.legend(['Normal dist. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(mu, sigma)],
                loc=loc_)
    plt.ylabel('Frequency')
    plt.title(col_target);


def features_vs_frequency(df_target_, col_target=None, criterion_of_cont_var=15, figsize_tuple_=(12,10), loc_='best'):
    '''
    df_target_의 features_들의 분포를 행렬 그래프로 그리는 함수
    col_target (default=None / True : 연속형만 선택) : 빈도 분포를 파악하기를 원하는 features를 list형태로 입력.
    df_target_ : 그래프들 그려볼 data frame
    criterion_of_cont_var (default=15) : continuous variable의 기준! ex) 15 = value가 15종 이상으로 나눠지면 연속형변수.
        cf) col_target =True 일때는 중요. 아니면 불필요.
    figsize_tuple_ : 전체 그래프 사이즈를 튜플로 입력
    loc_ : lengend 위치 설정
      ex) loc_ = 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 
                'center left', 'center right', 'lower center', 'upper center', 'center' 
    '''    
    df_target = df_target_
    figsize_tuple = figsize_tuple_
    
    if col_target == None: #구분할 행을 입력하지 않으면 df의 전체 행을 입력해준다.
        col = list(df_target.columns)
    elif col_target == True:
        col = categ_or_contin(df_target,criterion_of_cont_var,True,False)
    else :
        col = col_target
        
    # data frame의 feature의 갯수에 따라 적절한 행과 열을 결정해준다. 
    row_len, col_len = rowXcol_for_subfig(len(col))
    print('그래프가 {}X{}행렬로 그려집니다.'.format(row_len, col_len))
    
    # let's plot a histogram with the fitted parameters used by the function
    fig = plt.figure(figsize=figsize_tuple)
    for i in range(len(col)):
        target = df_target[col[i]]
        axi = fig.add_subplot(row_len,col_len,i+1)
        sns.distplot(target , fit=norm, ax=axi)
        plt.ylabel('Frequency')
        plt.legend([col[i]], loc=loc_)


# In[9]:


def features_vs_label(df_target_, label_str , col_target=None,criterion_of_cont_var=15, figsize_tuple_ = (12,10), loc_='best'):
    '''
    df_target_의 col_target vs label를 행렬 그래프로 그리는 함수
    col_target (default=None / True : 연속형만 선택) : label에 대한 분포를 파악하기를 원하는 features를 list형태로 입력.
    df_target_ : 그래프들 그려볼 data frame
    label_str : df_target_의 label을 str 형태로 입력.
    criterion_of_cont_var (default=15) : continuous variable의 기준! ex) 15 = value가 15종 이상으로 나눠지면 연속형변수.
        cf) col_target =True 일때는 중요. 아니면 불필요.
    figsize_tuple_ : 전체 그래프 사이즈를 튜플로 입력
    loc_ : lengend 위치 설정
      ex) loc_ = 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 
                'center left', 'center right', 'lower center', 'upper center', 'center' 
    '''
    df_target = df_target_
    figsize_tuple = figsize_tuple_
    
    if col_target == None: #구분할 행을 입력하지 않으면 df의 전체 행을 입력해준다.
        col = list(df_target.columns)
    elif col_target == True:
        col = categ_or_contin(df_target,criterion_of_cont_var,True,print_col = False)
    else :
        col = col_target
    
    # data frame의 feature의 갯수에 따라 적절한 행과 열을 결정해준다.
    row_len, col_len = rowXcol_for_subfig(len(col))
    print('그래프가 {}X{}행렬로 그려집니다.'.format(row_len, col_len))

    # columns vs label
    fig = plt.figure(figsize=figsize_tuple)
    for i in range(len(col)):
        axi = fig.add_subplot(row_len,col_len,i+1)
        sns.regplot(x=col[i], y=label_str, data=df_target, ax=axi)
        plt.legend([col[i]], loc=loc_)


# In[10]:


def features_Boxplot(df_target_, y_label ,col_target_cat = None, criterion_of_cat_var=15, figsize_tuple_ = (12,10)):
    '''
    df_target_의 categorical variabel의 분포를 Boxploe의 행렬로 그려주는 함수
    df_target_ : 그래프들 그려볼 data frame
    y_label : df_target_의 label을 입력. Box plot의 y축을 담당할 것임
    col_target_cat (default=None): 원하는 columns list 입력, 입력 안하면 전체 categorical 변수가 대상
    criterion_of_cat_var (default=15) : categorical variable의 기준! ex) 15 = value가 15종 밑으로 나눠지면 categorical임.
        cf) col_target_cat =None 일때는 중요. 아니면 불필요.
    figsize_tuple_ : 전체 그래프 사이즈를 튜플로 입력
    '''    
    df_target = df_target_
    figsize_tuple = figsize_tuple_
    
    if col_target_cat == None: #구분할 행을 입력하지 않으면 df의 전체 행을 입력해준다.
        col = categ_or_contin(df_target,criterion_of_cat_var,False,False)
    else :
        col = col_target_cat  
    
    # data frame의 feature의 갯수에 따라 적절한 행과 열을 결정해준다. 
    row_len, col_len = rowXcol_for_subfig(len(col))
    print('그래프가 {}X{}행렬로 그려집니다.'.format(row_len, col_len))
    
    # let's plot a histogram with the fitted parameters used by the function
    fig = plt.figure(figsize=figsize_tuple)
    
    for i in range(len(col)):
        axi = fig.add_subplot(row_len,col_len,i+1)
        sns.boxplot(x=col[i], y=y_label, data=df_target, ax=axi)        





# In[11]:


def corr_heatmap(df_corr, sort_by_col, column_list_=None, figsize_tuple=(12, 10), ascending_=False, palette_color='purple', fmt_=".2f"):
    '''
    df_corr의 feature+label 사이의 correlation coefficient를 heatmap으로 나타내는 함수.
    df_corr : 상관계수 heatmap을 그려 볼 data frame
    sort_by_col : 상관계수를 sort_by_col 기준으로 정렬 cf) 보통 label로 설정
    fig_size (default=(12, 10)) : heatmap figure size
    ascending_ (default=False) : 상관계수 내림차순 정렬(False), 오름차순 정렬(True)
    palette_color (default='purple') : 상관계수 나타낼 색
    fmt_ (default=".2f") : 표시되는 상관계수의 자릿수. cf) ".2f": 소숫점 2자리수 float
    '''
    
    if column_list_ == None: #구분할 행을 입력하지 않으면 df의 전체 행을 입력해준다.
        column_list = list(df_corr.columns)
    else :
        column_list = column_list_
    
    # 상관계수 구해서 그래프 그리기.
    h_corr = df_corr[column_list].corr(method='pearson').sort_values(by=[sort_by_col], ascending = ascending_)                .sort_values(by=[sort_by_col], axis =1, ascending=ascending_)  
    # 상관계수 dataframe /  가격과 상관계수 큰 순으로 정렬(행과 열 모두다 정렬)
    
    #heatmap으로 그리기
    plt.figure(figsize=figsize_tuple)
    sns.heatmap(h_corr, cmap=sns.light_palette(palette_color, as_cmap=True), annot=True, fmt=fmt_)
    plt.show()


def x_vs_y_with_fixed_col(df_target, x_col, y_col, fixed_col, ylim_b=None, ylim_t=None, figsize_tuple=(12,10), loc_='best'):
    '''
    범주형 변수(fixed_col)의 범주별로 x_col vs y_col 그래프 출력 함수
    df_target : data frame 입력
    x_col : df_target의 columns 중 x축에 들어갈 변수명 입력.
    y_col : df_target의 columns 중 y축에 들어갈 변수명 입력.(ex) label 입력
    fixed_col : df_target의 columns 중 범주별로 그려보고 싶은 변수명 입력
    ylim_b (default=None) : 그래프 y축 범위 설정 cf) plt.ylim=(ylim_b, ylim_t)
    ylim_t (default=None) : 그래프 y축 범위 설정
    figsize_tuple (default==(12,10)) : 그래프 전체 사이즈 튜플로 입력
    loc_ (default='best') : Legend 위치 입력
        ex) loc_ = 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 
                'center left', 'center right', 'lower center', 'upper center', 'center' 
    '''    
    target = df_target 
    
    category_ls = list(count_category(target,[fixed_col],sort_category=True)['category']) #특정 범주형 변수의 범주 종류 list화
    j=0
    fig = plt.figure(figsize=figsize_tuple)
    row_len, col_len = rowXcol_for_subfig(len(category_ls))
    for i in category_ls:
        j+=1
        h_test = target[(target[fixed_col]==i)]
        if ylim_b==None:
            ylim_b_ = h_test[y_col].min()
        else:
            ylim_b_ = ylim_b
        if ylim_t==None:
            ylim_t_ = h_test[y_col].max()
        else:
            ylim_t_ = ylim_t
        axi = fig.add_subplot(row_len,col_len,j)
        sns.regplot(x=x_col, y=y_col, data=h_test, ax=axi)
        plt.ylim(ylim_b_,ylim_t_)
        plt.legend(['{} : {}'.format(fixed_col, i)], loc=loc_)

        
def corr_btw_x_y_VS_fixed_col(df_target, x_col, y_col, fixed_col, figsize_tuple=(7,6), palette_color='purple', fmt_=".2f"):
    '''
    범주형 변수(fixed_col)의 범주별로 x_col vs y_col 그래프 출력 함수
    df_target : data frame 입력
    x_col : df_target의 columns 중 x축에 들어갈 변수명 입력.
    y_col : df_target의 columns 중 y축에 들어갈 변수명 입력.(ex) label 입력
    fixed_col : df_target의 columns 중 범주별로 그려보고 싶은 변수명 입력
    ylim_b (default=None) : 그래프 y축 범위 설정 cf) plt.ylim=(ylim_b, ylim_t)
    ylim_t (default=None) : 그래프 y축 범위 설정
    figsize_tuple (default==(12,10)) : 그래프 전체 사이즈 튜플로 입력
    loc_ (default='best') : Legend 위치 입력
        ex) loc_ = 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 
                'center left', 'center right', 'lower center', 'upper center', 'center' 
    '''    
    target = df_target 
    
    category_ls = list(count_category(target,[fixed_col],sort_category=True)['category']) #특정 범주형 변수의 범주 종류 list화
    j=0
    fig = plt.figure(figsize=figsize_tuple)
    row_len, col_len = rowXcol_for_subfig(len(category_ls))
    
    data = []
    
    for i in category_ls:
        h_corr = target[target[fixed_col]==i][[x_col, y_col]].corr(method='pearson')
        x_y_corr = h_corr.loc[x_col, y_col]
        print('The correlation between {} and {} in {}({}) is {}.'.format(x_col, y_col, fixed_col, i, round(x_y_corr,2)))
        data.append(x_y_corr)
    
    plt.plot(data)
    plt.xlabel(fixed_col)
    plt.ylabel('correlation coefficient')
    plt.title('Correlation Coefficient btw {} and {}'.format(x_col, y_col))
    plt.show()     
        

