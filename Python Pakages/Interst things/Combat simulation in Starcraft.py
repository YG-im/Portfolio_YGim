
# coding: utf-8

# # 스타그래프트 전투 시뮬레이션
# - 마린의 체력은 50, 메딕의 체력은 20입니다.
# - 마린끼리 전투를 할 수 있고, 마린의 공격력은 5로 디폴트되어있습니다. 원할시 업그레이드 가능합니다.
# - 메딕은 마린을 치료할 수 있고 한번에 6씩 치료가 가능합니다.
#  

# In[40]:


class Human:  #사람에 대해 정의하는 클래스.
    
    def __init__(self):
        self.health = 50  #체력 디폴트값 설정.

    def set_health(self, var):
        self.health += var #공격 및 힐에 따른 체력 증감을 반영해주는 수식.


# In[41]:


class Marin(Human):
    
    def __init__(self, attack_power = 5, kill = 0): #attack_power에 디폴트값줌.
        super().__init__() #Human의 init을 가져온다. 이거 아니면 변수 다시 다 적어줘야하니..
        self.attack_power = attack_power
        self.kill = kill
        
    def stimpack(self): #체력이 1/3으로 깍인다. 공격력이 2배로 증가.
        self.health = self.health//3
        self.attack_power = 2 * self.attack_power
        
    def attack(self, unit): #괄호에입력한 유닛의 체력을 깍는다.
        
        if unit.health == 0:  # 유닛 클래스에 health를 불러와서 체력 확인.
            return "aleady die!"
        
        unit.set_health(-self.attack_power)  #unit 클래스에서 상속한 human클래스의 set_health함수를 통해 어택만큼 깍는다.
        
        if unit.health <= 0:
            unit.health = 0
            self.kill += 1   # 유닛 죽이면 킬수 하나 올려준다.
            return "die" # killed
        
        return "health:{}".format(unit.health) # alive #"alive [health:{}]"


# In[35]:


class Medic(Human):
    
    def __init__(self):
        self.health = 20   #메딕의 체력은 마린보다 낮게 설정.
        self.heal_power = 6 #메딕의 힐 파워 설정.
    
    def heal(self, unit):
        
        if unit.health == 0:
            print("aleady die!")  #치료하려는 유닛의 헬스가 0이면 죽었다고 표시한다.
            return
        
        unit.set_health(self.heal_power)
        
        if unit.health > 40:
            unit.health = 40


# In[50]:


# 유닛 생산.
marin1 = Marin()
marin2 = Marin()
medic = Medic()

# marin1.health, marin2.health, medic.health #마린 메딕들 체력
# marin1.stimpack() #마린1의 체력 1/3, 공격력 2배 증가.
# marin1.attack(marin2) #마린1이 마린2 공격
# medic.heal(marin1) #메딕이 마린 힐


# In[51]:


#마린1과 마린2의 전투 시뮬레이션, 중간에 마린1은 스팀팩을 먹는다.

i = 1

while True:

    war_result = []

    marin1_health = marin1.attack(marin2)
    marin2_health = marin2.attack(marin1)

    war_result.append(marin1_health)
    war_result.append(marin2_health)
    i += 1
    
    print("{}번째 공격 : ".format(i), war_result)
    
    if 'health:40' == marin1_health: #마린1은 체력이 40이 되면 메딕에게 1회 치료 받고 스팀팩을 먹는다.
        #medic.heal(marin1)
        marin1.stimpack()
    elif "die" in war_result:
        break
    else:
        continue

