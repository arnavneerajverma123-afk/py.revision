total_chores=4
orignal_count = total_chores 
completed_count=0
chore_num = 1
while chore_num <= total_chores:
    if chore_num ==1:next_chore = "Make your bed"
    elif chore_num ==2:next_chore = "Feed the pet"
    elif chore_num ==3:next_chore = "Take out the trash"
    elif chore_num ==4:next_chore = "Wash the dishes"
    ans=input(f"Have you finished{next_chore}?(y/n)")
    if ans=='y':
        completed_count+=1
        chore_num+=1
        print("Great jod!Chore complete")
    else:
        print("Okay, finish it and check again")
    print("Chores remaining",total_chores-completed_count)
    print()
print("====ALL CHORES COMPLETE!====")
print("Now lets safely peek at an infinite loop")
test_value=0
safety_counter=0
while test_value<=0:
    print("this condition never changes, so this would run forever!")
    safety_counter+=1
    if safety_counter==3:
        print("Stoping here on purpose - a real infinity loop never stops on its own")
        break
print("\n=====CHORE CHECKLIST SUMMARY=====")
print("Chores Assigned Today:",orignal_count)
print("Chores Completed:",completed_count)
print("Chores Remaining:",total_chores-completed_count)
print("===============================================")
