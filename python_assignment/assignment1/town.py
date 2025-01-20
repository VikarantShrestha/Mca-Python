men_perc = 52
literacy_perc = 48
literate_men_perc = 35
population = 80000

illiteracy_perc = 100-literacy_perc

total_num_of_mens = (men_perc/100)*80000

num_of_literate_mens=(literate_men_perc/100)*80000
num_of_iliterate_mens = total_num_of_mens - num_of_literate_mens

total_num_of_literates = (literacy_perc/100)*80000
total_num_of_iliterates = 80000-total_num_of_literates

num_of_iliterate_womens = total_num_of_iliterates-num_of_iliterate_mens

print("num of iliterate mens : ", num_of_iliterate_mens)
print("num of iliterate womens : ", num_of_iliterate_womens)
