def validate_answers(l1,l2,l3,l4,l5):
    answers1 = [9,'left','right',2]
    score1 = 0
    for answer in answers1:
        if answer in l1:
            score1+=1
    
    answers2 = [6,14,3,3]
    score2 = 0
    for answer in answers2:
        if answer in l2:
            score2+=1

    answers3 = [13,6,5,25]
    score3 = 0
    for answer in answers3:
        if answer in l3:
            score3+=1
            
    answers4 = ['01:45','04:30','09:15','02:00']
    score4 = 0
    for answer in answers4:
        if answer in l4:
            score4+=1
    
    answers5 = ['triangle','circle',4,'square']
    score5 = 0
    for answer in answers5:
        if answer in l5:
            score5+=1

    return score1,score2,score3,score4,score5