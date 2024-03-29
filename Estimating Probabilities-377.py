## 2. The Empirical Probability ##

p_tail = 44/100
p_six = 28/200
p_odd = 102/200

## 3. Probability as Relative Frequency ##

p_heads_1 = 138/300
percentage_1 = 46

p_heads_2 = 2550/5000
percentage_2 = 51

## 4. Repeating an Experiment ##

# INITIAL CODE
from numpy.random import seed, randint

seed(1)

def coin_toss():
    if randint(0,2) == 1:
        return 'HEAD'
    else:
        return 'TAIL'
    
probabilities = []
heads = 0

for n in range(1, 10001):
    outcome = coin_toss()
    if outcome == 'HEAD':
        heads += 1
    current_probability = heads / n
    probabilities.append(current_probability)
    
print(probabilities[:10])

## 5. The True Probability Value ##

p_l = 87/200
p_l_and_c = 40/200
p_h = 63/200
p_no = 40/200

## 6. The Theoretical Probability ##

p_5 = 1/6
p_ht = 1/4
p_tt= 1/4

## 7. Events vs. Outcomes ##

p_even = 1/2
p_odd_no_3 = 2/6
p_odd_greater_5 = 0

## 8. A Biased Die ##

p_blue = 10/100
p_red = 90/100