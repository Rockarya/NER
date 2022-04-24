def money_lf(x):
    i_lst = ['dinar','dinars','dollars','million','millions','donor','jordanian','billion','billions']
    b_lst = ['$','£','wage','wages','salaries','money']

    dict = {}
    for i in range(len(x)):
        if x[i] in i_lst:
            dict[i] = i_money
        if x[i] in b_lst:
            dict[i] = b_money

    for i in range(len(x)):
        if i+1< len(x) and dict.get(i) != None and dict[i] == b_money and dict.get(i+1)==None:
            dict[i+1] = i_money

        if i-1 >=0 and dict.get(i) != None and dict[i] == i_money and dict.get(i-1)==None:
            dict[i-1] = b_money        

