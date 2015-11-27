import csv
print('1 for Class A\n2 for Class B\n3 for Class C')
chosen = int(input())

if chosen == 1:
    class_a = open('Class_A_Results.txt')
    print('1 for alphabetical orderwith each students highest score\n2 for highest score, Highest to lowest\n3 for average score, Highest to lowest')
    cho_two=int(input())
    csv_a = csv.reader(class_a)
    a_list = []
    for row in csv_a:
        if row:
            row[1] = int(row[1])
            row[2] = int(row[2])
            row[3] = int(row[3])
            minimum = min(row[1:3])
            row.append(minimum)
            maximun = max(row[1:3])
            row.append(maximum)
            average = sum(row[1:3])//3
            row.append(average)
            a_list.append(row[0:9])
        if cho_two == 1:
            alphabetical = [[x[0],x[6]] for x in a_list]
            print('\nCLASS A\N Each nstudent highest by alpabetical order\n')
            for alpha_order in sorted(alphabetical):
                print(alpha_order)
            elif cho_town == 1:
                alphabetical = [[x[0],x[6]] for x in a_list]
                print('\nCLASS A\nEach student highest score to lowest\n')
                for high_scr in sorted(high_score,reverse = True):
                    print(high_scr)
            elif cho_two == 3:
                average_score = [[x[6],x[0]] for x in a_list]
                print('\nCLASS A\nThe average score from the highest to lowest\n')
                for ave_scr in sorted(average_score,reverse = True):
                    print(ave_scr)
        class_a.close()
