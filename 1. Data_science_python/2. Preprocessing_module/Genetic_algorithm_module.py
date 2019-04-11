#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
from sklearn.model_selection import cross_val_score
import itertools
from sklearn.naive_bayes import *
from sklearn.metrics import * 

def generating_initial_generation(number_of_solutions, number_of_features):
    return np.random.choice([True, False], (number_of_solutions, number_of_features))


def solution_evaulation(X, Y, generation, model, metric):
    score_list = []
    for solution in generation:
        score = cross_val_score(model, X.iloc[:, solution], Y, cv=5, scoring = metric).mean() 
        score_list.append(score)
    return score_list

def top_k_solution_selection(solutions, score_list, k):
    score_list = np.array(score_list)
    top_k_index = (-score_list).argsort()[:k]
    selected_solutions = solutions[top_k_index]
    return selected_solutions

def one_point_crossover(solution1, solution2):
    sol_length = len(solution1)
    point = np.random.choice(range(1, sol_length - 1))
    new_solution = list(solution1[:point]) + list(solution2[point:])
    return (np.array(new_solution))

def flip_bit_muation(solution, prob):
    for i in range(len(solution)):
        random_number = np.random.random()
        if random_number <= prob: 
            solution[i] = 1 - solution[i] 
    return solution


# In[45]:


def genetic_algorithm(df_target, num_of_sol, num_of_top_sol, iter_number, fit_model, label_in_df, metric_scoring,                       mutation_ratio_in_sol=0.2, prob_mutation=0.1):
    '''
    유전 알고리즘 : 특징 선택 알고리즘으로 생명체의 유전 원리를 활용하여 최적의 특징 조합을 만들어서 반환.
    df_target : 유전 알고리즘을 수행할 데이터 프레임.
    num_of_sol : 한 세대에 포함되는 해의 갯수 (best 'n=100')
    num_of_top_sol : 한세대가 지나고 살아남을 상위 해의 갯수 및 미래 세대에 추가
    iter_number : 몇 세대 걸쳐서 유전 알고리즘을 진행할 것인지.
    fit_model : fitting에 사용할 모델. 객체화해서 모델 넣기 ex) model = BernoulliNB(), fit_model = model
    label_in_df : df_target의 label입력 ex) 'price'
    metric_scoring : scoring 방법 ex) 'r2', 'f1'
    mutation_ratio_in_sol (default= 0.2) : 매 세대마다 새로운 세대의 전체 해의 20%에 돌연변이 연산 적용
    prob_mutation (default= 0.1) : 돌연변이 연산을 수행하는 해의 성분 중 10%를 돌연변이바꿈. True->False/ False->True
    -----------------------------------------
    알고리즘 순서
    1. generating_initial_generation
     - 총 특징의 수(number_of_features)와 같은 길이를 가지는 행을 number_of_solutions개 만들어라.
     - 행의 성분은 True, False가 임의로 배치되어있음.
     - True로 되어있으면 그 위치의 column이 활성화된 것임.
    2. solution_evaulation
     - 해집단의 score을 평가한다.
    3. top_k_solution_selection
     - score 상위 k개를 고르고 나머지를 제거한다.
    4. one_point_crossover
     - 남아있는 탑랭크 데이터로 제거한만큼 자식데이터를 생성한다.
    5. flip_bit_muation
     - 새롭게 생성되는 자식데이터 중 돌연변이를 생성한다.
    6. 정해진 세대만큼 유전이 완료되면 종료한다.
    -----------------------------------------
    '''

    '''
    metric_scoring
    1. Classification
    ‘accuracy’	metrics.accuracy_score	 
    ‘balanced_accuracy’	metrics.balanced_accuracy_score	for binary targets
    ‘average_precision’	metrics.average_precision_score	 
    ‘brier_score_loss’	metrics.brier_score_loss	 
    ‘f1’	metrics.f1_score	for binary targets
    ‘f1_micro’	metrics.f1_score	micro-averaged
    ‘f1_macro’	metrics.f1_score	macro-averaged
    ‘f1_weighted’	metrics.f1_score	weighted average
    ‘f1_samples’	metrics.f1_score	by multilabel sample
    ‘neg_log_loss’	metrics.log_loss	requires predict_proba support
    ‘precision’ etc.	metrics.precision_score	suffixes apply as with ‘f1’
    ‘recall’ etc.	metrics.recall_score	suffixes apply as with ‘f1’
    ‘roc_auc’	metrics.roc_auc_score	 

    Clustering	 	 
    ‘adjusted_mutual_info_score’	metrics.adjusted_mutual_info_score	 
    ‘adjusted_rand_score’	metrics.adjusted_rand_score	 
    ‘completeness_score’	metrics.completeness_score	 
    ‘fowlkes_mallows_score’	metrics.fowlkes_mallows_score	 
    ‘homogeneity_score’	metrics.homogeneity_score	 
    ‘mutual_info_score’	metrics.mutual_info_score	 
    ‘normalized_mutual_info_score’	metrics.normalized_mutual_info_score	 
    ‘v_measure_score’	metrics.v_measure_score	 

    Regression
    ‘explained_variance’	metrics.explained_variance_score	 
    ‘neg_mean_absolute_error’	metrics.mean_absolute_error	 
    ‘neg_mean_squared_error’	metrics.mean_squared_error	 
    ‘neg_mean_squared_log_error’	metrics.mean_squared_log_error	 
    ‘neg_median_absolute_error’	metrics.median_absolute_error	 
    ‘r2’	metrics.r2_score	 
    '''
    
    # best score 리셋
    best_score = 0.00
    best_feature_set = []

    # features와 label 구분
    df = df_target
    X = df.drop(label_in_df, axis = 1)
    Y = df[label_in_df]

    current_generation = generating_initial_generation(number_of_solutions = num_of_sol, number_of_features = len(X.columns))
    
    for iter_num in range(1, 1+iter_number): # 유전 알고리즘을 iter_number회 수행
        print(iter_num, "- interation")
        # 해 평가 및 최고 해 저장 (best_score_index, best_feature_set)
        evaluation_result = solution_evaulation(X, Y, current_generation, model = fit_model, metric = metric_scoring)
        current_best_score = max(evaluation_result) # 현재 세대의 최고 성능 저장
        if current_best_score > best_score:
            best_score = current_best_score
            best_score_index = np.where(evaluation_result == best_score)
            best_feature_set = current_generation[best_score_index]
    
        # 상위 k개 해를 선택 및 미래 세대에 추가
        selected_solutions = top_k_solution_selection(current_generation, evaluation_result, num_of_top_sol)
        future_generation = selected_solutions
        
        for i in range(num_of_sol - num_of_top_sol): # n-k번을 반복하여 자식해를 생성
            p1 = np.random.randint(len(future_generation))  
            p2 = np.random.randint(len(future_generation))    
            parent_solution_1 = future_generation[p1] # 살아있는 해 (futer_generation) 중에 임의로 부모 선택
            parent_solution_2 = future_generation[p2] 
            child_solution = one_point_crossover(parent_solution_1, parent_solution_2) #one_point_crossover로 자식해 생성
            future_generation = np.vstack((future_generation, child_solution)) # child_solution을 future_generation에 추가
    
        for s in range(len(future_generation)):
            random_number = np.random.random() # 0~1사이의 랜덤 숫자 생성
            if random_number <= mutation_ratio_in_sol: # 랜덤으로 생성된 숫자가 mutation_ratio_in_sol이하면 그 해에대해 돌연변이 연산 적용
                future_generation[s] = flip_bit_muation(future_generation[s], prob = prob_mutation) # 요소에서 돌연변이 비율 0.1
    
    selected_features = X.columns[np.where(best_feature_set[0])[0]] # np.where : array의 성분 중 True인 것의 index 만 골라낸다.
    print(selected_features, best_score)
    return selected_features
    




