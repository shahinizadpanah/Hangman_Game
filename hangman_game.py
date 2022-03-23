from wrong_acct import wrong_act

goal_word = input('insert your word :\n').lower()
#print(goal_word)                                                                                    #for log
len_goal_word = len(goal_word)
#print(len_goal_word)                                                                                #for log
list_word = []
for item in goal_word:
    list_word.append(item)
list_word.sort()
#print(list_word)                                                                                    #for log
currect_letters_list = []
wrong_count = 0
while wrong_count != 6:
    guess_user = input('please enter your letter :\n').lower()
    #print(guess_user)                                                                               #for log
    count_letter = goal_word.count(guess_user) - 1
    #print(count_letter)                                                                             #for log
    if guess_user in goal_word:
        curr_coun_lis = []
        print('good job\nplease continue')
        count_currect_letter = goal_word.count(guess_user)
        #print(count_currect_letter)                                                                 #for log
        if count_currect_letter > 1:
            for i in range(count_currect_letter):
                curr_coun_lis.append(guess_user)
            print(curr_coun_lis)                                                                    #for log
        else:
            currect_letters_list.append(guess_user)
            #print(currect_letters_list)                                                             #for log
        currect_letters_list.extend(curr_coun_lis)
        #print(currect_letters_list)                                                                 #for log
        currect_letters_list.sort()
        print(currect_letters_list)                                                                 #for log
        if set(currect_letters_list) == set(list_word):
            print('\tyou victory\n\tword is %s'%goal_word)
            break
    else:
        wrong_count += 1
        print('sorry letter isnt in word\n\n',wrong_act(wrong_count))
        if wrong_count == 6:
            print('\tyou lose\n\tword is %s'%goal_word)
            break
